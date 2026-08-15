#!/usr/bin/env bash
# 离线测试：不调真实 API，不烧积分。
# 覆盖：所有脚本 --help 可跑、参数缺失正确拦截、状态文件 CRUD 正常、模型清单完整。
# 用法：bash tests/test_offline.sh
set -u
cd "$(dirname "$0")/../scripts"
export LIBTV_ACCESS_KEY="dummy_for_offline_test"

PASS=0
FAIL=0
FAILED_CASES=()

run() {
    local name="$1"; shift
    local expect_rc="$1"; shift
    local out
    out=$("$@" 2>&1)
    local rc=$?
    if [ "$rc" = "$expect_rc" ]; then
        PASS=$((PASS+1))
        printf "  ✔ %s\n" "$name"
    else
        FAIL=$((FAIL+1))
        FAILED_CASES+=("$name [expected rc=$expect_rc, got rc=$rc]")
        printf "  ✗ %s [rc=$rc]\n" "$name"
        printf "    %s\n" "$(echo "$out" | head -3 | sed 's/^/      /')"
    fi
}

assert_contains() {
    local name="$1"; local needle="$2"; local haystack="$3"
    if echo "$haystack" | /usr/bin/grep -q -- "$needle"; then
        PASS=$((PASS+1))
        printf "  ✔ %s\n" "$name"
    else
        FAIL=$((FAIL+1))
        FAILED_CASES+=("$name [missing: $needle]")
        printf "  ✗ %s [missing: %s]\n" "$name" "$needle"
    fi
}

echo "═══ 1. 所有脚本 --help 应正常 ═══"
for f in _common.py libtv.py create_session.py query_session.py change_project.py upload_file.py \
         download_results.py batch_create.py monitor_session.py quick_poll.py \
         workflow_template.py export_results.py session_history.py manage_project.py \
         flow.py node.py edit.py model.py; do
    if [ "$f" = "_common.py" ]; then
        # _common.py 是模块，不是入口
        run "import: $f" 0 python3 -c "import sys; sys.path.insert(0,'.'); import _common"
    else
        run "$f --help" 0 python3 "$f" --help
    fi
done

echo ""
echo "═══ 1b. libtv.py 统一入口 ═══"
run "libtv.py --help"                0 python3 libtv.py --help
run "libtv.py model list (经入口)"   0 python3 libtv.py model list
run "libtv.py 未知子命令"            2 python3 libtv.py unknown_cmd_xyz
run "libtv.py flow --help"           0 python3 libtv.py flow --help
LIBTV_OUT=$(python3 libtv.py model list --kind video 2>&1)
assert_contains "libtv.py model list --kind video 含 wan-2.6" "wan-2.6" "$LIBTV_OUT"

echo ""
echo "═══ 1c. --dry-run 应不调 API（生成类子命令）═══"
# flow / node / edit / model 都支持 --dry-run，输出应含 dry_run: true
for case in \
    "flow story_script x:flow story_script Testxyz --dry-run" \
    "flow character_views x:flow character_views Testxyz --dry-run" \
    "node text_to_video_prompt x:node text_to_video_prompt Testxyz --dry-run" \
    "node image_caption x:node image_caption --ref https://x/a.png --dry-run" \
    "edit style x:edit style Testxyz --target URL --dry-run" \
    "edit camera x:edit camera Testxyz --target URL --dry-run" \
    "model with seedance x:model with seedance-2.0-vip Testxyz --ratio 16:9 --duration 5s --dry-run"; do
    name="${case%%:*}"
    cmd="${case#*:}"
    OUT=$(python3 libtv.py $cmd 2>&1)
    assert_contains "$name 输出 dry_run: true" '"dry_run": true' "$OUT"
    assert_contains "$name 输出 would_send 字段"  '"would_send"'   "$OUT"
done

echo ""
echo "═══ 2. 参数缺失应拦截 ═══"
run "flow.py keyframe_to_video 缺 --ref"        1 python3 flow.py keyframe_to_video "test"
run "flow.py audio_to_video 缺 --ref"           1 python3 flow.py audio_to_video "test"
run "node.py image_to_image 缺 --ref"           1 python3 node.py image_to_image "test"
run "node.py first_last_frame 缺 --ref/--ref2"  1 python3 node.py first_last_frame "test"
run "node.py first_last_frame 只有 --ref"       1 python3 node.py first_last_frame "test" --ref a.png
run "edit.py 无 topic"                          2 python3 edit.py style
run "model.py 无子命令"                         1 python3 model.py
run "model.py with 缺 model 参数"               2 python3 model.py with
run "manage_project.py 无子命令"                1 python3 manage_project.py
run "manage_project.py describe 缺 desc"        2 python3 manage_project.py describe abc
run "session_history.py 无子命令"               1 python3 session_history.py

