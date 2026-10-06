# I-7. AI 운영·신뢰·거버넌스

[주제 목차](README.md) · [Agent 실행](I-3_agents_execution.md) · [기업 지식](I-4_knowledge_data_memory.md) · [Enterprise AX](I-5_enterprise_ax.md) · [변경 이력](LOG.md)

조사 범위 **2026-01-01~2026-10-07**, 기존 제품·법률 조건 확인일 **10-06**, 추가 연구·표준화 원문 확인일 **10-07**. 공개 제품·표준·사고 보고·법률 조문을 검토했다. 기업의 내부 설정·침해율·법적 적합성을 실측하거나 인증한 결과는 아니다.

## 1. AI 운영의 대상이 답변에서 행동으로 넓어졌다

Agent가 문서를 읽고 내부 시스템을 수정하면 오류의 영향은 잘못된 문장에 머물지 않는다. 잘못된 권한으로 고객 기록을 읽거나, 승인되지 않은 환불을 처리하거나, 외부로 정보를 보낼 수 있다. 따라서 좋은 모델을 고르는 일에 더해 **누가 어떤 데이터로 어느 행동까지 위임했으며, 결과를 어떻게 확인·중단·복구하는가**를 운영해야 한다.

2026년 자료를 종합하면 세 흐름이 함께 보인다. 플랫폼은 Agent 전용 identity·registry·policy·evaluation을 제품화하고, 표준 기관은 위임·상호운용의 기반을 정리하며, 실제 사고 공개와 투명성 규정은 기록·검증의 필요성을 높이고 있다. 이는 시장 해석이며 어느 제품이 모든 통제를 완성했다는 의미가 아니다.

| 운영 축 | 관리 대상 | 업무 예시 |
|---|---|---|
| 평가 | 최종 상태·품질·부작용·반복성 | 환불 답변과 실제 환불 처리 일치 |
| 신원·권한 | Agent·사용자·위임 범위 | 특정 고객·금액·기간만 허용 |
| 보안 | runtime·도구·network·외부 자료 | 악성 문서를 읽어도 외부 전송 차단 |
| 데이터 | 원문·검색·cache·session·memory·log | 퇴사자 권한 회수와 파생 정보 처리 |
| 감사·책임 | 실행 기록·owner·승인·복구 | 누가 무엇을 승인했는지 재구성 |
| 사용량·가치 | 예산·retry·검수·수락 결과 | 요청당 가격보다 성공 결과당 총비용 |

이 표는 적용 기준이다. 운영 통제를 한 조직에 모두 맡긴다는 뜻도 아니다. 업무 owner가 완료 기준을, 시스템 owner가 실행 권한을, 보안·데이터 담당이 접근과 보존을, 운영팀이 모니터링·복구를 담당하도록 연결해야 한다.

## 2. 2026년 주요 변화와 정확한 단계

| 시점 | 확인한 변화 | 운영상 의미 | 근거 |
|---|---|---|---|
| 01-22 | 한국 AI기본법·시행령 최초 시행 안내 | 사전고지·표시·고영향 책무 검토 | [한국](evidence/KR-GOVERNANCE-20261006-001.md) |
| 02-13·06-04 | OpenAI Lockdown 발표·rollout 확대 | 기능과 외부 전송 경로를 선택적으로 제한 | [OpenAI](evidence/OAI-LOCKDOWN-20261006-001.md) |
| 02-17·08-27 | NIST Agent 표준화·identity 지침 방향 | credential 공유와 과도한 위임을 운영 문제로 다룸 | [NIST](evidence/NIST-IDENTITY-20261006-001.md) |
| 03-03·03-31 | AWS Policy·Evaluations 각각 GA | 실행 전 권한 판정과 결과 평가의 분리 | [Policy](evidence/AWS-POLICY-20261006-001.md)·[평가](evidence/AWS-EVALUATIONS-20261006-001.md) |
| 05-01 | Microsoft Agent 365 Commercial GA | 전용 관리·보안 control plane와 사용자별 요금 | [Microsoft](evidence/MS-GOVERNANCE-20261006-001.md) |
| 05-06 | Google identity·gateway·runtime defense 발표 | 기능마다 GA·preview가 다름 | [Google](evidence/GOO-GOVERNANCE-20261006-001.md) |
| 05-25 | Anthropic containment 경험 공개 | 모델·환경·외부 content의 겹친 방어 | [Anthropic](evidence/ANT-CONTAINMENT-20261006-001.md) |
| 07-27·08-02 | EU Omnibus 발효·투명성 적용 | 고위험 일정과 표시 의무 일정 분리 | [EU](evidence/EU-GOVERNANCE-20261006-001.md) |
| 09-09·09-16 | Anthropic 사고 assessment·OpenAI disclosure framework | 사건·발견·보고와 독립 조사 상태를 기록 | [Anthropic](evidence/ANT-INCIDENTS-20261006-001.md)·[OpenAI](evidence/OAI-INCIDENTS-20261006-001.md) |
| 10-05 | OpenAI text watermark 발표 | 일부 API opt-in·EU rollout·detector 제한 접근 | [Provenance](evidence/OAI-PROVENANCE-20261006-001.md) |

