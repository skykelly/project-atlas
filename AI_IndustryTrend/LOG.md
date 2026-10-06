# AI Industry Trend — 조사·변경 이력

[주제 목차](README.md)

## 2026-10-06 — 계획 6단계: I-7 작성과 전체 정합성 검토

- 시작 main: `5b65816e94da10619f525c38a125cb98c69cf0d3`. I-1~I-6·35개 근거를 이어받았다. 6단계는 I-6 재작성이 아니라 I-7 운영·신뢰·거버넌스 및 전체 정합성 검토다.
- I-7을 표·불렛·번호와 설명 문단으로 작성했다. 플랫폼 관리·identity/policy·injection/오용·평가·보존/감사·국내/EU 규정·provenance·FinOps·배포/사고 책임을 연결했다.
- 신규 근거 14개를 추가했다. NIST·Microsoft·Google·AWS·OpenAI·Anthropic·European Commission·국가법령정보센터/NIA·FinOps Foundation의 공식 원문을 검토했다. 총 7개 종합·49개 근거다.
- Microsoft Commercial GA와 team workflow Preview, Google 기능별 GA/preview, AWS Policy/Evaluations의 날짜·리전 차이를 분리했다. 인증·권한·content 검사·결과 평가는 다른 책임으로 정리했다.
- Anthropic 단일/adaptive 공격 실험·phishing 실험·4건 평가 사고와 OpenAI 내부 연구 사건을 전체 production 실패율로 쓰지 않았다. 사건·발견·보고·독립 조사 계약/완료를 구분했다.
- OpenAI 감사 30일·03-05/06-05 conversation route 전환, 10-05 textGrain opt-in/rollout·검출/편집 조건을 기록했다. 로그·memory·학습·정확성·provenance를 구분했다.
- 한국 최초 01-22 시행 안내와 현행 조문 07-21 시행본, EU 투명성 08-02와 Omnibus 이후 고위험 2027/2028 일정을 구분했다. 원문 일부 PDF 미추출 범위를 근거 파일에 명시했다.
- FinOps 전체 1,192와 세부 N=632·현재/향후 기대를 구분했다. 63%→98%는 35%p로 표기했다. 0/100건의 가상 이항 95% 상한 약 2.95% 계산을 확인했다.

### 전체 정합성 검토

| 확인 축 | 검토 결과 |
|---|---|
| 주제·중복 | 시장/모델/실행/지식/업무/인프라/통제로 목적 구분; I-7에서 기존 근거를 재사용하고 신규 원문 범위만 추가 |
| 제공 조건 | GA·Preview·Beta·계획·rollout을 기능/상품/날짜 단위로 유지; 리전·ZDR·license 전이 금지 |
| 숫자·기간 | 매출/run rate·%/%p·단가/총비용·표본/전체·관측/전망·발생/발견/공개 구분 |
| 용어 | 인증≠권한, trace≠최종 상태, session≠memory, containment≠무위험, provenance≠정확성 |
| 기존 결과 보존 | 기존 I-1~I-6 본문과 35개 evidence를 다시 생성하지 않고 그대로 유지 |
| 문서 구조 | 7개 카테고리·49개 근거의 링크·ID·필수 메타데이터·URL·표 구조 검사; 목차·루트 안내 갱신 |

### 검증·적용 한계

공개 원문 검토이며 실제 API·한국 계정·IAM/tenant·침해·로그/삭제·수락/청구·기업 법적 적합성을 실측하지 않았다. NIA 가이드 PDF와 EU 개정 법률 전체 조문은 도구에서 추출되지 않아 검토 완료로 표시하지 않았다. OpenAI hub의 third-party 통지는 확인 본문 ‘dozens’를 사용했고 보도의 100+를 확정 수치로 채택하지 않았다. 사건 공개·독립 조사 계약을 독립 최종 감사로 표시하지 않았다.

### 후속 범위

