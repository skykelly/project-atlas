---
id: "AWS-EVALUATIONS-20261006-001"
category: "I-7"
company: "AWS"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-06"
updated_at: "2026-10-06"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# 온라인 trace 표본과 배포 전 평가의 결합

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-03-31 GA 발표 | [Online/on-demand; 13 evaluators; Ground Truth; nine Regions](https://aws.amazon.com/about-aws/whats-new/2026/03/agentcore-evaluations-generally-available/) |

## 확인한 내용과 조건

- 03-31 GA. Online은 live traces를 표본 추출해 채점하고, on-demand는 CI/CD·개발 regression test를 지원한다.
- 내장 evaluator 13개는 response quality·safety·task completion·tool usage를 다룬다. Ground Truth는 reference answer·session goal assertion·expected tool sequence를 사용한다.
- 사용자 정의 LLM judge 또는 Lambda의 Python/JavaScript 검사와 Observability 연결을 안내한다.
- GA 발표 9리전은 서울을 포함하지 않는다. 현행 계정·추가 리전은 확인하지 않았고 3월 발표 조건만 기록한다.

## 검증 수준·한계

13개 evaluator는 항목 수이며 정확도나 기업 안전성 점수가 아니다. 표본 trace 평가가 모든 transaction을 차단하거나 backend 최종 상태를 자동 보장하지 않는다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.
