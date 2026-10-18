from textbook.blocks import *
from textbook import figs as F

GOALS = []
INTRO = ""

BLOCKS = [
    TABLE(
        ["재귀대명사 용법", "규칙", "예문"],
        [
            ["**재귀** (생략 X)", "주어 = 목적어", "She looked at **herself** in the mirror.\n그녀는 거울 속 자신을 보았다."],
            ["**강조** (생략 O)", "'직접, 스스로' 강조", "I made this cake (**myself**).\n내가 직접 이 케이크를 만들었다."],
            ["**관용 표현**", "by oneself 혼자서 / for oneself 스스로 / enjoy oneself 즐겁게 지내다 / help yourself 마음껏 먹다",
             "Help **yourself** to the cookies.\n쿠키 마음껏 먹어."],
        ],
        widths=[20, 38, 42], caption="재귀대명사 (-self / -selves)",
    ),
    FIG(F.indefinite_pronouns(), "부정대명사: 먼저 고른 것(●)과 나머지(○)"),
    PILGI([
        "주어 = 목적어 → 목적어는 {{재귀대명사}}",
        "나머지 하나 → {{the other}}  /  나머지 전부 → {{the others}}",
        "another = 또 하나 (아직 남은 게 {{있다}})",
        "each / every + {{단수}}명사 + 단수동사",
        "대명사는 가리키는 명사의 {{수}}에 맞춘다 (복수 → they / them / their)",
    ]),
    TABLE(
        ["수일치", "동사", "예문"],
        [
            ["each / every / either / neither", "**단수**", "Each of the students **has** a locker.\n학생들 각자 사물함이 있다."],
            ["both / few / many / several", "**복수**", "Both of them **are** doctors.\n둘 다 의사다."],
            ["all / most / some / half / 분수 **of + 명사**", "**of 뒤 명사**에 맞춤",
             "Most of the water **is** dirty. / Most of the students **are** tired."],
        ],
        widths=[36, 20, 44], caption="대명사·수량 표현 수일치",
    ),
    CHAIN([
        ("2개", "I have two pens. **One** is red, and **the other** is blue.", "펜 두 개 중 하나는 빨강, 나머지 하나는 파랑"),
        ("3개", "**One** is red, **another** is blue, and **the other** is black.", "또 하나 / 마지막 하나"),
        ("여러 개", "**Some** like cats, and **others** like dogs.", "어떤 사람들은 / 다른 사람들은 (일부)"),
        ("정해진 전체", "Some of the students went home, and **the others** stayed.", "나머지 학생들 전부"),
    ], title="one → another → the other(s)"),
    QUICK([
        "대명사 문제: ① 가리키는 명사 찾기 → ② 단수/복수 → ③ 주어와 같은 대상이면 **재귀**",
        "the가 붙으면 **나머지 전부**(정해짐), the가 없으면 **일부**",
        "부분 표현 of + 명사 → 동사는 **of 뒤 명사**에 맞춘다",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  He hurt (him / himself) while cooking.", "himself", "주어 = 목적어"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I have two sisters. One is a nurse, and (another / the other) is a teacher.",
              "the other", "2개 중 나머지 하나"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Every student (has / have) a laptop.", "has", "every + 단수"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Some of the money (was / were) stolen.", "was", "of 뒤 money(셀 수 없음) → 단수"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The children cleaned the room by (them / themselves).", "themselves", "by oneself"),
            Q("다음 중 어법상 틀린 것은?", "③", "the dogs(복수)를 가리킴 → their",
              options=["Both of my parents are teachers.", "Help yourself to the pizza.",
                       "The dogs wagged its tails.", "Half of the apples are rotten."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("빈칸에 알맞은 말을 쓰시오.  There are three cups. One is mine, ______ is Mina's, and ______ is Jake's.",
              "another / the other", "3개: one – another – the other", lines=1),
            Q("어법상 틀린 부분을 고치시오.  Each of the players have their own number.", "have → has", "each → 단수", lines=1),
        ]),
    ]),
]
