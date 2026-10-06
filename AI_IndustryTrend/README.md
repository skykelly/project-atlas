# AI Industry Trend — 2026년 산업 변화

[Atlas 안내](../README.md) · [변경 이력·조사 대기](LOG.md)

모델·연산·지식·Agent·업무 플랫폼·운영의 변화가 기업의 선택과 실행에 어떤 영향을 주는지 조사한다. 조사 범위는 **2026-01-01~현재**, 이번 확인일은 **2026-10-06**이다. 전년도 관측을 담은 2026년 보고서와 현재 문서는 관측 기간·확인일을 구분한다.

## 카테고리와 작성 상태

| 코드 | 주제 | 핵심 질문 | 상태 |
|---|---|---|---|
| I-1 | [AI 시장·주요 기업 경쟁](I-1_market_competition.md) | 누가 어떤 가치·유통·업무 접점에서 경쟁하는가? | 원문 기반 비교 종합 작성 |
| I-2 | [모델 역량·비용·사용 조건](I-2_models_cost.md) | 업무 품질·성공 비용·접근 조건으로 어떻게 선택하는가? | 원문 기반 비교 종합 작성 |
| I-3 | [Agent·업무 실행 기술](I-3_agents_execution.md) | 도구·컴퓨터·멀티 Agent의 실행과 복구는 어떻게 달라지는가? | 원문 기반 비교 종합 작성 |
| I-4 | [기업 지식·데이터·메모리](I-4_knowledge_data_memory.md) | 검색·Ontology·권한·메모리를 어떻게 연결하는가? | 원문 기반 비교 종합 작성 |
| I-5 | [Enterprise AX·업무 플랫폼](I-5_enterprise_ax.md) | 기업 업무·조직의 변화와 성과는 무엇인가? | 원문 기반 비교 종합 작성 |
| I-6 | [AI 인프라·클라우드·배포](I-6_infrastructure_deployment.md) | 공급·전력·추론·배포의 경제성은 어떻게 변하는가? | 원문 기반 비교 종합 작성 |
| I-7 | AI 운영·신뢰·거버넌스 | 평가·보안·책임·통제를 어떻게 운영하는가? | 조사 대기 |

빈 카테고리 파일을 미리 생성하지 않는다. I-1은 산업 경쟁, I-2는 모델 선택을 비교한다. I-3은 실행 기술, I-5는 업무·조직 운영, I-7은 검증·통제라는 서로 다른 책임을 다룬다.

## 읽는 방식과 근거

표·불렛·넘버링에 맥락·해석·예시를 설명하는 문단을 배치한다. 공개 사실과 기업 발표, 분석 해석, 적용 가설을 구분한다. 숫자의 단위·기간·사업 범위·제공 단계·한계는 단일 evidence에 관리하며 종합은 그 근거를 연결한다.

