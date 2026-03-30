---
description: SDD 第一步 — 撰寫 Gherkin 行為規格 + 按需架構設計
---

# /ozen spec <feature>

// turbo-all

1. **載入全部角色**
   - 讀 `roles/architect.md` — 架構邊界
   - 讀 `roles/qa-engineer.md` — 測試思維
   - 讀 `roles/ui-engineer.md` — UI 實作
   - 讀 `roles/platform-engineer.md` — 跨平台
   - 讀 `roles/recorder.md` — 記錄規範
   - **每個角色依自身「何時介入」判斷本次是否參與**

2. **讀取需求**
   - 讀 `spec/GAME_RULES.md` — 遊戲規則定義
   - 讀 `spec/SCREENS.md` — 相關畫面的 UI 行為
   - 讀已有的 `spec/features/*.feature` — 避免重複
   - 讀已有的 `spec/design/*.md` — 瞭解已有架構決策

3. **架構設計判斷（按需）**
   - 評估 feature 是否滿足以下任一條件：
     - 需要新的跨平台抽象層（具體機制查 spec/TECH_SPEC.md）
     - 涉及 ≥2 個模組的交互
     - 引入新依賴或新技術
     - 包含難以用 Gherkin 表達的系統約束（效能、併發、DI 配置）
   - **若符合** → 建立 `spec/design/{feature}_design.md`
   - **若不符合** → 跳過此步驟，直接撰寫 Gherkin

4. **撰寫 Gherkin**
   - 建立 `spec/features/{feature}.feature`
   - 格式：同一檔案內中文版在上、英文版（以 # 註解）在下
   - 涵蓋：正常流程、邊界條件、異常情況
   - 使用 `場景大綱` + `例子` 處理參數化場景

5. **驗證完整性**
   - 確認中英文版行為一致
   - 確認每個場景都是可測試的
   - 若有 design 文件，確認 Gherkin 場景涵蓋設計中定義的所有對外行為
