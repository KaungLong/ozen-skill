---
description: Ozen Team 指令入口 — 啟動角色 + 技能 + 工作流的完整鏈路
---

# /ozen — Ozen Team 調度指令

## 使用方式

```
/ozen spec <feature>         → 撰寫 Gherkin 行為規格（SDD）
/ozen test <feature>         → 從 Gherkin 生成 Kotlin 測試（TDD Red）
/ozen screen <畫面名稱>     → 實作畫面（TDD Green）
/ozen review                → 程式碼審查
/ozen build <平台>          → 構建驗證
/ozen fix <問題描述>        → 問題修復
/ozen status                → 專案狀態
```

---

## /ozen spec <feature>

> SDD 第一步：撰寫行為規格 + 按需架構設計，定義「什麼叫做正確」和「系統怎麼組裝」。

// turbo-all

1. **載入全部角色**
   - 讀 `.agents/roles/architect.md` — 架構邊界
   - 讀 `.agents/roles/qa-engineer.md` — 測試思維
   - 讀 `.agents/roles/ui-engineer.md` — UI 實作
   - 讀 `.agents/roles/platform-engineer.md` — 跨平台
   - 讀 `.agents/roles/recorder.md` — 記錄規範
   - **每個角色依自身「何時介入」判斷本次是否參與**

2. **讀取需求**
   - 讀 `spec/GAME_RULES.md` — 遊戲規則定義
   - 讀 `spec/SCREENS.md` — 相關畫面的 UI 行為
   - 讀已有的 `spec/features/*.feature` — 避免重複
   - 讀已有的 `spec/design/*.md` — 瞭解已有架構決策

3. **架構設計判斷（按需）**
   - 評估 feature 是否滿足以下任一條件：
     - 需要新的 `expect/actual` 跨平台抽象
     - 涉及 ≥2 個模組的交互
     - 引入新依賴或新技術
     - 包含難以用 Gherkin 表達的系統約束（效能、併發、DI 配置）
   - **若符合** → 建立 `spec/design/{feature}_design.md`，內含：
     - 技術決策與理由
     - 介面設計（interface / expect class 簽名）
     - 依賴方向與模組邊界
     - 需要的 DI 配置
   - **若不符合** → 跳過此步驟，直接撰寫 Gherkin

4. **撰寫 Gherkin**
   - 建立 `spec/features/{feature}.feature`
   - 格式：同一檔案內中文版在上、英文版（以 # 註解）在下
   - 涵蓋：正常流程、邊界條件、異常情況
   - 使用 `場景大綱` + `例子` 處理參數化場景
   - Gherkin 只描述用戶可觀察的行為，不描述實作細節（實作細節在 design 文件）

5. **驗證完整性**
   - 確認中英文版行為一致
   - 確認每個場景都是可測試的
   - 若有 design 文件，確認 Gherkin 場景涵蓋 design 中定義的所有對外行為

---

## /ozen test <feature>

> TDD 第一步：從 Gherkin 手動轉為 Kotlin 測試，先跑出 Red。

// turbo-all

1. **確認角色已載入**
   - Gate 1 已載入全部角色，qa-engineer 的測試思維在此階段主導

2. **讀取 Gherkin**
   - 讀 `spec/features/{feature}.feature` — 每個場景對應一個 @Test

3. **生成測試**
   - 建立 `commonTest/kotlin/.../domain/{Feature}Test.kt`
   - 每個 Gherkin 場景 → 一個 `@Test fun`
   - 使用 `// Given` / `// When` / `// Then` 註解對應 Gherkin 步驟
   - 測試名稱使用反引號中文：`` `想想正確猜出瞎掰人得2分`() ``

4. **執行測試**
   - `./gradlew :composeApp:allTests`
   - 預期結果：🔴 **全部 FAIL**（因為邏輯尚未實作或需修正）

---

## /ozen screen <畫面名稱>

> 完整實作一個畫面，自動載入相關角色、技能和規格。

// turbo-all

1. **載入角色思維**
   - 讀 `.agents/roles/architect.md` — 確認架構一致性
   - 讀 `.agents/roles/ui-engineer.md` — UI 實作思維

2. **載入技能**
   - 讀 `.agents/skills/compose-ui/SKILL.md` — Compose UI 元件與已知陷阱
   - 讀 `.agents/skills/decompose-navigation/SKILL.md` — 導航配置
   - 讀 `.agents/skills/koin-di/SKILL.md` — 依賴注入

3. **讀取規格**
   - 讀 `spec/SCREENS.md` — 找到目標畫面的 UI 規格
   - 讀 `spec/DEVELOPMENT.md` — 確認技術棧和現有進度

4. **執行 implement-screen workflow**
   - 按 `.agents/workflows/implement-screen.md` 的步驟執行

5. **驗證**
   - 構建全平台：`./gradlew :composeApp:compileDebugKotlinAndroid :composeApp:compileKotlinWasmJs :composeApp:compileKotlinIosSimulatorArm64`
   - 確認零 error