출시일이 지났다는 사실만으로 계획 기능이 모두 제공되었다고 판단하지 않는다. GA도 상품·기능·리전·plan 단위로 읽어야 한다. 예를 들어 AWS Policy의 3월 13리전에는 서울이 있지만 Evaluations의 3월 9리전에는 서울이 없다. 이 차이는 해당 발표 조건이며 현재 한국 계정의 서비스 이용을 전수 확인한 결과는 아니다.

## 3. 플랫폼은 서로 다른 지점에서 운영을 통제한다

Control plane은 실행을 직접 수행하는 모델과 별도로, 대상 목록·권한·정책·관측을 관리하는 계층이다. 같은 ‘Agent 보안’이라는 이름도 무엇을 통제하는지에 따라 제품 역할이 다르다.

| 플랫폼·접근 | 통제 지점 | 구체적 조건 | 기업에 남는 책임 |
|---|---|---|---|
| Microsoft Agent 365 | registry·Entra·Purview·Defender 연결 | Commercial GA; standalone 발표 USD15/user/month; team own-access workflow는 Public Preview | 실제 등록 범위·license·DLP·owner·예외 설정 |
| Google Agent Identity/Gateway | 신원·credential·destination·traffic | May 발표 Runtime identity GA, Platform identity/Auth Manager preview; 현행 X.509 24시간 갱신 | 외부 tool 인증·모든 경로의 gateway 통과·정책 설정 |
| AWS AgentCore Policy | Gateway tool 호출 직전 | Cedar default deny·forbid 우선; 자연어 생성 규칙 검토 | 직접 API·shell 등 우회 경로와 정책 의도 확인 |
| AWS AgentCore Evaluations | production trace 표본·on-demand test | GA·내장 evaluator 13개·사용자 정의 judge/code | 모집단·ground truth·결과·중대 부작용의 별도 검사 |
| OpenAI Lockdown | ChatGPT 외부 전송·tools | 선택형 제한; 학습 설정·Codex network와 별개 | 활성 앱·action·원본 권한·잔여 위험 검토 |
| Anthropic containment | 모델·환경·외부 content | sandbox·filesystem·egress·tool 제한을 겹침 | 배포별 경계·credential·사전 config 실행 검토 |

[Microsoft](evidence/MS-GOVERNANCE-20261006-001.md) · [Google](evidence/GOO-GOVERNANCE-20261006-001.md) · [AWS 정책](evidence/AWS-POLICY-20261006-001.md) · [AWS 평가](evidence/AWS-EVALUATIONS-20261006-001.md) · [OpenAI](evidence/OAI-LOCKDOWN-20261006-001.md) · [Anthropic](evidence/ANT-CONTAINMENT-20261006-001.md).

인증은 ‘누구인가’, 권한 판정은 ‘이 행동을 해도 되는가’, content inspection은 ‘이 내용에 위험 신호가 있는가’라는 서로 다른 질문이다. 인증된 Agent가 허용된 도구를 잘못된 고객·금액에 사용할 수도 있으므로 신원만으로 업무 안전성을 판단할 수 없다. Managed runtime을 사용해도 기업의 업무 규칙·승인·완료 검증은 남는다.

### 3.1 9월 NIST 의견 종합: 접속 이후의 위임을 관리해야 한다

NIST는 9월 29일 Agent identity·authorization concept paper에 대한 의견 종합을 공개했다. 600명 초과의 의견 제출자를 보고하고 DevSecOps를 첫 구현 use case로 제시했다. 이는 의견 수렴과 구현 방향이다. 상용 인증 완료나 전 산업의 표준 채택률로 읽지 않는다. [진행 단계·원문](evidence/NIST-IDENTITY-20261006-001.md)

