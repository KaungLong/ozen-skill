# learn-claude-code 完整研究報告

> **Repo**: [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> **授權**: MIT
> **研究日期**: 2026-03-25

## 核心哲學：Model IS the Agent

這個 repo 最重要的觀念：Agent = 模型本身，不是框架、不是 prompt chain。
你寫的程式碼是 Harness（外殼 / 馬具）：

```
Harness = Tools + Knowledge + Observation + Action Interfaces + Permissions
```

### 歷史佐證
- 2013 DeepMind DQN（Atari）— 一個模型學會玩 49 個遊戲
- 2019 OpenAI Five（Dota 2）— 勝率 99.4%，45000 年自我對弈
- 2019 AlphaStar（StarCraft II）— Grandmaster，前 0.15%
- 2019 Tencent 絕悟（Honor of Kings）— 職業選手 1/15 勝率
- 2024-25 LLM Agents — Claude, GPT, Gemini 作為 coding agent

### Agent 不是什麼
拖拉式工作流、no-code 平台、prompt-chain orchestration 不是 Agent。
那些是 "Rube Goldberg machine"——包裝了 LLM 外皮的 if-else 腳本。
Agency 是「學到的」，不是「程式寫出來的」。

---

## 12 個漸進 Session

### Phase 1: THE LOOP
| Session | 主題 | Tools |
|---------|------|-------|
| s01 | Agent Loop — `while + stop_reason` | 1 |
| s02 | Tool Use — dispatch map: `name→handler` | 4 |

### Phase 2: PLANNING & KNOWLEDGE
| Session | 主題 | Tools |
|---------|------|-------|
| s03 | TodoWrite — TodoManager + nag reminder | 5 |
| s04 | Subagents — fresh `messages[]` per child | 5 |
| s05 | Skill Loading — SKILL.md via tool_result | 5 |
| s06 | Context Compact — 3-layer compression | 5 |

### Phase 3: PERSISTENCE
| Session | 主題 | Tools |
|---------|------|-------|
| s07 | Tasks — file-based CRUD + deps graph | 8 |
| s08 | Background Tasks — daemon threads + notify | 6 |

### Phase 4: TEAMS
| Session | 主題 | Tools |
|---------|------|-------|
| s09 | Agent Teams — teammates + JSONL mailboxes | 9 |
| s10 | Team Protocols — shutdown + plan approval FSM | 12 |
| s11 | Autonomous Agents — idle cycle + auto-claim | 14 |
| s12 | Worktree Isolation — task + directory binding | 16 |

---

## 關鍵技術實作

### s01: Agent Loop
```python
def agent_loop(messages):
    while True:
        response = client.messages.create(
            model=MODEL, system=SYSTEM,
            messages=messages, tools=TOOLS, max_tokens=8000,
        )
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason != "tool_use":
            return
        results = []
        for block in response.content:
            if block.type == "tool_use":
                output = TOOL_HANDLERS[block.name](**block.input)
                results.append({"type": "tool_result", "tool_use_id": block.id,
                                "content": output})
        messages.append({"role": "user", "content": results})
```

### s05: Skill Loading（二層注入）
- `SkillLoader` 類掃描 `skills/<name>/SKILL.md` 的 YAML frontmatter
- Layer 1: `get_descriptions()` → 名稱+描述注入 System Prompt（~100 token/skill）
- Layer 2: `get_content(name)` → `<skill>` 標籤包裹全文，透過 tool_result 注入

### s06: Context Compact（三層壓縮）
- Layer 1 `micro_compact`: 每輪替換超過 3 輪的 tool_result 為 `[Previous: used {tool_name}]`
- Layer 2 `auto_compact`: token > 50000 時保存 transcript + LLM 摘要
- Layer 3: 模型主動呼叫 `compact` tool → 立即摘要
- Token 估算：`len(str(messages)) // 4`

### s09: JSONL Mailbox
- `MessageBus` 類：每個 teammate 一個 `.jsonl` 收件匣
- `send()`: append 一行 JSON 到目標的 `.jsonl`
- `read_inbox()`: 讀取所有行 + 清空檔案（drain）
- `TeammateManager`: 每個 teammate 在獨立 `threading.Thread` 中運行 agent_loop
- 5 種訊息類型：message / broadcast / shutdown_request / shutdown_response / plan_approval_response

---

## 生態系統

| 專案 | 說明 |
|------|------|
| [Kode Agent CLI](https://github.com/shareAI-lab/Kode-cli) | 開源 Coding Agent CLI，支援 GLM/MiniMax/DeepSeek |
| [Kode Agent SDK](https://github.com/shareAI-lab/Kode-agent-sdk) | 嵌入式 Agent SDK，無需每用戶獨立進程 |
| [claw0](https://github.com/shareAI-lab/claw0) | 永遠在線 Agent：heartbeat + cron + IM + soul |
| [OpenClaw](https://github.com/openclaw/openclaw) | 主動式 AI 助手，30 秒心跳 + 多 IM 平台 |

---

## 與 Ozen Team 對比

| 維度 | learn-claude-code | Ozen Team |
|------|-------------------|-----------|
| 哲學 | 模型即 Agent，只建外殼 | 角色扮演 + SOP + 技能庫 |
| 語言 | Python（直接呼叫 API） | Markdown 規則（AI 助手解讀）|
| Agent Loop | Python while 迴圈 | 宿主內建迴圈 |
| Skill 管理 | 二層注入 | SKILLS_INDEX + 按需載入 |
| Context | 三層壓縮管線 | checkpoint + strategic-compact |
| 多 Agent | JSONL mailbox + thread | 角色思維（單進程）|
| 錯誤學習 | 無 | ERROR_JOURNAL → TRAP |
| 適用場景 | 學習/自建 Agent 產品 | 實際專案開發 |
