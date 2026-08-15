# 集成到各个 AI 客户端

libtv-skill-pro 同时支持以下客户端，**主版本 `~/.agents/skills/libtv-skill/` 是唯一源**——其他客户端通过符号链接 / rule 文件复用主版本，修改一处同步多处。

## 客户端集成矩阵

| 客户端 | 集成方式 | 状态 | 路径 |
|---|---|---|---|
| **OpenClaw / ClawHub** | Skill (官方分发) | ✅ 已发布 | `clawhub.ai/qiuxiangxiang/libtv-skill-pro` |
| **Claude Code** | Plugin (本地 marketplace) | ✅ 已注册 | `~/.claude/libtv-marketplace/` |
| **Cursor** | Project rule (`.cursor/rules/*.mdc`) | ✅ 模板就绪 | `cursor/libtv-skill-pro.mdc` |
| **Cursor MCP** | （计划中） | ⏳ v0.5.0 |  |

---

## 1. OpenClaw / ClawHub

```bash
clawhub install libtv-skill-pro
# 安装到 ~/.openclaw/workspace/skills/libtv-skill-pro/，OpenClaw 自动识别
# 安装后可用 openclaw skills info libtv-skill-pro 查看详情
```

之后 OpenClaw agent 可通过 `/libtv-skill-pro` 触发。详见 [SKILL.md](./SKILL.md)。

## 2. Claude Code

### 已经为你装好

```bash
$ claude plugin list
Installed plugins:
  ❯ libtv-skill-pro@libtv-marketplace
    Version: 0.4.0
    Status: ✔ enabled
```

下次启动 `claude` 时，新会话的 system reminder 里会出现 `libtv-skill-pro` 可用 skill。Agent 看到生成/编辑图片或视频的需求时会自动触发。

### 如果换机器了，复制下面这段重新装

```bash
# 假设主版本已 git clone 到 ~/.agents/skills/libtv-skill/

mkdir -p ~/.claude/libtv-marketplace/.claude-plugin
mkdir -p ~/.claude/libtv-marketplace/plugins/libtv-skill-pro/.claude-plugin
mkdir -p ~/.claude/libtv-marketplace/plugins/libtv-skill-pro/skills/libtv-skill-pro

# 符号链接 scripts + examples
ln -snf ~/.agents/skills/libtv-skill/scripts \
        ~/.claude/libtv-marketplace/plugins/libtv-skill-pro/skills/libtv-skill-pro/scripts
ln -snf ~/.agents/skills/libtv-skill/examples \
        ~/.claude/libtv-marketplace/plugins/libtv-skill-pro/skills/libtv-skill-pro/examples

# SKILL.md 替换 OpenClaw 占位符为 Claude Code 的
sed 's|{baseDir}|${CLAUDE_PLUGIN_ROOT}/skills/libtv-skill-pro|g' \
    ~/.agents/skills/libtv-skill/SKILL.md \
    > ~/.claude/libtv-marketplace/plugins/libtv-skill-pro/skills/libtv-skill-pro/SKILL.md

# marketplace.json
cat > ~/.claude/libtv-marketplace/.claude-plugin/marketplace.json <<'EOF'
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "libtv-marketplace",
  "description": "Local marketplace for libtv-skill-pro",
  "owner": {"name": "Qiuxiangxiang"},
  "plugins": [{
    "name": "libtv-skill-pro",
    "description": "🎬 LibTV (liblib.tv) AI 视频/图像生成 skill",
    "author": {"name": "Qiuxiangxiang"},
    "category": "creative",
    "source": "./plugins/libtv-skill-pro",
    "homepage": "https://clawhub.ai/qiuxiangxiang/libtv-skill-pro"
  }]
}
EOF

# plugin.json
cat > ~/.claude/libtv-marketplace/plugins/libtv-skill-pro/.claude-plugin/plugin.json <<'EOF'
{
  "name": "libtv-skill-pro",
  "description": "🎬 LibTV AI 视频/图像生成 Claude Code skill",
  "version": "0.4.0",
  "author": {"name": "Qiuxiangxiang"},
  "license": "MIT-0"
}
EOF

# 注册并安装
claude plugin marketplace add ~/.claude/libtv-marketplace
claude plugin install libtv-skill-pro@libtv-marketplace
```

### 卸载

```bash
claude plugin uninstall libtv-skill-pro
claude plugin marketplace remove libtv-marketplace
```

## 3. Cursor

Cursor 没有"用户级 skill"概念，但有项目级 rules 和 User Rules 文本框。

### 方式 A：项目级 rule（推荐 · 立即生效）

```bash
# 在你想用 libtv 的项目里跑
mkdir -p .cursor/rules
cp ~/.agents/skills/libtv-skill/cursor/libtv-skill-pro.mdc .cursor/rules/
```

或者用软链：
```bash
mkdir -p .cursor/rules
ln -s ~/.agents/skills/libtv-skill/cursor/libtv-skill-pro.mdc .cursor/rules/libtv-skill-pro.mdc
```

### 方式 B：全局 User Rules（一次性配置所有项目）

1. 打开 Cursor → ⚙️ Settings → Rules
2. 在 **User Rules** 文本框里粘贴 `cursor/libtv-skill-pro.mdc` 的全部内容
3. 保存

之后所有项目都自动启用此规则。

### 验证

新开 Cursor 会话，对 AI 说："帮我用 libtv 生一张猫图"。Cursor 应该回复一条 `python3 /Users/liuqinghua/.agents/skills/libtv-skill/scripts/libtv.py model with lib-nano-pro "白色短毛猫..." --dry-run` 命令。

## 4. Cursor MCP（计划中 · v0.5.0）

把所有 `libtv.py` 子命令包装成 MCP tools，让 Cursor / Claude Desktop / 任何 MCP 客户端都能以 function call 形式调用，比 rule 更精确。

待 v0.5.0 实现后补 `~/.cursor/mcp.json` 配置示例。

---

## 共享前置：access key

所有客户端都依赖 `LIBTV_ACCESS_KEY` 环境变量：

```bash
# ~/.zshrc 或 ~/.bashrc
export LIBTV_ACCESS_KEY=你的key
```

key 从 [LibTV 用户中心](https://www.liblib.tv) 获取（个人设置 → API / 开发者）。

如果 Claude Code / Cursor 启动时没拿到这个环境变量，调用脚本会得到结构化错误：

```json
{"error": {"kind": "INVALID_ACCESS_KEY", "http_code": 0, "message": "请设置 LIBTV_ACCESS_KEY 环境变量"}}
```

让用户在 shell 配置文件加 export 后重启 IDE / terminal 即可。