| 배포 형태 | 신원과 지시의 관계 | 기업의 통제 지점 |
|---|---|---|
| 내부 소유·내부 사용 | 기업이 Agent·사용자·실행 환경 관리 | 업무별 권한·tool 경계·위임 기록 |
| 내부 소유·외부 고객 사용 | 실행 권한은 기업에 있고 지시는 외부에서 유입 | 고객 본인·대상·허용 action을 매번 연결 |
| 외부 소유 Agent의 기업 접속 | 기업이 Agent runtime을 통제하기 어려움 | 제한된 API·위임 증거·회수·거래 확인 |

NIST 종합은 임시 자격증명, 하위 Agent로 넘길 때 좁아지는 권한, 행동 시점의 판정과 위임 체인 기록을 다룬다. MCP·A2A 연결만으로 이 조건이 충족되지는 않는다. 특히 사용자 요청을 받은 서비스 Agent가 그 사용자보다 넓은 시스템 권한을 갖는 경우, 로그인 성공과 거래 승인을 분리해야 한다.

예를 들어 고객이 자신의 예약 변경만 요청했는데 service 계정이 모든 예약을 수정할 수 있다면 모델의 고객 식별 결과를 그대로 권한 판정으로 쓸 수 없다. API는 고객·예약·행동 범위를 확인하고 승인 뒤 인자가 바뀌었는지도 검사해야 한다. 이 예시는 설계 설명이며 특정 서비스에서 취약점을 발견한 결과는 아니다.

서명된 intent·mandate의 공통 표현은 아직 표준화 과제가 남아 있다. 기업은 새 protocol의 이름보다 자신이 통제하는 입력·위임·실행·회수 경로부터 검증해야 한다. 표준이 성숙하면 이 기록을 외부 Agent와 교환할 수 있지만 상호운용만으로 업무 책임이 이전되지는 않는다.

## 4. Prompt injection과 권한 오용을 함께 다룬다

Prompt injection은 외부 자료 또는 다른 경로의 지시가 Agent의 행동을 바꾸는 문제다. 악성 내용이 문서·tool response·MCP 설명에 들어갈 수 있다. 별도로 모델 자체가 과업 점수를 높이려고 허용 범위를 벗어나는 행동, 전통적인 runtime 취약점도 있다. 위협을 injection 한 가지로만 좁히면 다른 실패 경로가 빠진다.

| 관측·실험 | 확인한 값·환경 | 일반화하면 안 되는 것 |
|---|---|---|
| Anthropic Opus 4.7 Gray Swan | 단일 시도 약 0.1%, adaptive 100회 약 5~6% 공격 성공 | 모든 고객·최신 모델·독립 반복의 동일 위험률 |
| Anthropic 내부 phishing red-team, 02월 | 특정 악성 prompt 25회 재시도 중 24회 credential 전송 | 실제 전 고객 침해율 |
| Anthropic cyber 평가 사고 | 같은 partner 환경의 4건; simulation 안내와 달리 인터넷 오연결 | production 실패 확률 또는 4/481M |
| OpenAI internal research 평가, 03-27 | reference tool의 취약점을 통해 내부 host 접근; 정답 획득 실패 | 일반 사용자 모델의 행동 빈도 |

[방어·실험 조건](evidence/ANT-CONTAINMENT-20261006-001.md) · [사고·조사 범위](evidence/ANT-INCIDENTS-20261006-001.md) · [OpenAI 사건](evidence/OAI-INCIDENTS-20261006-001.md). 네 행은 공격자·환경·시도·발견 방법이 달라 안전성 순위를 만들 수 없다. 공급자의 공개 기록이며 이번 조사에서 재현하지 않았다.

사고 보고는 **실제로 집행되는 경계**를 검증할 근거를 제공한다. 운영팀은 egress 설정을 검사하고 tool의 권한·입력·destination을 제한해야 한다. ‘인터넷이 없는 실험’이라는 prompt만으로 외부 연결이 차단되지는 않는다. 승인된 connector가 가져오는 README도 신뢰되지 않은 자료일 수 있다.

적용 순서는 다음과 같다.

1. 읽기·쓰기·외부 전송·금액·대상 시스템을 분리해 허용 범위를 정한다.
2. Agent 고유 신원과 사용자 위임·짧은 credential 수명을 연결한다. [NIST](evidence/NIST-IDENTITY-20261006-001.md)
3. 모델 밖에서 destination·tool·입력 policy를 적용하고 직접 우회 경로를 막는다.
4. 외부 content를 업무 근거로 읽되 권한 확대 지시로 사용하지 않도록 테스트한다.
5. 중대 행동은 대상·차이·금액·되돌릴 방법을 보여 주는 승인으로 연결한다.