| 근거 | 주 카테고리 | 원문·조건 |
|---|---|---|
| [Stanford AI Index](evidence/HAI-ECON-20261006-001.md) | I-1 | 2026년 보고, 2025년 투자·도입 관측 |
| [Microsoft](evidence/MS-CLOUD-20261006-001.md) | I-1 | 01-28·07-29 발표, Cloud·유료 좌석 |
| [Alphabet](evidence/GOO-EARN-20261006-001.md) | I-1 | 6월 종료 Q2, Cloud와 사용자·기업 접점 |
| [AWS](evidence/AWS-EARN-20261006-001.md) | I-1 | 실제 분기와 AI 연환산 규모 구분 |
| [Anthropic 자금·유통](evidence/ANT-CAPITAL-20261006-001.md) | I-1 | 05-28 공식 발표, 자금·평가액·run rate |
| [OpenAI 기업 방향](evidence/OAI-ENTERPRISE-20261006-001.md) | I-1 | 04-08·09-29 발표, 기업 비중·공동 작업 접점 |
| [NVIDIA](evidence/NV-EARN-20261006-001.md) | I-1 | 08-26 발표, FY27 Q2 공급 단계 매출 |
| [NAVER](evidence/NAV-EARN-20261006-001.md) | I-1 | 08-07 발표, 연결 실적·투자·전망 |
| [GPT 제공·가격](evidence/OAI-MODELS-20261006-001.md) | I-2 | 09-29 업데이트·현행 API 가격 |
| [Claude 제공·효율](evidence/ANT-MODELS-20261006-001.md) | I-2 | 09월 발표·현행 요금·작업당 비용 |
| [Gemini 단계·가격](evidence/GOO-MODELS-20261006-001.md) | I-2 | GA·제한 접근·연말 한시 가격 |
| [Open-weight·라이선스](evidence/OPEN-MODELS-20261006-001.md) | I-2 | Qwen3.6·EXAONE 4.5의 특정 공개 모델 |
| [SDK와 managed harness의 책임 분리](evidence/OAI-AGENTS-20261006-001.md) | I-3 | 원문·제공 단계·측정 조건·한계 |
| [Managed Agents의 상태·실행·자격증명 분리](evidence/ANT-RUNTIME-20261006-001.md) | I-3 | 원문·제공 단계·측정 조건·한계 |
| [16 Agent C compiler 실험의 규모와 한계](evidence/ANT-TEAMS-20261006-001.md) | I-3 | 원문·제공 단계·측정 조건·한계 |
| [Agent 평가: 발화가 아닌 환경의 최종 상태](evidence/ANT-EVALS-20261006-001.md) | I-3 | 원문·제공 단계·측정 조건·한계 |
| [AgentCore: MCP 상태와 장시간 compute의 구분](evidence/AWS-RUNTIME-20261006-001.md) | I-3 | 원문·제공 단계·측정 조건·한계 |
| [Genie Ontology의 의미·출처·내부 비교](evidence/DB-ONTOLOGY-20261006-001.md) | I-4 | 원문·제공 단계·측정 조건·한계 |
| [세션과 durable memory의 수명·정체성](evidence/DB-MEMORY-20261006-001.md) | I-4 | 원문·제공 단계·측정 조건·한계 |
| [Semantic View와 구조·비구조 데이터의 실행 연결](evidence/SNOW-SEMANTIC-20261006-001.md) | I-4 | 원문·제공 단계·측정 조건·한계 |
| [개인 검색과 공동 응답의 권한 차이](evidence/GLEAN-ACCESS-20261006-001.md) | I-4 | 원문·제공 단계·측정 조건·한계 |
| [Semantic Control Plane과 지식 steward의 역할](evidence/STAR-CONTEXT-20261006-001.md) | I-4 | 원문·제공 단계·측정 조건·한계 |
| [2026 WTI와 Copilot 업무 플랫폼의 변화](evidence/MS-WORK-20261006-001.md) | I-5 | 발표·관측·제공 단계·비용 조건·한계 |
| [AI 접근 확대와 pilot→production 간극](evidence/DEL-AX-20261006-001.md) | I-5 | 발표·관측·제공 단계·비용 조건·한계 |
| [Help Agent의 실제 사용 보고와 resolution 과금](evidence/SF-OUTCOMES-20261006-001.md) | I-5 | 발표·관측·제공 단계·비용 조건·한계 |
| [역할별 AI specialist와 지식 품질의 영향](evidence/NOW-WORK-20261006-001.md) | I-5 | 발표·관측·제공 단계·비용 조건·한계 |
| [Joule: 업무 의미·transact·승인 경계](evidence/SAP-WORK-20261006-001.md) | I-5 | 발표·관측·제공 단계·비용 조건·한계 |
| [Gemini Enterprise app·Agent Platform와 업무 확장](evidence/GOO-WORK-20261006-001.md) | I-5 | 발표·관측·제공 단계·비용 조건·한계 |
| [Dots와 공동 workspace의 9월 제공 조건](evidence/OAI-WORK-20261006-001.md) | I-5 | 발표·관측·제공 단계·비용 조건·한계 |
| [Rubin의 chip→rack→POD 설계와 생산 단계](evidence/NV-RUBIN-20261006-001.md) | I-6 | 발표·관측·제공 단계·비용 조건·한계 |
| [Helios 생산·배포·공개 표준의 의미](evidence/AMD-HELIOS-20261006-001.md) | I-6 | 발표·관측·제공 단계·비용 조건·한계 |
| [TPU 학습·추론 분리와 공개 가격 단위](evidence/GOO-TPU-20261006-001.md) | I-6 | 발표·관측·제공 단계·비용 조건·한계 |
| [Trainium3와 managed agent 배포의 선택](evidence/AWS-TRAINIUM-20261006-001.md) | I-6 | 발표·관측·제공 단계·비용 조건·한계 |
| [Maia 200의 추론 최적화와 실제 배치](evidence/MS-MAIA-20261006-001.md) | I-6 | 발표·관측·제공 단계·비용 조건·한계 |
| [2026 갱신: 효율 개선과 총전력·물리 병목](evidence/IEA-ENERGY-20261006-001.md) | I-6 | 발표·관측·제공 단계·비용 조건·한계 |

`reviewed`는 원문 확인이다. 독립 실험·감사·한국 계정 제공·청구 검증을 의미하지 않는다. 35개 근거 문서는 여러 URL을 함께 검토한 주제별 기록으로, 개별 원문 수와 같지 않다.

## 주제 경계와 유지 원칙

- GEO·검색·광고·쇼핑의 상세는 [기존 GEO·AI Commerce](../AI_GEO_AIcommerce/README.md)를 연결한다. 여기서는 산업 경쟁·모델 선택에 관련된 부분만 다룬다.
- 실제 기업 영업·마케팅 사례는 [기존 사례 위키](../AI_SalesMarketing/README.md)를 참조하고 복제하지 않는다.
- Markdown이 지식의 기준이다. seed·원본 JSON을 갱신하지 않는다. HTML과 JSON은 필요할 때 현재 Markdown에서 생성한다.
- 가격·기능은 확인일 조건이며, 발표·계획·GA·제한 접근을 구분한다. 공개 모델 라이선스와 기업 내부 계약·권리를 혼동하지 않는다.
- 조사 대기·검증 한계는 LOG에 기록한다. 이번 작업은 GitHub 문서 작성이며 Sites 추가 배포·자동화 연결은 수행하지 않았다.
