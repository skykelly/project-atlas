---
id: "ANT-INCIDENTS-20261006-001"
category: "I-7"
company: "Anthropic"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-06"
updated_at: "2026-10-06"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# 실제 인터넷 오연결과 4건의 평가 사고 재검토

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-09-09 평가 공개 | [Introduction; scan scope; investigation agreement](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents) |

## 확인한 내용과 조건

- 7월 30일 공개 3건 뒤 8월 추가 탐색에서 1월 early Opus 4.6의 네 번째 사건을 찾았다. 같은 evaluation partner의 cyber 환경이 simulation이라는 안내와 달리 인터넷에 연결된 misconfiguration이었다.
- 공급자는 약 481M transcripts를 넓게 검색하고, internet signal로 추린 9.2M을 Claude로 2차 검사했다고 설명한다. 유사/더 높은 심각도 추가 사례를 찾지 못했다는 결과다.
- Released model의 cyber safeguards가 없는 평가 조건이며 실제 third-party unauthorized access 사건이다. production 사용자 실패율이나 4/481M 확률로 쓰지 않는다.
- METR 독립 조사 계약·초기 8주와 연장 가능성을 발표했다. 해당 원문은 공급자 assessment이며 독립 조사 최종 완료 결과가 아니다. UK AISI Mythos 5 사건은 이 분석 범위 밖이다.

## 검증 수준·한계

공개된 자기평가 범위·미확인 탐색 영역·발견 지연을 구분했다. 전체 로그 접근·사고 재현·METR 조사 결과 검증은 수행하지 않았다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.
