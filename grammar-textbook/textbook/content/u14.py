from textbook.blocks import *

GOALS = [
    "장소부사구 도치와 부정어 도치의 규칙을 구별한다.",
    "도치 문장에서 진짜 주어를 찾아 끊어 읽는다.",
]

INTRO = "도치는 **강조하고 싶은 말을 앞으로** 보내면서 주어와 동사 순서가 바뀌는 것. 장소면 S↔V, 부정어면 의문문 어순."

BLOCKS = [
    ANCHOR("Never does he study English.", "그는 결코 영어를 공부하지 않는다.", "He never studies English → 부정어를 앞으로 → 의문문 어순."),
    TABLE(
        ["유형", "핵심 규칙", "예문"],
        [
            ["**장소부사구 / 전치사구 도치**", "장소 표현을 앞으로 보내고 S ↔ V, 단 주어가 대명사면 보통 도치하지 않음",
             "In the car are the kids. / Here it comes."],
            ["**부정어 도치**", "의문문 어순으로 바뀜", "Never does he study English."],
        ],
        widths=[24, 40, 36],
    ),
    PILGI([
        "부정어 예: never, not, little, few, rarely, scarcely",
        "끊어 읽기 포인트: 긴 주어 뒤 / {{동사}} 뒤 / 목적어 뒤 / {{전치사}} 앞 / 수식어 앞",
        "장소 도치 → 그냥 {{S ↔ V}}  /  부정어 도치 → {{의문문}} 어순 (do/does/did)",
    ]),
    CHAIN([
        ("원래", "The kids are in the car.", None),
        ("장소 도치", "**In the car are the kids.**", "S ↔ V"),
        ("대명사 주어", "Here comes **the bus**. / Here **it comes**.", "대명사는 도치 X"),
    ], title="In the car are the kids"),
    CHAIN([
        ("원래", "He never studies English.", None),
        ("부정어 도치", "**Never does he study** English.", "의문문처럼 does + S + 원형"),
        ("과거", "Never **did he study** English.", None),
        ("완료", "Never **has he studied** English.", "have/has를 앞으로"),
    ], title="Never does he study English"),
    QUICK([
        "도치 문장은 **동사 뒤에서** 진짜 주어를 찾는다 → 동사 수일치 확인",
        "부정어 뒤에 일반동사가 그대로 있으면 틀린 것 → **do/does/did**",
    ]),
    LINK(15, "가정법 if 생략 도치: Were I you, … / Had I known, …"),

    STEPUP(),
    WARN([
        ("In the box ~~was~~ many old letters.", "In the box ++were++ many old letters.", "진짜 주어 letters (복수)"),
        ("Little ~~did I knew~~ about it.", "Little ++did I know++ about it.", "did 뒤 원형"),
    ]),
    TABLE(
        ["더 나오는 도치", "예문"],
        [
            ["Only + 부사(구)", "**Only then did I realize** the truth."],
            ["Not until ~", "**Not until** I lost my health **did I realize** its value."],
            ["No sooner ~ than", "**No sooner had I arrived than** it began to rain."],
            ["So / Neither", "I'm hungry. — **So am I.** / I can't swim. — **Neither can I.**"],
        ],
        widths=[26, 74],
    ),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  In the car (are the kids / the kids are).", "are the kids", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  Here (comes it / it comes).", "it comes", "대명사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Never (he studies / does he study) English.", "does he study", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  On the table (was / were) a cup and a book.", "were", ""),
            Q("다음 중 어법상 틀린 문장은?", "③", "Only then did I understand",
              options=["Rarely does she eat breakfast.", "Under the tree sat an old man.",
                       "Only then I understood his words.", "Never have I seen such a thing."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("밑줄 친 부분을 앞으로 보내 다시 쓰시오.  I ==never== dreamed that I would win.", "Never did I dream that I would win.",
              "", lines=1),
            Q("부정어를 앞으로 보내 다시 쓰시오.  He has never seen such a big dog.", "Never has he seen such a big dog.",
              "완료형 → has를 앞으로", lines=1),
            Q("장소 표현을 앞으로 보내 다시 쓰시오.  An old castle stands on the hill.", "On the hill stands an old castle.",
              "", lines=1),
            Q("다음 문장을 끊어 읽기 표시(/)를 하고 해석하시오.  Among the guests were two famous actors from Korea.",
              "Among the guests / were / two famous actors / from Korea. 손님들 중에는 한국에서 온 유명 배우 두 명이 있었다.",
              "동사 뒤에서 진짜 주어", lines=2),
        ]),
    ]),
]
