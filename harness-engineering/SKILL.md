---
name: harness-engineering
description: >
  Agent 外殼工程（Harness Engineering）原理與模式。涵蓋 Agent Loop、Skill 二層注入、
  Context 三層壓縮、JSONL Mailbox 團隊協作、Task DAG、Worktree 隔離等機制。
  當需要設計 Agent 系統架構、評估 Agent 框架選型、理解 Claude Code 內部運作原理、
  或建構自定義 Agent Harness 時使用。
  源自 shareAI-lab/learn-claude-code 的深度研究。
tags: agent, architecture, harness, claude-code, multi-agent, context-management
---

# Harness Engineering — Agent 外殼工程

> **The model IS the agent. The code is the harness. Build great harnesses.**

## 核心哲學

Agent = 模型本身（經過訓練的神經網路），不是框架、不是 prompt chain。
你寫的程式碼是 **Harness（外殼）**：給模型提供工具、知識、觀察能力、行動介面和權限邊界。

```
Harness = Tools + Knowledge + Observation + Action Interfaces + Permissions

    模型決策 → 外殼執行
    模型推理 → 外殼提供上下文
    模型是駕駛 → 外殼是車輛
```

## Agent Loop 核心模式

所有 Agent 的最小迴圈：

```python
def agent_loop(messages):
    while True:
        response = LLM(messages, tools)
        messages.append(assistant_turn)
        if stop_reason != "tool_use":
            return                    # 模型決定停止
        results = execute_tools(response)
        messages.append(tool_results)  # 繼續迴圈
```

**關鍵**：Loop 永遠不變。所有進階功能都在 loop「之外」添加。

## 6 大 Harness 機制

| # | 機制 | 核心思想 | Ozen Team 對應 |
|---|------|---------|---------------|
| 1 | **Tool Dispatch** | 新增工具 = 新增 handler | `SKILL.md` 中的工具指引 |
| 2 | **Planning (TodoWrite)** | 先列步驟再執行 | `/ozen spec` Gate checklist |
| 3 | **Skill Loading** | Layer 1: 名稱在 system prompt；Layer 2: 按需載入全文 | `SKILLS_INDEX.md` + 動態讀取 |
| 4 | **Context Compact** | 微壓縮 + 自動壓縮 + 手動壓縮 | `strategic-compact` + `/ozen checkpoint` |
| 5 | **Task DAG** | 檔案型任務圖 + 依賴排序 | Feature Checklist（線性 Gate） |
| 6 | **Team Coordination** | JSONL Mailbox + worktree 隔離 | 角色思維（單進程） |

## Skill 二層注入（詳細）

```
Layer 1（~100 token/skill）: 名稱 + 描述 → System Prompt
Layer 2（按需）: load_skill("xxx") → 完整 SKILL.md 透過 tool_result 注入
```

**設計原則**：別把所有知識塞進 System Prompt。只放目錄，按需載入。

## Context 三層壓縮（詳細）

```
每一輪 → Layer 1: micro_compact（靜默）
           替換 N 輪前的 tool_result 為佔位符
               ↓
         token > 閾值?
           No → 繼續
           Yes → Layer 2: auto_compact
                 保存 transcript → LLM 摘要 → 替換 messages[]
               ↓
         Layer 3: compact tool（手動觸發）
           模型主動呼叫 → 立即摘要
```

**關鍵洞察**：Agent 可以「策略性遺忘」，無限工作。

## JSONL Mailbox 團隊協作（參考模式）

```
.team/
  config.json       ← 成員配置 {name, role, status}
  inbox/
    alice.jsonl      ← append-only 收件匣
    bob.jsonl
```

- 每個 teammate 在獨立 Thread 運行 agent_loop
- 5 種訊息：message / broadcast / shutdown_request / shutdown_response / plan_approval
- s11: idle cycle + auto-claim（自主領取任務）
- s12: git worktree 每人獨立目錄

> ⚠️ 此模式需要自建 Python runtime，不適用於純 Markdown 規則庫架構。保留為設計參考。

## 進階閱讀

- 完整研究報告：`references/learn-claude-code-full.md`
- 原始 Repo：[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
- 姐妹專案：[claw0](https://github.com/shareAI-lab/claw0)（永遠在線 Agent：heartbeat + cron + IM + soul）
- 相關工具：[Kode Agent CLI](https://github.com/shareAI-lab/Kode-cli)、[Kode Agent SDK](https://github.com/shareAI-lab/Kode-agent-sdk)

## ⚠️ 已知陷阱

<!-- 新陷阱請加在這裡 ↓ -->

<!-- 陷阱區結束 -->
