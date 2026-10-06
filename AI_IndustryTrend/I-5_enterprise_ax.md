# I-5. Enterprise AX·업무 플랫폼

[주제 목차](README.md) · [Agent 실행](I-3_agents_execution.md) · [기업 지식](I-4_knowledge_data_memory.md) · [인프라·배포](I-6_infrastructure_deployment.md) · [변경 이력](LOG.md)

조사 범위 **2026-01-01~2026-10-06**, 현재 가격·문서 확인일 **10-06**. AX는 기업의 업무·역할·운영을 AI에 맞게 재설계하는 것을 뜻한다. 발표·설문·공급자 사례·분석 제안을 구분했다.

## 1. AI 도입과 업무 변화는 다른 단계다

직원에게 AI 도구를 제공하면 초안·검색·요약을 빠르게 만들 수 있다. 하지만 기업의 최종 결과는 여러 사람과 시스템을 통과한다. 보고서 생성이 빨라져도 데이터 확인·승인·정정·후속 실행이 그대로라면 업무 전체의 지연은 크게 줄지 않을 수 있다. 2026년 플랫폼 경쟁은 이 연결 지점을 공동 workspace·역할별 Agent·업무 실행·비용 관리로 확장하고 있다.

| 변화 단계 | 실제로 바뀌는 것 | 완료를 판단하는 기준 |
|---|---|---|
| 접근 | 승인 도구·계정·자료 연결 | 접근과 실제 사용을 각각 측정 |
| 개인 보조 | 초안·검색·코딩 | 검수 후 수락된 결과·시간 |
| 과업 위임 | 여러 단계의 실행 | 최종 상태·부작용·예외 처리 |
| 팀 재설계 | 담당·승인·공유·handoff | 전체 cycle time·재작업 |
| 기업 운영 | 예산·역할·지식·통제 | 유지 가능한 비용·성과·책임 |

이 단계는 분석 틀이며 모든 조직이 같은 순서를 밟는다는 실증 결과가 아니다. 중요한 것은 도입률을 결과로 대체하지 않는 것이다. Agent 수·좌석 수·token 사용량은 활동을 보여 주지만 수익·품질·고객 경험은 별도 측정이 필요하다.

## 2. 2026년 조사에서 드러난 실행 간극

| 관측 | 값 | 범위·읽는 방식 | 근거 |
|---|---:|---|---|
| pilot의 40% 이상 production 이관 | 응답자 25% | 2025년 8~9월 리더 조사, 2026년 보고 | [Deloitte](evidence/DEL-AX-20261006-001.md) |
| 3~6개월 내 같은 수준 예상 | 54% | 전망, 사후 달성 실적 아님 | [Deloitte](evidence/DEL-AX-20261006-001.md) |
| 핵심 process 재설계 | 30% | 자기보고, 전체 기업 전수 비율 아님 | [Deloitte](evidence/DEL-AX-20261006-001.md) |
| process 변화 거의 없는 surface 사용 | 37% | 다른 설문 문항과 단순 합산 금지 | [Deloitte](evidence/DEL-AX-20261006-001.md) |
| Frontier Professionals | 3,233/20,000, 약 16% | 2026년 AI 사용 지식근로자 설문 | [WTI](evidence/MS-WORK-20261006-001.md) |
| AI 실험을 위한 관리자 지원 체감 | 리더 78%·직원 59% | 역할별 자기보고의 19%p 차이 | [WTI](evidence/MS-WORK-20261006-001.md) |

Deloitte는 24개국 AI 관련 senior leader 3,235명을 2025년에 조사했다. WTI는 2026-02-18~04-07 10개 시장의 AI 사용 지식근로자 20,000명을 조사하며 미사용자를 제외했다. 한국은 WTI 표본 시장에 없다. 두 결과는 ‘세계 기업의 현재 AI 도입률’로 직접 비교할 수 없다.

WTI의 조직 요인 67%·개인 요인 32%는 자기보고 AI impact와 관련된 분석이다. 조직 문화를 바꾸면 생산성이 67% 오른다는 인과 효과가 아니다. 다만 직원 개인의 사용 능력과 관리자·보상·업무 구조를 함께 살펴야 한다는 분석 근거로 읽을 수 있다.

## 3. 주요 플랫폼은 어느 업무 접점을 확장하는가

