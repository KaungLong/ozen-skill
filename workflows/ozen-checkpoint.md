---
description: 把當前對話的關鍵資訊持久化到 spec/，防止 context 遺忘
---

# /ozen checkpoint

// turbo-all

1. **載入角色思維**
   - 讀 `roles/recorder.md`

2. **摘要當前進度**
   - 已完成的任務
   - 未完成的任務
   - 過程中的發現和決策

3. **更新 spec/ 持久記憶**
   - `spec/DEVELOPMENT.md` — 待辦狀態：⏳ → ✅ 或 🔧
   - `spec/CHANGELOG.md` — 本次對話的決策 + 變更 + 發現
   - `ERROR_JOURNAL.md` — 若有新錯誤
   - `skills/*/SKILL.md` — 若有新陷阱

4. **輸出摘要**
   - 告知用戶已持久化的內容
   - 若 context 見底，建議開新對話
