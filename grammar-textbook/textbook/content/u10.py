from textbook.blocks import *

GOALS = [
    "현재분사와 과거분사의 의미(능동·진행 / 수동·완료)를 구분한다.",
    "분사의 전치수식·후치수식, 보어로 쓰인 분사를 이해한다.",
    "감정을 나타내는 분사(-ing / p.p.)를 정확히 골라 쓸 수 있다.",
]

INTRO = "분사는 동사를 **형용사처럼** 쓰는 형태입니다. **현재분사(V-ing)** 와 **과거분사(p.p.)** 두 가지가 있고, 꾸밈을 받는 명사와의 관계가 **능동인지 수동인지**가 선택의 기준입니다."

BLOCKS = [
    TABLE(
        ["종류", "형태", "핵심 의미", "예시"],
        [
            ["**현재분사**", "V-ing", "능동 (~하는) / 진행 (~하고 있는)", "a **crying** baby, **falling** leaves"],
            ["**과거분사**", "p.p.", "수동 (~된, ~당한) / 완료 (~한)", "a **broken** window, **fallen** leaves"],
        ],
        widths=[16, 12, 36, 36],
    ),
    FORMULA("명사가 직접 하면 V-ing  /  명사가 당하면 p.p.", "falling leaves 떨어지고 있는 잎  vs  fallen leaves 떨어진(낙)엽"),

    H("1. 명사 수식 — 위치"),
    TABLE(
        ["위치", "조건", "예문"],
        [
            ["**전치수식** (명사 앞)", "분사 혼자 꾸밀 때", "a **sleeping** cat / a **used** car"],
            ["**후치수식** (명사 뒤)", "분사에 목적어·수식어가 붙어 길어질 때", "a cat **sleeping on the sofa** / a car **made in Korea**"],
        ],
        widths=[22, 36, 42],
    ),
    PARSE([("The girl", "S"), ("dancing on the stage", "M"), ("is", "V"), ("my sister", "C")],
          "무대 위에서 춤추고 있는 소녀는 내 여동생이다."),
    PARSE([("This", "S"), ("is", "V"), ("a novel", "C"), ("written by Hemingway", "M")],
          "이것은 헤밍웨이가 쓴 소설이다."),
    TIP("후치수식 분사 = 관계대명사 + be 생략", [
        "the girl (who is) dancing on the stage",
        "a novel (which was) written by Hemingway",
    ]),

    H("2. 보어로 쓰이는 분사"),
    EX([
        ("He sat **surrounded** by his fans.", "그는 팬들에게 둘러싸인 채 앉아 있었다. (주격보어)"),
        ("The kids kept **asking** questions.", "아이들은 계속 질문을 했다. (주격보어)"),
        ("I found the door **locked**.", "나는 문이 잠겨 있는 것을 발견했다. (목적격보어, 문 = 잠긴)"),
        ("Don't leave the water **running**.", "물을 틀어 놓은 채로 두지 마. (목적격보어, 물 = 흐르는)"),
    ]),

    H("3. 감정을 나타내는 분사"),
    P("감정 동사(excite, bore, interest, surprise …)는 원래 '**~한 감정을 일으키다**'라는 뜻입니다. 그래서 감정을 **일으키는** 쪽은 V-ing, 감정을 **느끼는** 쪽은 p.p.를 씁니다."),
    TABLE(
        ["구분", "형태", "예문"],
        [
            ["감정을 **일으키는** 대상 (주로 사물)", "**-ing** (~하게 하는)", "The movie was **exciting**."],
            ["감정을 **느끼는** 대상 (주로 사람)", "**p.p.** (~한 감정을 느끼는)", "I was **excited** about the movie."],
        ],
        widths=[36, 28, 36],
    ),
    TABLE(
        ["동사", "-ing (일으키는)", "p.p. (느끼는)"],
        [
            ["bore", "boring 지루하게 하는", "bored 지루해하는"],
            ["interest", "interesting 흥미로운", "interested 흥미를 느끼는"],
            ["surprise", "surprising 놀라운", "surprised 놀란"],
            ["disappoint", "disappointing 실망스러운", "disappointed 실망한"],
            ["tire", "tiring 피곤하게 하는", "tired 피곤한"],
            ["confuse", "confusing 혼란스럽게 하는", "confused 혼란스러워하는"],
            ["satisfy", "satisfying 만족스러운", "satisfied 만족한"],
        ],
        widths=[20, 40, 40], caption="자주 나오는 감정 분사",
    ),
    WARN([
        ("I was so ~~boring~~ during the class.", "I was so ++bored++ during the class.", "내가 지루함을 '느낌' → p.p."),
        ("The result was ~~disappointed~~.", "The result was ++disappointing++.", "결과가 실망을 '일으킴' → -ing"),
        ("He is a ~~bored~~ person.", "He is a ++boring++ person. (지루한 사람)", "사람도 감정을 일으키면 -ing"),
    ]),

    H("4. 자동사의 분사"),
    P("목적어를 갖지 않는 자동사의 과거분사는 '수동'이 아니라 **'완료'** 의 의미입니다."),
    EX([
        ("**fallen** leaves", "떨어진 잎 (떨어지는 동작이 완료됨)"),
        ("a **retired** teacher", "은퇴한 선생님"),
        ("an **escaped** prisoner", "탈옥한 죄수"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Look at the (rising / risen) sun.", "rising", "해가 떠오르고 있는 → 진행"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I bought a (using / used) car.", "used", "차가 '사용된' → 수동"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The game was really (excited / exciting).", "exciting", "경기가 흥분을 일으킴"),
            Q("괄호 안에서 알맞은 것을 고르시오.  She was (surprised / surprising) at the news.", "surprised", "그녀가 놀람을 느낌"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The language (speaking / spoken) in Brazil is Portuguese.", "spoken",
              "언어는 '말해지는' 대상"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I heard a dog (barking / barked) all night.", "barking", "개가 짖고 있는 → 능동"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Please keep the door (closing / closed).", "closed", "문이 '닫힌' 상태"),
            Q("다음 중 어법상 틀린 문장은?", "③", "③ 학생들이 흥미를 '느낌' → interested",
              options=["The story was very touching.", "There's a man waiting outside.",
                       "The students were interesting in science.", "I had my watch fixed."]),
        ]),
        ("STEP 3", "서술형", [
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  The lecture was bored, so many of the listening students fell asleep.",
              "bored → boring", "강의가 지루함을 일으킴 → boring (listening students는 '듣고 있는 학생들'로 맞음)", lines=1),
            Q("관계대명사를 생략하여 분사구로 바꿔 쓰시오.  The man who is talking to Sue is my uncle.",
              "The man talking to Sue is my uncle.", "관계대명사 + be 생략 → 후치수식 현재분사", lines=1),
            Q("우리말과 같도록 주어진 단어를 활용하여 영작하시오.  나는 깨진 꽃병을 발견했다. (find, break, vase)",
              "I found a broken vase.", "꽃병이 깨진 → 과거분사 전치수식", lines=1),
        ]),
    ]),
]
