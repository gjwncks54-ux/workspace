from textbook.blocks import *

GOALS = [
    "8품사의 이름과 역할을 표 하나로 정리한다.",
    "품사가 문장성분(S·V·O·C)으로 어떻게 연결되는지 안다.",
]

INTRO = "품사는 **단어의 이름표**, 문장성분은 **단어가 문장에서 맡은 자리**입니다. 이 단원에서는 이름표만 확실히 붙이고, 자리는 Unit 2에서 배웁니다."

BLOCKS = [
    TABLE(
        ["품사", "핵심 역할", "대표 예시"],
        [
            ["**명사**", "사람·사물·개념의 이름", "book / teacher / happiness"],
            ["**대명사**", "명사를 대신함", "he / she / it / they / we / you / I"],
            ["**동사**", "행동·상태를 나타냄", "run / eat / be"],
            ["**형용사**", "명사를 꾸밈", "a **beautiful** flower"],
            ["**부사**", "동사·형용사·부사·문장 전체를 수식", "quickly / very / fortunately"],
            ["**전치사**", "명사 앞에서 위치·시간·방향 관계를 나타냄", "in / at / on / under / for"],
            ["**접속사**", "단어·구·절을 연결", "and / but / because / if / when / that"],
            ["**감탄사**", "감탄 표현", "oh / wow"],
        ],
        widths=[16, 44, 40], caption="8품사",
    ),
    PILGI([
        "문장 성분으로 자주 연결되는 품사는 {{명사}} · {{대명사}} · {{동사}} · {{형용사}} 입니다.",
        "형용사는 {{명사}}만 꾸민다. 부사는 명사 빼고 다 꾸민다.",
        "전치사 뒤에는 {{명사}}, 접속사 뒤에는 {{주어 + 동사}}.",
    ]),
    CHAIN([
        ("품사", "I(대명사) made(동사) him(대명사) sad(형용사).", None),
        ("문장성분", "I [[S]]  made [[V]]  him [[O]]  sad [[O.C]]", "같은 단어에 '자리 이름'을 붙이면 문장성분"),
        ("부사 추가", "I **really** made him sad **yesterday**.", "부사는 빼도 문장이 성립 → 수식어"),
    ], title="한 문장으로 품사 → 문장성분 연결하기"),
    LINK(3, "I made him sad는 5형식 대표 예문으로 다시 나옵니다."),
    QUICK([
        "a / the / my 뒤 → **명사**  ·  a / the 와 명사 사이 → **형용사**",
        "주어 바로 뒤, 시제가 보이는 자리 → **동사**",
        "빼도 문장이 성립하는 자리 → **부사(구)**",
    ], title="위치로 품사 바로 찾기"),

    STEPUP(),
    H("형용사 vs 부사 — 내신 단골"),
    WARN([
        ("He looks ~~happily~~.", "He looks ++happy++.", "look(~하게 보이다) 뒤 보어 자리 → 형용사"),
        ("I could ~~hard~~ believe it.", "I could ++hardly++ believe it.", "hardly = 거의 ~않다 (hard와 뜻이 다름)"),
    ]),
    TABLE(
        ["-ly가 붙으면 뜻이 바뀌는 부사", "뜻"],
        [
            ["hard / **hardly**", "열심히 / 거의 ~않다"],
            ["late / **lately**", "늦게 / 최근에"],
            ["high / **highly**", "높이 / 매우"],
            ["near / **nearly**", "가까이 / 거의"],
        ],
        widths=[45, 55],
    ),
    TIP("-ly인데 형용사", ["friendly, lovely, lonely, costly → 형용사 (부사로 쓰지 않음)"]),

    H("한 단어, 여러 품사"),
    EX([
        ("I **like** pizza.  /  She sings **like** a bird.", "동사 (좋아하다) / 전치사 (~처럼)"),
        ("He is a **fast** runner.  /  He runs **fast**.", "형용사 / 부사"),
        ("I stayed home **because of** the rain.  /  **because** it rained.", "전치사 + 명사 / 접속사 + 절"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 단어의 품사를 쓰시오.  She ==quickly== finished her homework.", "부사", "동사 finished를 꾸밈"),
            Q("밑줄 친 단어의 품사를 쓰시오.  I made him ==sad==.", "형용사", "him의 상태를 설명"),
            Q("밑줄 친 단어의 품사를 쓰시오.  He looked ==at== the sky.", "전치사", "명사 the sky 앞"),
            Q("밑줄 친 단어의 품사를 쓰시오.  Turn off the light ==before== you leave.", "접속사", "뒤에 주어+동사"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The soup tastes (good / well).", "good", "감각동사 뒤 보어 → 형용사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The game was cancelled (because / because of) the storm.", "because of",
              "뒤에 명사구만 있음 → 전치사"),
            Q("다음 중 밑줄 친 like의 품사가 나머지와 다른 하나는?", "③", "③은 동사, 나머지는 전치사",
              options=["She looks ==like== her mother.", "It sounds ==like== a good idea.",
                       "Do you ==like== spicy food?", "He swims ==like== a fish."]),
        ]),
        ("STEP 3", "서술형", [
            Q("다음 문장의 각 단어 아래에 품사를 쓰시오.  Wow, my teacher speaks English very fluently.",
              "감탄사, 대명사(소유격), 명사, 동사, 명사, 부사, 부사", "my는 대명사의 소유격", lines=1),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  She smiled friendly at me.", "friendly → in a friendly way",
              "friendly는 형용사", lines=1),
        ]),
    ]),
]
