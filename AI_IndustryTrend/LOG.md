# AI Industry Trend — 조사·변경 이력

[주제 목차](README.md)

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
