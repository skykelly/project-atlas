# Atlas — AI 리서치 위키

문서와 운영을 단순하게 유지하며 AI 활용 사례·동향·근거를 축적한다.

## 주제

- [AI_SalesMarketing](AI_SalesMarketing/README.md): 영업·마케팅 AI 활용 사례. 10개 카테고리와 117개 seed 사례 초안으로 시작.
- [AI_IndustryTrend](AI_IndustryTrend/README.md): 2026년 AI 산업 변화. I-1~I-7 시장·모델·Agent·기업 지식·AX·인프라·운영 거버넌스의 원문 기반 종합, 63개 근거 문서; I-1~I-7 시장 분석 심층 보강·문체·전체 정합성 검토 완료(2026-10-07).
- [AI_GEO_AIcommerce](AI_GEO_AIcommerce/README.md): GEO & AI Commerce. 2026년 시장·10개 플랫폼, 발견·탐색/접근/측정/거래/광고/생태계/시장 행동의 7개 운영 카테고리(G-1~G-7).
- [AI_LGgroup](AI_LGgroup/README.md): LG Group AI 전략·실행. 기존 6개 테마를 유지한 2026년 공식 원문 기반 종합과 35개 사례; L-1~L-6 심층 보완; 계약·목표·시연·성과를 분리.

## 구조

```text
atlas/
├── README.md                 # 전체 안내와 운영 계획
├── AGENTS.md                 # LLM 작업 규칙
├── AI_SalesMarketing/
│   ├── README.md             # 목차·문서 작성 방식
│   ├── 1-1_…md ~ 2-5_…md     # 10개 카테고리: 정의·사례 링크·종합
│   ├── cases/                # 사례 본문·성과·출처·검증 상태
│   └── LOG.md                # 변경·보류·다음 조사
├── AI_IndustryTrend/
├── AI_GEO_AIcommerce/
├── AI_LGgroup/
├── scripts/                  # 필요한 코드와 설정만 추가
└── data/
    └── AI_SalesMarketing/
        ├── seed/             # 제공 원본 세 파일·체크섬
        └── structure-before-simplification-2026-10-05.zip
```

## 운영 원칙

**Markdown이 지식의 기준이다.** 사례 사실·성과·출처·검증은 사례 문서 안에서, 비교·시사점은 카테고리 안에서 관리한다. 조사 대기·변경 이력은 각 주제의 LOG.md에 모은다.

JSON과 HTML은 원본 또는 필요할 때 만드는 출력물이다. 별도로 편집하거나 Markdown의 변경을 다시 덮어쓰는 입력으로 사용하지 않는다. 현재 남아 있는 HTML은 이관 당시 원본으로, 최신 위키와 자동 동기화되지 않는다.

새 문서·설정·폴더는 실제 필요가 생길 때만 만든다. 공통 작업은 scripts에 파일로 추가하며 미리 역할별 폴더를 만들지 않는다. 새 크롤링 자료와 출력물은 data의 해당 주제 아래에 저장한다. 동일 사례는 한 문서만 유지하고 다른 카테고리·주제에서 링크한다.

## 현재 상태와 다음 단계

폴더 단순화와 117개 사례의 Markdown 이관을 완료했다. 모든 사례는 seed 원문 미검토 초안이다. 10개 카테고리의 정의를 유지했고 원본 세 파일의 내용은 변경하지 않았다.

1. [조사 목록](AI_SalesMarketing/LOG.md)에서 대표 사례 약 10건을 골라 원문을 검토한다.
2. 검토한 사례로 카테고리별 비교·시사점을 작성한다.
3. 최소 두 차례 반복 갱신을 확인한 뒤 기존 예약과 로컬 운영을 연결한다.
4. 이후 주제 2~4를 하나씩 확장한다.

현재 새 크롤러·예약·HTML/JSON 생성기는 연결하지 않았다. 과거 대화의 자동화가 지금도 활성인지 별도 확인이 필요하다.

[원본 JSON](data/AI_SalesMarketing/seed/cases_updated_all.json) · [원본 조사 보고서](data/AI_SalesMarketing/seed/cases_update_report.md) · [원본 HTML](data/AI_SalesMarketing/seed/ax_cases_atlas.html) · [체크섬](data/AI_SalesMarketing/seed/manifest.json)

이전 계획·설정·문서 배치는 [변경 전 보존본](data/AI_SalesMarketing/structure-before-simplification-2026-10-05.zip)에 남겨 두었다. 과거 경로·규칙은 현재 운영 기준이 아니다.

