from textbook.blocks import *

GOALS = [
    "8품사의 이름과 역할을 구분할 수 있다.",
    "같은 단어도 문장 속 위치에 따라 품사가 달라짐을 이해한다.",
    "형용사와 부사를 어법에 맞게 골라 쓸 수 있다.",
]

INTRO = "품사는 단어를 **'문장 안에서 하는 일'** 에 따라 나눈 이름표입니다. 품사를 알아야 다음 단원의 문장성분(주어·동사·목적어·보어)이 보입니다."

BLOCKS = [
    TABLE(
        ["품사", "핵심 역할", "대표 예시"],
        [
            ["**명사** Noun", "사람·사물·개념의 이름", "book, teacher, Seoul, happiness"],
            ["**대명사** Pronoun", "명사를 대신함", "I, you, he, it, this, someone"],
            ["**동사** Verb", "동작·상태를 나타냄", "run, eat, be, have"],
            ["**형용사** Adjective", "명사를 꾸미거나 설명함", "a **beautiful** flower / She is **kind**."],
            ["**부사** Adverb", "동사·형용사·부사·문장 전체를 꾸밈", "quickly, very, often, fortunately"],
            ["**전치사** Preposition", "명사(구) 앞에서 시간·장소·방향 등을 나타냄", "in, at, on, under, for, with"],
            ["**접속사** Conjunction", "단어·구·절을 연결함", "and, but, because, if, when, that"],
            ["**감탄사** Interjection", "놀람·기쁨 등 감정을 표현함", "oh, wow, oops, ouch"],
        ],
        widths=[24, 38, 38], caption="한눈에 보는 8품사",
    ),

    H("1. 명사와 대명사"),
    P("명사는 셀 수 있는지에 따라 쓰는 방법이 달라집니다. 셀 수 있는 명사는 단수일 때 **a/an**, 복수일 때 **-s/-es** 가 붙고, 셀 수 없는 명사는 a/an도 -s도 붙지 않습니다."),
    TABLE(
        ["구분", "예시", "주의"],
        [
            ["셀 수 있는 명사", "a book, two apples, many students", "단수 단독 사용 불가: ~~I have book.~~"],
            ["셀 수 없는 명사", "water, money, information, advice, furniture", "~~an advice~~, ~~informations~~ (X)"],
        ],
        widths=[22, 42, 36],
    ),
    P("대명사는 문장 속 자리(격)에 따라 모양이 바뀝니다."),
    TABLE(
        ["주격 (~은/는)", "소유격 (~의)", "목적격 (~을/를)", "소유대명사 (~의 것)", "재귀대명사 (~자신)"],
        [
            ["I", "my", "me", "mine", "myself"],
            ["you", "your", "you", "yours", "yourself / yourselves"],
            ["he / she", "his / her", "him / her", "his / hers", "himself / herself"],
            ["it", "its", "it", "–", "itself"],
            ["we / they", "our / their", "us / them", "ours / theirs", "ourselves / themselves"],
        ],
        center=[0, 1, 2, 3, 4],
    ),
    WARN([
        ("The dog wagged ~~it's~~ tail.", "The dog wagged ++its++ tail.", "it's = it is. 소유격은 its"),
        ("This bag is ~~her's~~.", "This bag is ++hers++.", "소유대명사에는 아포스트로피(')가 없다"),
    ]),

    H("2. 동사"),
    P("동사는 문장의 중심입니다. 영어 문장에는 반드시 동사가 **하나** 있어야 하며, 동사의 종류에 따라 문장의 형식(Unit 3)이 결정됩니다."),
    TABLE(
        ["종류", "역할", "예시"],
        [
            ["be동사", "~이다 / ~에 있다", "am, is, are, was, were"],
            ["일반동사", "동작이나 상태", "go, study, like, know"],
            ["조동사", "동사 앞에서 의미를 더함", "can, will, must, should, may"],
        ],
        widths=[20, 35, 45],
    ),

    H("3. 형용사 vs 부사"),
    P("형용사는 **명사**만 꾸밉니다. 부사는 **명사를 제외한 거의 모든 것**(동사·형용사·부사·문장 전체)을 꾸밉니다."),
    TABLE(
        ["", "쓰임", "예문"],
        [
            ["형용사", "① 명사 앞에서 꾸밈 (한정적 용법)", "She is a **careful** driver."],
            ["", "② 보어로 주어를 설명 (서술적 용법)", "She is **careful**."],
            ["부사", "동사 수식", "She drives **carefully**."],
            ["", "형용사 수식", "The test was **very** difficult."],
            ["", "부사 수식", "He speaks **really** fast."],
            ["", "문장 전체 수식", "**Fortunately**, nobody was hurt."],
        ],
        widths=[14, 40, 46],
    ),
    WARN([
        ("He looks ~~happily~~.", "He looks ++happy++.", "look(~하게 보이다) 뒤 보어 자리 → 형용사"),
        ("She smiled ~~friendly~~ at me.", "She smiled at me ++in a friendly way++.", "friendly, lovely, lonely는 -ly로 끝나지만 형용사 → 부사 자리에 못 씀"),
    ], title="흔한 실수"),
    TABLE(
        ["형태가 비슷한 형용사 / 부사", "뜻 비교"],
        [
            ["hard / **hardly**", "hard 열심히, 단단한 / hardly 거의 ~않다"],
            ["late / **lately**", "late 늦은, 늦게 / lately 최근에"],
            ["high / **highly**", "high 높은, 높이 / highly 매우"],
            ["near / **nearly**", "near 가까운, 가까이 / nearly 거의"],
        ],
        widths=[40, 60], caption="내신 단골: -ly가 붙으면 뜻이 바뀌는 부사",
    ),

    H("4. 전치사 · 접속사 · 감탄사"),
    P("**전치사** 뒤에는 반드시 명사(구)·대명사·동명사가 옵니다. **접속사** 뒤에는 보통 주어와 동사가 있는 절이 옵니다."),
    EX([
        ("I stayed home **because of** the rain.", "비 때문에 집에 있었다. (전치사 + 명사)"),
        ("I stayed home **because** it rained.", "비가 와서 집에 있었다. (접속사 + 절)"),
        ("**Wow**, that's amazing!", "와, 정말 놀랍다! (감탄사)"),
    ]),
    TIP("같은 의미, 다른 품사", [
        "because of / despite / during  → 전치사 (+ 명사)",
        "because / although / while  → 접속사 (+ 주어 + 동사)",
    ]),

    H("5. 한 단어, 여러 품사"),
    P("품사는 단어에 고정된 것이 아니라 **문장 속 위치**가 결정합니다."),
    EX([
        ("I **like** pizza.", "like = 동사 (좋아하다)"),
        ("She sings **like** a bird.", "like = 전치사 (~처럼)"),
        ("He is a **fast** runner.", "fast = 형용사 (빠른)"),
        ("He runs **fast**.", "fast = 부사 (빠르게)"),
        ("**Water** is important.", "water = 명사 (물)"),
        ("Please **water** the plants.", "water = 동사 (물을 주다)"),
    ]),
    TIP("위치로 품사 찾기", [
        "a / the / my 뒤, 문장 맨 앞 주어 자리 → 명사",
        "a / the 와 명사 사이 → 형용사",
        "주어 바로 뒤, 시제가 드러나는 자리 → 동사",
        "빼도 문장이 성립하는 자리 → 부사(구)",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 단어의 품사를 쓰시오.  She ==quickly== finished her homework.", "부사",
              "동사 finished를 꾸미므로 부사"),
            Q("밑줄 친 단어의 품사를 쓰시오.  The movie was ==boring==.", "형용사",
              "be동사 뒤에서 주어를 설명하는 보어 → 형용사"),
            Q("밑줄 친 단어의 품사를 쓰시오.  He looked ==at== the sky.", "전치사",
              "명사 the sky 앞에서 방향을 나타냄"),
            Q("밑줄 친 단어의 품사를 쓰시오.  Turn off the light ==before== you leave.", "접속사",
              "뒤에 주어(you)+동사(leave)의 절이 왔으므로 접속사"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The soup tastes (good / well).", "good",
              "taste(~한 맛이 나다) 뒤 보어 자리 → 형용사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I could (hard / hardly) believe the news.", "hardly",
              "hardly = 거의 ~않다. '그 소식을 거의 믿을 수 없었다'"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The game was cancelled (because / because of) the storm.", "because of",
              "뒤에 명사구(the storm)만 있으므로 전치사"),
            Q("다음 중 밑줄 친 like의 품사가 나머지와 다른 하나는?",
              "③", "③은 동사(좋아하다), 나머지는 전치사(~처럼, ~같은)",
              options=["She looks ==like== her mother.", "It sounds ==like== a good idea.",
                       "Do you ==like== spicy food?", "He swims ==like== a fish."]),
        ]),
        ("STEP 3", "서술형", [
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  She gave me some useful advices.", "advices → advice",
              "advice는 셀 수 없는 명사라 -s를 붙이지 않는다.", lines=1),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  The cat licked it's paw.", "it's → its",
              "소유격은 its, it's는 it is의 줄임말", lines=1),
        ]),
    ]),
]
