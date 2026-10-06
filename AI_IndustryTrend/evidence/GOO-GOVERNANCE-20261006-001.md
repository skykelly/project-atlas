---
id: "GOO-GOVERNANCE-20261006-001"
category: "I-7"
company: "Google Cloud"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-06"
updated_at: "2026-10-06"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# Agent Identity·Gateway·Model Armor의 책임 분리

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-05-06 발표 | [Agent Identity; Agent Gateway; Runtime defense](https://cloud.google.com/blog/products/identity-security/whats-new-in-iam-security-governance-and-runtime-defense) |
| 2026-10-06 현행 확인 | [Authentication models; SPIFFE-based identity; identity lifecycle](https://docs.cloud.google.com/iam/docs/agent-identity-overview) |

## 확인한 내용과 조건

- 5월 발표에서 Agent Runtime의 Agent Identity는 GA, Agent Platform의 identity·Auth Manager·certificate manager 지원은 preview로 구분한다. Agent Security dashboard도 preview다.
- Identity는 주체·credential, Registry는 대상 목록, Gateway는 호출 경로·policy, Model Armor는 prompt/tool response inspection이라는 서로 다른 기능이다.
- 현행 문서는 고유 SPIFFE ID·X.509 certificate 24시간 유효와 자동 갱신, certificate-bound access token을 설명한다. 사용자 위임과 Agent 자체 권한을 구분하며 외부 서비스 auth manager를 통한 API key 경로도 남는다.
- 문서의 identity 수명·정책 통합은 모든 외부 도구의 동일한 인증 강도나 전체 제품의 현재 GA를 보장하지 않는다.

## 검증 수준·한계

문서 기반 구조 비교다. 실제 certificate rotation·권한 회수·MCP 우회·공격 탐지율·리전 지원은 테스트하지 않았다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.
