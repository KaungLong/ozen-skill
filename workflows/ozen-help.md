---
description: 顯示 Ozen Team 所有可用指令與幫助說明
---

# /ozen help

> **[🤖 Claude Code 指令]** 當使用者呼叫 `/ozen help` 時，請**直接將下方的表格格式化成友善的 Markdown 回覆給使用者**，並加入溫暖的招呼語。不要在背景執行其他的分析或搜尋操作。

## 🚀 Ozen Team 核心開發指令

| 指令 | 說明 |
|------|------|
| `/ozen spec <feature>` | ✍️ 撰寫 Gherkin 行為規格 (SDD) |
| `/ozen test <feature>` | 🧪 從 Gherkin 生成測試 (TDD Red 階段) |
| `/ozen screen <畫面>`  | 📱 實作 UI 畫面與邏輯 (TDD Green 階段) |
| `/ozen build <平台>`   | 🏗️ 構建應用程式驗證 (例如 Android, iOS) |
| `/ozen fix <問題>`     | 🐛 針對錯誤進行排查與修復 |

## 🛠️ 管理與工具指令

| 指令 | 說明 |
|------|------|
| `/ozen review`         | 🧐 啟動 Code Reviewer 進行程式碼審查 |
| `/ozen status`         | 📊 產出目前的專案狀態與健康度報告 |
| `/ozen checkpoint`     | 💾 持久化當前的技術決策與進度到 CHANGELOG |
| `/ozen research <主題>`| 📚 啟動架構師研究，蒐集最佳實踐與實作參考 |
| `/ozen add-skill <需求>`| 🧩 動態尋找並安裝外部套件或擴充技能 |
| `/ozen triage <輸入>`  | 🚦 自動分流您模糊的需求，決定下一步該走哪條工作流 |
| `/ozen help`           | 🆘 顯示此幫助選單 |

> 💡 **Ozen Team 核心理念**：我們嚴格遵循 Context 控制與職責分工。如果有破壞性操作 (例如刪除整個資料庫或強制 Git Push)，系統的 `.hooks` 防線會主動跳出確認框，請您安心下指令開發！