6. **紀錄（Recorder）**
   - 讀 `.agents/roles/recorder.md`
   - 更新 `spec/DEVELOPMENT.md` 的待辦清單狀態
   - 寫入 `spec/CHANGELOG.md`：決策、變更、發現

---

## /ozen review

> 對當前變更進行程式碼審查。

// turbo-all

1. **載入角色思維**
   - 讀 `.agents/roles/qa-engineer.md`

2. **載入技能**
   - 讀當前修改涉及的 skill（UI → compose-ui，導航 → decompose-navigation 等）

3. **執行 code-review workflow**
   - 按 `.agents/workflows/code-review.md` 的步驟執行

4. **紀錄（Recorder）**
   - 審查結果寫入 `spec/CHANGELOG.md`

---

## /ozen build <平台>

> 構建指定平台並驗證。平台：android | ios | web | all

// turbo-all

1. **讀取構建配置**
   - 讀 `spec/DEVELOPMENT.md` — 取得構建指令

2. **執行 build workflow**
   - 按 `.agents/workflows/build.md` 的步驟執行

---

## /ozen fix <問題描述>

> 修復問題，自動載入相關技能的已知陷阱清單。

// turbo-all

1. **載入角色思維**
   - 讀 `.agents/roles/platform-engineer.md`

2. **載入技能的已知陷阱**
   - 掃描 `.agents/skills/*/SKILL.md` 中的 `⚠️ 已知陷阱` 區塊
   - 比對問題描述，找出相關陷阱

3. **分析與修復**
   - 根據問題描述 + 陷阱清單 + 程式碼分析，提出修復方案
   - 實作修復

4. **驗證**
   - 構建全平台確認修復不破壞其他功能

5. **紀錄（Recorder）**
   - 若發現新陷阱，更新對應 skill 的 `⚠️ 已知陷阱`
   - 修復紀錄寫入 `spec/CHANGELOG.md`

---

## /ozen status

> 快速檢查專案狀態。

// turbo-all

1. **執行 status-check workflow**
   - 按 `.agents/workflows/status-check.md` 的步驟執行

---

## /ozen checkpoint

> 把當前對話的關鍵資訊持久化到 spec/，防止 context 遺忘。

// turbo-all

1. **載入角色思維**
   - 讀 `.agents/roles/recorder.md`

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

---

## /ozen research <主題>

> 深度搜索 + 結構化整理。調用 deep-research skill。

// turbo-all

1. **載入技能**
   - 讀 `.agents/skills/deep-research/SKILL.md` — 搜索方法論

2. **執行三維搜索**
   - 趨勢：`search_web("<主題> methodology best practice 2025")`
   - 實作：`search_web("<主題> GitHub project", domain="github.com")`
   - 深度：`search_web("<主題> architecture technical blog")`

3. **整理報告**
   - 按 skill 定義的報告結構輸出
   - 標註與 Ozen Team 的映射關係

4. **持久化（Recorder）**
   - 關鍵發現寫入對應 skill / spec
   - 研究結論寫入 `spec/CHANGELOG.md`

---

## 🚨 Feature Checklist Template

> **每次開發新 feature 時，必須將以下 checklist 展開到 task.md。**
> 每個 gate (🚪) 必須完成並標記後才能進入下一步。
> 這是防止跳步的強制機制。

```markdown
## [Feature Name]

### /ozen spec
- [ ] 🚪 Gate 1: 讀全部 5 角色（每個角色自行判斷是否介入）
- [ ] 🚪 Gate 2: 讀 `GAME_RULES.md` + `SCREENS.md` + 已有 features
- [ ] 🚪 Gate 3: 架構設計判斷（需要 design doc? Y/N → 記錄原因）
- [ ] 🚪 Gate 4: 撰寫 `{feature}.feature`（中英文）
- [ ] 🚪 Gate 5: 驗證完整性（中英文一致、場景可測試）

### /ozen test
- [ ] 🚪 Gate 6: 確認 qa-engineer 主導（Gate 1 已載入）
- [ ] 🚪 Gate 7: 讀 `{feature}.feature` 確認場景數
- [ ] 🚪 Gate 8: 撰寫 `{Feature}Test.kt`（場景 → @Test）
- [ ] 🚪 Gate 9: 執行測試 → 🔴 RED（貼上錯誤訊息）

### 實作
- [ ] 🚪 Gate 10: 寫 domain/presentation 程式碼
- [ ] 🚪 Gate 11: 執行測試 → 🟢 GREEN（貼上測試數）

### Recorder
- [ ] 🚪 Gate 12: 更新 `spec/CHANGELOG.md`
- [ ] 🚪 Gate 13: 更新 `spec/DEVELOPMENT.md`

### 收尾
- [ ] 🚪 Gate 14: `git add -A && git commit`
```

