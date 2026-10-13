from textbook.blocks import *

GOALS = [
    "선행사 유무 + 뒤 절의 완전성으로 that / what / 접속사 that을 구별한다.",
    "같은 문장을 which / in which / where로 바꿔 쓴다.",
]

INTRO = "관계사는 **두 가지만 확인**합니다. ① 앞에 선행사가 있나? ② 뒤의 절이 완전한가, 불완전한가?"

BLOCKS = [
    ANCHOR("I bought a house that I had wanted to live in.", "나는 살고 싶었던 집을 샀다.", "that → which → in which → where → what: 한 문장으로 관계사 전부."),
    FORMULA("관계대명사 = 선행사 + 관계대명사 + 불완전한 절",
            "관계부사 = 선행사를 설명하는 완전한 절을 이끎 (where / when / how / why)"),
    TABLE(
        ["형태", "선행사", "뒤 절의 완전성", "예문"],
        [
            ["**that** (관계대명사)", "O", "불완전", "I bought a house that I had wanted to live in."],
            ["**what**", "X", "불완전", "You are what you eat."],
            ["**that** (접속사)", "X", "완전", "I know that he is honest."],
        ],
        widths=[20, 12, 18, 50], center=[1, 2],
    ),
    TABLE(
        ["표현", "설명"],
        [
            ["I bought a house **which** I had wanted to live in.", "불완전한 절 / 관계대명사 / that 가능"],
            ["I bought a house **in which** I had wanted to live.", "전치사 + 관계대명사 / that 불가"],
            ["I bought a house **where** I had wanted to live.", "완전한 절 / 관계부사"],
        ],
        widths=[58, 42],
    ),
    PILGI([
        "선행사 O + 불완전 → {{관계대명사}} (that 가능)",
        "선행사 X + 불완전 → {{what}}",
        "선행사 X + 완전 → {{접속사 that}}",
        "전치사 + 관계대명사 뒤는 {{완전한}} 절, that {{불가}}.",
    ]),
    CHAIN([
        ("두 문장", "I bought a house. I had wanted to live **in it**.", None),
        ("which", "I bought a house **which** I had wanted to live **in**.", "it → which, 전치사 in은 끝에 남음"),
        ("in which", "I bought a house **in which** I had wanted to live.", "전치사를 앞으로 → 뒤가 완전해짐"),
        ("where", "I bought a house **where** I had wanted to live.", "in which = where (관계부사)"),
        ("생략", "I bought a house (that) I had wanted to live in.", "목적격은 생략 가능"),
        ("what", "This house is **what** I had wanted.", "선행사(the thing)를 품으면 what"),
    ], title="I bought a house that I had wanted to live in"),
    QUICK([
        "뒤 절에서 주어나 목적어(전치사의 목적어 포함)가 빠졌나? → **빠졌으면 관계대명사, 다 있으면 관계부사·접속사**",
        "콤마 뒤, 전치사 뒤 → **that 금지**",
    ]),
    LINK(2, "관계사절 = 형용사절 / that절 = 명사절"),

    STEPUP(),
    TABLE(
        ["선행사", "주격", "소유격", "목적격"],
        [
            ["사람", "who / that", "whose", "who(m) / that"],
            ["사물·동물", "which / that", "whose", "which / that"],
        ],
        widths=[22, 26, 26, 26], center=[1, 2, 3], caption="관계대명사 격",
    ),
    TABLE(
        ["관계부사", "선행사", "= 전치사 + which"],
        [
            ["when", "시간", "at / on / in which"],
            ["where", "장소", "at / on / in which"],
            ["why", "이유 (the reason)", "for which"],
            ["how", "방법 (the way) — 둘 중 하나만", "in which"],
        ],
        widths=[20, 44, 36],
    ),
    WARN([
        ("This is ~~the way how~~ I solved it.", "This is ++the way++ (또는 ++how++) I solved it.", "the way와 how는 같이 X"),
        ("This is the town ~~where~~ I visited.", "This is the town ++which++ I visited.", "visited 뒤 목적어 빠짐 → 불완전"),
    ]),
    EX([
        ("I have two sons, **who** became doctors.", "계속적 용법: 아들이 둘뿐, 그들은 의사가 됨"),
        ("He passed the exam, **which** surprised everyone.", "which가 앞 문장 전체를 받음"),
        ("**Whatever** you do, I'll support you. / **However** hard you try, …", "복합관계사"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  You are (that / what) you eat.", "what", "선행사 X + 불완전"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I know (that / what) he is honest.", "that", "선행사 X + 완전 → 접속사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  This is the hospital (which / where) I was born.", "where", "완전한 절"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I have a friend (who / whose) brother is a singer.", "whose", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  I bought a house in (that / which) I had wanted to live.", "which",
              "전치사 뒤 that 불가"),
            Q("다음 중 빈칸에 that을 쓸 수 없는 것은?", "③", "계속적 용법",
              options=["He is the tallest boy ______ I know.", "I know ______ she is right.",
                       "I read the book, ______ was very boring.", "This is the house ______ I bought."]),
            Q("다음 중 어법상 올바른 문장은?", "④", "① the way how ② where → which ③ whose → who",
              options=["Tell me the way how you did it.", "Seoul is the city where I want to visit.",
                       "The girl whose is singing is my sister.", "I don't understand what you mean."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("세 가지 방법으로 한 문장으로 쓰시오.  This is the chair. My grandfather used to sit on it.",
              "This is the chair which(that) my grandfather used to sit on. / … on which my grandfather used to sit. / … (생략) my grandfather used to sit on.",
              "", lines=3),
            Q("관계대명사로 한 문장을 만드시오.  I know a girl. Her mother is a famous actress.",
              "I know a girl whose mother is a famous actress.", "", lines=1),
        ]),
    ]),
]