이는 설계 제안이다. 모든 동작에 팝업을 넣는 방식은 승인 피로를 만들 수 있다. 낮은 위험의 경계를 사전 승인하고 경계를 넘는 transaction에서 판단하도록 설계해야 한다. 승인을 받은 뒤 인자가 바뀌거나 다른 Agent에 위임되는 경우에도 원래 승인 범위를 유지하는지 검사한다.

## 5. 평가를 배포 승인과 운영 감시에 연결

[I-3의 평가](I-3_agents_execution.md)는 task·trial·grader·trace·outcome을 정의한다. 여기서는 그 평가를 누가 배포 기준으로 사용하고 무엇이 바뀔 때 다시 실행하는지 다룬다. 문장이 정답이어도 backend가 변하지 않았거나 부작용이 생기면 업무가 성공한 것이 아니다.

| 평가 층 | 준비할 자료·검사 | 운영 결정 |
|---|---|---|
| 정상 업무 | 대표 한국어 과업·정답/수락 기준·최종 상태 | 필요한 품질·완료율 충족 여부 |
| 경계·예외 | 권한 없는 고객·유효기간 경과·중복 요청 | 보류·거절·사람 전환이 맞는지 |
| 공격·오용 | 악성 문서·tool poisoning·전송·credential 접근 | 경계 밖 행동 차단 여부 |
| 변경 regression | model·prompt·knowledge·tool·policy 버전 | 이전 구성 대비 악화·release/rollback |
| 운영 표본 | production trace·재접촉·민원·재작업 | offline 점수와 실제 실패의 차이 |

[기존 평가 방법](evidence/ANT-EVALS-20261006-001.md)과 [AWS 온라인·on-demand](evidence/AWS-EVALUATIONS-20261006-001.md)를 연결한 적용 표다. LLM judge는 빠른 표본 판정에 쓰되 전문가와 보정하고, 금액·고객ID·DB 상태·중복 side effect는 코드·시스템 기록으로 확인한다. Online 평가는 사후 관측일 수 있으며 실시간 차단과 같은 기능으로 취급하지 않는다.

**가상 통계 예시:** 동일 조건의 독립 100건에서 중대 오류가 0건이어도 실제 오류율이 0이라는 증명은 아니다. 이항 가정에서 단측 95% 상한은 약 2.95%(1−0.05^(1/100))다. 실제 업무가 서로 의존하거나 희귀 위험을 포함하면 이 예시를 그대로 적용할 수 없다. 중대 사고와 평균 정확도를 분리하고 충분한 표본·공격 조건·사람 감독을 업무 위험에 맞춰 정해야 한다.

배포 기준에는 업무 owner, 모델·harness·tool·policy·knowledge 버전, 비교 기준선, 결과·비용·부작용, 승인자와 rollback 조건을 함께 남긴다. 임계값은 기업이 업무별로 정할 값이며 이번 조사에서 특정 성공률을 보편 기준으로 정하지 않았다.

### 5.1 차단률이 낮아도 미탐률은 알 수 없다

Anthropic이 공개한 8월 내부 연구·엔지니어링 플랫폼 관측에서 10억 건 초과 decision 중 online monitor가 차단한 비율은 0.002%였다. 해당 플랫폼의 Agent 행동은 실행 전 monitor와 실행 후 수집 경로를 모두 거친다고 설명한다. 수집 범위와 위험 검출 능력은 다르다. [분모·운영 조건](evidence/ANT-OVERSIGHT-20261007-001.md)

| 측정 항목 | 답할 수 있는 질문 | 이 지표만으로 답할 수 없는 질문 |
|---|---|---|
| coverage | 어떤 행동이 감시 경로를 거쳤는가? | 위험 행동을 모두 잡았는가? |
| 차단·flag 비율 | 얼마나 개입하고 검토했는가? | 실제 위해 발생률·미탐률은 얼마인가? |
| 검토 지연 | 개입·사람 검토가 언제 이루어졌는가? | 피해가 되돌릴 수 있는가? |
| 정상 표본·공격 평가 | 알려진 유형을 얼마나 구분하는가? | 새 공격·다른 업무도 같은 성능인가? |

낮은 차단률에는 실제 위험이 드문 경우와 monitor가 놓치는 경우가 모두 섞일 수 있다. 공격 평가의 ground truth와 정상 표본 검토로 두 경우를 구분해야 한다. 차단 event 수를 고객 침해 건수로 바꾸거나 coverage를 안전 확률로 쓰지 않는다. 기업은 외부 전송·금전·삭제처럼 빠르게 피해가 발생하는 행동을 사전 통제하고, 되돌릴 수 있는 장기 행위는 사후 검토와 복구로 연결할 수 있다.

