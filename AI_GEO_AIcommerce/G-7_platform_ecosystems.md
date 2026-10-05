# G-7. AI 플랫폼 생태계·개인화·앱·에이전트 전략

[목차](README.md) · [광고](G-6_ai_ads_monetization.md) · [시장 개관](G-8_market_adoption.md)

> **핵심 결론:** AI 검색·쇼핑의 경쟁 단위는 모델 정확도에 더해 사용자 맥락·데이터·실행 접점이다. 여러 플랫폼에 하나의 정보 기반을 제공하면서 국가·브랜드 UX·거래 조건은 따로 설계해야 한다.

_조사 범위: 2026-01-01~2026-10-06. 원문 확인일: 2026-10-06._

이 문서는 플랫폼 선택·데이터/접점 경쟁·공통 운영 구조를 비교한다. 실제 질문-근거 설계는 [G-1](G-1_ai_search_geo.md), 기술 접근 점검은 [G-3](G-3_crawlers_content_access.md), 거래 프로토콜·승인·복구는 [G-5](G-5_agentic_commerce.md)에 모아 관리한다.

## 주요 플랫폼 방향 비교

| 플랫폼 | 공식 발표·문서에서 확인한 방향 | 기업 참여 경로 | 현황을 과장하지 않기 위한 경계 |
|---|---|---|---|
| [Google](evidence/GOO-SEARCH-20261006-001.md) | Search·Gemini·개인 연결·지속 에이전트·cart 통합 | 웹·Merchant Center·UCP·브랜드 상담·광고 | 모델·agent·결제의 출시 단계와 국가가 서로 다름 |
| [OpenAI](evidence/OAI-DISCOVERY-20261006-001.md) | 발견·비교를 강화하고 판매자 checkout·브랜드 경험 허용 | 피드·자사 checkout·앱/Plugins·광고 | 초기 Instant Checkout 방향을 최신 전략으로 유지하지 않음 |
| [Microsoft](evidence/MS-COMMERCE-20261006-001.md) | Copilot 발견·checkout와 자사 Brand Agents·측정 | catalog·판매자 파트너·UCP·Clarity/Bing | 미국 초기 제공과 내부 benchmark의 관측 시점 분리 |
| [Amazon](evidence/AMZ-COMMERCE-20261006-001.md) | 상품·리뷰·구매 이력과 가정 내 Alexa 맥락 결합 | 상품·리뷰·marketplace·대화형 광고 | 2025 이용 고객·회사 추정을 2026 MAU로 바꾸지 않음 |
| [Perplexity](evidence/PER-COMMERCE-20261006-001.md) | 조사·개인화 상품 추천·Instant Buy | 깊은 상품 정보·적격 판매자 연동 | 날짜 없는 현행 문서를 신규 발표로 기록하지 않음 |
| [Anthropic](evidence/ANT-STRATEGY-20261006-001.md) | 광고 없는 사용자 주도 도구·과업·commerce 방향 | 사용자 요청 근거·도구 연결 | 전략 관심과 공통 native checkout 출시를 구분 |
| [네이버](evidence/NAV-AGENT-20261006-001.md) | 국내 검색·리뷰·UGC·쇼핑·로컬 실행 연결 | 한국어 공식 근거·국내 상품/판매 접점 | AI탭 이용자 집계 창·beta 비교 조건 미공개 |

위의 ‘방향’은 공개 문서를 종합한 해석이며 각 회사의 비공개 로드맵을 뜻하지 않는다. Meta·중국 주요 commerce 생태계의 직접 참여 조건은 이번 조사에서 충분히 검증하지 못해 다음 조사에 남긴다. 주요 플랫폼 비교를 전 세계 서비스의 완전 목록으로 표현하지 않는다.

## 세 가지 경쟁 자산

### 1. 유통 규모: 검색 내장, 독립 앱, marketplace는 다른 시장이다

Google AI Overviews·AI Mode, Gemini app, ChatGPT weekly 이용자, Similarweb 도메인 방문은 각각 다른 집계다. [시장 개관](G-8_market_adoption.md)의 수치를 이용자 순위로 합치지 않는다. 검색·앱 배포 기반이 크더라도 우리 고객의 제품 질문·구매를 얼마나 담당하는지는 별도 확인해야 한다.

### 2. 맥락: 같은 질문도 연결 데이터와 계정에 따라 달라진다

Google 개인 연결, Amazon 대화·구매 이력, Perplexity 선호 기억은 제품 적합성 판단의 입력을 넓힌다. 익명 단일 prompt로 얻은 순위는 전체 고객 경험을 대표하지 못한다. [독립 UI/API 연구](evidence/RES-AUDIT-20261006-001.md)는 실제 consumer UI 관찰 필요성을 뒷받침한다.

### 3. 실행: 발견과 거래, 도구 연결과 브랜드 경험을 분리한다

선택한 플랫폼에 따라 데이터 전달·도구 연결·브랜드 UI·거래를 따로 검토한다. 스키마 존재·앱 설치·웹 색인은 각각 다른 자격이며 하나를 구현해 모든 플랫폼 거래가 열리지는 않는다. 프로토콜별 역할·국가 자격·실행 책임은 [G-5 거래 설계](G-5_agentic_commerce.md), [현행 ChatGPT Plugins](evidence/OAI-PLUGINS-20261006-001.md)의 외부 checkout·선정 beta 조건을 따른다.

## Brand Answer Engine·AI Chat 실행 모델 — 적용 가설

| 공통 기반 | 플랫폼별 분기 | 관리 책임 |
|---|---|---|
| 모델/국가별 사양·식별자·호환·설치 기준 | 웹 답변·상품 피드·상담 UI·도구 API | 제품 사실 원본·버전·충돌 해결 |
| 가격·재고·프로모션·배송·보증 | 발견 snapshot·실시간 주문 확인 | 신선도·실행 가능성·만료 |
| 고객 과업·근거·실패 원인 | 자연 답변·paid agent·자사 상담 | 설명·출처·브랜드 이관 |
| 승인·계정·멤버십·사후관리 | 외부 checkout·embedded·자사 거래 | 사용자 권한·중복·취소·지원 |

권장 순서는 공통 근거 정비 → 한국어·주요 시장 질문 baseline → 실제 자격 확인 → 정보/상담 pilot → 거래 연결이다. 플랫폼별 별도 지식 복제보다 같은 사실의 배포 정합성을 검토한다. 이 표는 도입 설계 가설이며 내부 LGE.com 구조 설명이 아니다.

## 30·60·90일 검증안

- **30일:** 대상 국가·제품군·핵심 과업을 정의하고 자연 답변·상품 카드·광고·브랜드 상담의 baseline을 기록한다.
- **60일:** 대표 SKU의 웹·피드·설치 FAQ를 개선하고 같은 질문·환경·반복 수로 전후 관찰한다. 시즌·프로모션 변화는 따로 표시한다.
- **90일:** 참여 자격이 확인된 채널에서 상담/구매 pilot을 검토한다. 증분 구매·마진·반품과 사용자 이관을 평가해 확대 여부를 결정한다.

실행 완료·효과 확정·예약 설정을 뜻하지 않는다. 실제 기간·표본은 담당자 데이터 접근에 맞춰 정해야 한다.

## 다음 조사

국내 네이버·해외 Google/ChatGPT의 실제 consumer 화면, Plugins 심사·merchant 자격·한국 판매 조건, Meta와 지역 commerce 플랫폼을 순차적으로 검증한다.
