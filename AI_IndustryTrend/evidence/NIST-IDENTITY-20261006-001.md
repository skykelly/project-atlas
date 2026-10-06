---
id: "NIST-IDENTITY-20261006-001"
category: "I-7"
company: "NIST"
tags: ["industry_trend", "2026", "governance"]
review_status: "reviewed"
source_checked_at: "2026-10-07"
updated_at: "2026-10-07"
evidence_type: "primary_source_review"
independent_verification: "not_reproduced"
---

# Agent 표준화와 위임 신원의 운영 기준

[주 카테고리](../I-7_operations_trust_governance.md) · [근거 목차](../README.md)

## 원문과 근거 위치

| 발표·문서 시점 | 출처·근거 위치 |
|---|---|
| 2026-02-17 발표 | [three pillars](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure) |
| 2026-05-18 보고 | [Abstract; RFI response summary](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai) |
| 2026-08-27 게시 | [Credential Sharing; Static and Long-lived Credentials; Broadly Scoped Access](https://www.nist.gov/blogs/cybersecurity-insights/back-future-why-agentic-ai-needs-strong-identity-foundation) |

## 확인한 내용과 조건

- 2월 Initiative는 산업 주도 표준·공개 protocol·security/identity 연구의 세 축이다. 인증 프로그램 완성이나 특정 제품 승인이라는 뜻이 아니다.
- 5월 보고서는 RFI 응답의 종합이다. 새 위협과 기존 cybersecurity 원칙의 적응 필요성에 대한 응답자 의견이며 공격 발생률의 모집단 조사·독립 실험이 아니다.
- 8월 글은 사용자 비밀번호 공유 대신 Agent 고유 신원과 위임 관계, 좁은 scope·짧은 수명·대상 제한 credential을 설명한다. OAuth·SPIFFE 등의 기존 기반을 활용하되 신원 확인 자체가 모든 transaction 권한을 뜻하지 않는다.

## 검증 수준·한계

표준화의 진행과 설계 권고를 구분했다. 조직의 IAM 설정·토큰 회수·위임 체인은 실제 검사하지 않았다.

`reviewed`는 위 URL의 원문 확인이다. 독립 재현·고객 계약·계정 설정·실제 배포 검증을 뜻하지 않는다. 개별 미열람 PDF·하위 문서는 위 한계에 구분했다.

## 2026-10-07 추가 원문 확인

- [9월 29일 공개](https://www.nist.gov/news-events/news/2026/09/comments-software-and-agentic-ai-identity-concept-paper): 600명 초과 commenter의 의견 종합과 첫 DevSecOps 구현 use case를 설명한다. 완료 인증·시장 채택률이 아니다.
- [Resource hub 의견 종합](https://pages.nist.gov/nccoe-ai-identity/summary-of-comments.html): Agentic Deployment Models·Ephemeral Identity·Task Scoped Authorization·Signed Intent·Delegation·Auditability·Standards를 읽었다.

내부 관리·외부 고객 접점·외부 소유 Agent의 세 배포 형태를 구분한다. 행동 단위 판정·임시 credential·하위 위임 scope 축소·회수·위임 chain과 정책 기록을 강조한다. MCP·A2A는 연결/협업 protocol이며 완결된 identity·authorization 체계로 취급하지 않는다. 서명된 intent 표현은 합의된 공통 구현 표준이 아직 남은 과제다.

내용은 NIST가 정리한 공개 의견·설계 과제다. 의견이 개별 법적 의무·모든 구현의 검증된 효능을 뜻하지 않는다. 하위 protocol specification과 조직 IAM·실제 회수·거래 gate를 전수 검사하지 않았다.
