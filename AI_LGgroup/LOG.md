# LG Group AI 조사·변경 이력

[목차](README.md) · [Atlas](../README.md)

## 2026-10-06 — 기존 여섯 테마 기반 조사 및 종합

### 기준과 범위

- Atlas main 기준 커밋: `0dab4d37a65335f7fe9d1c2d2ec5043b97482a9d`.
- 기존 테마 참고: `skykelly/lggroup-ai-strategy` main `680ff865baf9320138cd31d1cbe984729180992a`. README 및 `docs/01`~`docs/06`을 참고했다.
- 루트 AGENTS·README와 LG 주제 README를 확인하고, Markdown을 기준으로 작업했다.
- 조사 기간: 2026-01-01~2026-10-06. 공식 회사·연구원·파트너 원문과 회사가 배포한 보도자료를 우선 확인했다.
- 2025년 CES 사전 기술 설명은 배경으로 날짜를 표시했다. 2026년 인터뷰가 소개한 과거 공장 성과도 신규 성과와 분리했다.

### 작성 결과

| 테마 | 종합 문서 | 주 분류 사례 |
|---|---|---|
| L-1 AI Data Center / Infra | docs/01_ai_data_center_infra.md | 6 |
| L-2 Physical AI / Smart Manufacturing | docs/02_physical_ai_smart_manufacturing.md | 6 |
| L-3 AI Mobility / SDV·AIDV | docs/03_ai_mobility_sdv_aidv.md | 7 |
| L-4 Enterprise AX / Agentic Operating Model | docs/04_enterprise_ax_agentic_operating_model.md | 6 |
| L-5 AI for Science / Bio / Materials / Battery | docs/05_ai_for_science_bio_materials_battery.md | 3 |
| L-6 Global AI Alliance / Open Innovation | docs/06_global_ai_alliance_open_innovation.md | 3 |
| 합계 | 6 | 31 |

- 사례 31건에 회사·주 분류·원문 확인 상태·확인일·발표/사건일·근거 위치·수치 조건·한계·해석을 기록했다. 사례 문서에서 연결한 공식 URL은 중복 제거 35개다.
- 종합은 계열사 역할, 현재 단계, 수치의 범위, 실행 흐름, 비교·평가 기준을 표·번호·불렛과 맥락 설명으로 구성했다.
- 10월 6일 AIR 장기 공급 및 Renault 콕핏 공급, 10월 1일 공동투자, 9월 Microsoft·DSX Ready·전문가 AI, 8월 데이터팩토리·삼송·텔레매틱스를 반영했다.
- LG README를 목차·그룹 비교·근거 기준·사례 목록으로 갱신했다. 루트 README는 LG 주제 설명 한 줄만 갱신했다.
- EXAONE 일반 모델·라이선스는 기존 Industry 근거를 링크했다. 공통 인프라·AX·Agent 거버넌스도 기존 문서를 재사용했다.
- AI Factory는 독립 테마로 추가하지 않았다. 연산·냉각·전력과 제조 데이터·로봇 학습을 각각 L-1·L-2로 구분했다.

### 검증 및 한계

- 초기 링크 검사에서 아직 작성하지 않은 LOG 링크가 발견돼 추가했다. 최종 검사에서 로컬 링크 192개, 사례 ID·필수 메타데이터, 테마별 집계, 표 열 수가 모두 통과했다. 주제 39개 문서와 루트 README를 포함한 변경 파일은 40개다.
- 원문 확인과 독립 성과 검증을 분리했다. 독립 실측, 실험·임상 재현, 계약 원본·감사 자료 검토는 수행하지 않았다.
- 1만 GPU 도입설은 공식 협력 원문의 확정 수량에 없어 채택하지 않았다.
- Baton의 15%·18%는 특정 조건의 기대 효과, 전자 30%는 목표, One Day RFx는 프로젝트 목표로 기록했다.
- 파주 사전 계약과 준공·가동, 제품 자격과 구매 계약, 콕핏·통신 공급과 AIDV 전체 상용화를 구분했다.
- Microsoft 자료는 LG전자 공식 공개 게시를 확인했다. 회의일과 절대 게시일을 분리하고, 공급 기회·전 직원 환경 전환 계획을 계약 실적·배포 완료로 쓰지 않았다.
- 같은 사례의 테마 간 연결은 문서 링크로 재사용했다. 기존 Sales·GEO·Industry 본문, seed·보존 ZIP·설정은 변경하지 않았다.
- 이번 범위는 Markdown 조사·정리다. HTML 생성·Sites 반영·배포는 수행하지 않았다.

### 보류·후속 확인 항목

본문의 결론은 현재 공개된 근거로 완결하고, 아직 공개되지 않은 결과만 아래에 남긴다. 새 조사를 예약하거나 자동화를 생성하지 않았다.

1. AIR 연도별 납품·매출 인식, 미국 공장 가동, CDU/BESS의 실제 고객 성능·발주.
2. 파주 준공·사용률, AI 박스 실제 구축 기간과 GPU 설치·가동 현황.
3. 로봇 현장 처리량·안전·개입률, 양재 실제 데이터와 합성 데이터 비중 및 목표 달성.
4. AI Cabin 양산 차종·지연·전력, Renault 공급 및 최종 차량 탑재 기능.
5. 전사 생산성 공통 산정식·활성 사용자·개발 결함과 고객별 ROI.
6. 소재 상용화·고객 검증, D&D 공동개발 후보·시험 단계, Virtual Lab의 동일 조건 실측.
7. 협력별 IP·데이터 귀속·투자 조건·실제 거래 및 반복 매출.

## 2026-10-06 — L-1·L-2 심층 리포트 재작성

- 시작 main: `2fcbc4ae449a41b5d6ca458a20733ae681598a15`. 계획·평가 기준 위주의 종합을 실제 사업·고객·제품·공정과 해석 중심으로 재작성했다.
- L-1: AIR 거래 구조·미국 생산 확대·장치 효율 조건, 칩~시설 냉각 구조, 삼송 고밀도 운영, AI 박스/PMDC 상품 변화, 파주 운영·BESS의 수익 구조를 비교했다.
- L-2: 외부 스마트팩토리 수주, Factova 데이터/MES 흐름과 고객 성과, 제조 특화 모델, Forge/Baton 역할, 양재 공간별 작업·데이터 경로, 청라 외부 검증을 연결했다.
- AIR 거래 상대방 발표와 LG 데이터팩토리 영문 원문을 읽고 두 기존 사례에 추가했다. 기존 ID·분류·31건 집계를 유지했다. 새로 읽지 못한 IMTS 자료는 채택하지 않았다.
- L-3~L-6, Sales/GEO/Industry, seed·HTML·Sites는 변경하지 않았다. 다음 묶음은 L-3·L-4이며 L-5·L-6은 그 뒤다.
- 검증: 로컬 링크 202개·사례 ID·필수 메타데이터·카테고리 집계·표 열 검사 통과. 변경은 종합 2개·기존 사례 2개·주제 README·LOG의 6개 Markdown에 한정했다.
