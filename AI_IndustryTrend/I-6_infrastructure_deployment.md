# I-6. AI 인프라·클라우드·배포

[주제 목차](README.md) · [모델·비용](I-2_models_cost.md) · [Agent 실행](I-3_agents_execution.md) · [Enterprise AX](I-5_enterprise_ax.md) · [변경 이력](LOG.md)

조사 범위 **2026-01-01~2026-10-07**, 기존 제품·가격표 확인일 **10-06**, 추가 에너지·시장 분석 확인일 **10-07**. 전년도 GA는 2026년 배포 선택지의 배경으로만 다뤘다. 공급자 성능·설계 수치와 실제 제공·운영 비용을 구분했다.

## 1. 인프라 선택은 chip 성능보다 업무 공급 능력이다

AI 서비스는 모델 계산 외에도 입력 처리·검색·기억·도구·파일·네트워크·재시도를 사용한다. GPU가 빠르더라도 대기열·데이터 이동·실행 환경 준비가 병목이면 고객의 완료시간은 줄지 않는다. 2026년 공개 자료는 chip 단품에서 rack·POD·메모리·네트워크·냉각을 함께 설계하고, 학습과 추론의 요구를 구분하는 방향을 보여 준다.

| 업무 유형 | 우선 요구 | 주요 병목 |
|---|---|---|
| 대규모 학습·post-training | 동기화·메모리·checkpoint·goodput | interconnect·장애·재시작 |
| 대화형 추론 | TTFT·사용자당 token 속도·동시성 | queue·KV cache·메모리 bandwidth |
| 일괄 분석 | 처리량·비용·기한 | data loading·batch·capacity |
| Agent 업무 | 모델+tool+state+compute | 다단계 지연·외부 도구·복구 |
| Local·edge | 연결·응답·데이터 경계 | 메모리·전력·갱신·관리 |

이 구분은 선택을 위한 분석이다. peak FLOPS는 초당 이론 연산량, goodput은 실제 유용한 계산·처리의 비율이다. 서로 다른 정밀도·모델·latency 조건의 수치를 나란히 놓고 단일 순위를 만들면 업무 성능을 잘못 판단할 수 있다.

## 2. 2026년 주요 공급 변화

| 시점 | 변화 | 단계·선택에 미치는 의미 | 근거 |
|---|---|---|---|
| 01-05 | NVIDIA Rubin 6-chip platform | MoE·memory·network 공동 설계 | [Rubin](evidence/NV-RUBIN-20261006-001.md) |
| 01-26 | Microsoft Maia 200 | inference 중심·Iowa 배치·SDK preview | [Maia](evidence/MS-MAIA-20261006-001.md) |
| 04-16 | IEA 에너지 전망 갱신 | 효율 향상과 총수요·공급 병목 동시 관측 | [IEA](evidence/IEA-ENERGY-20261006-001.md) |
| 04-22 | TPU 8t·8i | 학습·추론 특화; 발표상 coming soon | [TPU](evidence/GOO-TPU-20261006-001.md) |
| 05-31 | Vera Rubin full production ramp | 5-rack POD·agent throughput 비교 | [생산 단계](evidence/NV-RUBIN-20261006-001.md) |
| 07-23 | AMD Helios in production | rack 설계·OEM·고객별 배포 일정 | [AMD](evidence/AMD-HELIOS-20261006-001.md) |
| 09-29 연결 | Bedrock Managed Agents powered by OpenAI | 현행 Preview, Codex harness+AgentCore AWS 실행 | [AWS](evidence/AWS-TRAINIUM-20261006-001.md) |
| 10-06 확인 | Trainium3·TPU 공개 가격 | 기존 GA·현재 상품 조건으로 배포 비용 검토 | [AWS](evidence/AWS-TRAINIUM-20261006-001.md)·[가격](evidence/GOO-TPU-20261006-001.md) |

발표·생산 ramp·OEM 판매·cloud quota·기업의 실제 운영 시작은 서로 다르다. 7월 AMD는 production을 발표하면서도 OpenAI의 online 시작은 Q4 예정, Meta는 testing/validation이라고 설명했다. 구매 담당자는 공급 형태·리전·capacity 조건으로 실제 도입 일정을 확인해야 한다.

## 3. GPU·custom accelerator의 비교 조건

