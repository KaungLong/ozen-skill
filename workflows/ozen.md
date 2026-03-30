---
description: Ozen Team 指令入口 — 啟動角色 + 技能 + 工作流的完整鏈路
---

# /ozen — Ozen Team 調度指令

> **[🚨 CRITICAL]** 此檔為路由表。收到指令後，只讀對應的 `workflows/ozen-<cmd>.md`，不要載入其他子工作流。

## 指令路由表

| 指令 | 子工作流 | 用途 |
|------|---------|------|
| `/ozen spec <feature>` | [`ozen-spec.md`](ozen-spec.md) | 撰寫 Gherkin 行為規格 (SDD) |
| `/ozen test <feature>` | [`ozen-test.md`](ozen-test.md) | 從 Gherkin 生成測試 (TDD Red) |
| `/ozen screen <畫面>` | [`ozen-screen.md`](ozen-screen.md) | 實作畫面 (TDD Green) |
| `/ozen review` | [`ozen-review.md`](ozen-review.md) | 程式碼審查 |
| `/ozen build <平台>` | [`ozen-build.md`](ozen-build.md) | 構建驗證 |
| `/ozen fix <問題>` | [`ozen-fix.md`](ozen-fix.md) | 問題修復 |
| `/ozen status` | [`ozen-status.md`](ozen-status.md) | 專案狀態 |
| `/ozen checkpoint` | [`ozen-checkpoint.md`](ozen-checkpoint.md) | 持久化決策與進度 |
| `/ozen research <主題>` | [`ozen-research.md`](ozen-research.md) | 主題研究與整理 |
| `/ozen add-skill <需求>` | [`ozen-add-skill.md`](ozen-add-skill.md) | 動態安裝外部擴充技能 |
| `/ozen triage <輸入>` | [`ozen-triage.md`](ozen-triage.md) | 自動分流模糊需求 |
| `/ozen help` | [`ozen-help.md`](ozen-help.md) | 顯示可用指令選單 (Help) |

---

## 🚨 Feature Checklist Template

> **每次開發新 feature 時，必須將以下 checklist 展開到 task.md。**
> 每個 gate (🚪) 必須完成並標記後才能進入下一步。

```markdown
## [Feature Name]

### /ozen spec
- [ ] 🚪 Gate 1: 讀全部角色（每個角色自行判斷是否介入）
- [ ] 🚪 Gate 2: 讀 `GAME_RULES.md` + `SCREENS.md` + 已有 features
- [ ] 🚪 Gate 3: 架構設計判斷（需要 design doc? Y/N → 記錄原因）
- [ ] 🚪 Gate 4: 撰寫 `{feature}.feature`（中英文）
- [ ] 🚪 Gate 5: 驗證完整性（中英文一致、場景可測試）

### /ozen test
- [ ] 🚪 Gate 6: 確認 qa-engineer 主導
- [ ] 🚪 Gate 7: 讀 `{feature}.feature` 確認場景數
- [ ] 🚪 Gate 8: 撰寫測試檔案（場景 → 測試案例）
- [ ] 🚪 Gate 9: 執行測試 → 🔴 RED

### RPI 實作迴圈
- [ ] 🚪 Gate 10: Code Discovery (分析模式與影響範圍)
- [ ] 🚪 Gate 11: Implementation (撰寫程式碼)
- [ ] 🚪 Gate 12: Self-Validation (測試 → 🟢 GREEN)
- [ ] 🚪 Gate 13: Code Review (載入 code-reviewer)
- [ ] 🚪 Gate 14: User Validation Gate

### 收尾
- [ ] 🚪 Gate 15: Documentation Update
- [ ] 🚪 Gate 16: `git add -A && git commit`
```