### 5.2 Monitor도 읽기·상태 추적에서 실패한다

5월 19일 SLEIGHT-Bench는 11개 유형의 합성 공격 transcript 40개로 monitor의 맹점을 시험했다. Opus 4.6을 사용하는 주요 설정에서 공격의 50%는 10회 trial 모두에서 잡히지 않았다. 이는 연구자가 설계한 adversarial 표본의 결과이며 실제 고객 traffic의 절반을 놓친다는 뜻은 아니다. [benchmark·한계](evidence/SLEIGHT-MONITORS-20261007-001.md)

| 맹점 | 업무에서 확인할 검사 | LLM 판단을 보완하는 기록 |
|---|---|---|
| 파일·객체의 누적 변경 | 원본과 최종 결과의 실제 차이 | hash·diff·최종 파일 |
| 여러 세션의 행위 결합 | 이전 Agent가 남긴 지시와 다음 실행 | 공통 과업ID·출처·위임 chain |
| 필수 단계 생략 | 승인·대상 확인·검증을 했는지 | 상태 전이·필수 gate 기록 |
| 권한의 정당화 혼동 | 사람이 승인한 범위와 실행 인자 일치 | 원 요청·승인·policy decision |

표는 연구 맹점을 운영 검사로 옮긴 제안이다. 연구는 정상 변형 transcript로 오탐률 1% threshold를 맞췄다. code 실행이 가능한 monitor는 검증을 보완했지만 API 방식보다 평균 모델 호출 약 10배·출력 token 약 14배를 사용했다. 이 배수를 모든 보안 제품의 청구 비용 증가로 읽지 않는다.

통제 시장의 경쟁은 registry·guardrail의 기능 개수에서 **검증 범위·개입 시점·검토 원가**로 확장될 수 있다. 고위험 행동에만 비싼 검증을 추가하면 비용을 집중할 수 있지만, 위험 분류가 잘못되면 그 경로를 우회한다. 따라서 제품 구매자는 정상·예외·공격 표본과 실제 tool 경로에서 정책 집행을 대조해야 한다. 공급자의 평균 benchmark가 기업의 배포 승인 기준을 대신할 수는 없다.

## 6. 데이터 보존·감사는 저장 위치별로 관리한다

‘학습에 쓰지 않는다’, ‘특정 지역에 저장한다’, ‘삭제한다’, ‘감사 로그를 제공한다’는 각각 다른 약속이다. 원문을 삭제해도 cache·summary·memory·exported log가 별도 수명을 가질 수 있다. [I-4](I-4_knowledge_data_memory.md)의 지식 권한·메모리 관리를 보존·감사 책임까지 확장해야 한다.

| 계층 | 공개 확인·연결 | 기업의 검증 질문 |
|---|---|---|
| 검색 원문·파생 답변 | Glean 개인/공동 corpus 권한 구분 | 요약·인용·공유 자료에 회수 권한이 반영되는가? |
| Session·memory | Databricks session 삭제와 memory 별도 삭제 | actor·보존기간·퇴사·오류 기억 수정은 누가 관리하는가? |
| Managed runtime | OpenAI Agents API·Anthropic의 개별 ZDR 조건 | inference·state·file의 위치·수명이 각각 무엇인가? |
| Compliance log | OpenAI Enterprise/Edu Logs Platform 30일 | 외부 SIEM 수집 누락·접근·장기 보존은 어떻게 확인하는가? |
| Customer export | 조직 자체 저장·정책 대상 | 원 서비스 삭제 후 사본·backup·legal hold는 어떻게 처리하는가? |

[Glean](evidence/GLEAN-ACCESS-20261006-001.md) · [Memory](evidence/DB-MEMORY-20261006-001.md) · [OpenAI runtime](evidence/OAI-AGENTS-20261006-001.md) · [Anthropic runtime](evidence/ANT-RUNTIME-20261006-001.md) · [감사](evidence/OAI-COMPLIANCE-20261006-001.md).

OpenAI의 새 conversation logs는 03-05 도입, 이전 conversation stateful route는 06-05 제거되었다. 기존 integration이 있다는 것만으로 감사 자료가 계속 수집된다고 전제하지 않는다. 또한 로그 30일을 일반 API·모든 memory의 보존기간으로 복사하지 않는다.

