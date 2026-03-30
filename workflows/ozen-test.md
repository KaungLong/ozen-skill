---
description: TDD 第一步 — 從 Gherkin 轉為測試程式碼，先跑出 Red
---

# /ozen test <feature>

// turbo-all

1. **確認角色已載入**
   - Gate 1 已載入全部角色，qa-engineer 的測試思維在此階段主導

2. **讀取 Gherkin**
   - 讀 `spec/features/{feature}.feature` — 每個場景對應一個測試案例

3. **生成測試**
   - 在專案的測試目錄下建立測試檔案（路徑與命名依 spec/TECH_SPEC.md 慣例）
   - 每個 Gherkin 場景 → 一個測試函數
   - 使用 `// Given` / `// When` / `// Then` 註解對應 Gherkin 步驟
   - 測試名稱清晰描述場景行為

4. **執行測試**
   - 使用專案定義的測試指令（查 spec/TECH_SPEC.md 的構建指令）
   - 預期結果：🔴 **全部 FAIL**（因為邏輯尚未實作或需修正）