| 플랫폼 | 2026년 방향 | 제공 조건·단계 | 조직의 확인 지점 |
|---|---|---|---|
| Microsoft Copilot | Home·Office 편집·Code·Autopilot | 09-25 Frontier rollout, Autopilot private preview 확대, Managed Runtime preview | M365 맥락·역할·구독과 UBB 비용 |
| OpenAI | Dots·Space·Pages·팀 tasks·Slack/Teams | 09-29 Dots eligible markets·plan 조건, enterprise admin beta 기본 off | 지속 업무 owner·연결 tool·공동 자료 |
| Google Gemini Enterprise | 직원 app와 Agent Platform 통합 | 04-22 출시·확장 발표, 개별 기능 조건 별도 | Apps·data·identity·registry·workflow |
| Salesforce | Help Agent·self-service·해결 과금 | 7월 제공 발표, 현재 $2/resolution | CRM action·knowledge·과금 해결 정의 |
| ServiceNow | 역할별 end-to-end AI specialists | 5월 L1 IT·CRM·employee available, 다른 specialist는 예정 단계 구분 | case·CMDB·승인·audit·예외 |
| SAP | Joule·업무 transaction·Agent Hub | mobile·Hub GA, Work/A2A 계획과 runtime 공동 개발 분리 | ERP 권한·business rule·transaction |

[Microsoft](evidence/MS-WORK-20261006-001.md) · [OpenAI](evidence/OAI-WORK-20261006-001.md) · [Google](evidence/GOO-WORK-20261006-001.md) · [Salesforce](evidence/SF-OUTCOMES-20261006-001.md) · [ServiceNow](evidence/NOW-WORK-20261006-001.md) · [SAP](evidence/SAP-WORK-20261006-001.md).

비교는 기능 개수의 순위가 아니다. 기존 조직의 일상 접점이 M365·ERP·CRM·ITSM·Google Cloud 중 어디에 있고, 업무 완료를 어떤 시스템이 기록하는지에 따라 통합 비용이 다르다. 새로운 AI 화면을 추가하는 비용뿐 아니라 기존 권한·검수·예외·사람 간 인수인계가 어떻게 이어지는지를 확인해야 한다.

## 4. 공개 성과는 범위가 좁을수록 해석이 명확하다

| 공개 보고 | 수치 | 의미와 제한 |
|---|---|---|
| Salesforce 자사 help site | 430만 inquiries·70% 해결 | 기간·case mix·재접촉 미공개, 일반 고객 전체 성과 아님 |
| ServiceNow 자사 assigned IT cases | 인간보다 99% 빠른 해결 | 배정된 범위·절대 시간·동일 품질 미공개 |
| 익명 restaurant franchise | 초기 추천 수락률 20%; 평균 10분/case 절감 | 지식 검색 1단계 개선 보고, 사후 수락률·기간 미공개 |
| SAP LC Waikiki 질문 조회 | 최대 10분→약 3초; 효율 +70%·수동 오류 -50% | 조회 속도와 효율·오류는 서로 다른 지표 |
| Google Capcom testing | 월 30,000시간 이상 | 기계 test 시간, 사람 노동 대체 시간 아님 |
| Google Tata Steel | 9개월 300개 이상 specialized agents | 배포 규모, 실사용·ROI 수치 아님 |

[성과 조건](evidence/SF-OUTCOMES-20261006-001.md) · [ServiceNow 조건](evidence/NOW-WORK-20261006-001.md) · [SAP 조건](evidence/SAP-WORK-20261006-001.md) · [Google 조건](evidence/GOO-WORK-20261006-001.md).

각 수치는 공급자 보고이며 이번 조사에서 독립 재현하지 않았다. 특히 속도 향상을 인력 절감으로 바로 바꾸면 오류가 생긴다. 남은 업무의 검수·예외가 늘거나 절약한 시간이 다른 결과를 만드는 데 쓰일 수 있기 때문이다. 실무에서는 사람의 touch time과 대기 포함 전체 cycle time, 재작업·품질을 함께 측정해야 한다.

ServiceNow의 익명 사례는 지식 articles가 19,000개 이상이어도 추천 수락이 낮을 수 있음을 보여 준다. 기사 수 자체보다 최근 case와의 관련성·중복·정책이 중요했다는 공급자 설명이다. 지식과 실행의 연결 조건은 [I-4](I-4_knowledge_data_memory.md)에서 다룬다.

## 5. ‘해결 과금’은 업무 결과의 정의부터 읽어야 한다

Salesforce 현행 list price는 Help Agent **$2/resolution**이다. 그러나 resolution이 어떤 조건으로 집계되는지 읽지 않으면 실제 총비용을 예측하기 어렵다. 표의 조건은 10-06 확인한 공식 billing 문서다.

| 항목 | 공개 조건 | 조직이 추가로 볼 것 |
|---|---|---|
| 기본 resolution | 최소 각 2개 메시지·응답, 긍정 feedback 또는 미feedback·미escalation 등의 조건 | 실제 backend 처리·재접촉·반복 문의 |
| Chat·messaging | 최대 2시간 단위, 초과 시 추가 | 같은 문제의 여러 세션 |
| Voice | 10분 단위 | 긴 통화의 추가 resolution |
| Email | 3일 단위 | 장기간 열린 issue |
| 제외·예외 | abandon·부정 feedback·일부 escalation 제외, login/member 예외 | 계약·channel·license 조건 |