| 플랫폼 | 공개 구성·지표 | 비교할 때 지킬 조건 |
|---|---|---|
| NVIDIA Vera Rubin | 6-chip 공동 설계; Blackwell 대비 MoE token cost 최대 10배 낮음, training GPU 4배 적음 | 공급자 특정 비교; 모든 API 가격·모델의 가속 아님 |
| AMD Helios | 72 MI455X·18 Venice CPU; rack HBM4 31TB·peak FP4 2.9EF | reference design·내부 분석, 실제 workload goodput과 구분 |
| Google TPU 8t | 9,600-chip superpod·2PB HBM; goodput 97% 초과 target | target을 모든 고객 실측으로 쓰지 않음 |
| Google TPU 8i | 288GB HBM·384MB SRAM; 이전 세대 대비 performance/$ +80% | 내부 비교·모델/latency 조건과 출시 단계 확인 |
| AWS Trn3 | 최대 144 chips·362 FP8 PFLOPs; Trn2 대비 성능 최대 4.4배 | 2025-12 GA 배경; Neuron·지원 모델·capacity 확인 |
| Microsoft Maia 200 | 216GB HBM3e·7TB/s; 750W chip TDP·fleet 대비 performance/$ +30% | 내부 fleet 비교; TDP와 시스템 실소비·고객 VM 구매 구분 |

[Rubin](evidence/NV-RUBIN-20261006-001.md) · [AMD](evidence/AMD-HELIOS-20261006-001.md) · [TPU](evidence/GOO-TPU-20261006-001.md) · [Trainium](evidence/AWS-TRAINIUM-20261006-001.md) · [Maia](evidence/MS-MAIA-20261006-001.md).

수치의 목적이 달라 이 표로 승자를 정할 수 없다. rack 메모리와 chip TDP, 최대 연산량과 tokens/$를 비교할 수 없기 때문이다. FP4·FP8·sparsity·batch·context·동시성·p95 latency를 고정한 업무 실험으로 선택해야 한다. 공급자가 공개 표준·framework 지원을 강조해도 kernel·compiler·quantization·운영 도구의 이식 비용은 남을 수 있다.

AMD 현행 페이지에는 per-GPU bandwidth 23.3TB/s와 compute-tray 19.6TB/s가 함께 있다. 이번 비교는 이 값을 단일 확정값으로 채택하지 않았다. 원문 내부의 표현 차이도 구매·벤치마크에서 확인할 조건이다.

## 4. 긴 context와 Agent가 만드는 메모리·통신 부담

추론은 입력을 처리하는 prefill과 token을 순차 생성하는 decode의 성격이 다르다. 많은 사용자의 긴 대화를 동시에 유지하면 모델 weights와 함께 KV cache와 중간 상태를 메모리에 유지해야 한다. Agent가 여러 도구 결과를 읽고 반복하면 모델 호출·저장·네트워크가 함께 늘어난다.

| 설계·운영 항목 | 기대 효과 | 함께 보는 비용·조건 |
|---|---|---|
| HBM·SRAM·KV cache | 데이터 대기 줄이기·긴 context | 유효 capacity·cache 정책·동시성 |
| Scale-up·scale-out network | 큰 모델·여러 chip 협업 | 통신 패턴·장애·혼잡·topology |
| Batch·routing | 처리량·작은 모델 활용 | tail latency·품질·queue |
| Checkpoint·session | 중단 후 재개 | 저장·복원·외부 side effect |
| CPU·storage·tools | 입력·자료·실행 연결 | GPU 유휴 시간·전체 완료 지연 |

이 표는 기술 해설·평가 항목이다. Google은 8t/8i를 학습·추론으로 나누고 메모리·interconnect·냉각을 함께 설계한다. NVIDIA·AMD도 rack 전체의 구성과 연결을 강조한다. 고객은 chip 성능에 더해 업무를 실행할 메모리·연결·냉각 구성을 비교해야 한다.

Agent의 stateful compute 선택은 [I-3](I-3_agents_execution.md)에 연결한다. runtime microVM invocation 8시간과 EC2 instances 세션 최대 14일은 서로 다른 조건이며, 긴 세션이 memory의 영구 보존이나 모든 작업의 성공을 보장하지 않는다.

