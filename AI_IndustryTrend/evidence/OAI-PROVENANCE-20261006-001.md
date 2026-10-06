---
id: "OAI-PROVENANCE-20261006-001"
category: "I-7"
company: "OpenAI"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-06"
updated_at: "2026-10-06"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# textGrain의 단계적 제공과 검출 한계

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-10-05 발표 | [rollout; How watermarking performs; What watermark does not tell you](https://openai.com/index/eu-text-provenance/) |

## 확인한 내용과 조건

- 일부 API model에서 글로벌 opt-in 가능, 기본 off. EU ChatGPT·Codex eligible text output은 향후 몇 주 rollout, detector는 승인 연구자·전문기관 초기 제한 접근이다.
- 자사 영어 ELI5 기반 평가: target false-positive 1%에서 psychology 등 200-token 약 80%, 400-token 약 95% 검출. 수학처럼 단어 선택이 제한되면 더 낮다.
- 별도 400-token 편집 실험에서 동의어 교체 10%는 약 92%→66%, 25%는 17%로 검출이 낮아졌다. 서로 다른 평가 조건을 같은 baseline으로 섞지 않는다.
- 표식은 사용자 신원·사람 기여량·소유권·정확성을 입증하지 않는다. 미검출도 사람 작성의 증거가 아니다.

## 검증 수준·한계

공급자 평가이며 한국어·실제 편집·번역에서 독립 재현하지 않았다. 1%는 설정한 오탐 목표이며 문서별 확정 판정 확률이 아니다. rollout·future open source 계획을 전 고객 GA로 쓰지 않았다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.
