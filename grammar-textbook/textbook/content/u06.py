from textbook.blocks import *

GOALS = [
    "능동태를 수동태로 바꾸는 원리를 이해한다.",
    "3·4·5형식 문장의 수동태를 정확하게 만들 수 있다.",
    "시제·조동사와 결합한 수동태, by 이외의 전치사를 쓰는 수동태를 익힌다.",
]

INTRO = "수동태는 **'행동을 당하는 대상'** 을 주어로 내세우는 문장입니다. 누가 했는지보다 **무엇이 어떻게 되었는지**가 중요할 때 씁니다."

BLOCKS = [
    FORMULA("be + p.p. (+ by 행위자)", "be동사로 시제를, p.p.로 '당함'을 나타낸다"),

    H("1. 수동태 만드는 3단계"),
    PARSE([("Shakespeare", "S"), ("wrote", "V"), ("Hamlet", "O")], "능동태: 셰익스피어가 햄릿을 썼다."),
    PARSE([("Hamlet", "S"), ("was written", "V"), ("by Shakespeare", "M")], "수동태: 햄릿은 셰익스피어에 의해 쓰였다."),
    LIST([
        "**①** 능동태의 목적어 → 수동태의 주어로",
        "**②** 동사 → be + p.p. (시제와 주어의 수에 맞춰 be동사 결정)",
        "**③** 능동태의 주어 → by + 목적격 (일반인·불분명하면 생략)",
    ], title="변환 순서"),
    TIP("목적어가 있어야 수동태가 된다", [
        "1·2형식(자동사)은 수동태 불가:  The accident ~~was happened~~. → The accident ++happened++.",
        "happen, occur, appear, disappear, arrive, seem, consist of 등은 수동태 X",
    ]),

    H("2. 형식별 수동태"),
    TABLE(
        ["형식", "변환 공식", "예문"],
        [
            ["3형식", "O + be p.p. + by S", "**The window was broken** by Mike."],
            ["4형식 (I.O 주어)", "I.O + be p.p. + D.O + by S", "**He was given** a medal (by the mayor)."],
            ["4형식 (D.O 주어)", "D.O + be p.p. + **to/for/of** + I.O", "**A medal was given to** him."],
            ["5형식", "O + be p.p. + O.C + by S", "**She was elected** president."],
            ["5형식 (사역·지각)", "O + be p.p. + **to V**", "**He was made to apologize.**"],
        ],
        widths=[22, 38, 40],
    ),
    WARN([
        ("A cake was made ~~him~~ by Mom.", "A cake was made ++for him++ by Mom.",
         "make, buy, cook 등은 직접목적어만 주어로, 간접목적어 앞에 for"),
        ("I was made ~~clean~~ the room.", "I was made ++to clean++ the room.", "사역 make의 수동태: 동사원형 → to V"),
    ]),

    H("3. 시제·조동사와 결합한 수동태"),
    TABLE(
        ["형태", "공식", "예문"],
        [
            ["진행 수동태", "be **being** p.p.", "The road **is being repaired**."],
            ["현재완료 수동태", "have/has **been** p.p.", "The report **has been finished**."],
            ["과거완료 수동태", "had **been** p.p.", "The room **had been cleaned** before I arrived."],
            ["미래 수동태", "will **be** p.p.", "The results **will be announced** tomorrow."],
            ["조동사 수동태", "조동사 + **be** p.p.", "This problem **must be solved** quickly."],
        ],
        widths=[22, 30, 48],
    ),
    NOTE("미래진행·완료진행 수동태", [
        "will be being p.p., have been being p.p. 같은 형태는 문법적으로 가능하지만 실제로는 거의 쓰이지 않습니다.",
    ]),

    H("4. by 이외의 전치사를 쓰는 수동태"),
    TABLE(
        ["표현", "의미", "표현", "의미"],
        [
            ["be interested **in**", "~에 관심이 있다", "be filled **with**", "~로 가득 차다"],
            ["be satisfied **with**", "~에 만족하다", "be covered **with**", "~로 덮여 있다"],
            ["be surprised **at**", "~에 놀라다", "be known **to**", "~에게 알려져 있다"],
            ["be pleased **with**", "~에 기뻐하다", "be known **for**", "~로 유명하다"],
            ["be worried **about**", "~을 걱정하다", "be known **as**", "~로서 알려져 있다"],
            ["be made **of**", "~로 만들어지다 (물리적)", "be made **from**", "~로 만들어지다 (화학적)"],
        ],
        widths=[24, 26, 24, 26],
    ),

    H("5. 구동사의 수동태"),
    P("'동사 + 전치사/부사'로 이루어진 구동사는 **한 덩어리**로 취급합니다. 전치사를 빠뜨리지 않도록 주의합니다."),
    EX([
        ("Everyone laughed at him. → He **was laughed at** by everyone.", "그는 모두에게 비웃음을 당했다."),
        ("They put off the meeting. → The meeting **was put off**.", "회의가 연기되었다."),
        ("Grandma looked after the baby. → The baby **was looked after** by Grandma.", "아기는 할머니가 돌보셨다."),
    ]),

    H("6. 목적어가 that절일 때"),
    P("say, think, believe, know 등의 목적어가 that절이면 두 가지 수동태가 가능합니다."),
    EX([
        ("People say that he is a genius.", "능동태"),
        ("→ **It is said that** he is a genius.", "가주어 It"),
        ("→ He **is said to be** a genius.", "that절의 주어를 문장 주어로 + to V"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  English (speaks / is spoken) in many countries.", "is spoken", "영어는 '말해지는' 대상"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The accident (happened / was happened) at night.", "happened", "happen은 자동사 → 수동태 불가"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The bridge (is building / is being built) now.", "is being built", "진행 수동태: be being p.p."),
            Q("빈칸에 알맞은 전치사를 쓰시오.  The mountain was covered ______ snow.", "with", "be covered with ~로 덮이다"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The new library (has been / has) opened to the public.", "has been",
              "도서관이 '개방된' 것 → 현재완료 수동태"),
            Q("괄호 안에서 알맞은 것을 고르시오.  This homework must (finish / be finished) by tomorrow.", "be finished",
              "조동사 + be p.p."),
            Q("다음 능동태를 수동태로 바르게 바꾼 것은?  My uncle bought me a bike.", "④",
              "buy는 직접목적어(a bike)만 주어로 쓰고, 간접목적어 앞에 for",
              options=["I was bought a bike by my uncle.", "A bike was bought to me by my uncle.",
                       "A bike bought for me by my uncle.", "A bike was bought for me by my uncle."]),
            Q("다음 중 어법상 틀린 문장은?", "③", "③ 구동사는 전치사까지 포함 → The cat was taken care of by Jane.",
              options=["Wine is made from grapes.", "The singer is known to everyone.",
                       "The cat was taken care by Jane.", "He was seen to leave the house."]),
        ]),
        ("STEP 3", "서술형", [
            Q("다음 문장을 수동태로 바꿔 쓰시오.  The police have caught the thief.", "The thief has been caught by the police.",
              "현재완료 수동태 have/has been p.p.", lines=1),
            Q("다음 문장을 두 가지 수동태로 바꿔 쓰시오.  People believe that the house is haunted.",
              "It is believed that the house is haunted. / The house is believed to be haunted.",
              "It is p.p. that ~ / S + be p.p. + to V", lines=2),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  The room was filled by smoke and everyone was surprised with it.",
              "by → with, with → at", "be filled with / be surprised at", lines=1),
        ]),
    ]),
]