## 5. 공개 가격 — chip-hour와 model tokens를 구분

다음은 **10-06 확인, USD/chip-hour**다. cloud quota·최소 topology·예약·부대비용을 확인해야 하며, 서로 다른 세대의 품질·속도가 같다는 가정은 하지 않는다.

| TPU·리전 | On Demand | 1년 commitment | 3년 commitment |
|---|---:|---:|---:|
| Ironwood·us-central1 | $12.00 | $8.40 | $5.40 |
| Trillium·us-east1 | $2.70 | $1.89 | $1.22 |
| Trillium·asia-northeast1 | $3.24 | $2.27 | $1.46 |

[현재 표·단위](evidence/GOO-TPU-20261006-001.md). node가 READY인 동안 과금된다. 여러 chip이 하나의 VM을 구성하므로 chip-hour를 VM 전체 요금으로 읽으면 비용이 과소 추정된다. 이 표에는 TPU 8t/8i 가격이 없으며 기존 세대 가격을 새 제품에 적용하지 않는다.

**가상 비용 예시**: Ironwood us-central1 chip 4개를 100시간 확보하면 On Demand accelerator 항목은 4×100×$12=$4,800이다. 유용한 처리 시간을 40시간으로 가정하면 유용 chip-hour당 비용은 $30, 80시간이면 $15다. 실제 지원 topology·VM 구성·storage·network·운영비를 제외한 단위 계산이며 구매 가능한 SKU 견적이 아니다.

장기 할인은 같은 기간 계속 비용을 부담하는 commitment다. 사용률·모델 변경·리전 이동·capacity 조건을 무시하고 할인율만 비교하면 위험하다. 모델 API는 [I-2](I-2_models_cost.md)의 token·tool 단위, 자체 배포는 compute 시간과 이용률이 비용의 시작점이다.

## 6. 효율 향상과 총전력 증가가 함께 일어나는 이유

| IEA 2026 갱신 | 값·범위 | 관측과 전망 구분 |
|---|---|---|
| 2025년 모든 데이터센터 전력 | 485TWh·전년비 +17% | 보고서의 과거 관측 추정 |
| AI-focused 데이터센터 2025 증가 | +50% | 전체 data centre와 다른 모집단 |
| 2030년 모든 데이터센터 전력 | 950TWh·세계 약 3% | central projection |
| AI-focused 2025→2030 | 약 3배 | 전망 |
| AI server power density | 2020~2025 11배·2027까지 추가 4배 | 과거 변화와 전망 분리 |

[2026-04-16 보고](evidence/IEA-ENERGY-20261006-001.md). 효율이 개선되면 같은 과업에 필요한 전력은 줄 수 있다. 동시에 사용자가 늘고 단순 문장 생성에서 긴 reasoning·video·agentic work로 과업이 바뀌면 총사용량은 증가한다. 따라서 ‘query당 효율 개선’과 ‘데이터센터 총수요 증가’는 모순이 아니다.

이 수치들은 AI만의 전력 소비를 정확히 분리한 세계 전수 계량값이 아니다. TWh는 일정 기간 소비 에너지이고 GW는 전력·capacity다. 계약서의 GW를 연간 소비 TWh로 바꾸려면 실제 부하와 가동시간을 고정해야 한다.

## 7. 공급 병목은 chip 외부에도 있다

| 병목 | 배포에 미치는 영향 | 기업이 확인할 질문 |
|---|---|---|
| HBM·제조·package | 시스템 수량·일정 | 실제 납기·지원 구성·대체 수단 |
| 전력 연결·변압기 | 부지·시운전 지연 | 확정 전력·연결 시점·증설 비용 |
| Rack density·냉각 | 기존 공간 사용 불가 | liquid cooling·전력 shelf·시설 개조 |
| 자금·capacity 계약 | 비용·이용률 부담 | commitment·유휴·가격 변경 |
| 소프트웨어·운영 | 성능·개발 일정 | kernel·model 지원·장애·관측 |

IEA는 HBM과 전력·grid·허가·자금의 제약을 지적한다. 글로벌 전력 증가가 모든 지역의 전기요금 상승으로 직결된다고 보지는 않는다. 공급 여력·부하 집중·투자 비용 배분이 다르기 때문이다. 한국의 개별 부지·인허가·요금은 이번 조사에서 확인하지 않았다.