계획의 문서 종합 6단계는 완료했다. 검토 결과를 보존하기 위해 README·LOG·링크 검사와 GitHub 반영까지 함께 처리했다. 내부 평가 표본·한국 계약/리전·시행령/고시·가이드 전체 법률 검토·독립 조사 결과는 해당 자료/환경 접근 시 추가 검증할 범위다. Sites 통합·HTML 배포는 별도 요청 범위이며 이번에 수행하지 않았다. 기존 GEO·SalesMarketing·seed·Sites·자동화는 변경하지 않았다.

## 2026-10-06 — I-5·I-6 원문 조사와 비교 종합

- 시작 main: `2ddf4b74f5c522fc2a7c19504790c1d6fdf24f39`. I-3·I-4 반영을 이어받아 I-5 Enterprise AX·업무 플랫폼, I-6 인프라·클라우드·배포를 작성했다.
- 새 evidence 13개를 추가했다. WTI·Deloitte·Microsoft·OpenAI·Google·Salesforce·ServiceNow·SAP의 업무·조직·제공 조건, NVIDIA·AMD·TPU·Trainium·Maia·IEA의 공급·비용·전력 조건을 검토했다.
- 2026년 발행된 Deloitte 조사는 2025년 8~9월 관측, WTI는 2026년 AI 사용자 표본임을 기록했다. 전망과 actual·접근과 실사용·속도와 품질·과금 resolution과 사업 완결을 분리했다.
- 9월 Microsoft Autopilot private preview·Managed Runtime preview와 OpenAI Dots의 plan/market/admin 조건을 확인했다. SAP 9월 공동 개발·FedRAMP/FIPS roadmap을 인증 완료로 쓰지 않았다.
- Salesforce 현행 $2/resolution·400 credits·chat/voice/email window를 확인했다. 자사 430만 문의/70% 해결의 범위와 독립 검증 한계를 기록했다.
- NVIDIA 생산 ramp·AMD reference design/고객 배포 일정·TPU coming soon·Trainium의 2025-12 GA 배경을 구분했다. AMD 페이지 bandwidth 표현 차이도 남겼다.
- TPU chip-hour/VM-hour·READY 과금·commitment·지역 조건을 기록하고 가상 비용 계산을 검증했다. IEA 2025 관측/2030 전망·전체 데이터센터/AI-focused·TWh/GW를 구분했다.
- 기존 I-1~I-4와 22개 evidence는 다시 작성하지 않았다. 기존 GEO·SalesMarketing·seed·Sites·자동화도 변경하지 않았다.

### 검증·적용 한계

공개 공식 원문을 읽었으나 기업 업무 표본·고객 계약·한국 계정·실제 배포·hardware 성능·청구·전력은 실측하지 않았다. 사례는 공급자 보고, 설문은 각 표본의 자기보고, 성능은 내부 비교·peak/target이며 독립 인과 ROI가 아니다. Google 8t/8i 최신 전 고객 GA·한국 quota와 SAP H2/Q4 계획의 개별 달성은 확인되지 않아 계획으로 표시했다. 계획된 날짜 경과만으로 출시 완료를 추정하지 않았다.

### 검사와 다음 단계

6개 category·35개 evidence의 링크·ID·필수 메타데이터·출처 URL·표 열 수와 가상 시간/가격 계산을 검사했다. 기존 4개 category·22개 evidence의 동일성을 확인했다.

다음은 I-7 AI 운영·신뢰·거버넌스와 전체 정합성 검토다. 2026년 보안·평가·감사·사용량 통제·data retention·model access를 운영 책임에 연결한다. I-5·I-6의 추가 범위는 업무별 실측 ROI·한국 계약/리전/전력·동일 과업 hardware benchmark이며 실험 접근이 확보되면 보완한다. Markdown 이후 Sites 통합은 별도 작업이다.

## 2026-10-06 — I-3·I-4 원문 조사와 비교 종합

