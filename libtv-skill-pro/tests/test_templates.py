#!/usr/bin/env python3
"""
模板渲染测试：mock _common.create_session，断言各脚本发送的 prompt 内容符合预期。
不调真实 API，不烧积分。

用法：python3 tests/test_templates.py
"""

import os
import sys
import io
import tempfile
import json
import contextlib

# 让 scripts/ 可被 import
SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts")
sys.path.insert(0, SCRIPTS_DIR)

# 关键：在 import 业务脚本前先把 _common.create_session 换掉
os.environ.setdefault("LIBTV_ACCESS_KEY", "dummy_for_template_test")
# 隔离本地状态文件
TMP_HOME = tempfile.mkdtemp(prefix="libtv-test-")
os.environ["HOME"] = TMP_HOME

import _common  # noqa: E402

CAPTURED = []


def fake_create_session(session_id="", message=""):
    CAPTURED.append({"session_id": session_id, "message": message})
    return {"projectUuid": "test-proj-uuid", "sessionId": "test-session-id"}


_common.create_session = fake_create_session
_common.record_project = lambda *a, **kw: None

import flow  # noqa: E402
import node  # noqa: E402
import edit  # noqa: E402
import model  # noqa: E402


# ---------- 测试辅助 ----------

PASS = 0
FAIL = 0
FAILED = []


def run_main(module, argv):
    """以 argv 替换 sys.argv 执行 module.main()，吞 stdout"""
    CAPTURED.clear()
    saved_argv = sys.argv
    sys.argv = argv
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            try:
                module.main()
            except SystemExit:
                pass
    finally:
        sys.argv = saved_argv
    return buf.getvalue()


def assert_in(name, needle, haystack):
    global PASS, FAIL
    if needle in haystack:
        PASS += 1
        print(f"  ✔ {name}")
    else:
        FAIL += 1
        FAILED.append(f"{name}（缺：{needle!r}）")
        print(f"  ✗ {name}（缺：{needle!r}）")
        snippet = haystack[:200].replace("\n", " ⏎ ")
        print(f"      实际 prompt 片段：{snippet}")


def last_message():
    assert CAPTURED, "没有捕获到 create_session 调用"
    return CAPTURED[-1]["message"]


# ---------- flow.py ----------

print("═══ flow.py 模板渲染 ═══")

run_main(flow, ["flow.py", "story_script", "机器人来到唐朝"])
msg = last_message()
assert_in("flow.story_script: 主题写入 prompt", "机器人来到唐朝", msg)
assert_in("flow.story_script: 含「故事脚本」字样", "故事脚本", msg)
assert_in("flow.story_script: 含「多场景」要求",   "多场景",   msg)

run_main(flow, ["flow.py", "character_views", "穿汉服的赛博朋克少女"])
msg = last_message()
assert_in("flow.character_views: 主题写入",        "穿汉服的赛博朋克少女", msg)
assert_in("flow.character_views: 含「三视图」",    "三视图",              msg)

run_main(flow, ["flow.py", "keyframe_to_video", "拔剑出鞘", "--ref", "https://x/start.png"])
msg = last_message()
assert_in("flow.keyframe_to_video: ref URL 写入",  "https://x/start.png", msg)
assert_in("flow.keyframe_to_video: 动作描述写入",  "拔剑出鞘",            msg)
assert_in("flow.keyframe_to_video: 含「首帧」",    "首帧",                msg)

run_main(flow, ["flow.py", "audio_to_video", "暗黑风 MV", "--ref", "https://x/song.mp3"])
msg = last_message()
assert_in("flow.audio_to_video: 音频 URL 写入",    "https://x/song.mp3", msg)
assert_in("flow.audio_to_video: 含「音频」",       "音频",               msg)


# ---------- node.py ----------

print("")
print("═══ node.py 模板渲染 ═══")

run_main(node, ["node.py", "text_to_video_prompt", "一只猫在屋顶看月亮"])
msg = last_message()
assert_in("node.text_to_video_prompt: 主题写入",   "一只猫在屋顶看月亮", msg)
assert_in("node.text_to_video_prompt: 含「prompt」", "prompt",         msg)

run_main(node, ["node.py", "image_caption", "--ref", "https://x/a.png"])
msg = last_message()
assert_in("node.image_caption: ref 写入",          "https://x/a.png",   msg)
assert_in("node.image_caption: 含「反推」",        "反推",              msg)

run_main(node, ["node.py", "text_to_music", "悲伤、钢琴独奏、60秒"])
msg = last_message()
assert_in("node.text_to_music: 描述写入",          "悲伤、钢琴独奏",     msg)
assert_in("node.text_to_music: 含「音乐」",        "音乐",              msg)

run_main(node, ["node.py", "image_to_image", "换成赛博朋克风", "--ref", "https://x/a.png"])
msg = last_message()
assert_in("node.image_to_image: 目标写入",         "换成赛博朋克风",     msg)
assert_in("node.image_to_image: ref 写入",         "https://x/a.png",   msg)

