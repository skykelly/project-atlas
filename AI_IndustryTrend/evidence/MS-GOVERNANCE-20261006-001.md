---
id: "MS-GOVERNANCE-20261006-001"
category: "I-7"
company: "Microsoft"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-06"
updated_at: "2026-10-06"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# Agent 365의 상용 GA·통제 범위·요금

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-05-01 발표 | [GA; supported access table; local discovery; How to get started](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) |
| 2026-08-20 문서 갱신 | [Observe/Govern/Secure; availability; prerequisites](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) |

## 확인한 내용과 조건

- 05-01 Commercial GA, 사용자별 license다. 발표 가격 standalone USD15/user/month 또는 E7 포함이며 Agent 실행·모델 소비를 모두 포함한 가격으로 읽지 않는다.
- 사용자 위임·behind-the-scenes own access는 GA, team workflow own access는 발표 표에서 Public Preview다. Agent 365 전체 GA를 모든 하위 기능의 GA로 확대하지 않는다.
- Registry·Entra·Purview·Defender를 연결해 lifecycle·identity·DLP·threat monitoring을 관리한다. 현행 overview는 E5 사용 시 최적, 활성화를 위한 적격 license 조건을 안내한다.
- Windows local discovery의 초기 OpenClaw 범위·Frontier 조건과 향후 다른 Agent 확대는 별도다. May 글의 June 예정 asset mapping을 이번 확인만으로 전 고객 제공 완료로 쓰지 않았다.

## 검증 수준·한계

공급자 제품 설명이다. tenant·한국 계약 가격·기능별 배포·미등록 Agent 탐지율·방어 효과는 검증하지 않았다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.
