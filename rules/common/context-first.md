---
description: Context-First 全域約束。所有 Agent 在執行任何任務前，必須先完成上下文收集與充分性檢查，完工後必須回寫上下文，確保知識鏈不斷裂。
---

# Context-First 原則 (上下文優先)

> 來源啟發：Linear Next — "The next system is not designed around handoffs. It is designed around context and agents."

## 核心鐵律

**Context > Handoff（上下文 > 交接）**

禁止「接單就做」。在進入 OODA 的 ACT 階段之前，你必須先完成完整的 Context 收集。

## 三大強制行為

### 1. 進場讀取義務 (Context Intake)
每次接到新任務時，必須先讀取所有可取得的上下文：
- `spec/` 目錄下的規格文件（GAME_RULES, SCREENS, features, design）
- 相關 Skill 的 `⚠️ 已知陷阱` 區塊
- `ERROR_JOURNAL.md`（如果存在）
- `spec/CHANGELOG.md`（了解近期決策）

### 2. 充分性檢查 (Sufficiency Gate)
讀取完畢後，你必須自我審視：「我手上的資訊足以正確執行這個任務嗎？」
- **足夠** → 進入 DECIDE / ACT 階段。
- **不足夠** → 必須主動向使用者盤問缺失的資訊，而非自行假設或編造。嚴禁跳過此步驟直接行動。

### 3. 離場回寫義務 (Context Output)
任務完成後，你必須將新產生的知識反向寫回 `spec/`：
- 新的架構決策 → `spec/design/` 或 `spec/CHANGELOG.md`
- 新發現的陷阱 → 對應 `SKILL.md` 的已知陷阱區塊
- 任務進度變化 → `spec/DEVELOPMENT.md` 的狀態更新

**目的**：確保下一個 Agent（或下一段對話）能繼承完整的 Context Chain，徹底消除「斷裂式交接」。
