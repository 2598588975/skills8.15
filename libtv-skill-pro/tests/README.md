# libtv-skill-pro 测试集

分三层，按从快到慢、从安全到耗资源排列。

## 1. 离线测试 `test_offline.sh`

**几秒跑完，不调任何 API，不烧积分。**

覆盖：
- 所有 17 个脚本 `--help` 能正常退出
- 缺参数时正确报错退出（非 0）
- `model.py list` 输出 9 个已知模型完整
- `model.py list --kind video` 过滤正确（含 4 个视频模型，不含图像模型）
- 状态文件 CRUD：`manage_project.py` 与 `session_history.py` 的 add/list/get/remove 全流程
- `workflow_template.py --list` 输出 8 个预设模板

跑法：
```bash
bash tests/test_offline.sh
```

跑出来类似：
```
═══ 1. 所有脚本 --help 应正常 ═══
  ✔ import: _common.py
  ✔ create_session.py --help
  ...
═══════════════════════════════════════
通过: 60  失败: 0  总计: 60
全部通过 ✓
```

## 2. 模板测试 `test_templates.py`

**几秒跑完，mock 掉 `create_session`，不调真实 API。**

覆盖：
- `flow.py` 4 个预设 prompt 模板的字段渲染（主题/参考素材是否正确写入）
- `node.py` 7 个动作 prompt 模板
- `edit.py` 5 个修饰器 prompt 模板（含 fallback target 处理）
- `model.py with` 的模型指令拼装（[模型/参数指令] 块 + 各参数 + 生成需求）
- 未知模型应给出 stderr 提醒但不阻塞

跑法：
```bash
python3 tests/test_templates.py
```

跑出来类似：
```
═══ flow.py 模板渲染 ═══
  ✔ flow.story_script: 主题写入 prompt
  ✔ flow.story_script: 含「故事脚本」字样
  ...
═══════════════════════════════════════
通过: 56  失败: 0  总计: 56
全部通过 ✓
```

## 3. 在线测试 `test_online.sh`

**调真实 LibTV API，会消耗积分。** 默认全部跳过，需要显式开关。

| 开关 | 测什么 | 估算积分 | 估算时长 |
|---|---|---|---|
| `ONLINE_SESSION=1` | 仅创建会话 + 查询 | ≈ 0 | < 5s |
| `ONLINE_TEXT=1` | GVLM 文本生成 | ≈ 0 | ≈ 30s |
| `ONLINE_IMAGE=1` | lib-nano-pro 生成 1 张图 | ≈ 14 | ≈ 60s |
| `ONLINE_VIDEO=1` | seedance-2.0-vip 生成 5s 视频 | ≈ 135 | ≈ 5-8min |
| `ONLINE_ALL=1` | 全部 | ≈ 150 | ≈ 10min |

前置：
```bash
export LIBTV_ACCESS_KEY="你的真实 key"
```

跑法（推荐先小范围）：
```bash
# 最便宜：只验证会话能创建
ONLINE_SESSION=1 bash tests/test_online.sh

# 加 GVLM 文本生成
ONLINE_SESSION=1 ONLINE_TEXT=1 bash tests/test_online.sh

# 全开（约 150 积分）
ONLINE_ALL=1 bash tests/test_online.sh
```

## 一键全跑（离线）

```bash
bash tests/test_offline.sh && python3 tests/test_templates.py
```

## 不覆盖什么

下列情况测试集**不能**自动验证，需要人工肉眼或后续在线观察：

1. **后端 Agent 是否严格按指令路由模型/参数**——比如 `model.py with seedance-2.0-vip --duration 5s` 后端是否真用 Seedance 2.0、是否真 5 秒
2. **生成质量**——图像/视频清晰度、prompt 还原度、风格一致性
3. **修饰器是否作用于上一条结果**——`edit.py` 在同一 session 内的"叠加"语义是否被后端正确识别
4. **角色库 `character_lib`**——需要后端真有角色库且能匹配角色名
5. **`upload_file.py` 实际上传到 OSS**——需要本地真实文件
6. **`download_results.py` 下载 OSS 文件**——需要会话里真有结果 URL

这些需要在线 + 人工核对，跑完 `ONLINE_ALL` 后看项目画布链接确认。

## 跑完测试的下一步

- 离线全通过 + 模板全通过 → 可以放心发新版（`clawhub publish ... --version X.Y.Z`）
- 在线测试发现某条 prompt 模板路由不准 → 改对应脚本的 `template`，重跑离线测试，再发 patch 版（0.3.1）
