---
id: "ANT-CONTAINMENT-20261006-001"
category: "I-7"
company: "Anthropic"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-06"
updated_at: "2026-10-06"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# 모델·환경·외부 자료를 함께 제한하는 containment

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-05-25 게시 | [three defense components; HITL sandbox; user as injection vector](https://www.anthropic.com/engineering/how-we-contain-claude) |

## 확인한 내용과 조건

- 모델 guardrail, runtime/파일/network 경계, 외부 content·tool 권한을 함께 방어한다. 안전한 connector가 읽는 문서까지 안전하다는 보장은 아니다.
- Opus 4.7 Gray Swan Agent Red Teaming: 단일 시도 공격 성공 약 0.1%, adaptive 100회 약 5~6%. 같은 시도의 확률로 곱하거나 현재 모든 모델의 위험률로 일반화하지 않는다.
- Claude Code OS sandbox 뒤 permission prompts 84% 감소는 공급자 보고다. 승인 횟수 감소와 공격 성공 감소는 다른 지표다.
- 2026-02 통제된 내부 phishing red-team에서 악성 prompt 재시도 25회 중 24회 credential 전송. 실제 전 고객 침해율이 아니며 사용자 경로로 들어온 지시도 환경 경계를 필요로 한다.

## 검증 수준·한계

공급자 실험·설계 설명이다. 과업·harness·공격자·retry 조건이 달라 benchmark끼리 안전 순위를 만들지 않았다. 자체 환경의 containment를 테스트하지 않았다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.
