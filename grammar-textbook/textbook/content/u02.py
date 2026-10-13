from textbook.blocks import *

GOALS = [
    "구와 절을 '동사의 유무' 하나로 구별한다.",
    "S·V·O·C 자리에 어떤 품사가 오는지 안다.",
    "보어와 목적어를 바로 구별한다.",
]

INTRO = "Unit 1의 품사가 문장 안에서 **어떤 자리(문장성분)** 를 맡는지 연결하는 단원입니다."

BLOCKS = [
    TABLE(
        ["구분", "정의", "예시"],
        [
            ["**구** (phrase)", "2단어 이상이지만 동사가 없음", "my English teacher"],
            ["**절** (clause)", "2단어 이상이며 동사가 있음", "I ran."],
        ],
        widths=[20, 44, 36],
    ),
    TABLE(
        ["문장성분", "주로 오는 품사", "설명"],
        [
            ["**S** (주어)", "명사 / 대명사", "문장의 주체"],
            ["**V** (동사)", "동사", "행동·상태"],
            ["**O** (목적어)", "명사 / 대명사", "동사의 대상"],
            ["**C** (보어)", "명사 / 형용사", "주어·목적어를 설명"],
        ],
        widths=[22, 38, 40], center=[1],
    ),
    QUICK([
        "동사가 없으면 → **구**",
        "동사가 있으면 → **절**",
        "보어는 **설명**, 목적어는 **동작의 대상**",
    ]),
    PILGI([
        "주어·목적어 자리에는 {{명사}}·대명사, 보어 자리에는 명사·{{형용사}}.",
        "부사는 문장성분이 아니다 → {{수식어(M)}}.",
        "보어 확인법: 주어 {{=}} 보어 이면 보어, 아니면 목적어.",
    ]),
    CHAIN([
        ("구", "my English teacher", None),
        ("절 (1형식)", "My English teacher ran.", "동사 ran이 붙는 순간 절"),
        ("2형식 (C)", "My English teacher is **kind**.", "teacher = kind → 보어"),
        ("3형식 (O)", "My English teacher loves **music**.", "teacher ≠ music → 목적어"),
    ], title="my English teacher 를 키워 보기"),
    PARSE([("My English teacher", "S"), ("loves", "V"), ("music", "O"), ("very much", "M")],
          "우리 영어 선생님은 음악을 아주 좋아하신다."),

    STEPUP(),
    H("구·절도 명사·형용사·부사 역할을 한다"),
    TABLE(
        ["역할", "구", "절"],
        [
            ["명사", "**To learn English** is fun.", "I know **that he is honest**."],
            ["형용사", "the girl **with long hair**", "the girl **who has long hair**"],
            ["부사", "He left **in a hurry**.", "I left **because I was tired**."],
        ],
        widths=[14, 43, 43],
    ),
    LINK(11, "that절·관계사절은 관계사 단원에서 완전/불완전으로 다시 구별합니다."),
    H("수식어를 지우면 진짜 주어가 보인다 (수일치)"),
    EX([
        ("The box (of old books) **is** heavy.", "주어 The box → 단수"),
        ("The keys (on the table) **are** mine.", "주어 The keys → 복수"),
    ]),
    WARN([
        ("One of my friends ~~live~~ in Busan.", "One of my friends ++lives++ in Busan.", "주어는 One (단수)"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 부분이 구인지 절인지 쓰시오.  I lost my umbrella ==on the bus==.", "구", "동사 없음"),
            Q("밑줄 친 부분이 구인지 절인지 쓰시오.  Call me ==when you arrive==.", "절", "you arrive"),
            Q("밑줄 친 부분의 문장성분을 쓰시오.  My dream is ==a teacher==.", "C (보어)", "My dream = a teacher"),
            Q("밑줄 친 부분의 문장성분을 쓰시오.  She met ==a teacher== yesterday.", "O (목적어)", "She ≠ a teacher"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The pictures on the wall (was / were) painted by my aunt.", "were",
              "주어 The pictures (복수)"),
            Q("다음 문장에서 수식어(M)를 모두 고른 것은?  ⓐ Yesterday ⓑ my sister ⓒ found ⓓ a wallet ⓔ on the street.",
              "②", "시간 부사·장소 전치사구는 수식어", options=["ⓐ, ⓑ", "ⓐ, ⓔ", "ⓑ, ⓓ", "ⓒ, ⓔ"]),
        ]),
        ("STEP 3", "서술형", [
            Q("S / V / O / C / M 으로 끊어 표시하시오.  The girl with the red hat looked tired after the long trip.",
              "The girl with the red hat (S) / looked (V) / tired (C) / after the long trip (M)", "", lines=2),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  The number of tourists visiting Jeju have increased.",
              "have → has", "The number of ~ 는 단수", lines=1),
        ]),
    ]),
]