- 시작 main: `8a234ed885ffc60eee26456c5d7fff5c0e133b00`. 이전 I-1·I-2 및 12개 evidence를 이어받았다.
- I-3 Agent·업무 실행과 I-4 기업 지식·데이터·메모리를 표·불렛·번호와 설명 문단으로 작성했다. 2026년 발표와 10-06 현행 문서를 구분했다.
- 새 evidence 10개를 추가했다. SDK/managed 책임·세션/compute/memory 차이·최종 상태·복구·멀티 Agent·평가·metric 의미·source authority·공유 권한·memory 수명을 기록했다.
- 숫자의 조건을 확인했다: compiler 16 Agent·약 2주·API 약 $20,000 미만, TTFT p50 약 60%·p95 90% 이상 개선, Genie 내부 28-question 비교 84.5%/52.4%·32.1%p 차이.
- Genie 제품 GA와 Ontology Public Preview, 새 memory Beta와 legacy UC memory를 구분했다. overview의 semantic search와 상세 BM25 표현 차이도 남겼다.
- AWS microVM invocation 8시간과 instances 세션 14일을 구분했다. MCP 서버 14리전 서울 지원을 instances 리전에 전이하지 않았다.
- OpenAI SDK GA와 managed Agents API beta 예제를 구분하고 미국 residency·ZDR 조건을 기록했다. Anthropic의 ZDR·HIPAA BAA 미대상과 파일 별도 삭제도 기록했다.
- 공개 공급자 실험·고객 인용·비전 글을 독립 성과로 표시하지 않았다. 기존 I-1·I-2·GEO·SalesMarketing·seed·Sites·자동화는 갱신하지 않았다.

### 검증·적용 한계

공식 원문을 읽었으나 모델/API 호출·배포·권한 회수·주체 간 memory 격리·복구·청구·한국어 평가를 수행하지 않았다. 내부 벤치마크는 독립 재현하지 않았고 개별 기업 ROI를 추정하지 않았다. 발표 리전은 해당 발표의 조건이며 신규 한국 계정의 현재 계약·제공 보장은 아니다.

### 검사와 다음 단계

주제 내부 링크·22개 evidence ID/메타데이터·출처 URL·표 열 수·산술을 확인했다. 기존 12개 evidence와 I-1·I-2 본문의 동일성을 확인했다.

다음은 I-5 Enterprise AX·업무 플랫폼과 I-6 인프라·클라우드·배포다. 실제 조직의 생산성·수락률·업무 범위·관측기간과 연산·전력·추론 비용을 분리해 조사한다. 이후 I-7 운영·신뢰·거버넌스에서 보안·평가·책임을 종합한다. I-3·I-4의 추가 실측은 업무별 평가 데이터·계정·도구 접근이 확보될 때 수행한다. Sites 통합은 별도 작업이다.

## 2026-10-06 — I-1·I-2 원문 조사와 비교 종합

- 시작 main: `407e558c9d875cfa2289803f11c5c217664eedb9`. 루트 AGENTS·README와 Industry Trend README를 확인했다. 기존 폴더에는 README만 있었고 LOG는 없었다.
- I-1 시장·기업 경쟁과 I-2 모델 역량·비용을 작성했다. 표·불렛·넘버링 사이에 맥락 설명을 배치했다.
- 공식 실적·발표·현행 문서·보고서·모델 repository·LICENSE를 원문 검토해 12개 evidence를 작성했다. 현재 모델 가격은 10-06 확인일 기준이다.
- 투자·실제 매출·run rate·평가액·유료 좌석·사용자를 구분했다. Cloud와 순수 AI 매출을 분리하고 공급망 매출의 중복 합산을 피했다.
- 2026년 발표와 실제 관측 기간을 구분했다. Microsoft 1월 발표는 2025년 말 분기, HAI 도입·투자는 2025년, NVIDIA는 달력 2026년/FY27 Q2다.
- GPT standard short/long·Claude tokenizer·cache·Gemini 도입 가격과 2027년 정상 가격·제한 접근을 기록했다. context 입력과 최대 출력, 공개 weights와 상업 권리도 분리했다.
- 동일 토큰량과 실패·검수의 가상 비용 예시를 계산했다. 실제 모델 품질·내부 ROI를 추정한 수치가 아니다.
- README에 7개 계획 카테고리·완료 2개·근거 목차를 기록하고 루트 주제 설명만 갱신했다. I-3~I-7의 빈 파일은 만들지 않았다.

