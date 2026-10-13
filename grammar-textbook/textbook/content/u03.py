from textbook.blocks import *

GOALS = [
    "자동사와 타동사를 목적어의 유무로 구분할 수 있다.",
    "문장의 5형식을 구분하고 각 형식의 대표 동사를 익힌다.",
    "4형식 ↔ 3형식 전환과 감각동사 + 형용사 어법을 정확히 적용한다.",
]

INTRO = "영어 문장은 **동사가 무엇이냐**에 따라 뒤에 올 성분이 정해집니다. 그 결과 모든 문장은 다섯 가지 틀(5형식) 중 하나에 들어갑니다."

BLOCKS = [
    H("1. 자동사와 타동사"),
    TABLE(
        ["구분", "핵심", "대표 동사", "예문"],
        [
            ["**자동사**", "목적어 **없음**", "go, come, arrive, happen, appear, disappear, rise", "The sun **rises** in the east."],
            ["**타동사**", "목적어 **필요**", "love, buy, read, invite, need, raise, discuss", "She **raised** her hand."],
        ],
        widths=[13, 17, 38, 32],
    ),
    TIP("자동사인지 타동사인지 헷갈릴 때", [
        "동사 뒤에 '~을/를'이 바로 붙으면 타동사, 전치사가 필요하면 자동사",
        "rise(자) – rose – risen / raise(타) – raised – raised",
        "lie(자, 눕다) – lay – lain / lay(타, 놓다) – laid – laid",
    ]),
    WARN([
        ("We discussed ~~about~~ the problem.", "We ++discussed++ the problem.", "discuss는 타동사 → 전치사 X"),
        ("She married ~~with~~ him.", "She ++married++ him.", "marry는 타동사"),
        ("He entered ~~into~~ the room.", "He ++entered++ the room.", "enter(들어가다)는 타동사"),
        ("They reached ~~at~~ the top.", "They ++reached++ the top.", "reach는 타동사 (= arrive at)"),
    ], title="전치사를 쓰면 틀리는 타동사"),

    H("2. 문장의 5형식 한눈에 보기"),
    TABLE(
        ["형식", "구조", "예문", "해석"],
        [
            ["**1형식**", "S + V", "Birds **sing**.", "새들이 노래한다."],
            ["**2형식**", "S + V + C", "The food **smells** delicious.", "음식에서 맛있는 냄새가 난다."],
            ["**3형식**", "S + V + O", "I **love** you.", "나는 너를 사랑한다."],
            ["**4형식**", "S + V + I.O + D.O", "I **gave** him a book.", "나는 그에게 책을 주었다."],
            ["**5형식**", "S + V + O + O.C", "The news **made** him sad.", "그 소식은 그를 슬프게 했다."],
        ],
        widths=[12, 24, 34, 30], center=[0],
    ),

    H("3. 1형식  S + V"),
    P("동사만으로 의미가 완성됩니다. 뒤에 붙는 장소·시간 표현은 모두 **수식어(M)** 입니다."),
    PARSE([("A strange thing", "S"), ("happened", "V"), ("last night", "M")], "어젯밤 이상한 일이 일어났다."),
    PARSE([("There", None), ("is", "V"), ("a cat", "S"), ("under the table", "M")],
          "탁자 아래에 고양이가 있다. (There is/are 구문: 동사 뒤가 진짜 주어)"),

    H("4. 2형식  S + V + C"),
    P("주어를 설명하는 **주격보어(C)** 가 필요합니다. 보어 자리에는 **명사나 형용사**가 오고, **부사는 올 수 없습니다.**"),
    TABLE(
        ["의미", "동사", "예문"],
        [
            ["상태 (~이다, ~인 채로 있다)", "be, keep, remain, stay", "Please **keep** quiet."],
            ["변화 (~이 되다)", "become, get, grow, turn, go, come", "The leaves **turned** red."],
            ["감각 (~하게 보이다/들리다…)", "look, sound, smell, taste, feel", "This cake **tastes** sweet."],
            ["판단 (~인 것 같다)", "seem, appear", "He **seems** tired."],
        ],
        widths=[30, 34, 36],
    ),
    FORMULA("감각동사 + 형용사   /   감각동사 + like + 명사", "You look tired.  /  You look like a movie star."),
    WARN([
        ("Your idea sounds ~~greatly~~.", "Your idea sounds ++great++.", "보어 자리 → 형용사"),
        ("She looks ~~a princess~~.", "She looks ++like++ a princess.", "감각동사 뒤 명사는 like와 함께"),
    ]),

    H("5. 3형식  S + V + O"),
    P("동작의 대상인 **목적어**가 하나 필요합니다. 목적어 자리에는 명사뿐 아니라 to부정사, 동명사, 명사절도 올 수 있습니다."),
    EX([
        ("I **need** some help.", "명사 목적어"),
        ("She **decided** to study abroad.", "to부정사 목적어 (Unit 8)"),
        ("He **finished** writing the report.", "동명사 목적어 (Unit 9)"),
        ("I **think** that you are right.", "명사절 목적어"),
    ]),

    H("6. 4형식  S + V + I.O + D.O"),
    P("'~에게(간접목적어) ~을(직접목적어) 주다'라는 의미의 **수여동사**가 쓰입니다. 4형식은 두 목적어의 순서를 바꾸고 **전치사**를 넣어 3형식으로 바꿀 수 있습니다."),
    PARSE([("My aunt", "S"), ("sent", "V"), ("me", "I.O"), ("a birthday card", "D.O")],
          "이모가 나에게 생일 카드를 보냈다."),
    PARSE([("My aunt", "S"), ("sent", "V"), ("a birthday card", "O"), ("to me", "M")],
          "→ 3형식 전환: 직접목적어 + 전치사 + 간접목적어"),
    TABLE(
        ["전치사", "동사", "느낌"],
        [
            ["**to**", "give, send, show, tell, teach, lend, bring, write, pass", "상대방에게 '전달'되는 동작"],
            ["**for**", "make, buy, cook, get, find, build, choose", "상대방을 '위해' 해 주는 동작"],
            ["**of**", "ask", "질문을 '구하다'"],
        ],
        widths=[12, 55, 33], caption="4형식 → 3형식 전환 시 전치사",
    ),
    EX([
        ("He bought **me** a hat. → He bought a hat **for** me.", "그는 나에게 모자를 사 주었다."),
        ("Can I ask **you** a favor? → Can I ask a favor **of** you?", "부탁 하나 해도 될까?"),
    ]),
    WARN([
        ("He explained ~~me the rule~~.", "He explained ++the rule to me++.", "explain은 4형식 불가 → 3형식만"),
        ("She suggested ~~us a new plan~~.", "She suggested ++a new plan to us++.", "suggest, introduce, say, describe 도 같음"),
    ], title="4형식으로 쓸 수 없는 동사"),

    H("7. 5형식  S + V + O + O.C"),
    P("목적어를 설명하는 **목적격보어(O.C)** 가 필요합니다. 목적어와 목적격보어 사이에는 **'O가 O.C이다/하다'** 라는 주어-서술어 관계가 숨어 있습니다."),
    PARSE([("We", "S"), ("call", "V"), ("him", "O"), ("Captain", "O.C")], "우리는 그를 캡틴이라고 부른다. (him = Captain)"),
    PARSE([("This blanket", "S"), ("will keep", "V"), ("you", "O"), ("warm", "O.C")],
          "이 담요가 너를 따뜻하게 해 줄 것이다. (you are warm)"),
    TIP("4형식 vs 5형식 구별법", [
        "O = 뒤의 명사 → 5형식:  They made **him** captain. (he = captain)",
        "O ≠ 뒤의 명사 → 4형식:  She made **him** a cake. (he ≠ a cake)",
    ]),
    NOTE("다음 단원 미리보기", ["목적격보어 자리에 to부정사·동사원형·분사가 오는 5형식 심화(사역·지각동사)는 Unit 4에서 다룹니다."]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("문장의 형식을 쓰시오.  The baby slept peacefully.", "1형식", "peacefully는 수식어"),
            Q("문장의 형식을 쓰시오.  My grandfather told us an old story.", "4형식", "us(I.O) + an old story(D.O)"),
            Q("문장의 형식을 쓰시오.  The song made her famous.", "5형식", "her = famous (O.C)"),
            Q("문장의 형식을 쓰시오.  The milk went bad.", "2형식", "go + 형용사 = ~하게 되다 (변화)"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The blanket feels (soft / softly).", "soft",
              "감각동사 feel 뒤 보어 → 형용사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Prices (rose / raised) sharply last year.", "rose",
              "뒤에 목적어가 없으므로 자동사 rise의 과거형"),
            Q("괄호 안에서 알맞은 것을 고르시오.  My dad cooked dinner (to / for) us.", "for", "cook은 for를 쓰는 동사"),
            Q("다음 중 어법상 올바른 문장은?", "④",
              "① discuss about → discuss  ② looks sadly → looks sad  ③ explained me → explained the answer to me",
              options=["Let's discuss about the issue.", "He looks sadly today.",
                       "She explained me the answer.", "Can I ask a question of you?"]),
        ]),
        ("STEP 3", "서술형", [
            Q("다음 4형식 문장을 3형식으로 바꿔 쓰시오.  She showed me her photos.",
              "She showed her photos to me.", "show는 to를 쓰는 동사", lines=1),
            Q("다음 4형식 문장을 3형식으로 바꿔 쓰시오.  Dad built us a treehouse.",
              "Dad built a treehouse for us.", "build는 for를 쓰는 동사", lines=1),
            Q("<보기>의 단어를 배열하여 문장을 완성하시오.  그 소식은 모두를 행복하게 만들었다. (made / happy / everyone / the news)",
              "The news made everyone happy.", "5형식: S + made + O + O.C(형용사)", lines=1),
        ]),
    ]),
]
