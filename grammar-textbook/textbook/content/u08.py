from textbook.blocks import *

GOALS = [
    "to부정사의 명사적·형용사적·부사적 용법을 구분하여 해석한다.",
    "to부정사를 목적어로 쓰는 동사, 가주어 it 구문, 의문사 + to부정사를 익힌다.",
    "too ~ to, enough to, be to 용법 등 to부정사 관용 표현을 활용한다.",
]

INTRO = "to부정사는 **to + 동사원형**으로, 문장 안에서 명사·형용사·부사 세 가지 역할을 모두 하는 '만능 준동사'입니다. 해석은 위치와 역할로 결정됩니다."

BLOCKS = [
    TABLE(
        ["용법", "해석", "자리", "예문"],
        [
            ["**명사적**", "~하는 것, ~하기", "주어·목적어·보어", "I want **to be** a pilot."],
            ["**형용사적**", "~할, ~하는", "명사 뒤 (명사 수식)", "I have homework **to do**."],
            ["**부사적**", "~하기 위해, ~해서, ~하다니 등", "동사·형용사·문장 수식", "I got up early **to catch** the bus."],
        ],
        widths=[15, 25, 24, 36], caption="to부정사 3가지 용법",
    ),

    H("1. 명사적 용법  ~하는 것"),
    TABLE(
        ["역할", "예문", "해석"],
        [
            ["주어", "**To learn** English is fun. → It is fun **to learn** English.", "영어를 배우는 것은 재미있다."],
            ["목적어", "She hopes **to win** the contest.", "그녀는 대회에서 우승하기를 바란다."],
            ["보어", "My goal is **to read** 50 books this year.", "내 목표는 올해 책 50권을 읽는 것이다."],
        ],
        widths=[12, 52, 36],
    ),
    TIP("주어 자리 to부정사는 가주어 it으로", [
        "To V가 주어로 길게 나오면 보통 It을 앞에 두고 진주어 to V를 뒤로 보냅니다. (Unit 13)",
        "It is important **to wear** a helmet.",
    ]),
    TABLE(
        ["to부정사만 목적어로 쓰는 동사 (미래·의지)"],
        [["want, hope, wish, expect, plan, decide, promise, agree, refuse, learn, choose, manage, afford, pretend, fail"]],
        caption="to부정사를 목적어로 쓰는 동사",
    ),
    P("**의문사 + to부정사**는 명사 역할을 하며, '의문사 + 주어 + should + 동사원형'으로 바꿀 수 있습니다."),
    EX([
        ("I don't know **what to say**.  = what I should say", "무슨 말을 해야 할지 모르겠다."),
        ("Can you tell me **how to get** to the station?", "역에 어떻게 가는지 알려 주시겠어요?"),
        ("We haven't decided **where to go**.", "우리는 어디로 갈지 정하지 않았다."),
    ]),

    H("2. 형용사적 용법  ~할, ~하는"),
    P("명사 **뒤에서** 명사를 꾸밉니다. 꾸밈을 받는 명사가 to부정사 뒤 **전치사의 목적어**이면 전치사를 반드시 남겨야 합니다."),
    EX([
        ("I need a friend **to talk with**.", "나는 함께 이야기할 친구가 필요하다. (talk with a friend)"),
        ("Give me something **to write with**.", "쓸 것(필기구)을 좀 줘. (write with a pen)"),
        ("Give me something **to write on**.", "쓸 것(종이)을 좀 줘. (write on paper)"),
        ("He has no house **to live in**.", "그는 살 집이 없다. (live in a house)"),
    ]),
    WARN([
        ("I'm looking for a chair ~~to sit~~.", "I'm looking for a chair ++to sit on++.", "sit on a chair → 전치사 on 필요"),
        ("I want ~~cold something~~ to drink.", "I want ++something cold++ to drink.", "-thing + 형용사 + to부정사 순서"),
    ]),
    NOTE("be to 용법 (형용사적 용법의 확장)", [
        "be + to V 는 **예정 · 의무 · 가능 · 운명 · 의도** 를 나타냅니다.",
        "The meeting **is to be held** tomorrow. (예정: ~할 예정이다)",
        "You **are to finish** this by six. (의무: ~해야 한다)",
        "If you **are to pass** the exam, you must study hard. (의도: ~하려면)",
    ]),

    H("3. 부사적 용법"),
    TABLE(
        ["의미", "해석", "예문"],
        [
            ["**목적**", "~하기 위해", "She went to the library **to borrow** books. (= in order to / so as to)"],
            ["**감정의 원인**", "~해서", "I'm glad **to see** you again."],
            ["**판단의 근거**", "~하다니", "He must be smart **to solve** the problem."],
            ["**결과**", "(…해서) 결국 ~하다", "He grew up **to be** a famous chef. / She woke up **only to find** it was a dream."],
            ["**형용사 수식**", "~하기에", "This question is easy **to answer**."],
        ],
        widths=[16, 20, 64],
    ),

    H("4. to부정사 관용 표현"),
    TABLE(
        ["표현", "의미", "바꿔 쓰기"],
        [
            ["**too** + 형/부 + **to V**", "너무 ~해서 …할 수 없다", "so + 형/부 + that + S + can't V"],
            ["형/부 + **enough to V**", "…할 만큼 충분히 ~하다", "so + 형/부 + that + S + can V"],
            ["**in order to V** / **so as to V**", "~하기 위해", "so that + S + can V"],
            ["**to tell the truth**", "사실을 말하자면", "독립부정사"],
            ["**to be honest** / **strange to say**", "솔직히 말해서 / 이상한 얘기지만", "독립부정사"],
        ],
        widths=[34, 30, 36],
    ),
    EX([
        ("The box is **too heavy for me to lift**.  = The box is so heavy that I can't lift it.", "그 상자는 너무 무거워서 나는 들 수 없다."),
        ("She is **old enough to drive**.  = She is so old that she can drive.", "그녀는 운전할 만큼 나이가 들었다."),
    ]),
    WARN([
        ("The box is too heavy for me to lift ~~it~~.", "The box is too heavy for me to ++lift++.", "주어 = lift의 목적어 → 다시 쓰지 않음 (so ~ that 절에서는 it 필요)"),
        ("She is ~~enough old~~ to drive.", "She is ++old enough++ to drive.", "enough는 형용사·부사 뒤에"),
    ]),

    H("5. 원형부정사 (to 없는 부정사)"),
    P("사역동사·지각동사의 목적격보어(Unit 4), 조동사 뒤, 그리고 아래 관용 표현에서는 to 없이 동사원형을 씁니다."),
    EX([
        ("You **had better** take an umbrella.", "우산을 가져가는 게 좋겠다."),
        ("I **would rather** stay home than go out.", "나가느니 차라리 집에 있겠다."),
        ("I **cannot but** laugh. = I cannot help laughing.", "웃지 않을 수 없다."),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 to부정사의 용법을 쓰시오.  My plan is ==to visit== my grandparents.", "명사적 용법 (보어)", "My plan = to visit ~"),
            Q("밑줄 친 to부정사의 용법을 쓰시오.  There are many places ==to see== in Seoul.", "형용사적 용법", "places를 꾸밈"),
            Q("밑줄 친 to부정사의 용법을 쓰시오.  I was surprised ==to hear== the news.", "부사적 용법 (감정의 원인)", "놀란 이유"),
            Q("괄호 안에서 알맞은 것을 고르시오.  He promised (to call / calling) me.", "to call", "promise는 to부정사를 목적어로"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  She has no one to (depend / depend on).", "depend on", "depend on someone → 전치사 필요"),
            Q("괄호 안에서 알맞은 것을 고르시오.  This tea is (too hot to / hot enough to) drink right now. 지금 마실 수 없다.",
              "too hot to", "너무 ~해서 …할 수 없다"),
            Q("다음 중 밑줄 친 to부정사의 용법이 나머지와 다른 것은?", "②",
              "②는 형용사적 용법(chance 수식), 나머지는 부사적 용법(목적)",
              options=["I saved money ==to buy== a bike.", "This is a good chance ==to learn== Chinese.",
                       "He ran fast ==to catch== the train.", "She studied hard ==to pass== the exam."]),
            Q("다음 우리말을 영어로 옮길 때 빈칸에 알맞은 것은?  나는 무엇을 입어야 할지 모르겠다. = I don't know ______.", "③",
              "의문사 + to부정사 = 의문사 + S + should + V",
              options=["what wearing", "what wear", "what to wear", "to what wear"]),
        ]),
        ("STEP 3", "서술형", [
            Q("so ~ that 구문으로 바꿔 쓰시오.  The soup was too salty for us to eat.", "The soup was so salty that we couldn't eat it.",
              "that절에서는 목적어 it을 써 줘야 한다", lines=1),
            Q("어법상 틀린 부분 2곳을 찾아 고쳐 쓰시오.  I need warm something to wear and a pen to write.",
              "warm something → something warm, to write → to write with", "-thing + 형용사 / write with a pen", lines=1),
            Q("우리말과 같도록 to부정사를 활용하여 영작하시오.  그는 자라서 유명한 과학자가 되었다. (grow up)",
              "He grew up to be(become) a famous scientist.", "부사적 용법 (결과)", lines=1),
        ]),
    ]),
]
