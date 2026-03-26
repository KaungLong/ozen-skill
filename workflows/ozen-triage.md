---
description: 自動分流模糊需求為標準工單
---

# /ozen triage <輸入>

// turbo-all

1. **載入角色思維**
   - 讀 `roles/triage-manager.md` — 專職分流管理員

2. **辨識與提煉**
   - 判斷輸入類型（Bug / Feature Request / Improvement / Question）
   - 從自然語言中提煉影響範圍、嚴重程度、期望行為
   - 若資訊不足，主動向使用者追問（遵守 Context-First 原則）

3. **比對現有規格**
   - 掃描 `spec/features/*.feature`、`spec/SCREENS.md`、`ERROR_JOURNAL.md`
   - 確認是否與已有規格重疊或衝突

4. **生成工單與路由建議**
   - 按 Feature Checklist Template 格式產出標準 Checklist
   - 建議接下來走哪條 `/ozen` 指令
   - 展示結果，等待使用者確認後才轉交
