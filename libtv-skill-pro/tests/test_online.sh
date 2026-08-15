#!/usr/bin/env bash
# 在线测试：会调用真实 LibTV IM API，**会消耗 LIBTV 积分**。
# 默认全部跳过，需要显式打开对应开关：
#
#   ONLINE_SESSION=1   bash tests/test_online.sh   # 仅测最便宜的会话创建（几乎不耗）
#   ONLINE_TEXT=1      bash tests/test_online.sh   # 加测文本生成（GVLM，便宜）
#   ONLINE_IMAGE=1     bash tests/test_online.sh   # 加测图片生成（约 14 积分/张）
#   ONLINE_VIDEO=1     bash tests/test_online.sh   # 加测视频生成（约 135 积分/条）
#   ONLINE_ALL=1       bash tests/test_online.sh   # 全开
#
# 前置：
#   export LIBTV_ACCESS_KEY="你的真实 key"
#
set -u
cd "$(dirname "$0")/../scripts"

if [ -z "${LIBTV_ACCESS_KEY:-}" ] || [ "${LIBTV_ACCESS_KEY}" = "dummy_for_offline_test" ]; then
    echo "✖ 请先 export LIBTV_ACCESS_KEY=你的真实 key"
    exit 1
fi

if [ "${ONLINE_ALL:-0}" = "1" ]; then
    ONLINE_SESSION=1; ONLINE_TEXT=1; ONLINE_IMAGE=1; ONLINE_VIDEO=1
fi
ONLINE_SESSION=${ONLINE_SESSION:-0}
ONLINE_TEXT=${ONLINE_TEXT:-0}
ONLINE_IMAGE=${ONLINE_IMAGE:-0}
ONLINE_VIDEO=${ONLINE_VIDEO:-0}

if [ "$ONLINE_SESSION$ONLINE_TEXT$ONLINE_IMAGE$ONLINE_VIDEO" = "0000" ]; then
    cat <<EOF
没有打开任何在线测试开关。

可用开关（按积分消耗从小到大）：
  ONLINE_SESSION=1   仅创建会话不发消息（≈0 积分）
  ONLINE_TEXT=1      文生视频提示词改写（GVLM，几乎免费）
  ONLINE_IMAGE=1     生成 1 张图（≈14 积分）
  ONLINE_VIDEO=1     生成 1 条 5s 视频（≈135 积分）
  ONLINE_ALL=1       全开（约 150 积分）

示例：
  ONLINE_SESSION=1 ONLINE_TEXT=1 bash tests/test_online.sh
EOF
    exit 0
fi

PASS=0; FAIL=0

assert() {
    local name="$1"; local cond="$2"; local detail="$3"
    if [ "$cond" = "1" ]; then
        PASS=$((PASS+1))
        printf "  ✔ %s\n" "$name"
    else
        FAIL=$((FAIL+1))
        printf "  ✗ %s\n    %s\n" "$name" "$detail"
    fi
}

# ───────── 测试 1：仅创建会话（≈0 积分）─────────
if [ "$ONLINE_SESSION" = "1" ]; then
    echo "═══ Test 1: create_session (no message, ≈0 积分) ═══"
    OUT=$(python3 create_session.py 2>&1)
    SID=$(echo "$OUT" | python3 -c "import sys, json; print(json.loads(sys.stdin.read()).get('sessionId',''))" 2>/dev/null)
    PUUID=$(echo "$OUT" | python3 -c "import sys, json; print(json.loads(sys.stdin.read()).get('projectUuid',''))" 2>/dev/null)
    [ -n "$SID" ] && assert "返回 sessionId"  1 "" || assert "返回 sessionId"  0 "$OUT"
    [ -n "$PUUID" ] && assert "返回 projectUuid" 1 "" || assert "返回 projectUuid" 0 "$OUT"

    echo "═══ Test 2: query_session 应能拉到刚建的会话 ═══"
    if [ -n "$SID" ]; then
        Q_OUT=$(python3 query_session.py "$SID" 2>&1)
        if echo "$Q_OUT" | /usr/bin/grep -q '"messages"'; then
            assert "query_session 返回 messages 字段" 1 ""
        else
            assert "query_session 返回 messages 字段" 0 "$Q_OUT"
        fi
    fi
fi

