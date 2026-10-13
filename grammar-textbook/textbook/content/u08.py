from textbook.blocks import *

GOALS = [
    "to부정사 3용법을 '해석'으로 구별한다.",
    "같은 to lose weight가 위치에 따라 용법이 바뀌는 것을 안다.",
    "too~to, enough to, 의문사+to V 등 자주 나오는 표현을 익힌다.",
]

INTRO = "to부정사는 **해석으로 구별**합니다. '~하는 것'이면 명사, '~할'이면 형용사, '~하기 위해'면 부사."

BLOCKS = [
    ANCHOR("I walk to school to lose weight.", "나는 살을 빼기 위해 걸어서 등교한다.",
           "to lose weight 한 덩어리를 자리만 옮겨 명사·형용사·부사 용법을 모두 만듭니다."),
    TABLE(
        ["용법", "해석", "예문"],
        [
            ["**명사적** 용법", "~하는 것", "My goal is to lose weight."],
            ["**형용사적** 용법", "~할 / ~하는 / ~될", "I have homework to do."],
            ["**부사적** 용법", "~하기 위해 / ~하다니", "I walk to school to lose weight."],
        ],
        widths=[24, 34, 42],
    ),
    TNOTE("예문 교체 이유", [
        "I love to go on a diet: go on a diet는 '다이어트를 시작하다'라는 뜻이라 love와 함께 쓰면 '다이어트 시작하는 걸 사랑한다'처럼 어색합니다.",
        "→ 같은 주제를 살리면서 자연스러운 lose weight(살을 빼다)로 바꿨습니다.",
    ]),
    PILGI([
        "to부정사도 동사의 성질을 일부 가지므로 {{목적어}}를 가질 수 있고, {{not to V}}와 같은 부정형도 가능합니다.",
        "명사 뒤에서 명사를 꾸미면 {{형용사적}} 용법, 문장이 끝난 뒤 '목적'을 붙이면 {{부사적}} 용법.",
    ]),
    CHAIN([
        ("명사적 (보어)", "My goal is **to lose weight**.", "goal = to lose weight → ~하는 것"),
        ("명사적 (목적어)", "I decided **to lose weight**.", "decide의 목적어"),
        ("형용사적", "I need a good way **to lose weight**.", "a good way를 꾸밈 → 살 뺄 방법"),
        ("부사적", "I walk to school **to lose weight**.", "걸어가는 목적 → ~하기 위해"),
        ("부정", "I decided **not to eat** late at night.", "not은 to 앞"),
    ], title="to lose weight 하나로 3용법"),
    QUICK([
        "빼면 문장이 깨진다 → **명사적** (주어·목적어·보어)",
        "바로 앞에 명사가 있고 그 명사를 꾸민다 → **형용사적**",
        "빼도 문장이 완전하다 → **부사적**",
    ]),
    LINK(12, "To V가 주어로 길면 가주어 It: It is impossible for me to try it once more."),

    STEPUP(),
    H("형용사적 용법 — 전치사를 남겨라"),
    EX([
        ("I need a friend **to talk with**.", "talk with a friend"),
        ("He has no house **to live in**.", "live in a house"),
    ]),
    WARN([
        ("I'm looking for a chair ~~to sit~~.", "… a chair ++to sit on++.", "sit on a chair"),
        ("I want ~~cold something~~ to drink.", "I want ++something cold++ to drink.", "-thing + 형용사 + to V"),
    ]),
    H("자주 나오는 to부정사 표현"),
    TABLE(
        ["표현", "의미", "바꿔 쓰기"],
        [
            ["**too** 형 **to V**", "너무 ~해서 …할 수 없다", "so 형 that S can't V"],
            ["형 **enough to V**", "…할 만큼 충분히 ~하다", "so 형 that S can V"],
            ["**in order to V**", "~하기 위해", "so that S can V"],
            ["**의문사 + to V**", "무엇을/어떻게 ~할지", "의문사 + S + should V"],
            ["**to부정사만 목적어**", "want, hope, plan, decide, promise, agree, refuse", "미래·의지"],
        ],
        widths=[24, 34, 42],
    ),
    WARN([
        ("The box is too heavy for me to lift ~~it~~.", "… too heavy for me to ++lift++.", "주어 = lift의 목적어 → 반복 X"),
        ("She is ~~enough old~~ to drive.", "She is ++old enough++ to drive.", "enough는 형용사 뒤"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 to부정사의 용법을 쓰시오.  My goal is ==to lose weight==.", "명사적 용법 (보어)", ""),
            Q("밑줄 친 to부정사의 용법을 쓰시오.  I have homework ==to do==.", "형용사적 용법", "homework 수식"),
            Q("밑줄 친 to부정사의 용법을 쓰시오.  I walk to school ==to lose weight==.", "부사적 용법 (목적)", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  He promised (to call / calling) me.", "to call", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  She has no one to (depend / depend on).", "depend on", ""),
            Q("다음 중 밑줄 친 to부정사의 용법이 나머지와 다른 것은?", "②", "②만 형용사적, 나머지 부사적(목적)",
              options=["I saved money ==to buy== a bike.", "This is a good way ==to lose== weight.",
                       "He ran fast ==to catch== the train.", "She studied hard ==to pass== the exam."]),
            Q("빈칸에 알맞은 것은?  나는 무엇을 입어야 할지 모르겠다. = I don't know ______.", "③", "",
              options=["what wearing", "what wear", "what to wear", "to what wear"]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("to lose weight를 명사적 용법(목적어)으로 쓰시오. (decide)", "I decided to lose weight.", "", lines=1),
            Q("to lose weight를 형용사적 용법으로 쓰시오. (a good way)", "This is a good way to lose weight.", "", lines=1),
            Q("in order to를 이용해 바꾸시오.  I walk to school so that I can lose weight.",
              "I walk to school in order to lose weight.", "", lines=1),
            Q("so ~ that 구문으로 바꾸시오.  The soup was too salty for us to eat.",
              "The soup was so salty that we couldn't eat it.", "that절에서는 it 필요", lines=1),
        ]),
    ]),
]
