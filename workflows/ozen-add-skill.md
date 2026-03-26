---
description: 動態尋找並安裝外部擴充技能
---

# /ozen add-skill <需求>

// turbo-all

1. **載入角色思維**
   - 讀 `roles/librarian.md` — 專職技能庫圖書管理員

2. **了解需求與查閱排行榜**
   - 確認所需技術領域（如 TypeScript, DevOps）
   - 參考 `skills.sh` 等開源榜單的大廠級技能

3. **執行搜尋器 (CLI Search)**
   - `npx skills find <關鍵字>`
   - 嚴格遵守 Librarian 的品管防線：過濾掉安裝數 < 1000 的套件

4. **推薦與代客安裝**
   - 列出找到的優質技能與安裝量，請使用者確認
   - 若同意，執行 `npx skills add <技能名稱> -g -y` 進行安裝
