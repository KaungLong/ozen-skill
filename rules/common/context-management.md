# 🧠 Context Management & Dynamic Loading 法則

這個法則是為了防止 Ozen Team 發生 "Lost in the Middle"（AI 遺忘指令）或 Context Window 全爆滿而設立的底線。

## 1. 技能動態載入 (Dynamic Skill Loading)
當你需要使用技能、工具或找尋解決方案時：
- 🚫 **絕對禁止** 嘗試一次讀取多個 `SKILL.md` 的內容。這會塞爆記憶體！
- ✅ **永遠優先讀取** 根目錄下的 `SKILLS_INDEX.md` 扁平化目錄。
- 只有當你在 `SKILLS_INDEX.md` 確定了某個技能 (如 `taste-skill`), 才可以去讀取那個特定的 `路徑/SKILL.md` 來看詳細使用說明。

## 2. 任務隔離機制 (Compartmentalization)
不要讓一個對話視窗承載無限長的工作流：
- 從 `產品經理審核` 到 `架構設計`，再到 `UI 實作`，請運用 **戰略性壓縮 (Strategic Compaction)**。
- 當一個角色完成工作，將產出總結寫成文件 (例如：`spec/PRODUCT_REVIEW.md` 或 `spec/build.md`)。
- 這樣下一個角色接手時，他的 Context 是全新且乾淨的，只需要讀取前一個角色的輸出檔案即可。

## 3. Quality Gates (品質閘門) 與驗證鐵律
為了防範「未驗證先宣告完成」的幻覺，每次執行重要任務 (如 Feature 實作或修復) 時，必須遵守 RPI 迴圈與分階段驗證。

### The Iron Law (驗證鐵律)
**"NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE"**
(沒有新鮮的驗證證據，就不准宣稱完成)

開發者(你) 在宣佈某個 Phase 結束前，必須**主動**經歷這四個步驟並張貼輸出：
1. **Identify**: 找出可以證明功能正確的指令 (如 `npm run build`, `npm test`)
2. **Run**: 實際執行該完整指令
3. **Read**: 讀取完整的 Stdout 輸出與 Exit code
4. **Verify & Claim**: 只有在確認輸出無誤後，才允許輸出完成聲明。絕對禁止使用「這應該會正確運作」、「Linter 通過了 (但忘記跑 Test)」等推測性字眼。

### 驗證清單
在滿足 Iron Law 的前提下，輸出以下自我檢查：
- [ ] Code Discovery 已執行（已了解舊有依賴與模式）
- [ ] 所有需求 Deliverables 已實作
- [ ] Lint 檢查通過 (需附上執行指令與輸出)
- [ ] 測試撰寫完畢且執行通過 (需附上執行指令與輸出)
- [ ] Code Review (如果是架構重要變更，需呼叫 Code Reviewer)
