from textbook.blocks import *

GOALS = [
    "구와 절을 '동사의 유무'로 구분할 수 있다.",
    "명사·형용사·부사 역할을 하는 구와 절을 알아본다.",
    "문장성분 S·V·O·C·M을 표시하며 문장을 끊어 읽을 수 있다.",
]

INTRO = "긴 문장도 결국 몇 개의 **덩어리**로 이루어져 있습니다. 덩어리를 찾는 눈(구·절)과 그 덩어리가 맡은 역할(문장성분)을 익히면 독해와 영작이 빨라집니다."

BLOCKS = [
    H("1. 구(phrase)와 절(clause)"),
    TABLE(
        ["구분", "정의", "예시"],
        [
            ["**구** phrase", "두 단어 이상 + **주어·동사 없음**", "my English teacher / in the morning / to study hard"],
            ["**절** clause", "두 단어 이상 + **주어·동사 있음**", "when I was young / that he is honest"],
        ],
        widths=[18, 37, 45],
    ),
    FORMULA("동사(주어 + 동사)가 없으면 → 구  /  있으면 → 절"),

    H("2. 구와 절이 하는 역할"),
    P("구와 절은 문장 안에서 하나의 품사처럼 움직입니다. 역할에 따라 **명사구/절, 형용사구/절, 부사구/절** 이라고 부릅니다."),
    TABLE(
        ["역할", "구 (phrase)", "절 (clause)"],
        [
            ["**명사** 역할\n주어·목적어·보어", "**To learn English** is fun.\nI enjoy **playing soccer**.",
             "**What he said** is true.\nI know **that she is honest**."],
            ["**형용사** 역할\n명사 수식", "the girl **with long hair**\na book **to read**",
             "the girl **who has long hair**\nthe house **where I was born**"],
            ["**부사** 역할\n시간·이유·조건 등", "He left **in a hurry**.\nI went there **to see her**.",
             "I left **because I was tired**.\n**If it rains**, I'll stay home."],
        ],
        widths=[22, 39, 39],
    ),

    H("3. 문장성분"),
    P("문장성분은 문장 안에서 맡은 **자리 이름**입니다. 문장을 이루는 데 꼭 필요한 **주요 성분**(S·V·O·C)과, 빼도 문장이 성립하는 **수식어**(M)로 나뉩니다."),
    TABLE(
        ["성분", "주로 오는 품사", "역할", "예시"],
        [
            ["**S** 주어", "명사 / 대명사 (명사구·절)", "문장의 주체 (~은/는/이/가)", "**Tom** runs."],
            ["**V** 동사", "동사", "동작·상태 (~하다/~이다)", "Tom **runs**."],
            ["**O** 목적어", "명사 / 대명사 (명사구·절)", "동작의 대상 (~을/를)", "I love **music**."],
            ["**C** 보어", "명사 / 형용사", "주어나 목적어를 설명", "She is **a doctor**. / It's **cold**."],
            ["**M** 수식어", "형용사·부사(구·절)", "꾸며 주는 말 (생략 가능)", "He runs **every morning**."],
        ],
        widths=[15, 27, 28, 30],
    ),
    PARSE([("My little brother", "S"), ("plays", "V"), ("the piano", "O"), ("after school", "M")],
          "내 남동생은 방과 후에 피아노를 친다."),
    PARSE([("The students in the library", "S"), ("were", "V"), ("very quiet", "C")],
          "도서관에 있는 학생들은 매우 조용했다."),
    PARSE([("I", "S"), ("believe", "V"), ("that he will win the race", "O")],
          "나는 그가 경주에서 이길 거라고 믿는다. (명사절 = 목적어)"),
    TIP("보어 vs 목적어", [
        "주어 = 보어 관계가 성립하면 보어:  She is **a doctor**. (She = a doctor)",
        "주어 ≠ 목적어, 동작의 대상이면 목적어:  She met **a doctor**. (She ≠ a doctor)",
    ]),

    H("4. 수식어를 걷어내면 뼈대가 보인다"),
    P("긴 주어 뒤에 붙은 **전치사구·분사구·관계사절**은 수식어입니다. 괄호로 묶어 지우면 진짜 주어와 동사가 드러나고, **주어-동사 수일치** 문제가 쉽게 풀립니다."),
    EX([
        ("The box (of old books) **is** heavy.", "주어는 The box (단수) → is"),
        ("The keys (on the table) **are** mine.", "주어는 The keys (복수) → are"),
        ("The man (who lives next door) **is** a pilot.", "주어는 The man (단수) → is"),
    ]),
    WARN([
        ("The quality of these products ~~are~~ excellent.", "The quality of these products ++is++ excellent.",
         "진짜 주어는 The quality (단수)"),
        ("One of my friends ~~live~~ in Busan.", "One of my friends ++lives++ in Busan.",
         "'One of + 복수명사' 의 주어는 One (단수)"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 부분이 구인지 절인지 쓰시오.  I lost my umbrella ==on the bus==.", "구",
              "주어·동사가 없다"),
            Q("밑줄 친 부분이 구인지 절인지 쓰시오.  Call me ==when you arrive==.", "절",
              "주어(you) + 동사(arrive)가 있다"),
            Q("밑줄 친 부분의 문장성분을 쓰시오.  My dream is ==to become a vet==.", "C (주격보어)",
              "My dream = to become a vet"),
            Q("밑줄 친 부분의 문장성분을 쓰시오.  She bought ==a new laptop== yesterday.", "O (목적어)",
              "bought의 대상 / She ≠ a new laptop"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The pictures on the wall (was / were) painted by my aunt.", "were",
              "주어는 The pictures (복수). on the wall은 수식어"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Each of the students (has / have) a locker.", "has",
              "Each of + 복수명사 → 단수 취급"),
            Q("다음 문장에서 수식어(M)를 모두 고른 것은?  ⓐ Yesterday ⓑ my sister ⓒ found ⓓ a wallet ⓔ on the street.",
              "②", "Yesterday(시간 부사), on the street(장소 전치사구)는 빼도 문장이 성립한다",
              options=["ⓐ, ⓑ", "ⓐ, ⓔ", "ⓑ, ⓓ", "ⓒ, ⓔ"]),
        ]),
        ("STEP 3", "서술형", [
            Q("다음 문장을 S / V / O / C / M 으로 끊어 표시하시오.  The girl with the red hat looked tired after the long trip.",
              "The girl with the red hat (S) / looked (V) / tired (C) / after the long trip (M)",
              "with the red hat은 주어를 꾸미는 수식어로, 주어 덩어리에 포함된다", lines=2),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  The number of tourists visiting Jeju have increased.",
              "have → has", "The number of ~ (~의 수)는 단수 취급. cf. A number of ~ (많은 ~)는 복수", lines=1),
        ]),
    ]),
]
