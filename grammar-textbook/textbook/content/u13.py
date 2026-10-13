from textbook.blocks import *

GOALS = [
    "가주어 it과 진주어(to부정사·that절)의 구조를 이해한다.",
    "가목적어 it을 쓰는 5형식 문장을 만들 수 있다.",
    "It is ~ that 강조구문을 가주어 구문과 구별한다.",
]

INTRO = "영어는 **머리가 무거운 문장**을 싫어합니다. 긴 주어나 목적어를 문장 뒤로 보내고, 빈자리에는 **뜻이 없는 it** 을 채웁니다. 같은 it을 이용해 특정 부분을 강조하는 **강조구문**도 함께 익힙니다."

BLOCKS = [
    TABLE(
        ["구문", "형태", "예문"],
        [
            ["**가주어**", "It + be + 형용사 (+ for/of 의미상 주어) + to V", "It is impossible **for me** to try it once more."],
            ["", "It + be + 형용사 + that + S + V", "It is true **that** he won the race."],
            ["**가목적어**", "S + V + it + 형용사/명사 + to V / that절", "I found it difficult to finish the work."],
            ["**강조구문**", "It is/was + 강조 대상 + that + 나머지", "It was I **that** sent you an invitation."],
        ],
        widths=[14, 44, 42],
    ),

    H("1. 가주어 it, 진주어 to부정사 / that절"),
    PARSE([("It", "S"), ("is", "V"), ("dangerous", "C"), ("to swim in this river", "S")],
          "이 강에서 수영하는 것은 위험하다. (It = to swim in this river)"),
    EX([
        ("**To swim** in this river is dangerous. → **It** is dangerous **to swim** in this river.", "to부정사 진주어"),
        ("**That** she passed the test is surprising. → **It** is surprising **that** she passed the test.", "that절 진주어"),
        ("**It** doesn't matter **whether** you win or lose.", "whether절 진주어: 이기든 지든 중요하지 않다."),
    ]),
    TIP("가주어 it은 해석하지 않는다", [
        "It is important to exercise. → ~~그것은~~ 운동하는 것은 중요하다.",
    ]),

    H("2. 의미상 주어 for vs of"),
    TABLE(
        ["형태", "형용사", "예문"],
        [
            ["It is 형용사 **for** + 목적격 + to V", "easy, hard, difficult, important, necessary, possible …",
             "It is hard **for him** to get up early."],
            ["It is 형용사 **of** + 목적격 + to V", "사람의 성격·태도: kind, nice, wise, foolish, careless, rude, polite …",
             "It was careless **of you** to leave the door open."],
        ],
        widths=[30, 38, 32],
    ),

    H("3. 가목적어 it"),
    P("5형식 문장에서 목적어가 to부정사나 that절이면 **목적어 자리에 it**을 두고 진짜 목적어는 뒤로 보냅니다. 이때 it은 생략할 수 없습니다."),
    PARSE([("I", "S"), ("found", "V"), ("it", "O"), ("difficult", "O.C"), ("to finish the work", "O")],
          "나는 그 일을 끝내는 것이 어렵다는 것을 알았다."),
    TABLE(
        ["가목적어를 자주 쓰는 동사"],
        [["make, find, think, believe, consider, keep  +  it  +  형용사/명사  +  to V / that절"]],
    ),
    EX([
        ("He **made it** a rule **to take** a walk every morning.", "그는 매일 아침 산책하는 것을 규칙으로 삼았다."),
        ("I **think it** strange **that** she didn't come.", "나는 그녀가 오지 않은 것이 이상하다고 생각한다."),
    ]),
    WARN([
        ("I found ~~to finish the work difficult~~.", "I found ++it++ difficult ++to finish the work++.", "to부정사 목적어는 가목적어 it 사용"),
        ("She made ~~possible~~ for us to win.", "She made ++it++ possible for us to win.", "가목적어 it 생략 불가"),
    ]),

    H("4. It is ~ that 강조구문"),
    P("문장에서 강조하고 싶은 부분(주어·목적어·부사구)을 **It is/was와 that 사이**에 넣습니다. 동사는 강조할 수 없습니다."),
    PARSE([("Tom", "S"), ("broke", "V"), ("the window", "O"), ("yesterday", "M")], "원래 문장: 톰이 어제 창문을 깼다."),
    EX([
        ("**It was Tom that** broke the window yesterday.", "어제 창문을 깬 사람은 바로 톰이었다. (주어 강조, who 가능)"),
        ("**It was the window that** Tom broke yesterday.", "톰이 어제 깬 것은 바로 그 창문이었다. (목적어 강조, which 가능)"),
        ("**It was yesterday that** Tom broke the window.", "톰이 창문을 깬 것은 바로 어제였다. (부사 강조, when 가능)"),
    ]),
    TIP("강조구문 vs 가주어 구문 구별", [
        "It is/was와 that을 지웠을 때 **완전한 문장**이 남으면 → 강조구문",
        "It was Tom that broke the window. → Tom broke the window. (완전) → 강조구문",
        "It is true that he lied. → ~~true~~ he lied. (불완전) → 가주어 구문",
    ]),
    NOTE("동사를 강조하려면 do/does/did", ["I **did** finish my homework! (정말로 끝냈다니까!)",
                                      "She **does** look happy today."]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("빈칸에 알맞은 말을 쓰시오.  ______ is not easy to learn a foreign language.", "It", "가주어"),
            Q("괄호 안에서 알맞은 것을 고르시오.  It is very kind (for / of) you to help me.", "of", "kind는 성격 형용사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  It is necessary (for / of) us to save water.", "for", "necessary는 일반 형용사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I found (it / that) easy to use the app.", "it", "가목적어 it"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("다음 문장에서 강조된 부분을 쓰시오.  It was in the park that I lost my phone.", "in the park", "장소 부사구 강조"),
            Q("다음 중 밑줄 친 It의 쓰임이 나머지와 다른 것은?", "④",
              "④는 강조구문의 It, 나머지는 가주어 It",
              options=["==It== is fun to play soccer.", "==It== is strange that he is late.",
                       "==It== is important to eat breakfast.", "==It== was Mina that called me last night."]),
            Q("다음 중 어법상 틀린 문장은?", "②", "② 가목적어 it이 필요 → made it possible",
              options=["It is dangerous to drive fast.", "The Internet made possible to work at home.",
                       "It was silly of me to believe him.", "It was at 7 that the show started."]),
        ]),
        ("STEP 3", "서술형", [
            Q("가주어 It을 이용하여 바꿔 쓰시오.  To keep a promise is important.", "It is important to keep a promise.", "", lines=1),
            Q("밑줄 친 부분을 강조하는 문장으로 바꿔 쓰시오.  I met ==Jenny== at the library.", "It was Jenny that(who) I met at the library.",
              "목적어 강조 / 사람이므로 who도 가능", lines=1),
            Q("우리말과 같도록 주어진 단어를 활용하여 영작하시오.  나는 매일 영어로 일기를 쓰는 것이 어렵다는 것을 알았다. (find, hard, keep a diary)",
              "I found it hard to keep a diary in English every day.", "가목적어 it + 형용사 + to V", lines=2),
        ]),
    ]),
]
