---
id: "SLEIGHT-MONITORS-20261007-001"
category: "I-7"
company: "Anthropic Fellows · Redwood Research · Anthropic"
tags: ["industry_trend", "2026", "market_deep_dive"]
review_status: "reviewed"
source_checked_at: "2026-10-07"
updated_at: "2026-10-07"
evidence_type: "primary_research_review"
independent_verification: "not_reproduced"
---

# 합성 transcript에서 드러난 monitor 맹점

[주제 목차](../README.md)

## 원문·근거 위치

[SLEIGHT-Bench: Finding Blind Spots in AI Monitors](https://alignment.anthropic.com/2026/sleight-bench/), 2026-05-19. Benchmark·Evaluating monitors·Results. 확인 2026-10-07.

## 평가 조건·관측

- 연구자가 설계한 합성 transcript 공격 40개·11유형. 실제 고객 공격 발생률 표본이 아니다.
- 공격의 정상 변형과 짝지어 1% 오탐 threshold를 보정한다. 반복 중 한 번 잡는 any-trial과 per-trial을 구분한다.
- 주요 Opus 4.6 설정에서 공격 50%는 10회 모두 미검출, 40개 중 8개만 안정적으로 검출했다고 설명한다.
- code 실행 monitor는 API 판독 방식보다 평균 호출 약 10배·출력 token 약 14배. ensemble은 추가 원가를 요구한다. 가격·청구 총액의 동일 배수는 아니다.
- 누적 file/object 상태·여러 세션·필수 단계 생략·권한 정당화 등 맹점을 제시한다. code 검증·전문 prompt가 일부를 개선해도 다른 유형을 악화시킬 수 있다.

## 한계

원 연구팀 블로그를 검토했고 연결된 논문 전문·데이터·모델 실험을 재현하지 않았다. 합성 자료의 현실성 한계와 의도적으로 어려운 표본 선택을 원문이 명시한다. 최신 model·전체 traffic·특정 한국 업무의 검출 성능으로 확대하지 않는다. 실제 실행 권한·egress·결과 검사와 함께 사용하는 운영 해석으로 연결한다.