[과금 근거](evidence/SF-OUTCOMES-20261006-001.md). 과금상 성공은 ‘문제가 다시 발생하지 않았다’라는 사업 지표와 같지 않다. 또한 Salesforce의 다른 conversation·Flex Credit 가격과 같은 단위로 혼동하면 안 된다. base Service Cloud·integration·통신·검수·운영비를 더해 수락된 결과당 비용을 비교한다.

Microsoft도 9월 발표에서 일상 구독 USL과 장기 agentic work의 UBB를 분리했다. ‘구독을 샀다’는 사실만으로 Cowork·Code·Autopilot 사용량 비용이 모두 포함된다고 가정하지 않는다. [조건](evidence/MS-WORK-20261006-001.md)

## 6. 재설계할 것은 prompt보다 업무의 연결이다

**설명 예시**로 주간 공급자 검토를 맡긴다고 하자. 자료 수집·변동 분석·보고서 초안은 Agent가 수행할 수 있지만, 누가 최종 기준을 결정하고 협력사에 연락하며 계약을 바꾸는지까지 정해야 업무가 완결된다. 담당자가 불명확한 상태에서 자동 보고서만 늘면 검토 backlog가 커질 수 있다.

| 업무 구성 | 설계할 경계 | 운영 책임 |
|---|---|---|
| 입력 | 대상·기간·자료·권한 | data/knowledge owner |
| 판단 | 기준·예외·보류 | business owner |
| 실행 | 읽기·쓰기·금액·대상 제한 | system owner |
| 검수 | 수락 기준·표본·오류 등급 | 전문가·quality owner |
| 예외 | 사람에게 넘길 조건·응답 시간 | 실제 담당 팀 |
| 개선 | 실패·변경·cost·사용 이력 | process/AI operations |

이 표는 적용 제안이다. 개인마다 잘 쓰는 prompt를 공유하는 것에서 더 나아가, 반복 가능한 업무 기준·skills·검수·실행 경계를 관리해야 한다. OpenAI·Google·Microsoft의 공동 workspace와 SAP·ServiceNow의 process context는 이 연결을 제품화하는 서로 다른 접근으로 볼 수 있다.

## 7. 성과·원가를 업무 단위로 측정

| 측정 축 | 권장 관측 | 해석 주의 |
|---|---|---|
| 채택 | 승인 사용자·실사용·반복 사용 | 좌석 수와 사용률 구분 |
| 완료 | end-to-end success·재접촉 | 도구 호출·답변과 구분 |
| 품질 | 오류·재작업·근거·고객 불만 | 빠른 실패를 개선으로 집계하지 않음 |
| 시간 | touch time·queue·cycle time | 한 단계의 속도를 전사 성과로 확대하지 않음 |
| 경제성 | 수락당 tokens·tools·검수·운영 | 절약 시간을 바로 cash savings로 환산하지 않음 |
| 확장 | 유지·갱신·owner·예외·교육 | pilot 성공 뒤 관리 부담 확인 |

**가상 계산**: 월 10,000개 과업, 기존 12분, 적용 후 AI 결과 검수 3분·실패 후 사람 처리 12분, 수락률 70%라면 사람 시간은 120,000분에서 66,000분으로 줄어든다(검수 30,000 + 실패 3,000×12=36,000). 차이 54,000분=900시간이다. 도구비·교육·운영·수락된 결과의 품질을 제외한 계산이며 실제 인력·현금 절감 성과가 아니다.

1. 동일한 업무 모집단과 quality 기준을 정한다.
2. AI를 쓰지 않는 기준선과 과업 난이도·기간을 맞춘다.
3. 성공·검수·예외·재접촉을 기록한다.
4. 수락률이 낮으면 지식·tool·workflow 원인을 먼저 수정한다.
5. 전체 비용과 품질이 유지되는 범위에서 확대한다.

## 8. 비교 종합

2026년 Enterprise AX는 직원 AI 접속과 자율 실행 플랫폼이 함께 확대되는 국면으로 읽을 수 있다. 공개 조사와 사례가 보여 주는 간극은 도구의 능력만으로 조직의 업무가 바뀌지 않는다는 점이다. 플랫폼 선택은 기존 업무 시스템·지식·권한·과금과 맞는지, 남은 사람의 역할이 명확한지로 판단해야 한다.

- 단일 반복 과업의 완료 정의·예외·owner를 먼저 고정한다.
- 개인 초안 생산과 공동 업무 위임을 각각 평가한다.
- preview·rollout·현재 접근을 확인한 뒤 일정에 반영한다.
- 실제 수락·품질·전체 cycle time·원가로 확장을 결정한다.

이는 적용 우선순위 제안이다. 기술의 실행·복구는 [I-3](I-3_agents_execution.md), 지식·권한은 [I-4](I-4_knowledge_data_memory.md), 공급·배포 경제성은 [I-6](I-6_infrastructure_deployment.md)에 연결한다. 현재 조사는 공개 원문 검토이며 내부 업무의 ROI를 측정하지 않았다.
