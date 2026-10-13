from textbook.blocks import *

GOALS = [
    "관계대명사(who·which·that·whose·what)를 선행사와 격에 맞게 고른다.",
    "관계대명사와 관계부사를 '뒤 절의 완전성'으로 구분한다.",
    "전치사 + 관계대명사, 계속적 용법, 복합관계사를 이해한다.",
]

INTRO = "관계사는 **두 문장을 하나로 묶으면서, 앞의 명사(선행사)를 뒤에서 꾸며 주는 말**입니다. 판단 기준은 딱 두 가지, **선행사의 종류**와 **뒤에 오는 절이 완전한지 불완전한지**입니다."

BLOCKS = [
    FORMULA("관계대명사 + 불완전한 절   /   관계부사 + 완전한 절",
            "불완전한 절: 주어나 목적어(또는 전치사의 목적어)가 빠진 절"),

    H("1. 관계대명사의 종류"),
    TABLE(
        ["선행사", "주격", "소유격", "목적격"],
        [
            ["사람", "who / that", "whose", "who(m) / that"],
            ["사물·동물", "which / that", "whose (of which)", "which / that"],
            ["선행사 포함", "what", "–", "what"],
        ],
        widths=[22, 26, 26, 26], center=[1, 2, 3],
    ),
    PARSE([("I have a friend", None), ("who", "S"), ("lives in Canada", "V")],
          "나는 캐나다에 사는 친구가 있다. (주격: who 뒤에 주어가 없음)"),
    PARSE([("This is the book", None), ("which", "O"), ("I", "S"), ("bought yesterday", "V")],
          "이것은 내가 어제 산 책이다. (목적격: bought 뒤에 목적어가 없음)"),
    PARSE([("I met a girl", None), ("whose", None), ("father", "S"), ("is a pilot", "V")],
          "나는 아버지가 조종사인 소녀를 만났다. (소유격: whose + 명사)"),
    TIP("관계대명사 고르기", [
        "① 선행사가 사람인가 사물인가?  ② 뒤 절에서 빠진 것이 주어인가 목적어인가?",
        "주격 관계대명사 뒤 동사의 수는 **선행사**에 맞춘다: the boys who **are** …",
        "목적격 관계대명사는 생략 가능: the book (which) I bought",
    ]),

    H("2. that만 쓰는 경우 / that을 못 쓰는 경우"),
    TABLE(
        ["that을 주로 쓰는 경우", "that을 쓸 수 없는 경우"],
        [
            ["선행사가 사람 + 사물 (a boy and his dog **that** …)", "**전치사 바로 뒤** (~~in that~~ → in which)"],
            ["선행사에 최상급, 서수, the only, the very, all, every, -thing (the best movie **that** …)", "**계속적 용법** (콤마 뒤) (~~, that~~ → , which)"],
        ],
        widths=[55, 45],
    ),

    H("3. 관계대명사 what"),
    P("what은 선행사를 **포함**한 관계대명사(= the thing(s) which)로, '**~하는 것**'으로 해석합니다. what절은 명사절로 주어·목적어·보어 역할을 합니다."),
    EX([
        ("**What** he said is true.", "그가 말한 것은 사실이다. (주어)"),
        ("You are **what** you eat.", "당신이 먹는 것이 곧 당신이다. (보어)"),
        ("Show me **what** you bought.", "네가 산 것을 보여 줘. (목적어)"),
    ]),
    TABLE(
        ["", "선행사", "뒤 절", "예문"],
        [
            ["**that** (관계대명사)", "O", "불완전", "I bought a house **that** I had wanted to live in."],
            ["**what** (관계대명사)", "X", "불완전", "You are **what** you eat."],
            ["**that** (접속사)", "X", "완전", "I know **that** he is honest."],
        ],
        widths=[22, 12, 14, 52], center=[1, 2], caption="that / what / 접속사 that 비교",
    ),

    H("4. 전치사 + 관계대명사"),
    P("관계대명사가 전치사의 목적어일 때, 전치사는 **절 끝**에 두거나 **관계대명사 앞**으로 옮길 수 있습니다. 전치사를 앞으로 옮기면 뒤 절은 **완전한 절**이 됩니다."),
    TABLE(
        ["표현", "구조"],
        [
            ["I bought a house **which** I had wanted to live **in**.", "불완전한 절 / which·that 가능 / 생략 가능"],
            ["I bought a house **in which** I had wanted to live.", "전치사 + 관계대명사 / that 불가 / 생략 불가"],
            ["I bought a house **where** I had wanted to live.", "관계부사 + 완전한 절"],
        ],
        widths=[55, 45],
    ),

    H("5. 관계부사"),
    TABLE(
        ["관계부사", "선행사", "= 전치사 + which", "예문"],
        [
            ["**when**", "시간 (the day, the time…)", "at/on/in which", "I remember the day **when** we first met."],
            ["**where**", "장소 (the place, the city…)", "at/on/in which", "This is the town **where** I grew up."],
            ["**why**", "이유 (the reason)", "for which", "Tell me the reason **why** you were late."],
            ["**how**", "방법 (the way)", "in which", "This is **how** I solved it."],
        ],
        widths=[12, 28, 20, 40],
    ),
    WARN([
        ("This is ~~the way how~~ I solved it.", "This is ++the way++ I solved it. / This is ++how++ I solved it.",
         "the way와 how는 함께 쓰지 않는다"),
        ("This is the town ~~where~~ I visited last year.", "This is the town ++which(that)++ I visited last year.",
         "visited 뒤 목적어가 빠진 불완전한 절 → 관계대명사"),
    ]),

    H("6. 계속적 용법  , which / , who"),
    P("콤마(,) 뒤의 관계사는 선행사에 대해 **추가 정보**를 줍니다. 앞에서부터 '그리고 그것은/그 사람은'으로 해석합니다. **which는 앞 문장 전체**를 받을 수도 있습니다."),
    EX([
        ("I have two sons, **who** became doctors.", "나는 아들이 둘 있는데, 그들은 의사가 되었다. (아들이 둘뿐)"),
        ("I have two sons **who** became doctors.", "나는 의사가 된 아들이 둘 있다. (다른 아들이 더 있을 수도)"),
        ("He passed the exam, **which** surprised everyone.", "그는 시험에 합격했는데, 그것은 모두를 놀라게 했다. (앞 문장 전체)"),
    ]),

    H("7. 복합관계사  -ever"),
    TABLE(
        ["복합관계사", "명사절 / 부사절 의미", "예문"],
        [
            ["**whoever**", "~하는 누구든지 / 누가 ~하더라도", "**Whoever** comes first will win."],
            ["**whatever**", "~하는 무엇이든지 / 무엇을 ~하더라도", "You can eat **whatever** you want."],
            ["**whenever**", "~할 때마다 / 언제 ~하더라도", "**Whenever** I see this photo, I smile."],
            ["**wherever**", "~하는 곳은 어디든지", "I'll follow you **wherever** you go."],
            ["**however**", "아무리 ~하더라도 (+ 형/부 + S + V)", "**However** hard you try, you can't beat him."],
        ],
        widths=[16, 40, 44],
    ),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The man (who / which) called you is my uncle.", "who", "선행사가 사람 + 주격"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I have a friend (who / whose) brother is a singer.", "whose", "뒤에 명사 brother → 소유격"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (That / What) I need is your help.", "What", "선행사 없음 + 불완전한 절"),
            Q("괄호 안에서 알맞은 것을 고르시오.  This is the hospital (which / where) I was born.", "where", "was born 뒤 완전한 절 → 관계부사"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The students who (study / studies) hard will pass.", "study",
              "선행사 The students (복수)에 수일치"),
            Q("괄호 안에서 알맞은 것을 고르시오.  This is the house in (that / which) Mozart lived.", "which", "전치사 뒤 that 불가"),
            Q("다음 중 빈칸에 that을 쓸 수 없는 것은?", "③",
              "③ 계속적 용법(콤마 뒤)에는 that을 쓸 수 없다 → which",
              options=["He is the tallest boy ______ I know.", "I know ______ she is right.",
                       "I read the book, ______ was very boring.", "Look at the man and the dog ______ are running."]),
            Q("다음 중 어법상 올바른 문장은?", "④",
              "① the way how → the way 또는 how  ② where → which  ③ whose → who",
              options=["Tell me the way how you did it.", "Seoul is the city where I want to visit.",
                       "The girl whose is singing is my sister.", "I don't understand what you mean."]),
        ]),
        ("STEP 3", "서술형", [
            Q("두 문장을 관계대명사를 이용하여 한 문장으로 쓰시오.  I know a girl. Her mother is a famous actress.",
              "I know a girl whose mother is a famous actress.", "Her → whose", lines=1),
            Q("두 문장을 '전치사 + 관계대명사'를 이용하여 한 문장으로 쓰시오.  This is the chair. My grandfather used to sit on it.",
              "This is the chair on which my grandfather used to sit.", "on it → on which", lines=1),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  Whatever hard you try, you can't finish it in a day.",
              "Whatever → However", "However + 형/부 + S + V: 아무리 ~하더라도", lines=1),
        ]),
    ]),
]
