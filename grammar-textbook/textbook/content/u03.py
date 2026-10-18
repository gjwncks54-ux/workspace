from textbook.blocks import *
from textbook import figs as F

GOALS = [
    "자동사와 타동사를 목적어 유무로 구별한다.",
    "5형식을 대표 예문 하나씩으로 외운다.",
    "make 하나로 3·4·5형식을 구별한다.",
]

INTRO = "5형식은 **대표 예문 5개**만 확실히 외우면 됩니다. 나머지 문장은 전부 이 다섯 틀 중 하나입니다."

BLOCKS = [
    ANCHOR("I made him a cake.", "나는 그에게 케이크를 만들어 주었다.", "make 하나로 3형식 · 4형식 · 5형식을 오갑니다."),
    TABLE(
        ["구분", "핵심 포인트", "대표 동사"],
        [
            ["**자동사**", "목적어가 없음", "go / come / walk / run / jog / appear / disappear"],
            ["**타동사**", "목적어가 필요함", "love / buy / read / invite / need 등"],
        ],
        widths=[16, 26, 58],
    ),
    TABLE(
        ["형식", "설명", "예문"],
        [
            ["**1형식** S+V", "자동사", "I ran."],
            ["**2형식** S+V+C", "주격보어가 주어를 설명", "The food smells delicious."],
            ["**3형식** S+V+O", "타동사 + 목적어 1개", "I love you."],
            ["**4형식** S+V+I.O+D.O", "간접목적어 + 직접목적어", "I gave him a book."],
            ["**5형식** S+V+O+O.C", "목적어 + 목적격보어", "I made him sad."],
        ],
        widths=[28, 34, 38], caption="문장의 5형식",
    ),
    TABLE(
        ["형식", "대표 동사 (수업 판서)"],
        [
            ["**1형식** S+V", "**이동동사** → go / come / walk / run / jog / appear / disappear"],
            ["**2형식** S+V+C", "**감각동사** (feel, smell, taste, look, sound) / **be동사**, become, get / **remain**"],
            ["**3형식** S+V+O", "**모든 타동사** (love, buy, read, make, teach, need)"],
            ["**4형식** S+V+I.O+D.O", "**수여동사** → give, bring, lend, show, send, make, buy"],
            ["**5형식** S+V+O+O.C", "어떤 V가 오느냐에 따라 O.C 형태가 바뀜 (Unit 05)"],
        ],
        widths=[24, 76],
    ),
    PILGI([
        "자동사는 목적어가 {{없고}}, 타동사는 목적어가 {{필요}}하다.",
        "2형식 감각동사(smell, look, taste…) 뒤에는 {{형용사}}. (부사 X)",
        "4형식 = 누구{{에게}} + 무엇{{을}}.",
        "5형식 = 목적어와 목적격보어 사이에 '{{주어-서술어}}' 관계가 숨어 있다. (him = sad)",
    ]),
    CHAIN([
        ("3형식", "I made **a cake**.", None),
        ("4형식", "I made **him a cake**.", "him ≠ a cake → 간접목적어 + 직접목적어"),
        ("5형식", "I made **him sad**.", "him = sad → 목적어 + 목적격보어"),
        ("4→3 전환", "I made a cake **for** him.", "make는 for (give·show·tell은 to)"),
    ], title="make 하나로 3·4·5형식"),
    FIG(F.dative_shift(), "4형식 → 3형식: 직접목적어(~을/를)를 앞으로, 간접목적어(~에게) 앞에 to / for / of"),
    QUICK([
        "목적어 뒤 단어가 목적어와 **같으면(=) 5형식**, **다르면(≠) 4형식**",
        "동사 뒤에 '~을/를'이 바로 붙으면 타동사, 전치사가 필요하면 자동사",
    ]),
    LINK(4, "5형식 목적격보어 자리에 to V·동사원형·p.p.가 오는 경우는 다음 단원."),

    STEPUP(),
    H("전치사를 쓰면 틀리는 타동사"),
    WARN([
        ("We discussed ~~about~~ the problem.", "We ++discussed++ the problem.", "discuss는 타동사"),
        ("She married ~~with~~ him.", "She ++married++ him.", "marry는 타동사"),
        ("They reached ~~at~~ the top.", "They ++reached++ the top.", "reach = arrive at"),
    ]),
    H("2형식 동사 묶음"),
    TABLE(
        ["의미", "동사"],
        [
            ["상태", "be, keep, remain, stay"],
            ["변화", "become, get, grow, turn, go"],
            ["감각", "look, smell, taste, sound, feel  (+ like + 명사)"],
        ],
        widths=[16, 84],
    ),
    H("4형식 → 3형식 전치사"),
    TABLE(
        ["전치사", "동사"],
        [
            ["**to**", "give, send, show, tell, teach, lend, bring, write"],
            ["**for**", "make, buy, cook, get, find, build"],
            ["**of**", "ask"],
        ],
        widths=[14, 86],
    ),
    WARN([
        ("He explained ~~me the rule~~.", "He explained ++the rule to me++.", "explain, suggest, introduce, say는 4형식 불가"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("문장의 형식을 쓰시오.  The baby slept peacefully.", "1형식", "peacefully는 수식어"),
            Q("문장의 형식을 쓰시오.  My grandfather told us an old story.", "4형식", "us ≠ an old story"),
            Q("문장의 형식을 쓰시오.  The song made her famous.", "5형식", "her = famous"),
            Q("문장의 형식을 쓰시오.  The milk went bad.", "2형식", "go + 형용사 (변화)"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The food smells (delicious / deliciously).", "delicious", "감각동사 + 형용사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  My dad cooked dinner (to / for) us.", "for", "cook은 for"),
            Q("다음 중 어법상 올바른 문장은?", "④", "① discuss about X ② looks sadly X ③ explained me X",
              options=["Let's discuss about the issue.", "He looks sadly today.",
                       "She explained me the answer.", "I gave a book to him."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("3형식으로 바꿔 쓰시오.  I gave him a book.", "I gave a book to him.", "give는 to", lines=1),
            Q("3형식으로 바꾸시오.  Mom made me a cake.", "Mom made a cake for me.", "make는 for", lines=1),
            Q("3형식으로 바꾸시오.  Can I ask you a question?", "Can I ask a question of you?", "ask는 of", lines=1),
            Q("밑줄 친 made의 문장 형식을 각각 쓰시오.  ⓐ Mom ==made== me a sandwich. ⓑ The news ==made== me happy.",
              "ⓐ 4형식 ⓑ 5형식", "me ≠ a sandwich / me = happy", lines=1),
        ]),
    ]),
]
