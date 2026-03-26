---
description: 完整實作一個畫面 — 自動載入相關角色、技能和規格
---

# /ozen screen <畫面名稱>

// turbo-all

1. **載入角色思維**
   - 讀 `roles/architect.md` — 確認架構一致性
   - 讀 `roles/ui-engineer.md` — UI 實作思維
   - 讀 `roles/platform-engineer.md` — 平台差異與共享層邊界

2. **載入技能**
   - 讀與畫面最接近的 skill（如 `visual-design-foundations`、`interaction-design`、`accessibility-compliance`）
   - 若涉及狀態或資料流，補讀對應技術 skill

3. **讀取規格**
   - 讀 `spec/SCREENS.md` — 找到目標畫面的 UI 規格
   - 讀 `spec/DEVELOPMENT.md` — 確認技術棧和現有進度

4. **執行 implement-screen workflow**
   - 按 `workflows/implement-screen.md` 的步驟執行

5. **驗證**
   - 構建全平台確認零 error

6. **紀錄（Recorder）**
   - 讀 `roles/recorder.md`
   - 更新 `spec/DEVELOPMENT.md` 的待辦清單狀態
   - 寫入 `spec/CHANGELOG.md`