NVIDIA production ramp나 AMD reference design 공개는 설치 가능한 시설·quota까지 확보되었다는 뜻이 아니다. 기존 data centre를 새 rack에 활용할 때도 전력·냉각·network·운영 인력의 조건을 따로 검토해야 한다.

### 7.1 자체 발전도 설비·납기·자금을 요구한다

IEA의 4월 보고를 10월 7일 재확인했다. 안정적인 onsite gas 공급을 설계하려면 변동하는 데이터센터 부하 대비 발전 설비를 30~70% 더 확보해야 한다는 분석이다. 2030년 onsite gas 15~27GW와 데이터센터 배터리 20~25GW는 전망이다. 터빈 공급이 부족하면 전력망 연결을 기다리지 않는 선택도 납기를 단축하지 못할 수 있다. [조건·근거](evidence/IEA-ENERGY-20261006-001.md)

| 공급 선택 | 줄일 수 있는 제약 | 함께 발생하는 책임 |
|---|---|---|
| 전력망 연결 | 발전 설비의 자체 운영 부담 | 연결 대기·계통 증설·요금 계약 |
| 자체 가스 발전 | 계통 연결 의존 일부 | 여유 발전 설비·연료·터빈 납기·허가 |
| 배터리·부하 조절 | 급격한 부하 변동·짧은 공급 공백 | 저장 시간·열화·운영 제어·비용 |
| 여러 리전 배포 | 특정 지역의 capacity 부족 | 데이터 이동·지연·규정·중복 운영 |

표는 선택의 작동 원리를 비교한다. 발표된 GW를 즉시 사용할 수 있는 확정 연산으로 읽지 않는다. 발전 설비가 있어도 서버·냉각·네트워크가 준비되고 모델이 허용 지연 안에서 작동해야 고객 업무를 처리한다. 한국 프로젝트의 자체 발전 가능성·허가·전력 단가를 검증한 표는 아니다.

시설 공급자는 전력·냉각·저장·제어를 함께 제공하는 기회를 얻을 수 있다. 그러나 높은 rack 밀도가 시설 업체의 매출로 바로 전환되지는 않는다. 고객 부지의 개조 가능성, 제품 인증, 실제 납기·운영 성능과 계약 범위가 매출 인식의 조건이다. 이 전망은 시장 구조의 분석이며 특정 한국 기업의 계약·매출을 확인한 결과는 아니다.

### 7.2 계약·설비·가동률의 시간차가 자금 부담을 만든다

[I-1의 Oracle 실적](evidence/ORCL-EARN-20261007-001.md)은 실제 서비스 매출·미이행 계약·현금흐름을 분리한다. 이 구분을 인프라 구매에도 적용해야 한다. 장기 고객 계약이 먼저 늘어도 전력과 장비를 확보하는 동안 투자금이 나간다. 설치한 장비를 충분히 쓰지 못하면 할인받은 chip-hour보다 유용한 처리 시간당 원가가 높아진다.

| 시점 | 확인할 기록 | 비용·위험이 발생하는 경로 |
|---|---|---|
| 계약 | 최소 사용·기간·취소·공급 조건 | 사용 전에도 약정 부담이 생길 수 있음 |
| 시설·장비 조달 | 확정 전력·납기·시운전·대금 일정 | 수익 발생보다 투자 지출이 앞섬 |
| 서비스 개시 | quota·리전·모델·실제 가동 | 공급 지연·지원 구성 차이 |
| 반복 운영 | 이용률·수락 처리량·장애·교체 | 유휴·재시도·모델 교체가 원가를 바꿈 |

IEA는 증설에 자본시장 자금이 중요해지면서 투자 수익 기대와 조달 조건이 성장 속도에 영향을 준다고 분석한다. 전력 전망도 투자·장비 공급·사용량의 영향을 받는다. 2026년 전체 설비투자가 이미 확정되었다고 쓰거나 장기 계약을 올해 가동률에 대입하지 않는다.

기업이 자체 배포를 선택할 때는 보안 요구와 함께 지속 부하를 확인한다. 내부 전용 장비가 낮은 이용률로 대기하면 외부 API 단가 인하의 이익을 얻기 어렵다. 반대로 높은 반복 부하와 고정된 지연·데이터 조건이 있으면 자체 배포가 유리해질 수 있다. 손익분기점은 모델·시설·지원 인력·계약마다 달라 이 문서에서 보편 사용률을 정하지 않는다.

