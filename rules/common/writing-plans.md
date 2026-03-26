## 撰寫計畫守則 (Writing Plans)

當你（Agent）被要求撰寫 `implementation_plan.md` 或規劃任務步驟時，必須遵守以下嚴格的防呆與 TDD 紀律：

### 1. 零佔位符 (No Placeholders)
寫計畫時，假設執行者是「有技術但對專案零常識、沒品味、討厭寫測試的 Junior 開發者」。
- **絕對禁止**：寫入 `TODO`、`TBD`、`加入適當的錯誤處理`、`處理邊界情況`。
- **必須提供**：確切的目標檔案路徑 (`/path/to/file.ts`)、具體的指令、帶有程式碼片段的實作指引。

### 2. 微型任務粒度 (Bite-Sized Task Granularity)
每一個 Checklist 打勾項目 (`- [ ]`) 必須是一個 **單一動作 (2~5 分鐘內可完成)**。不能將「實作整個 API」當成一個步驟。

### 3. TDD 循環 (The TDD Loop)
任務步驟中，只要是新增邏輯，必須強迫執行完整的 TDD 紅綠燈循環。標準 Checklist 如下：
- [ ] **Step 1: Write the failing test** (寫測試，包含測試 Code 範例)
- [ ] **Step 2: Run test to verify it fails** (執行測試，並標明預期錯誤為 FAIL)
- [ ] **Step 3: Write minimal implementation** (寫最少的手動實作使其通過)
- [ ] **Step 4: Run test to verify it passes** (重新執行測試，預期為 PASS)
- [ ] **Step 5: Commit** (提供確切的 `git commit` 指令)

> **核心精神**：如果計畫中有任何一步沒有清楚交代「How (如何做)」，只有寫「What (做什麼)」，那這份計畫就是不合格的。