### 검증·적용 한계

공개 원문을 확인했으나 API 호출·계정·한국어 실험·GPU 배포·청구·실제 기업 계약·내부 시스템 검증은 수행하지 않았다. HAI는 Economy 웹 요약으로, 원 설문·투자 데이터의 상세 집계 재현은 하지 않았다. 회사 발표는 독립 인과 검증으로 표시하지 않았다.

일부 원문에 최초 게시일이 없으면 확인일·명시된 관측기간을 사용했다. OpenAI Sol은 Astra의 09-29 업데이트 연결로 시점을 기록하고 본문에 없는 날짜를 만들어 넣지 않았다. Gemini 3.8 Flash는 현행 guide 확인일 기준이다. Anthropic 비공개 재무 보도는 이번 공식 발표 수치에 덧붙여 확정하지 않았다.

### 검사

주제 내부 링크·12개 evidence ID·필수 메타데이터·출처 URL·표 열 수·산술 예시를 확인했다. 기존 GEO·SalesMarketing·data·Sites·자동화는 변경하지 않았다.

### 다음 조사 — I-3·I-4

1. Agent SDK·managed runtime·컴퓨터 사용·멀티 Agent: 지속 실행·상태·권한·승인·실패 복구·평가의 2026년 변화와 실제 과업 조건.
2. 기업 지식·RAG·GraphRAG·Ontology·메모리: Databricks·Snowflake·Glean·Stardog 등 공식 제품 조건과 도입 사례. 지식 갱신·권한·검색 품질과 장기 메모리를 분리.
3. I-1 추가 범위: Meta·Oracle·Salesforce·한국 기업의 독립 사업 수치, AI-specific 시장 추정의 정의·방법론. 현재 8개 사업자 비교를 전체 산업 전수조사로 쓰지 않는다.
4. I-2 추가 범위: 모델별 한국어·동시성·응답 지연·리전·사용 조건 및 open-weight 최신 계열의 모델별 권리 검토. 현재 비교는 대표 후보의 공개 문서 조건이다.

계획한 진행 순서는 I-3·I-4 → I-5·I-6 → I-7·전체 정합성 검토다. Markdown 완성 뒤 Sites 통합은 별도 작업으로 한다.

## 2026-10-07 — 문체 편집 I-1~I-4

- 시작 main: `26f9249cecd91194e79b007f59c741ea7976c4bf`. 진행 대기열에서 I-1·I-2·I-3·I-4를 편집했다. 근거 문서·README·data seed는 변경하지 않았다.
- I-1은 하나의 AI 수요가 소프트웨어·모델·클라우드·칩 매출에 중복 포착되는 구조를 전면에 세웠다. 공급자 매출과 고객 ROI를 분리하고 유통·실행 접점의 지배력을 명확히 했다.
- I-2는 모델 순위보다 수락 가능한 결과당 비용을 중심에 뒀다. 기간 한정 가격·캐시·추론·도구·검수비와 공개 weights의 운영 책임을 직설적으로 정리했다.
- I-3은 Agent의 상태·중복 방지·복구·외부 쓰기 검증을 중심으로 재구성했다. 관리형 런타임이 운영 코드를 줄여도 업무 책임은 기업에 남는다는 경계를 유지했다.
- I-4는 검색 실패보다 업무 정의·권한·메모리의 실패가 먼저 발생한다는 구조를 강조했다. semantic layer·ontology·공유 권한·장기 기억의 책임선을 분리했다.
- 네 문서 모두 숫자 목록·링크 목록·표 구조를 보존했다. 금지 표현과 경고 표현은 검출되지 않았다. 수치의 단위·기간·제공 단계·성과 범위를 수정 전후로 대조했다.
- 진행 현황은 10개 완료·20개 대기다. 다음 묶음은 I-5~I-7과 G-1이다. 전체 편집이 끝날 때까지 Sites에는 중간 배포하지 않는다.

