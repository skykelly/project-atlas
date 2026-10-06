---
id: "OAI-COMPLIANCE-20261006-001"
category: "I-7"
company: "OpenAI"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-06"
updated_at: "2026-10-06"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# 감사 로그 30일 수집과 conversation route 전환

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-03-05·06-05 전환, 10-06 현행 확인 | [access; How it works; retention; deprecation notice](https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers) |

## 확인한 내용과 조건

- Enterprise·Edu workspace용이며 scope별 Admin key·owner/admin 권한을 요구한다. Append-only Compliance Logs Platform과 stateful 조회를 구분한다.
- 새 conversation logs 03-05 도입, 이전 stateful conversation route는 06-05 제거다. 모든 stateful API가 없어졌다는 뜻은 아니다.
- Logs Platform 보관 30일. 더 긴 보관은 고객이 지속 수집하고 자체 정책으로 저장하도록 안내한다.
- 삭제 API가 OpenAI 내부의 보안·감사 기록까지 삭제하는 기능은 아니다. 삭제 후 내부 보관 최대 30일 설명과 customer exported copy의 보관 책임을 구분한다.

## 검증 수준·한계

공개 문서 조건이다. Enterprise/Edu의 감사 접근을 모든 plan·일반 model API·memory의 동일 retention으로 전이하지 않았다. SIEM ingest·누락·삭제는 실측하지 않았다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.