run_main(node, ["node.py", "image_upscale", "--ref", "https://x/a.png"])
msg = last_message()
assert_in("node.image_upscale: ref 写入",          "https://x/a.png",   msg)
assert_in("node.image_upscale: 含「高清」",        "高清",              msg)

run_main(node, ["node.py", "first_last_frame", "拔剑过程", "--ref", "s.png", "--ref2", "e.png"])
msg = last_message()
assert_in("node.first_last_frame: 首帧写入",       "s.png",  msg)
assert_in("node.first_last_frame: 尾帧写入",       "e.png",  msg)
assert_in("node.first_last_frame: 过程描述写入",   "拔剑过程", msg)

run_main(node, ["node.py", "reference_video", "保留主体演绎新场景", "--ref", "ref.png"])
msg = last_message()
assert_in("node.reference_video: ref 写入",        "ref.png",            msg)
assert_in("node.reference_video: 描述写入",        "保留主体演绎新场景", msg)


# ---------- edit.py ----------

print("")
print("═══ edit.py 模板渲染 ═══")

run_main(edit, ["edit.py", "style", "宫崎骏吉卜力", "--target", "https://x/v.mp4"])
msg = last_message()
assert_in("edit.style: 风格描述写入",  "宫崎骏吉卜力",      msg)
assert_in("edit.style: target 写入",   "https://x/v.mp4",   msg)
assert_in("edit.style: 含「风格」",    "风格",              msg)

run_main(edit, ["edit.py", "camera", "无人机环绕镜头", "--target", "草原场景"])
msg = last_message()
assert_in("edit.camera: 运镜写入",     "无人机环绕镜头", msg)
assert_in("edit.camera: 含「运镜」",   "运镜",          msg)

run_main(edit, ["edit.py", "character_lib", "孙悟空", "--target", "花果山做早操"])
msg = last_message()
assert_in("edit.character_lib: 角色写入",      "孙悟空",         msg)
assert_in("edit.character_lib: 场景写入",      "花果山做早操",   msg)
assert_in("edit.character_lib: 含「角色库」",  "角色库",         msg)

run_main(edit, ["edit.py", "mark", "把纸船换成爱心", "--target", "https://x/img.png"])
msg = last_message()
assert_in("edit.mark: 描述写入",       "把纸船换成爱心",       msg)
assert_in("edit.mark: target 写入",    "https://x/img.png",    msg)

run_main(edit, ["edit.py", "focus", "强调右上角月亮", "--target", "https://x/img.png"])
msg = last_message()
assert_in("edit.focus: 描述写入",      "强调右上角月亮",       msg)
assert_in("edit.focus: 含「聚焦」",    "聚焦",                msg)

# 无 --target 时应使用「当前会话上一条结果」
run_main(edit, ["edit.py", "style", "电影感"])
msg = last_message()
assert_in("edit.style 无 target 时用 fallback", "当前会话", msg)


# ---------- model.py with ----------

print("")
print("═══ model.py with 模板渲染 ═══")

run_main(model, ["model.py", "with", "seedance-2.0-vip", "白马奔跑",
                 "--ratio", "16:9", "--duration", "5s", "--resolution", "720P"])
msg = last_message()
assert_in("model.with: 含模型指令标记",  "[模型/参数指令]",     msg)
assert_in("model.with: 指定模型",        "seedance-2.0-vip",    msg)
assert_in("model.with: 比例",            "16:9",                msg)
assert_in("model.with: 分辨率",          "720P",                msg)
assert_in("model.with: 时长",            "5s",                  msg)
assert_in("model.with: 生成需求",        "白马奔跑",            msg)

run_main(model, ["model.py", "with", "lib-nano-pro", "赛博朋克少女",
                 "--ratio", "16:9", "--resolution", "2K", "--count", "4张"])
msg = last_message()
assert_in("model.with: 指定 lib-nano-pro", "lib-nano-pro",  msg)
assert_in("model.with: 数量",              "4张",           msg)

# 未知模型应给出 stderr 提醒但不阻塞
import io as _io
saved_err = sys.stderr
sys.stderr = _io.StringIO()
try:
    run_main(model, ["model.py", "with", "unknown-model-xyz", "test"])
    err = sys.stderr.getvalue()
finally:
    sys.stderr = saved_err
assert_in("model.with 未知模型 stderr 提醒", "unknown-model-xyz", err)


# ---------- 总结 ----------

print("")
print("═══════════════════════════════════════")
print(f"通过: {PASS}  失败: {FAIL}  总计: {PASS + FAIL}")
if FAIL:
    print("")
    print("失败用例：")
    for c in FAILED:
        print(f"  - {c}")
    sys.exit(1)
print("全部通过 ✓")