echo ""
echo "═══ 3. model.py list 输出完整性 ═══"
ALL_MODELS=$(python3 model.py list 2>&1)
assert_contains "list 含 gvlm-3.1"          "gvlm-3.1"          "$ALL_MODELS"
assert_contains "list 含 lib-nano-pro"      "lib-nano-pro"      "$ALL_MODELS"
assert_contains "list 含 nano-banana"       "nano-banana"       "$ALL_MODELS"
assert_contains "list 含 midjourney"        "midjourney"        "$ALL_MODELS"
assert_contains "list 含 seedream-5.0"      "seedream-5.0"      "$ALL_MODELS"
assert_contains "list 含 seedance-2.0-vip"  "seedance-2.0-vip"  "$ALL_MODELS"
assert_contains "list 含 kling-3.0"         "kling-3.0"         "$ALL_MODELS"
assert_contains "list 含 kling-o3"          "kling-o3"          "$ALL_MODELS"
assert_contains "list 含 wan-2.6"           "wan-2.6"           "$ALL_MODELS"

VIDEO_MODELS=$(python3 model.py list --kind video 2>&1)
assert_contains "list --kind video 含 seedance-2.0-vip" "seedance-2.0-vip" "$VIDEO_MODELS"
assert_contains "list --kind video 含 wan-2.6"          "wan-2.6"          "$VIDEO_MODELS"
if echo "$VIDEO_MODELS" | /usr/bin/grep -q "midjourney"; then
    FAIL=$((FAIL+1))
    FAILED_CASES+=("list --kind video 不应含 midjourney")
    printf "  ✗ list --kind video 不应含 midjourney\n"
else
    PASS=$((PASS+1))
    printf "  ✔ list --kind video 正确排除 midjourney\n"
fi

echo ""
echo "═══ 4. 状态文件 CRUD（隔离的 HOME）═══"
TMPHOME=$(mktemp -d)

# manage_project
HOME=$TMPHOME python3 manage_project.py describe test-uuid-1 "test entry" > /dev/null 2>&1
LIST_OUT=$(HOME=$TMPHOME python3 manage_project.py list 2>&1)
assert_contains "manage_project: describe 后 list 含 test-uuid-1" "test-uuid-1" "$LIST_OUT"

HOME=$TMPHOME python3 manage_project.py remove test-uuid-1 > /dev/null 2>&1
LIST_OUT2=$(HOME=$TMPHOME python3 manage_project.py list 2>&1)
if echo "$LIST_OUT2" | /usr/bin/grep -q "test-uuid-1"; then
    FAIL=$((FAIL+1))
    FAILED_CASES+=("manage_project: remove 后仍存在")
    printf "  ✗ manage_project: remove 后仍存在\n"
else
    PASS=$((PASS+1))
    printf "  ✔ manage_project: remove 后正确清除\n"
fi

# session_history
HOME=$TMPHOME python3 session_history.py add sid-test-1 --desc "test session" > /dev/null 2>&1
HIST_OUT=$(HOME=$TMPHOME python3 session_history.py list 2>&1)
assert_contains "session_history: add 后 list 含 sid-test-1" "sid-test-1" "$HIST_OUT"

GET_OUT=$(HOME=$TMPHOME python3 session_history.py get 1 2>&1)
assert_contains "session_history: get 1 返回 sid-test-1" "sid-test-1" "$GET_OUT"

HOME=$TMPHOME python3 session_history.py remove 1 > /dev/null 2>&1
HIST_OUT2=$(HOME=$TMPHOME python3 session_history.py list 2>&1)
if echo "$HIST_OUT2" | /usr/bin/grep -q "sid-test-1"; then
    FAIL=$((FAIL+1))
    FAILED_CASES+=("session_history: remove 后仍存在")
    printf "  ✗ session_history: remove 后仍存在\n"
else
    PASS=$((PASS+1))
    printf "  ✔ session_history: remove 后正确清除\n"
fi

rm -rf "$TMPHOME"

echo ""
echo "═══ 5. workflow_template.py 列表 ═══"
TPL_OUT=$(python3 workflow_template.py --list 2>&1)
for tpl in storyboard character_design video_generation image_generation \
           style_transfer short_drama music_video product_showcase; do
    assert_contains "workflow_template 含 $tpl" "$tpl" "$TPL_OUT"
done

echo ""
echo "═══════════════════════════════════════"
printf "通过: %d  失败: %d  总计: %d\n" "$PASS" "$FAIL" "$((PASS+FAIL))"
if [ "$FAIL" -gt 0 ]; then
    echo ""
    echo "失败用例："
    for c in "${FAILED_CASES[@]}"; do
        echo "  - $c"
    done
    exit 1
fi
echo "全部通过 ✓"
