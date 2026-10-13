from textbook.blocks import *

GOALS = [
    "장소·방향 부사구 도치와 부정어 도치의 규칙을 이해한다.",
    "so/neither 도치, only 도치를 정확한 어순으로 쓸 수 있다.",
    "도치 문장에서 진짜 주어를 찾아 수일치를 판단한다.",
]

INTRO = "도치는 강조하고 싶은 말을 **문장 맨 앞**으로 보내면서 **주어와 동사의 순서가 바뀌는** 현상입니다. 독해에서는 진짜 주어를 찾는 것이, 어법에서는 **동사의 수일치와 어순**이 핵심입니다."

BLOCKS = [
    TABLE(
        ["유형", "핵심 규칙", "예문"],
        [
            ["**장소·방향 부사구 도치**", "부사구 + V + S\n단, 주어가 대명사면 도치 X", "In the car **are the kids**. / In the car **they are**."],
            ["**부정어 도치**", "부정어 + 조동사/be + S + V\n(의문문 어순)", "Never **does he study** English."],
            ["**only 도치**", "Only + 부사(구/절) + 조동사 + S + V", "Only then **did I realize** the truth."],
            ["**so / neither 도치**", "so/neither + 조동사 + S", "I'm hungry. — **So am I**."],
        ],
        widths=[22, 34, 44],
    ),

    H("1. 장소·방향 부사구 도치"),
    P("장소나 방향을 나타내는 부사(구)가 문장 앞에 오면 **1형식 동사(be, come, stand, lie, live 등)** 와 주어의 순서가 바뀝니다."),
    PARSE([("On the hill", "M"), ("stands", "V"), ("an old castle", "S")], "언덕 위에 오래된 성이 서 있다."),
    EX([
        ("Here **comes the bus**.", "버스가 온다."),
        ("Here **it comes**.", "그것이 온다. (대명사 주어 → 도치 X)"),
        ("Among the guests **were two famous actors**.", "손님들 중에는 유명 배우 두 명이 있었다."),
    ]),
    WARN([
        ("In the box ~~was~~ many old letters.", "In the box ++were++ many old letters.", "진짜 주어 many old letters (복수)"),
        ("Here ~~comes he~~.", "Here ++he comes++.", "주어가 대명사면 도치하지 않음"),
    ]),

    H("2. 부정어 도치"),
    P("부정어(구)가 문장 앞에 오면 뒤는 **의문문 어순**이 됩니다. 일반동사는 **do/does/did** 를 앞으로 꺼냅니다."),
    TABLE(
        ["부정어"],
        [["never, not, little, hardly, scarcely, seldom, rarely, few, not until, no sooner, nowhere, not only"]],
    ),
    TABLE(
        ["동사 종류", "도치 형태", "예문"],
        [
            ["be동사", "부정어 + be + S", "Never **was she** so happy."],
            ["조동사", "부정어 + 조동사 + S + V", "Little **can I** understand his words."],
            ["일반동사", "부정어 + do/does/did + S + V(원형)", "Hardly **did he** sleep last night."],
            ["완료형", "부정어 + have/had + S + p.p.", "Never **have I** seen such a big dog."],
        ],
        widths=[16, 38, 46],
    ),
    WARN([
        ("Never ~~he studies~~ English.", "Never ++does he study++ English.", "일반동사 → does + S + 원형"),
        ("Little ~~did I knew~~ about it.", "Little ++did I know++ about it.", "did 뒤 동사원형"),
    ]),
    NOTE("관용 도치 표현", [
        "**No sooner** had I arrived **than** it began to rain. (= 내가 도착하자마자 비가 오기 시작했다)",
        "**Hardly(Scarcely)** had I arrived **when(before)** it began to rain. (같은 의미)",
        "**Not until** I lost my health **did I realize** its value. (건강을 잃고 나서야 비로소 그 가치를 깨달았다)",
        "**Not only** is he smart, **but** he is also kind.",
    ]),

    H("3. Only + 부사(구/절) 도치"),
    EX([
        ("**Only after** the meeting **did I** find out the truth.", "회의가 끝나고 나서야 나는 진실을 알게 되었다."),
        ("**Only when** you are quiet **can you** hear the birds.", "조용히 있을 때에만 새소리를 들을 수 있다."),
    ]),

    H("4. so / neither 도치  (~도 그렇다 / ~도 그렇지 않다)"),
    TABLE(
        ["앞 문장", "응답", "규칙"],
        [
            ["I **am** tired.", "**So am** I.", "긍정 → so + V + S"],
            ["She **likes** pizza.", "**So do** I.", "일반동사 → do/does/did"],
            ["He **can't** swim.", "**Neither can** I. (= I can't, either.)", "부정 → neither + V + S"],
            ["I **didn't** see it.", "**Neither did** she.", "시제 일치"],
        ],
        widths=[28, 40, 32],
    ),
    TIP("so + S + V 와 구별", [
        "So am I. → 나도 그래. (도치, 다른 사람도 같음)",
        "So I am. → 정말 그렇네. (동의, 도치 X)",
    ]),

    H("5. 보어 도치 / 가정법 도치"),
    EX([
        ("**Happy are those** who are content.", "만족할 줄 아는 사람은 행복하다. (보어 강조, 주어가 김)"),
        ("**Were I** you, I wouldn't do that.", "내가 너라면 그렇게 하지 않을 텐데. (= If I were you, Unit 15)"),
    ]),
    TIP("끊어 읽기 포인트 (도치 문장 독해)", [
        "긴 주어 뒤 / 동사 뒤 / 목적어 뒤 / 전치사 앞 / 수식어(관계사·분사) 앞에서 끊는다",
        "도치 문장은 **동사 뒤에서** 진짜 주어를 찾는다",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Under the tree (sat an old man / an old man sat).", "sat an old man",
              "장소 부사구 + V + S"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Never (I have / have I) seen such a thing.", "have I", "부정어 도치 → 의문문 어순"),
            Q("괄호 안에서 알맞은 것을 고르시오.  A: I don't like carrots. B: (So / Neither) do I.", "Neither", "부정문에 대한 동의"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Here (she comes / comes she).", "she comes", "대명사 주어 → 도치 X"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  On the table (was / were) a cup and a book.", "were",
              "진짜 주어 a cup and a book (복수)"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Little (he knew / did he know) what would happen.", "did he know",
              "일반동사 과거 → did + S + 원형"),
            Q("다음 중 어법상 틀린 문장은?", "③", "③ Only + 부사구 → 도치: Only then did I understand.",
              options=["Rarely does she eat breakfast.", "So is my brother.",
                       "Only then I understood his words.", "Not until midnight did he come home."]),
            Q("다음 문장과 의미가 같은 것은?  As soon as he saw me, he ran away.", "①",
              "No sooner had + S + p.p. than ~ = ~하자마자",
              options=["No sooner had he seen me than he ran away.", "No sooner he had seen me than he ran away.",
                       "Hardly he saw me when he ran away.", "Not until he ran away did he see me."]),
        ]),
        ("STEP 3", "서술형", [
            Q("밑줄 친 부분을 문장 맨 앞으로 보내 다시 쓰시오.  I ==never== dreamed that I would win.",
              "Never did I dream that I would win.", "dreamed → did + 원형 dream", lines=1),
            Q("우리말과 같도록 Not until을 이용하여 영작하시오.  그가 떠나고 나서야 나는 그를 그리워했다. (leave, miss)",
              "Not until he left did I miss him.", "Not until + S + V + 조동사 + S + V", lines=1),
        ]),
    ]),
]
