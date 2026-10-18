from textbook.blocks import *
from textbook import figs as F

GOALS = [
    "3·4·5형식 수동태 공식을 같은 문장으로 비교한다.",
    "진행·완료 수동태 확장형을 만든다.",
    "수동태가 안 되는 동사와 by 이외의 전치사를 안다.",
]

INTRO = "기본형은 하나, **be + p.p.** 형식마다 '누가 주어로 올라가느냐'만 다릅니다."

BLOCKS = [
    ANCHOR("The teacher gave him a prize.", "선생님이 그에게 상을 주셨다.",
           "4형식 하나로 수동태 두 가지 → Unit 5 사역 문장의 수동태까지 연결합니다."),
    FORMULA("기본형: be + p.p."),
    FIG(F.passive_arrow(), "3형식 수동태 만들기 (수업 판서)"),
    TABLE(
        ["유형", "변환 공식", "예문"],
        [
            ["**3형식** 수동태", "O + be + p.p. + by S", "She is loved by everyone."],
            ["**4형식** 수동태 (I.O 주어)", "I.O + be + p.p. + D.O + by S", "He was given a prize (by the teacher)."],
            ["**4형식** 수동태 (D.O 주어)", "D.O + be + p.p. + to/for/of + I.O + by S", "A prize was given to him (by the teacher)."],
            ["**5형식** 수동태", "O + be + p.p. + O.C + by S", "She was made to clean the room."],
        ],
        widths=[24, 38, 38],
    ),
    TNOTE("예문 교체 이유", [
        "She is loved **by me** / He was shown my new wallet **by me** 는 공식 연습용으로는 좋지만, 실제 영어에서는 by me를 거의 쓰지 않습니다.",
        "행위자가 대명사·일반인·뻔한 사람이면 **by ~는 보통 생략**합니다. 시험 지문도 이 방식을 따릅니다.",
    ]),
    CHAIN([
        ("능동 4형식", "The teacher gave **him** **a prize**.", None),
        ("I.O 주어", "**He was given** a prize (by the teacher).", "간접목적어 him → He"),
        ("D.O 주어", "**A prize was given to him** (by the teacher).", "직접목적어가 주어면 I.O 앞에 to"),
        ("for 동사", "Mom bought him a bike. → A bike **was bought for** him.", "buy·make·cook은 D.O만 주어, for"),
    ], title="4형식 — 주어가 두 가지"),
    CHAIN([
        ("능동 5형식", "I made her clean the room.", None),
        ("수동", "**She was made to clean** the room.", "사역 동사원형 → to V"),
        ("지각", "Someone saw him enter. → **He was seen to enter**.", "지각동사도 to V"),
    ], title="5형식 — Unit 5 기준 문장의 수동태"),
    LINK(4, "사역·지각동사 O.C의 동사원형은 수동태에서 to V."),
    TABLE(
        ["확장형", "형태", "예시"],
        [
            ["**진행** 수동태", "be being p.p.", "The desk is being moved."],
            ["**완료** 수동태", "have been p.p.", "The report has been finished."],
            ["**과거완료** 수동태", "had been p.p.", "The room had been cleaned before I arrived."],
            ["**미래** 수동태", "will be p.p.", "The results will be announced tomorrow."],
        ],
        widths=[22, 30, 48],
    ),
    H("마네킹 + 옷: 수동태 옷까지 입히기"),
    P("Unit 06의 조립법에 **수동태 옷(be V p.p.)** 을 마지막에 겹쳐 입힙니다. 순서는 항상 **완료 → 진행 → 수동**."),
    FIG(F.stacks(
        F.stack("현재진행수동", ["Vs", "be V-ing", "be V p.p."], "be being V p.p.",
                "The desk <b>is being moved</b>.", "그 책상은 옮겨지는 중이다."),
        F.stack("과거완료수동", ["V-ed", "have p.p.", "be V p.p."], "had been V p.p.",
                "The room <b>had been cleaned</b> before I arrived."),
        F.stack("미래진행수동", ["will", "be V-ing", "be V p.p."], "will be being V p.p.",
                "The machine <b>will be being checked</b> then."),
        F.stack("미래완료진행수동", ["will", "have p.p.", "be V-ing", "be V p.p."], "will have been being V p.p.",
                "The chair <b>will have been being moved</b> in 2 hours.", "그 의자는 2시간 뒤면 옮겨지는 중일 것이다. (조립 시연용)"),
    )),
    PILGI([
        "미래완료진행수동 같은 형태는 문법적으로는 가능하지만 실제 사용 빈도는 {{매우 낮습니다}}. → 마네킹 + 옷 조립 연습용",
        "진행 수동 = be {{being}} p.p.  /  완료 수동 = have {{been}} p.p.",
        "4형식 D.O 주어일 때: give·show → {{to}} / make·buy → {{for}} / ask → {{of}}",
    ]),
    QUICK([
        "목적어가 없으면(자동사) 수동태 불가: happen, appear, arrive, disappear",
        "make·buy·cook (for 동사)는 **직접목적어만** 주어로",
    ]),

    STEPUP(),
    WARN([
        ("The accident ~~was happened~~.", "The accident ++happened++.", "자동사 → 수동태 X"),
        ("A cake was made ~~him~~ by Mom.", "A cake was made ++for him++ by Mom.", "make → for"),
        ("He was laughed ~~by~~ everyone.", "He was laughed ++at by++ everyone.", "구동사는 전치사까지 한 덩어리"),
    ]),
    TABLE(
        ["by 이외의 전치사", "뜻", "", ""],
        [
            ["be interested **in**", "~에 관심 있다", "be filled **with**", "~로 가득 차다"],
            ["be satisfied **with**", "~에 만족하다", "be covered **with**", "~로 덮여 있다"],
            ["be surprised **at**", "~에 놀라다", "be known **to / for / as**", "~에게 / ~로 / ~로서 알려지다"],
            ["be made **of**", "~로 만들어지다(물리)", "be made **from**", "~로 만들어지다(화학)"],
        ],
        widths=[25, 22, 28, 25],
    ),
    EX([
        ("People say that he is a genius.", "능동"),
        ("→ **It is said that** he is a genius. / He **is said to be** a genius.", "that절 목적어의 수동태 두 가지"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("수동태로 바꾸시오.  Everyone loves her.", "She is loved by everyone.", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  The desk (is moving / is being moved).", "is being moved", "책상은 옮겨지는 대상"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The accident (happened / was happened).", "happened", "자동사"),
            Q("빈칸에 알맞은 전치사를 쓰시오.  The mountain was covered ______ snow.", "with", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  A prize was given (to / for) him.", "to", "give → to"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The report (has finished / has been finished).", "has been finished", "완료 수동"),
            Q("다음 능동태를 수동태로 바르게 바꾼 것은?  My uncle bought me a bike.", "④", "buy는 D.O만 주어, for",
              options=["I was bought a bike by my uncle.", "A bike was bought to me by my uncle.",
                       "A bike bought for me by my uncle.", "A bike was bought for me by my uncle."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("두 가지 수동태로 바꾸시오.  The teacher gave him a prize.",
              "He was given a prize (by the teacher). / A prize was given to him (by the teacher).", "", lines=2),
            Q("수동태로 바꾸시오.  I made her clean the room.", "She was made to clean the room (by me).", "", lines=1),
            Q("수동태로 바꾸시오.  They had cleaned the room before I arrived.",
              "The room had been cleaned before I arrived.", "과거완료 수동 / 행위자 They는 생략", lines=1),
            Q("진행 수동태로 바꾸시오.  They are repairing the road.", "The road is being repaired.", "", lines=1),
        ]),
    ]),
]
