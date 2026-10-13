from textbook.blocks import *

GOALS = [
    "가주어·가목적어 it 구문을 만든다.",
    "It is ~ that 강조구문으로 원하는 부분을 강조한다.",
    "가주어 구문과 강조구문을 구별한다.",
]

INTRO = "세 구문 모두 **뜻 없는 it** 을 앞에 세우고 진짜 내용을 뒤로 보냅니다. it은 **해석하지 않습니다.**"

BLOCKS = [
    TABLE(
        ["구문", "형태", "예문"],
        [
            ["**가주어**", "It + be + 형용사 + for/of + 의미상 주어 + to V", "It is impossible for me to try it once more."],
            ["**가목적어**", "동사 + it + 형용사 + to V", "I found it difficult to finish the work."],
            ["**강조구문**", "It is/was + 강조대상 + that + 나머지", "It was I that sent you an invitation."],
        ],
        widths=[14, 42, 44],
    ),
    PILGI([
        "가목적어 it은 해석하지 않고, 진짜 내용은 뒤의 {{to V}}가 담당합니다.",
        "의미상 주어: 보통 {{for}} + 목적격, 사람 성격 형용사(kind, nice…)는 {{of}} + 목적격",
        "강조구문은 It is와 that을 지우면 {{완전한 문장}}이 남는다.",
    ]),
    CHAIN([
        ("원래", "**To try it once more** is impossible for me.", None),
        ("가주어", "**It** is impossible for me **to try it once more**.", "긴 주어를 뒤로, 빈자리에 It"),
    ], title="가주어"),
    CHAIN([
        ("틀린 문장", "I found ~~to finish the work~~ difficult.", None),
        ("가목적어", "I found **it** difficult **to finish the work**.", "목적어 자리에 it, to V는 뒤로"),
    ], title="가목적어"),
    CHAIN([
        ("원래", "I sent you an invitation.", None),
        ("주어 강조", "It was **I** that sent you an invitation.", "초대장을 보낸 건 바로 나"),
        ("목적어 강조", "It was **you** that I sent an invitation (to).", "내가 초대장을 보낸 건 바로 너"),
        ("목적어 강조", "It was **an invitation** that I sent you.", "내가 보낸 건 바로 초대장"),
    ], title="I sent you an invitation 강조하기"),
    QUICK([
        "It is/was와 that을 지웠을 때 문장이 **완전** → 강조구문",
        "남는 게 **불완전**(형용사만 덩그러니) → 가주어 구문",
    ]),
    LINK(8, "가주어의 진주어는 to부정사 명사적 용법."),

    STEPUP(),
    TABLE(
        ["의미상 주어", "형용사"],
        [
            ["**for** + 목적격", "easy, hard, difficult, important, necessary, impossible"],
            ["**of** + 목적격", "kind, nice, wise, foolish, careless, rude, polite"],
        ],
        widths=[24, 76],
    ),
    EX([
        ("**It** is true **that** he won the race.", "진주어가 that절"),
        ("He made **it** a rule **to take** a walk every morning.", "가목적어 + 명사 보어"),
        ("I **did** finish my homework!", "동사 강조는 do/does/did"),
    ]),
    WARN([
        ("She made ~~possible~~ for us to win.", "She made ++it++ possible for us to win.", "가목적어 it 생략 불가"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("가주어 It으로 바꾸시오.  To keep a promise is important.", "It is important to keep a promise.", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  It is very kind (for / of) you to help me.", "of", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  I found (it / that) difficult to finish the work.", "it", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("다음 문장에서 강조된 부분을 쓰시오.  It was in the park that I lost my phone.", "in the park", ""),
            Q("다음 중 밑줄 친 It의 쓰임이 나머지와 다른 것은?", "④", "④는 강조구문",
              options=["==It== is fun to play soccer.", "==It== is strange that he is late.",
                       "==It== is impossible for me to try it once more.", "==It== was I that sent you an invitation."]),
        ]),
        ("STEP 3", "서술형", [
            Q("밑줄 친 부분을 강조하시오.  I met ==Jenny== at the library.", "It was Jenny that(who) I met at the library.",
              "", lines=1),
            Q("우리말과 같도록 영작하시오.  나는 매일 일기를 쓰는 것이 어렵다는 것을 알았다. (find, hard)",
              "I found it hard to keep a diary every day.", "", lines=1),
        ]),
    ]),
]
