---
description: 跨模型協作守則 — 利用多個 AI 模型互相檢驗，防止上下文退化。
---

# 🤖 Cross-Model Workflow (跨模型協作)

**參與角色**：Code Reviewer, 架構師, QA 工程師

當面臨「重大架構重構」、「長時間上下文導致 AI 開始遺忘或變笨 (LLM Degradation)」，或「需要極高正確性的核心業務邏輯」時，請使用 **Cross-Model Workflow**。

這是一種「不把雞蛋放在同一個籃子裡」的防禦性開發策略。

## 什麼是 Cross-Model Workflow？

利用兩個完全獨立的終端機環境（或兩個不同的 AI 代理/模型模型，例如 Claude 3.5 Sonnet 與 GPT-4o），一個負責 **Plan & Implement (計畫與實作)**，另一個專門負責 **QA & Verify (質檢與驗收)**。

## 標準操作流程

```text
┌─────────────────────────────────────────────────────────────┐
│              CROSS-MODEL COLLABORATION LOOP                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TERMINAL 1 (主要實作區)                  TERMINAL 2 (質檢區) │
│  使用預設的 Ozen Agent                   使用第二個 Agent     │
│  (例如: Claude)                          (例如: Copilot/GPT) │
│                                                             │
│  STEP 1: PLAN                                               │
│  負責拆解需求，產出 `spec/PLAN.md`。                         │
│                                                             │
│  ─────────────────────────▼───────────────────────────────  │
│                                                             │
│                                          STEP 2: QA REVIEW  │
│                                 審查 `PLAN.md`，找出盲區與    │
│                                 邊界極端案例，加上          │
│                                 "QA Finding" 標籤，不覆寫。   │
│                                                             │
│  ─────────────────────────▼───────────────────────────────  │
│                                                             │
│  STEP 3: IMPLEMENT                                          │
│  讀取更新後的計畫，                                           │
│  嚴格執行 RPI 迴圈實作。                                      │
│                                                             │
│  ─────────────────────────▼───────────────────────────────  │
│                                                             │
│                                          STEP 4: VERIFY     │
│                                 載入 `roles/code-reviewer.md`│
│                                 對實作結果進行無情審查，並   │
│                                 產出 CODE REVIEW REPORT。   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 觸發時機
1. **超過 50 次 Tool Calls**：當 Agent 上下文即將溢出，除了執行 `/ozen checkpoint` 之外，也可讓第二個 Agent 從乾淨的上下文接手審查。
2. **Review 指令**：當使用者呼叫 `/ozen review` 時，強烈建議在一個全新的 conversation 或隔離的子代理 (Subagent) 中載入 `roles/code-reviewer.md`。
