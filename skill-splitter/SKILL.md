---
name: skill-splitter
description: Guide for splitting large skills into organized, modular components. Use when a skill exceeds 500 lines, contains multiple unrelated topics, or when context efficiency is critical. Provides patterns for progressive disclosure, indexing structures, and reference file organization.
---

# Skill Splitter

當 skill 內容過大或包含多個不同主題時，使用此指南將其拆分為更小、更有組織的模組。

## 何時需要拆分

滿足以下任一條件時，應考慮拆分：

| 情況 | 閾值 |
|------|------|
| SKILL.md 行數 | > 500 行 |
| 不同主題/領域數量 | ≥ 3 個獨立主題 |
| 單一參考文件大小 | > 10,000 字 |
| Context window 效率 | 多數內容僅特定場景使用 |

## 拆分策略

### 策略 1：按領域拆分 (Domain-Based)

適用於包含多個獨立領域的 skill：

```
my-skill/
├── SKILL.md              ← 核心流程 + 導航索引
└── references/
    ├── frontend.md       ← 前端相關
    ├── backend.md        ← 後端相關
    ├── database.md       ← 資料庫相關
    └── deployment.md     ← 部署相關
```

**SKILL.md 索引結構：**

```markdown
## 領域參考

根據任務領域載入對應參考：

- **前端開發**: 見 [frontend.md](references/frontend.md)
- **後端 API**: 見 [backend.md](references/backend.md)
- **資料庫操作**: 見 [database.md](references/database.md)
- **部署流程**: 見 [deployment.md](references/deployment.md)
```

### 策略 2：按框架/變體拆分 (Variant-Based)

適用於支援多種框架或平台的 skill：

```
cloud-deploy/
├── SKILL.md              ← 通用流程 + 選擇指南
└── references/
    ├── aws.md            ← AWS 特定
    ├── gcp.md            ← GCP 特定
    └── azure.md          ← Azure 特定
```

**SKILL.md 選擇邏輯：**

```markdown
## 平台選擇

1. 確認目標平台
2. 載入對應參考文件
3. 遵循平台特定流程

| 平台 | 參考文件 | 使用場景 |
|------|---------|---------|
| AWS | [aws.md](references/aws.md) | EC2, Lambda, S3 |
| GCP | [gcp.md](references/gcp.md) | GCE, Cloud Run |
| Azure | [azure.md](references/azure.md) | VM, Functions |
```

### 策略 3：按深度拆分 (Depth-Based)

適用於有基礎/進階層次的 skill：

```
data-processing/
├── SKILL.md              ← 快速入門 + 常見模式
└── references/
    ├── advanced.md       ← 進階技巧
    ├── optimization.md   ← 效能優化
    └── troubleshooting.md ← 疑難排解
```

**SKILL.md 結構：**

```markdown
## 快速入門

[基礎使用範例...]

## 進階功能

進階功能請參考以下文件：

- **複雜處理**: 見 [advanced.md](references/advanced.md)
- **效能優化**: 見 [optimization.md](references/optimization.md)
- **問題排解**: 見 [troubleshooting.md](references/troubleshooting.md)
```

## 索引結構設計

### 表格索引 (推薦)

```markdown
## 參考文件索引

| 文件 | 用途 | 載入時機 |
|------|------|---------|
| [api.md](references/api.md) | API 規格 | 呼叫 API 時 |
| [schema.md](references/schema.md) | 資料結構 | 處理資料時 |
| [errors.md](references/errors.md) | 錯誤處理 | 除錯時 |
```

### 條件式索引

```markdown
## 根據任務載入參考

**建立新專案時：**
→ 讀取 [setup.md](references/setup.md)

**修改現有程式碼時：**
→ 讀取 [patterns.md](references/patterns.md)

**效能問題時：**
→ 讀取 [performance.md](references/performance.md)
```

### 目錄結構索引 (適用於大型 skill)

```markdown
## 文件結構

references/
├── core/           ← 核心概念
│   ├── basics.md
│   └── principles.md
├── features/       ← 功能模組
│   ├── auth.md
│   ├── storage.md
│   └── messaging.md
└── guides/         ← 操作指南
    ├── migration.md
    └── debugging.md

根據需求載入對應子目錄文件。
```

## 參考文件格式規範

### 長文件目錄 (>100 行)

每個超過 100 行的參考文件應包含目錄：

```markdown
# API Reference

## Table of Contents

1. [Authentication](#authentication)
2. [Endpoints](#endpoints)
3. [Error Codes](#error-codes)
4. [Rate Limits](#rate-limits)

---

## Authentication
...
```

### 搜尋提示 (>10,000 字)

超大文件需在 SKILL.md 提供 grep 模式：

```markdown
## 大型參考文件

`references/full-api.md` 包含完整 API 文檔。

**搜尋模式：**
- 認證相關: `grep -i "auth\|token\|credential"`
- 錯誤處理: `grep -i "error\|exception\|fail"`
- 範例程式: `grep -A 10 "```"`
```

## 拆分檢查清單

執行拆分時依序確認：

- [ ] SKILL.md 僅保留核心流程 (<500 行)
- [ ] 每個主題有獨立參考文件
- [ ] SKILL.md 包含清晰的索引/導航
- [ ] 所有參考文件有明確的載入時機說明
- [ ] 長文件 (>100 行) 包含目錄
- [ ] 避免深層巢狀 (參考文件最多一層)
- [ ] 刪除重複內容 (資訊只存在一處)

## 反模式 (避免)

❌ **深層巢狀**: 參考文件引用其他參考文件
❌ **重複內容**: 同樣資訊出現在多個文件
❌ **無索引**: 拆分後沒有清晰的導航結構
❌ **過度拆分**: 每個小節都獨立成檔案
❌ **無載入時機**: 不說明何時該讀取哪個文件