## 2026-10-07 — I-1·I-2 시장 분석 심층 보강

- 시작 main: `478c20edcda0e58f2fa5f5c5ad651679e1deac51`. 최신 AGENTS·루트/주제 README·LOG와 I-1·I-2를 읽었다. 기존 문체 편집 완료 상태를 되돌리지 않았다.
- 사용자 요청에 따라 2개씩 보강하고 마지막 1개를 종합 검토하는 순서로 정했다: I-1·I-2 → I-3·I-4 → I-5·I-6 → I-7·전체 정합성. 예약을 만들거나 재개하지 않았다.
- Monthly Trend의 7월·8월 리포트는 분석의 깊이·사건 연결을 참고했다. 9월 페이지는 검색 도구에서 접근 오류가 발생했다. 그 페이지의 미확인 주장에 의존하지 않고 공급자 공식 9월 발표를 검토했다. 참고 글을 사실 원본으로 복제하지 않았다.
- I-1: Ramp의 실제 구매·모델 지출, embedded AI 과금, Oracle의 IaaS 매출·RPO·현금흐름, Hugging Face의 파생 모델·다운로드를 연결했다. 투자·매출·계약·현금·구매와 배포의 분모를 분리했다. 공급자 수익과 고객 비용이 어떻게 전달되는지, 각 전망이 성립하는 조건을 설명했다.
- I-2: 8월 구매 관측과 9월 효율 개선을 연결하되 인과 관계로 확정하지 않았다. 단가·캐시·소비량·속도·라우팅을 분리했다. AutomationBench의 fallback 없는 평가 조건과 FrontierCode의 수락 기준, 하네스·도구·제한 시간의 운영 영향을 보강했다. 공개 모델의 임베딩·반복 사용과 배포 artifact 책임을 설명했다.
- 신규 evidence 4개: RAMP-DEMAND·RAMP-SAAS·HF-ECOSYSTEM·ORCL-EARN. ANT-MODELS에 10-07 재확인한 평가 각주를 추가했다. 주제 evidence는 49개에서 53개로 늘었다. I-3~I-7·GEO·LG·Sales·seed 원본은 변경하지 않았다.

### 검증과 적용 한계

- 원본 종합의 제목·기존 링크·기존 표를 보존했다. 기존 가격표는 10-06 확인 상태이며 모든 가격을 새로 확인했다고 표시하지 않았다. 추가 시장·제품 원문은 10-07 확인으로 분리했다.
- 신규 수치의 단위·관측 기간·분모·성과 단계를 원문과 대조했다. Ramp 모델별 집계를 전체 고객 표본으로 확대하지 않았고, SaaS 사용량 과금의 지출 차이를 인과 효과로 쓰지 않았다. Oracle FY27 Q1은 2026-08-31 종료이며 RPO를 당기 AI 매출로 쓰지 않았다. HF 방법론의 첫 7개월 집계와 8월 제품 추가 편집을 구분했다.
- 종합 원본과 연구 보강본을 `editorial_review.py check`로 비교하면 새 수치·링크·표 추가가 changes로 검출된다. 이 작업은 사실을 추가하는 조사 요청이므로 순수 문체 편집의 불변 검사를 그대로 적용해 승인하지 않았다. 신규 근거를 대조한 연구 보강본을 별도 기준본으로 확보하고 그 뒤의 문체 수정에 check를 실행했다. 두 문서 모두 수치·링크·메타데이터·표 구조 보존, 금지·경고 표현 검사에 통과했다.
- 저장소 상대 링크, 표 열 수, 5개 수정·추가 evidence의 ID·필수 메타데이터·출처를 검사했다. 관측 사실·사업 해석·성립 조건·설명의 충분성을 별도로 검토했다.
- 고객 원시 결제 데이터, 다운로드 집계, API·하네스·한국어 업무·청구·ROI와 데이터센터 가동을 재현하지 않았다. 외부 수치의 독립 실측이나 전 산업 전수조사로 표시하지 않는다.
- 이번 묶음은 GitHub 조사 보강이다. Sites의 Monthly Trend 11개 iframe 탐색 기능은 별도 사이트 변경으로 배포 완료했으나, 이 두 종합의 새 조사 본문은 아직 Sites에 반영하지 않았다. 후속 묶음에서 최신 상태를 이어받는다.

