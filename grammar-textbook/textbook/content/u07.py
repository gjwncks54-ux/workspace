from textbook.blocks import *

GOALS = [
    "to부정사·동명사·분사의 형태와 역할을 한 표로 정리한다.",
    "준동사가 '동사의 성질'을 그대로 가진다는 것을 이해한다.",
]

INTRO = "준동사는 **동사에서 출발했지만 문장 안에서는 명사·형용사·부사처럼** 쓰입니다. Unit 8~10과 Unit 13 분사구문의 지도 역할을 하는 단원입니다."

BLOCKS = [
    ANCHOR("Having eaten lunch, I'm full now.", "점심을 먹어서 지금 배부르다.", "부사절 → 분사구문 → 부정형까지, 준동사의 공통 성질을 이 문장으로 확인합니다."),
    TABLE(
        ["종류", "형태", "문장 안 역할"],
        [
            ["**to부정사**", "to + V", "명사 / 형용사 / 부사"],
            ["**동명사**", "V-ing", "명사"],
            ["**분사**", "V-ing / p.p.", "형용사"],
        ],
        widths=[28, 32, 40], center=[1, 2],
    ),
    PILGI([
        "준동사는 동사에서 출발했지만 문장 안에서는 명사·형용사·부사처럼 쓰입니다.",
        "{{not}} + 준동사 형태가 가능하고, {{목적어}}나 부사의 수식을 받을 수 있습니다.",
        "완료형 {{have p.p.}}가 가능하며, 본동사보다 시제가 {{앞설}} 때 사용합니다.",
        "준동사는 동사의 특징을 갖고 있다. (부사 수식, 자동사/타동사 등)",
        "동사의 과거: V-ed  /  준동사의 과거: {{have p.p.}} = 주절보다 {{1시제}} 빠름",
        "예: Having eaten lunch, I'm full now.",
    ]),
    CHAIN([
        ("부사절", "**Because I have eaten** lunch, I'm full now.", None),
        ("분사구문", "**Having eaten** lunch, I'm full now.", "먹은 것이 배부른 것보다 먼저 → having p.p."),
        ("부정", "**Not having eaten** lunch, I'm hungry now.", "not은 준동사 맨 앞"),
    ], title="Having eaten lunch, I'm full now."),
    LINK(5, "eat lunch 시제 줄기 → 준동사에서도 '먼저 일어난 일'은 완료형."),
    LINK(13, "분사구문에서 having p.p.를 다시 씁니다."),
    QUICK([
        "한 절에 시제 있는 **본동사는 하나**. 나머지 동사 모양은 전부 준동사.",
        "주어 자리에 동사를 쓰고 싶으면 → **to V / V-ing**",
    ]),

    STEPUP(),
    H("준동사 공통 문법 4가지"),
    TABLE(
        ["성질", "to부정사", "동명사"],
        [
            ["의미상 주어", "**for** + 목적격 (성격 형용사는 **of**)", "**소유격**(목적격)"],
            ["부정", "**not** to V", "**not** V-ing"],
            ["완료형 (더 이전)", "to **have p.p.**", "**having p.p.**"],
            ["수동형", "to **be p.p.**", "**being p.p.**"],
        ],
        widths=[22, 39, 39],
    ),
    EX([
        ("It is hard **for me** to wake up early. / It was kind **of you** to help me.", "의미상 주어 for / of"),
        ("He seems **to have been** rich.  = It seems that he **was** rich.", "완료 부정사"),
        ("I hate **being treated** like a child.", "동명사 수동형"),
    ]),
    WARN([
        ("Exercise regularly ~~help~~ you stay healthy.", "++Exercising++ regularly ++helps++ you stay healthy.",
         "본동사는 하나 → 주어 자리 동사는 준동사로"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 부분의 준동사 종류를 쓰시오.  ==Learning== a new language takes time.", "동명사", ""),
            Q("밑줄 친 부분의 준동사 종류를 쓰시오.  I have homework ==to do==.", "to부정사", ""),
            Q("밑줄 친 부분의 준동사 종류를 쓰시오.  Look at the ==broken== window.", "분사 (과거분사)", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  (Having eaten / Eating) lunch an hour ago, I'm full now.", "Having eaten",
              "먹은 것이 먼저"),
            Q("괄호 안에서 알맞은 것을 고르시오.  She decided (not to go / to not go).", "not to go", "not은 준동사 앞"),
            Q("괄호 안에서 알맞은 것을 고르시오.  It is very nice (for / of) you to say so.", "of", "성격 형용사"),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("분사구문으로 바꾸시오.  Because I have finished my homework, I can watch TV now.",
              "Having finished my homework, I can watch TV now.", "", lines=1),
            Q("분사구문으로 바꾸시오.  Because I didn't eat lunch, I'm hungry now.",
              "Not having eaten lunch, I'm hungry now.", "부정 + 완료", lines=1),
            Q("같은 뜻이 되도록 완성하시오.  It seems that she was a singer. = She seems ______ a singer.",
              "to have been", "", lines=1),
        ]),
    ]),
]