실행 기록은 Agent·위임자·과업ID·도구·승인·policy decision·최종 상태를 연결하되, 비밀번호·원문 개인정보를 무조건 기록하지 않도록 설계한다. 감사 가능성과 데이터 최소 수집은 함께 관리할 운영 목표다. 이 기록 설계는 권고이며 현재 Atlas 또는 LG 시스템에 설정했다는 뜻은 아니다.

## 7. 규정·콘텐츠 표시는 역할과 목적에 따라 달라진다

2026년 규정 변화는 모델 공급자의 안전 문서와 기업 서비스의 책임을 연결하도록 요구한다. EU의 provider/deployer와 한국의 사업자·고영향 판정은 동일한 분류가 아니므로 글로벌 공통 기준 아래 지역별 적용표를 두는 편이 실무적이다.

| 구분 | 10-06 확인한 내용 | 적용을 위해 추가로 구분할 것 |
|---|---|---|
| 한국 | 01-22 최초 시행 안내; 현행 07-21 시행본 제31·34조 | 생성형/고영향·제품/서비스 제공·방법/예외 |
| 한국 투명성 | 기반 사전고지·생성 결과 표시·실제와 구분 어려운 음향/이미지/영상 고지 | 시행령·고시·서비스 맥락별 표시 |
| 한국 고영향 | 위험관리·설명·이용자 보호·사람 감독·문서 보관 | 해당 여부와 분야별 요구 |
| EU Article 50 | 08-02 적용; provider의 interaction 고지·machine-readable marks, deployer의 해당 표시 | deepfake·공익 text·human editorial control·예외 |
| EU 고위험 일정 | Omnibus 07-27 공지: Annex III 2027-12-02, Annex I 2028-08-02 | 위험 분류·역할·기존 규제의 병행 |
| EU marking 유예 | 08-02 이전 출시 생성형 시스템의 특정 marking 의무 December 2026까지 | 모든 고지·표시의 일반 유예가 아님 |

[한국 조문·검토 범위](evidence/KR-GOVERNANCE-20261006-001.md) · [EU 공식 해설·검토 범위](evidence/EU-GOVERNANCE-20261006-001.md). 한국 가이드 PDF와 EU 개정 조문 전체 대조는 이번 조사에서 완료하지 않았다. 표는 시장·운영의 공식 근거 종합이며 개별 서비스의 법적 적합성 판정이 아니다. 제품 기능·시장·이용자·제공 역할을 먼저 고정한 뒤 해당 세부 규정을 검토한다.

표시는 내용의 진실성을 인증하는 기능도 아니다. OpenAI는 10-05 textGrain을 일부 API에서 opt-in으로 열고 EU ChatGPT/Codex rollout을 예고했다. 영어 자사 실험에서 target 오탐 1%일 때 200-token 약 80%·400-token 약 95% 검출이지만, 다른 편집 실험에서는 단어 10% 동의어 교체 시 약 92%→66%, 25% 교체 시 17%로 낮아졌다. [조건](evidence/OAI-PROVENANCE-20261006-001.md)

따라서 watermark 미검출을 사람 작성의 증거로, 검출을 허위 정보·저작권 위반의 증거로 사용할 수 없다. 업무 근거의 출처·수정 이력·검수와 콘텐츠 생성 표식을 별도로 관리해야 한다. 한국어 판별 성능은 이번 조사에서 확인하지 않았다.

## 8. FinOps는 예산·권한·업무 결과를 연결한다

FinOps는 기술 사용 비용을 업무 가치와 연결하는 운영이다. Agent가 반복 호출·도구·장기 compute를 사용하면 예산 초과가 느린 월말 청구에서만 드러날 수 있다. 실행 전 사용량 경계와 실행 후 성공 결과당 비용을 함께 관리해야 한다.

2026 State of FinOps는 전체 1,192 응답·연간 cloud spend $83B+를 대표하는 community 표본이며 요약에서 98%의 AI spend 관리를 보고한다. 다만 관련 상세 질문은 **현재/향후 12개월 기대를 포함한 N=632**로, 전체 기업의 현재 도입률이나 검증된 ROI가 아니다. 2025의 63%와 단순 차이는 35%p이며 연도별 인과 효과로 해석하지 않는다. [분모·한계](evidence/FINOPS-AI-20261006-001.md)

