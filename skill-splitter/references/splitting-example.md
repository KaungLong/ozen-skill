# 拆分範例：大型 API 文件

此範例展示如何將一個過大的 API skill 拆分為模組化結構。

## 拆分前

```
api-skill/
└── SKILL.md (2000+ 行)
    ├── 認證說明
    ├── 用戶 API
    ├── 訂單 API
    ├── 支付 API
    ├── 通知 API
    └── 錯誤處理
```

**問題：**
- 每次載入都消耗大量 context
- 查詢用戶 API 時也載入了支付 API
- 難以維護和更新

---

## 拆分後

```
api-skill/
├── SKILL.md (150 行)
│   ├── 概述
│   ├── 認證流程
│   ├── 通用錯誤處理
│   └── 模組索引
└── references/
    ├── users.md       (200 行)
    ├── orders.md      (300 行)
    ├── payments.md    (250 行)
    └── notifications.md (150 行)
```

---

## 新的 SKILL.md 結構

```markdown
---
name: api-skill
description: 公司 API 整合指南。處理用戶、訂單、支付、通知 API 時使用。
---

# API Integration Skill

## 認證

所有 API 使用 Bearer Token 認證：

\`\`\`bash
Authorization: Bearer <token>
\`\`\`

## 通用錯誤處理

| 狀態碼 | 含義 | 處理方式 |
|--------|------|---------|
| 401 | 未授權 | 重新認證 |
| 429 | 頻率限制 | 等待後重試 |
| 500 | 伺服器錯誤 | 記錄並通報 |

## API 模組索引

根據任務載入對應模組：

| 模組 | 參考文件 | 使用場景 |
|------|---------|---------|
| 用戶 | [users.md](references/users.md) | 註冊、登入、資料查詢 |
| 訂單 | [orders.md](references/orders.md) | 建立、查詢、取消訂單 |
| 支付 | [payments.md](references/payments.md) | 付款、退款、帳單 |
| 通知 | [notifications.md](references/notifications.md) | 推播、郵件、簡訊 |
```

---

## 參考文件範例：users.md

```markdown
# Users API

## Table of Contents

1. [註冊用戶](#註冊用戶)
2. [用戶登入](#用戶登入)
3. [查詢用戶](#查詢用戶)
4. [更新用戶](#更新用戶)

---

## 註冊用戶

POST /api/v1/users

**Request:**
\`\`\`json
{
  "email": "user@example.com",
  "password": "securepass",
  "name": "John Doe"
}
\`\`\`

**Response:**
\`\`\`json
{
  "id": "usr_123",
  "email": "user@example.com",
  "created_at": "2024-01-01T00:00:00Z"
}
\`\`\`

## 用戶登入

POST /api/v1/auth/login

...
```

---

## 效益分析

| 指標 | 拆分前 | 拆分後 | 改善 |
|------|--------|--------|------|
| SKILL.md 大小 | 2000 行 | 150 行 | -92.5% |
| 單一任務載入 | 全部內容 | 僅相關模組 | -75% context |
| 維護難度 | 高 | 低 | 模組化 |
| 更新影響 | 全局 | 局部 | 降低風險 |
