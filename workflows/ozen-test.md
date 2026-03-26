---
description: TDD 第一步 — 從 Gherkin 手動轉為 Kotlin 測試，先跑出 Red
---

# /ozen test <feature>

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