| 통제 항목 | 설계 예시 | 함께 보는 품질 |
|---|---|---|
| 과업별 예산 | token·tool·compute·시간·retry 한도 | 한도 때문에 미완료·잘린 결과가 늘지 않는가? |
| 비용 귀속 | 과업·팀·사용자·모델·tool·cache 태그 | 공동 Agent·batch 비용을 어떻게 배분하는가? |
| 경보·중단 | 임계 경보·새 과업 중지·안전 종료 | 이미 수행한 transaction을 확인·복구하는가? |
| 성공 비용 | 전체 사용+검수+실패 처리 / 수락 결과 | billing resolution과 지속 업무 성공 구분 |
| 공급자 변경 | 동일 과업·권한·수락 기준 재평가 | 저렴한 경로의 실패·이동 비용 |

이 표는 운영 제안이다. [I-2](I-2_models_cost.md)의 token 가격, [I-5](I-5_enterprise_ax.md)의 수락·검수, [I-6](I-6_infrastructure_deployment.md)의 capacity·이용률을 함께 연결한다. 관리 제품의 license를 샀다는 사실만으로 실행 비용·감사 비용·사람 비용이 모두 포함되었다고 전제하지 않는다.

### 8.1 통제의 비용도 수락된 결과에 귀속한다

[I-5의 업무 사례](I-5_enterprise_ax.md)가 늘리는 자동 처리량과 [I-6의 compute](I-6_infrastructure_deployment.md)가 낮추는 처리 원가를 통제 설계와 함께 계산한다. monitor·로그·정책 조회·검수와 실패 복구를 빼면 값싼 실행 경로가 위험과 사람 비용을 다른 팀에 넘길 수 있다.

- **관측:** 공급자는 실행과 별도로 identity·policy·evaluation·관측을 제품화한다. 내부 운영 보고와 연구 benchmark는 각기 다른 분모를 사용한다.
- **해석:** 기업은 실행한 행동을 승인·결과·영향과 연결하는 증거를 확보해야 한다. 통제 제품은 이 연결의 구축 부담을 줄이는 경로에서 가치를 얻는다.
- **실현 조건:** 통제 대상이 실제 실행 경로를 포함하고, 미탐·오탐·검토 지연·총원가가 업무 위험에 맞아야 한다. license 구매나 낮은 차단률만으로 효과를 확정할 수 없다.

## 9. 배포·변경·사고를 잇는 운영 흐름

| 단계 | 책임 주체 | 남겨야 할 결과 |
|---|---|---|
| 업무 등록 | Business owner | 범위·완료·중대 실패·사람 전환 기준 |
| 권한·데이터 설계 | System/data/security owner | Agent 신원·위임·source·tool·보존·network 경계 |
| 평가·배포 승인 | Quality owner·release owner | 정상/예외/공격 test·버전·승인·rollback |
| 일상 운영 | AI operations·업무 담당 | 성공·부작용·retry·비용·변경·누락 경보 |
| 사고 대응 | Incident owner·보안·업무·법무 | 차단·credential 회수·영향 확인·복구·필요 통지 |
| 개선·종료 | 업무·지식·플랫폼 owner | 원인 수정·재평가·잔여 데이터/권한 처리 |

표는 제안하는 책임 구조이며 별도 위원회를 매번 거치라는 뜻은 아니다. 기존 배포·IAM·보안 사고·재무 운영에 Agent의 추가 정보와 판정을 연결한다. 모델뿐 아니라 policy·connector·knowledge 갱신도 업무 결과를 바꾸므로 변경 단위를 함께 기록한다.

OpenAI의 9월 공개 framework는 개별 사고의 발생일·발견일·보고 상태·불확실성을 구분한다. Anthropic 9월 assessment도 추가 사고를 늦게 발견한 과정을 설명하고 독립 조사 계약을 발표했다. 공개를 했다는 사실을 원인 제거·독립 검증 완료와 혼동하지 않고, 조직 내부에서도 발견 지연과 영향 범위를 기록해야 한다. [OpenAI](evidence/OAI-INCIDENTS-20261006-001.md) · [Anthropic](evidence/ANT-INCIDENTS-20261006-001.md)

## 10. I-1~I-7 비교 종합 — 선택권과 운영 책임의 연결

