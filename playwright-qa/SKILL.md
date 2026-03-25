---
name: playwright-visual-qa
description: Uses Playwright to automatically open the browser, interact with elements, and capture screenshots for visual AI validation.
triggers: ["/playwright-qa", "run visual QA", "check UI rendering"]
---

# 👁️ Playwright Visual QA Skill

這個技能賦予了 Ozen Team 切實的「眼睛」，主要由 `🧪 QA 工程師` 調用。它能透過 Playwright 執行真實瀏覽器環境，對頁面進行互動並截圖，接著用語義視角 (Vision AI) 來親自把關 UI 是否跑版。

## 🛡️ 業界自動化測試守則 (Best Practices)

在 AI 驅動的 QA 流程中，為了防止機器人陷入「一直截到登入畫面」或「截到 Loading 白畫面」的地雷，**所有自動化腳本都必須嚴格遵守以下兩大機制：**

### 1. 登入狀態重用 (Authentication & `storageState`)
- 🚫 **絕對禁止**：讓 AI 每次擷取截圖前都在腳本裡重複寫 `fill('username')`、`fill('password')` 走 UI 登入。這不僅容易因為 MFA (雙重驗證) 失敗，還會大幅拖慢流程。
- ✅ **必須做法**：要求目標專案準備好一個全局憑證 (Global Setup)。系統必須預先透過腳本或 API 繞過登入，並產生一個 Session 檔案 (例如 `state.json`)。
- **實質作法**：在 AI 產生的測試腳本中，開啟瀏覽器時必須帶入該憑證：
  ```javascript
  const context = await browser.newContext({ storageState: 'state.json' });
  const page = await context.newPage();
  ```

### 2. 對抗「水合延遲」與 Flaky Tests (Hydration & Waits)
- 🚫 **強烈抵制**：使用 `page.waitForTimeout(5000)` 這類死硬的等待時間。
- 🚫 **減少依賴**：Playwright 官方已不建議仰賴 `waitForLoadState('networkidle')`，因為現代 Web App (如 Next.js) 常有背景輪詢 (Polling) 導致 network 永遠不會 idle。
- ✅ **必須做法**：要確保前端框架 (React/Vue/Kotlin JS) 已經完成「水合 (Hydration)」且畫面渲染完畢，**必須針對特定具體元素進行顯式等待**。
- **實質作法**：
  ```javascript
  // 取代死等，精確等待畫面核心元件完成渲染且可被點擊
  await page.waitForSelector('[data-testid="main-dashboard-grid"]', { state: 'visible' });
  await page.locator('.critical-action-button').waitFor({ state: 'attached' });
  ```

## 如何運作 (執行流)
1. **載入憑證**：讀取上一次的登入 Context (`state.json`)。
2. **啟動測試環境**：導航至 `localhost:3000` 或預期網址。
3. **顯式等待渲染**：用 `waitForSelector` 掛勾確實驗證畫面已 Hydrated。
4. **視覺除錯 (VQA)**：QA 工程師將讀取截圖，檢查排版、文字截斷與元件擁擠問題。
5. **產生報告**：將問題記錄在 `spec/BUGS.md`，並通知 UI 工程師修復。
