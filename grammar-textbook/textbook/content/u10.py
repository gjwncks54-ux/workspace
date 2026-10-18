from textbook.blocks import *

GOALS = [
    "현재분사(능동·진행)와 과거분사(수동·완료)를 구별한다.",
    "감정 분사를 '일으키는 쪽 / 느끼는 쪽'으로 고른다.",
    "분사의 위치(전치·후치수식)를 꾸며 주는 말의 길이로 판단한다.",
]

INTRO = "분사는 동사를 **형용사처럼** 쓰는 것. 기준은 하나, 꾸밈받는 명사가 **하는가(-ing) 당하는가(p.p.)**."

BLOCKS = [
    ANCHOR("Look at the baby sleeping in the bed.", "침대에서 자고 있는 아기를 봐.", "a sleeping baby → a baby sleeping in the bed → a baby who is sleeping: 분사 위치와 관계사를 한 번에."),
    TABLE(
        ["종류", "핵심 의미", "예시"],
        [
            ["**현재분사** V-ing", "능동 / 진행", "a tree standing on the hill"],
            ["**과거분사** p.p.", "수동 / 완료", "a broken window"],
        ],
        widths=[28, 30, 42],
    ),
    TABLE(
        ["구분", "의미", "예문"],
        [
            ["감정을 **일으키는** 대상", "-ing", "The movie is exciting."],
            ["감정을 **느끼는** 대상", "p.p.", "I am excited."],
        ],
        widths=[36, 18, 46], center=[1],
    ),
    PILGI([
        "꾸며주는 말이 {{2단어}} 이상이면 후치수식을 한다.",
        "- I have a tall tree. ({{전치수식}})",
        "- I have a tree standing on the hill. ({{후치수식}})",
        "감정 형용사: 감정을 만드는 대상 → {{-ing}} / 감정을 받는 대상 → {{V p.p.}} (주로 사람, 동물)",
    ]),
    CHAIN([
        ("전치수식", "a **sleeping** baby", "짧으면 명사 앞"),
        ("후치수식", "a baby **sleeping in the bed**", "길어지면 명사 뒤"),
        ("관계사절", "a baby **who is sleeping** in the bed", "후치수식 분사 = 관계대명사 + be 생략"),
    ], title="a sleeping baby → a baby sleeping in the bed"),
    CHAIN([
        ("p.p.", "a **broken** window", "창문이 깨진 (수동)"),
        ("p.p. 후치", "a window **broken by the kids**", None),
        ("-ing", "the kids **breaking** the window", "아이들이 깨는 (능동)"),
    ], title="break — 능동과 수동"),
    CHAIN([
        ("-ing", "The movie is **exciting**.", "영화가 흥분을 일으킴"),
        ("p.p.", "I am **excited**.", "내가 흥분을 느낌"),
        ("사람도 -ing", "He is a **boring** person.", "그가 지루함을 일으킴"),
    ], title="excite"),
    LINK(11, "후치수식 분사 = 관계대명사 + be 생략"),
    LINK(13, "분사구문도 같은 기준: 주어가 하면 V-ing, 당하면 p.p."),
    QUICK([
        "명사가 직접 하면 → **V-ing**  /  명사가 당하면 → **p.p.**",
        "감정: 사물이 주어 → 대체로 **-ing** / 사람이 주어 → 대체로 **p.p.** (단, 사람이 일으키면 -ing)",
    ]),

    STEPUP(),
    TABLE(
        ["동사", "-ing (일으키는)", "p.p. (느끼는)"],
        [
            ["bore", "boring", "bored"],
            ["interest", "interesting", "interested"],
            ["surprise", "surprising", "surprised"],
            ["disappoint", "disappointing", "disappointed"],
            ["confuse", "confusing", "confused"],
            ["satisfy", "satisfying", "satisfied"],
        ],
        widths=[30, 35, 35], center=[1, 2], caption="자주 나오는 감정 분사",
    ),
    H("보어로 쓰이는 분사"),
    EX([
        ("I found the door **locked**.", "문이 잠긴 (목적격보어)"),
        ("Don't leave the water **running**.", "물이 흐르는 (목적격보어)"),
        ("**fallen** leaves / a **retired** teacher", "자동사의 p.p. = 완료 (떨어진, 은퇴한)"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Look at the (breaking / broken) window.", "broken", "창문이 깨진"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I saw a tree (standing / stood) on the hill.", "standing", "나무가 서 있는"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The movie was (exciting / excited).", "exciting", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  I am (exciting / excited) about the trip.", "excited", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The language (speaking / spoken) in Brazil is Portuguese.", "spoken", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  Please keep the door (closing / closed).", "closed", ""),
            Q("다음 중 어법상 틀린 문장은?", "③", "학생들이 흥미를 느낌 → interested",
              options=["The story was very touching.", "There's a man waiting outside.",
                       "The students were interesting in science.", "I had my watch fixed."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("분사를 이용해 바꾸시오.  Look at the baby who is sleeping in the bed.", "Look at the baby sleeping in the bed.", "", lines=1),
            Q("분사를 명사 앞에 두어 바꾸시오.  The window was broken. Don't touch it. → Don't touch the ______.",
              "broken window", "", lines=1),
            Q("어법상 틀린 부분을 고치시오.  The lecture was bored, so I fell asleep.", "bored → boring", "", lines=1),
        ]),
    ]),
]