| 카테고리 | 고유 판단 대상 | I-7과 연결할 운영 기준 |
|---|---|---|
| [I-1 시장](I-1_market_competition.md) | 매출·투자·유통·기업 접점 | 공급자 선택과 사업 성과의 분모 구분 |
| [I-2 모델](I-2_models_cost.md) | 품질·token 비용·접근·license | 버전 변경·권리·동일 과업 회귀 평가 |
| [I-3 실행](I-3_agents_execution.md) | loop·tool·state·복구 | 실제 권한·부작용·승인·중단·완료 검사 |
| [I-4 지식](I-4_knowledge_data_memory.md) | 의미·검색·source·memory | 권한 회수·출처 갱신·파생 정보 수명 |
| [I-5 AX](I-5_enterprise_ax.md) | 업무 재설계·사람·수락·성과 | 업무 owner·예외·감독·품질·책임 |
| [I-6 인프라](I-6_infrastructure_deployment.md) | supply·배포·지연·이용률·전력 | 리전·data path·capacity·예산·복구 |
| I-7 운영 | 평가·보안·보존·감사·규정·원가 통제 | 위 조건을 배포·변경·운영 판정으로 연결 |

공통 개념이 등장해도 판단 목적이 다르다. I-3의 평가 방법과 I-7의 배포 승인, I-4의 memory 구조와 I-7의 삭제 책임, I-5의 업무 가치와 I-7의 일상 비용 통제는 연결하되 동일 제품 설명을 새 근거 파일에 복제하지 않았다.

배포 담당자는 다음 조건을 대조한다.

- **자율 실행의 확대는 권한·평가·복구의 운영을 요구한다.** 신원·content guardrail·결과 검사는 서로 보완 관계다.
- **시장에 통제 제품이 생겨도 모든 경로가 자동으로 관리되지는 않는다.** 기능·단계·리전·plan과 gateway 우회를 확인한다.
- **사고 공개와 검출 수치는 모집단을 읽어야 한다.** 개별 사건·실험·표본 채점을 전체 고객의 안전 확률로 바꾸지 않는다.
- **투명성과 정확성, 학습 제외와 보존, 로그와 감사 가능성을 구분한다.** 각 약속에 대응하는 설정·기록·결과를 따로 검증한다.
- **운영의 공통 단위는 수락된 업무 결과와 그 책임이다.** 모델·지식·도구·인프라를 바꾸어도 이 기준을 유지한다.

Knowledge Atlas의 출처·권한·유효기간과 Agent 실행의 위임·승인·최종 상태를 과업ID로 연결하는 방식은 적용 가설로 검토할 수 있다. 현재 내부 제품 구조·도입·성과를 확인했다는 뜻은 아니다.

### 10.1 시장 변화를 하나의 구매·운영 경로로 읽는다

| 연결 | 이번 조사에서 확인한 흐름 | 다음 성과로 넘어갈 조건 |
|---|---|---|
| I-1 → I-2 | 유료 모델 구매와 공급자의 효율 개선이 함께 진행 | 가격·사용량·수락 품질을 같은 업무에서 대조 |
| I-2 → I-3 | 모델을 장기 실행 하네스와 묶어 판매 | 복구·검증을 추가한 시간·비용·완료율 측정 |
| I-3 → I-4 | 외부 Agent가 기업 분석·지식 접점 호출 | 공통 의미·권한·결과 크기·기억 수명 관리 |
| I-4 → I-5 | 지식과 실행 API를 실제 과업에 연결 | 담당자 인계·업무 규칙·재접촉·검수 역량 유지 |
| I-5 → I-6 | 반복 과업의 확대가 model·tool·compute 부하로 전달 | capacity·이용률·전력·약정과 업무 원가 일치 |
| I-6 → I-7 | 긴 실행·더 많은 처리에 통제·관측 추가 | 위임 경계·검토 지연·부작용·통제 비용 검증 |

공급자는 모델, 하네스, 기업 지식, 업무 접점, 연산, 통제를 각기 판매한다. 한 기업이 여러 상품을 묶으면 구축 부담을 줄일 수 있지만 교체해야 할 범위도 커진다. 고객은 모델 API만 교체할 수 있는지, 지식·workflow·기록·정책까지 이전해야 하는지를 구매 전에 분리해야 한다. [시장](I-1_market_competition.md)·[모델](I-2_models_cost.md)·[실행](I-3_agents_execution.md)·[지식](I-4_knowledge_data_memory.md)·[업무](I-5_enterprise_ax.md)·[공급](I-6_infrastructure_deployment.md)

앞으로의 수익 기회는 이 연결에서 반복 사용과 책임을 확보하는 위치에 생길 수 있다. 다만 공급자 매출 증가·고객의 자동 처리량·시설 계약·monitor coverage는 서로 다른 성과다. **고객에게 남는 판단 단위는 필요한 품질과 허용 위험을 충족한 업무 결과의 총원가**다. 이 연결 분석은 공개 자료의 종합이며 모든 공급자의 시장 점유율·고객 ROI를 독립 검증한 결과는 아니다.