# ───────── 测试 2：文本生成（GVLM，几乎免费）─────────
if [ "$ONLINE_TEXT" = "1" ]; then
    echo ""
    echo "═══ Test 3: node.py text_to_video_prompt (GVLM, ≈0 积分) ═══"
    OUT=$(python3 node.py text_to_video_prompt "黄昏草原一只白马奔跑" 2>&1)
    SID=$(echo "$OUT" | python3 -c "import sys, json; print(json.loads(sys.stdin.read()).get('sessionId',''))" 2>/dev/null)
    [ -n "$SID" ] && assert "text_to_video_prompt 返回 sessionId" 1 "" || assert "text_to_video_prompt 返回 sessionId" 0 "$OUT"

    echo "等待 20 秒后查 messages..."
    sleep 20
    if [ -n "$SID" ]; then
        Q_OUT=$(python3 query_session.py "$SID" --after-seq 0 2>&1)
        # 检查 assistant 返回了响应
        if echo "$Q_OUT" | /usr/bin/grep -q '"role": *"assistant"'; then
            assert "GVLM 返回了 assistant 响应" 1 ""
        else
            assert "GVLM 返回了 assistant 响应（可能需更长时间）" 0 "(only first 200 chars: $(echo "$Q_OUT" | head -c 200))"
        fi
    fi
fi

# ───────── 测试 3：图片生成（≈14 积分）─────────
if [ "$ONLINE_IMAGE" = "1" ]; then
    echo ""
    echo "═══ Test 4: model.py with lib-nano-pro (≈14 积分) ═══"
    OUT=$(python3 model.py with lib-nano-pro "一只白色短毛猫坐在窗台上" \
        --ratio 1:1 --resolution 2K --count "1张" 2>&1)
    SID=$(echo "$OUT" | python3 -c "import sys, json; print(json.loads(sys.stdin.read()).get('sessionId',''))" 2>/dev/null)
    [ -n "$SID" ] && assert "lib-nano-pro 返回 sessionId" 1 "" || assert "lib-nano-pro 返回 sessionId" 0 "$OUT"

    if [ -n "$SID" ]; then
        echo "轮询最多 3 分钟拿生成结果..."
        python3 quick_poll.py "$SID" --interval 8 --timeout 180 --quiet > /tmp/_libtv_poll.json 2>&1
        if /usr/bin/grep -qE 'https://[^"]*\.(png|jpg|webp)' /tmp/_libtv_poll.json; then
            assert "lib-nano-pro 生成了图片 URL" 1 ""
            /usr/bin/grep -oE 'https://[^"]*\.(png|jpg|webp)' /tmp/_libtv_poll.json | head -1 | sed 's/^/    URL: /'
        else
            assert "lib-nano-pro 生成了图片 URL" 0 "未在 3 分钟内拿到图片 URL，请稍后看项目画布"
        fi
    fi
fi

# ───────── 测试 4：视频生成（≈135 积分，较慢）─────────
if [ "$ONLINE_VIDEO" = "1" ]; then
    echo ""
    echo "═══ Test 5: model.py with seedance-2.0-vip (≈135 积分) ═══"
    OUT=$(python3 model.py with seedance-2.0-vip "黄昏草原一只白马奔跑" \
        --ratio 16:9 --resolution 720P --duration 5s 2>&1)
    SID=$(echo "$OUT" | python3 -c "import sys, json; print(json.loads(sys.stdin.read()).get('sessionId',''))" 2>/dev/null)
    [ -n "$SID" ] && assert "seedance-2.0-vip 返回 sessionId" 1 "" || assert "seedance-2.0-vip 返回 sessionId" 0 "$OUT"

    if [ -n "$SID" ]; then
        echo "轮询最多 8 分钟拿视频结果..."
        python3 quick_poll.py "$SID" --interval 15 --timeout 480 --quiet > /tmp/_libtv_poll_v.json 2>&1
        if /usr/bin/grep -qE 'https://[^"]*\.(mp4|mov|webm)' /tmp/_libtv_poll_v.json; then
            assert "seedance 生成了视频 URL" 1 ""
            /usr/bin/grep -oE 'https://[^"]*\.(mp4|mov|webm)' /tmp/_libtv_poll_v.json | head -1 | sed 's/^/    URL: /'
        else
            assert "seedance 生成了视频 URL" 0 "未在 8 分钟内拿到视频 URL，请稍后看项目画布"
        fi
    fi
fi

echo ""
echo "═══════════════════════════════════════"
printf "通过: %d  失败: %d\n" "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ] || exit 1
