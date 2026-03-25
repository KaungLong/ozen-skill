# 📖 Ozen Team 防呆與肌肉記憶法則 (Rules)

這個目錄存放所有與特定語言或領域相關的硬性法則 (Rules)，源自於 `everything-claude-code` 架構。
當 Ozen Team 的角色（如平台工程師）要在 TypeScript 或 Kotlin 專案中工作時，應該首先讀取對應的 Rules。

它類似於 `SKILL.md`，差異在於：
- **`SKILL.md` 是主動技能**：你需要它去執行特定 SOP（如 `code-review`、`playwright-qa`）。
- **`Rules` 是被動光環**：在寫程式碼的每一刻、每一次呼叫 Edit Tool 修改檔案時，都必須遵守的底層規範。

## 目錄結構
- `common/` - 所有語言都通用的法則 (如 變數命名、Git Commit 原則)
- `typescript/` - 前端/Node.js 的偏好寫法 (如 禁止 `any`, 強制 `useEffect` dependency array 完整)
- `kotlin/` - Android / KMP 的架構法則 (如 `StateFlow` 的最佳收集方式, DI 規範)

## Ozen OODA 結合點
在 `ORIENT` 階段，Agent 除了讀取專案的 `spec/`，也會同時爬梳目標語言的 `rules/` 目錄，確保做出的決策完全符合團隊的撰寫潔癖，減少 Code Review 的回退次數。