## 8. API·managed runtime·cloud compute·local 선택

| 배포 방식 | 주로 맡기는 책임 | 적합한 후보 상황 | 조직에 남는 책임 |
|---|---|---|---|
| Model API | 모델 serving·accelerator | 변동 사용·빠른 실험 | data·tools·품질·사용량 |
| Managed Agent | loop·state·compute 일부 | 긴 업무·실행 기반 부담 감소 | 승인·완료·권한·데이터 계약 |
| Cloud accelerator | 시설·hardware 일부 | 자체 model·큰 지속 부하 | serving·porting·이용률·관측 |
| On-prem | 외부 공급 의존 축소 | 데이터/연결/지속 부하 요구 | 시설·hardware·software·보안·교체 |
| Edge·local | 현장 응답·연결 독립 | 제한 연결·현장 자료 | device fleet·model 갱신·메모리·전력 |

이 표는 적용 선택 기준이다. Self-hosted sandbox는 실행 환경의 위치를 뜻하며 모든 model inference·session data도 같은 위치에 있다는 보장은 아니다. OpenAI Agents API의 미국 residency·ZDR 조건과, AWS 내부 runtime/inference를 설명하는 Bedrock Managed Agents Preview는 서로 다른 상품 조건으로 읽어야 한다. [API 조건](evidence/OAI-AGENTS-20261006-001.md) · [AWS 조건](evidence/AWS-TRAINIUM-20261006-001.md)

### 8.1 효율 개선이 공급자와 고객에게 전달되는 경로

| 변화 | 공급자가 얻을 수 있는 것 | 고객에게 전달될 조건 |
|---|---|---|
| chip·serving 효율 개선 | 같은 장비로 더 많은 처리·마진 여력 | 가격 인하 또는 같은 가격의 처리량 확대 |
| 긴 context·Agent 확대 | 실행·저장·compute 매출 기회 | 전체 호출·도구·재시도 원가 통제 |
| 시설 공급 병목 | 확보한 capacity의 계약 가치 | 실제 quota·리전·납기와 지연 준수 |
| 모델·accelerator 교체 | 새 제품 판매·구축 서비스 | porting·재검증·유휴 비용을 상쇄 |

이 표는 수익·비용 전달의 가설이다. 공급자 tokens/$ 개선률을 고객 API 요금 인하율로 바꿀 수 없다. 고객이 구매하는 단위가 tokens, 실행 시간, 사용자 구독, 수락 과업 중 무엇인지 먼저 맞춰야 한다. [I-2의 가격](I-2_models_cost.md)·[I-5의 과금](I-5_enterprise_ax.md)·[I-7의 비용 통제](I-7_operations_trust_governance.md)를 연결하면 기술 효율이 청구와 업무 결과에 도달하는 경로를 추적할 수 있다.

## 9. 배포 전 비교할 측정표

1. 같은 model·quantization·context·출력·동시성을 고정한다.
2. TTFT·tokens/s/user·p95 완료시간·deadline 성공률을 측정한다.
3. hardware 유휴·cache·retry·tool 대기를 포함한다.
4. 과업 품질과 수락률이 유지되는지 검증한다.
5. compute·storage·network·license·porting·운영·장애 원가를 합친다.

| 판단 기준 | 실질적 확인 |
|---|---|
| 품질당 비용 | 수락된 결과당 전체 비용 |
| 생산성 | queue·retry를 포함한 유용 처리량 |
| 신뢰성 | 장애·재개·복원·업데이트 시간 |
| 공급 | quota·리전·납기·전력·지원 계약 |
| 이동성 | model·kernel·tool·data의 전환 비용 |

2026년 공급자는 chip 성능과 serving 효율을 높이고 시설·전력 공급을 확보하려 한다. 공개 최대치·설계 수치만으로 고객의 실제 비용을 확정할 수는 없다. 구매자는 품질·지연·데이터 조건을 고정한 뒤 확보 가능한 공급과 유용한 처리량을 대조하고, 이용률·검수·유지 비용을 포함해 배포 방식을 결정해야 한다.