## 2026-10-07 — I-3·I-4 시장 분석 심층 보강

- 시작 main: `2c64ff9725634d560f468a558dde3c11c91c791b`. 최신 AGENTS·루트/주제 README·LOG 및 대상 종합을 읽고 앞선 I-1·I-2 심층 보강을 이어받았다. 두 개씩 진행하는 두 번째 묶음이다.
- I-3: 실행 하네스의 상품화와 기업이 유지해야 할 인증·복구·평가 책임을 구분했다. Anthropic의 장시간 앱 개발 실험을 비용·시간·완성도·과업 범위로 비교하고 Genie One MCP가 외부 Agent와 기업 분석 Agent를 연결하는 구조를 설명했다.
- I-4: 지식 플랫폼의 외부 Agent 유통, 의미·권한·메모리의 운영 조건을 보강했다. Fireblocks의 반복 분석 사용량, Glean의 문맥 저장 범위와 AgentSM의 실행 경험 재사용을 실제 구매·운영 판단에 연결했다. 관측·해석·실현 조건을 나눴다.
- 신규 evidence 5개: ANT-HARNESS·DB-MCP·FIREBLOCKS-ANALYTICS·GLEAN-MEMORY·AGENTSM. 전체 evidence는 53개에서 58개로 늘었다. 주제 README와 루트의 요약·현황을 맞췄다. 사례 원본·seed·문체 편집 진행 상태·다른 종합은 변경하지 않았다.

### 검증과 적용 한계

- 신규 원문은 10-07 확인으로 기록하고 기존 10-06 확인 상태와 구분했다. Fireblocks 원문의 최초 게시일과 성과 관측 기간은 공개되지 않아 2026년 신규 성과로 단정하지 않았다. 공급자·고객 보고 수치를 독립 실측으로 표시하지 않았다.
- Anthropic의 20분·$9와 6시간·$200 비교에는 기능 범위 확대와 잔여 버그가 있다. multi-agent의 일반적 비용 절감으로 확대하지 않았다. Genie MCP GA·기존 endpoint의 10-31 종료 예정·인증 및 결과 잘림 조건을 구분했다.
- Glean의 2시간 조건은 기록을 끈 세션의 후속 도구 문맥에 한정했다. 전체 데이터 삭제·조직의 영구 기억으로 확대하지 않았다. AgentSM은 1월 preprint 초록만 확인했다. Spider 2.0의 토큰·trajectory 절감과 Spider 2.0 Lite의 실행 정확도를 별도 집계로 기록했다.
- 원본의 제목·기존 링크·기존 표를 보존하고 새 수치의 단위·측정 조건·성과 단계를 원문과 대조했다. 조사에서 추가한 수치·링크·표는 순수 문체 편집 불변 검사의 승인 대상으로 삼지 않았다. 연구 보강본을 별도 기준본으로 확보한 뒤 최종 문체 수정에 `editorial_review.py check`를 적용했다.
- 저장소 상대 링크·표 열 수와 신규 evidence ID·필수 메타데이터·출처를 검사했다. 의미와 설명의 충분성을 별도로 검토했다. 고객 원시 데이터·API·하네스·청구·한국어 업무·ROI·논문 실험은 재현하지 않았다.
- 이번 묶음은 GitHub 조사 보강이다. Sites 배포와 예약 재개는 수행하지 않았다. 다음 묶음은 I-5·I-6이다.
