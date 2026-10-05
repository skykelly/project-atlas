# 영업·마케팅 AI 활용 사례

[Atlas 안내](../README.md) · [변경 이력·다음 조사](LOG.md)

## 카테고리

| 코드 | 카테고리 |
| --- | --- |
| 1-1 | [신규 고객 획득](1-1_customer_acquisition.md) |
| 1-2 | [전환율 상승](1-2_conversion.md) |
| 1-3 | [객단가·Mix 개선](1-3_order_value_mix.md) |
| 1-4 | [재구매·LTV 확대](1-4_retention_ltv.md) |
| 1-5 | [신규 수익모델](1-5_new_revenue_models.md) |
| 2-1 | [마케팅 운영비 절감](2-1_marketing_cost.md) |
| 2-2 | [영업 운영비 절감](2-2_sales_cost.md) |
| 2-3 | [CS·케어 비용 절감](2-3_customer_care_cost.md) |
| 2-4 | [운영 판단력·실행력](2-4_decision_execution.md) |
| 2-5 | [리스크·품질 비용](2-5_risk_quality.md) |

## 어떻게 읽고 갱신하는가

카테고리 문서에서 연구 질문·사례 목록·종합을 읽고, 연결된 cases의 개별 문서에서 적용 내용·성과·출처·검증 상태를 확인한다. 같은 사례는 한 번만 작성하고 여러 카테고리에서 연결한다.

수정 기준은 **Markdown**이다. 사례 사실·근거는 해당 사례 문서, 비교·시사점은 카테고리 문서, 변경·보류·다음 조사는 LOG.md에 둔다. 별도 출처 DB나 편집용 JSON을 함께 관리하지 않는다.

## 초기 자료와 현재 상태

2026-10-05에 기존 117개 레코드를 ID·카테고리 그대로 개별 Markdown 초안으로 이관했다. 전부 원문 미검토 상태이며, 기존 verified 값은 legacy_verified로 보존했다. 등록일과 원문 확인일을 구분하고 누락된 분류는 임의로 채우지 않았다.

[원본 JSON](../data/AI_SalesMarketing/seed/cases_updated_all.json) · [기존 조사 보고서](../data/AI_SalesMarketing/seed/cases_update_report.md) · [이관 당시 HTML](../data/AI_SalesMarketing/seed/ax_cases_atlas.html)

위 세 파일은 당시 원본이다. 현재 위키를 수정해도 자동으로 바뀌지 않으며, 최신 내용은 Markdown을 기준으로 읽는다.

## 새 사례의 최소 형식

cases 아래에 고유 ID.md를 만든다. 문서 상단에는 id, category, company, tags, review_status, source_checked_at, updated_at을 기록한다. topic과 ai_mode는 근거가 있을 때만 넣는다. seed에서 가져온 문서만 seed_added_date와 legacy_verified를 유지한다.

본문은 요약 → 적용 내용 → 성과와 측정 조건 → 출처와 검증 → 한계와 다음 확인 순서로 작성한다. 출처별 URL·게시일·확인일과 주장별 근거 위치를 같은 문서에 기록한다. 원문을 읽지 않았다면 source_checked_at은 null로 둔다.

지표는 가능하면 값·단위·기간·표본·비교 대상·근거를 함께 적고, 실제 성과·목표·예측·자기 보고를 구분한다. LG 적용 아이디어는 가설로 표시한다.
