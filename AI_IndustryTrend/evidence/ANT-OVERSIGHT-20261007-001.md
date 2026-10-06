---
id: "ANT-OVERSIGHT-20261007-001"
category: "I-7"
company: "Anthropic"
tags: ["industry_trend", "2026", "market_deep_dive"]
review_status: "reviewed"
source_checked_at: "2026-10-07"
updated_at: "2026-10-07"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# Agent 감시 coverage·지연·차단의 분모

[주제 목차](../README.md)

## 원문·근거 위치

[Measurements for understanding the pace of AI development inside frontier labs](https://www.anthropic.com/institute/measuring-pace-of-ai-development). 최초 게시일은 열람 HTML에 미표시; 2026년 8월 관측과 Appendix Oversight를 2026-10-07 확인했다. 게시일을 임의로 10월로 지정하지 않았다.

## 공개 관측

| 항목 | 8월 내부 플랫폼 보고 |
|---|---|
| online 차단 | 10억 decision 초과 중 0.002%, 약 47,000건당 1건 |
| online coverage | 해당 플랫폼 행동 100% 실행 전 monitor 통과 |
| offline coverage | 해당 플랫폼 행동 100% 사후 수집 |
| offline flag | transcript 1,000건당 약 1~2개 추가 검토 |
| 검토 지연 | online 차단의 사람 검토 1주 내; offline 우선순위 flag 약 주 50개 사람 검토 |

## 조건·한계

자사에서 가장 많이 사용하는 연구·engineering 플랫폼만의 관측이다. 모든 Anthropic 제품·고객 Agent·세계 Agent의 모집단이 아니다. decision·transcript·Agent·사고의 단위가 다르다. coverage는 경로 포괄 여부이며 차단률은 위험 발생률·검출률·미탐률을 제공하지 않는다. 수집은 즉시 사람 검토를 뜻하지 않는다. 보고서의 다른 automation·compute 지표와 합산하지 않았다. 연결된 risk report·METR 감사 전문·원시 로그를 독립 검증하지 않았다.
