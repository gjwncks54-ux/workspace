from textbook.blocks import *
from textbook import figs as F

GOALS = []
INTRO = ""

BLOCKS = [
    TABLE(
        ["상관접속사", "뜻", "동사 수일치"],
        [
            ["**both** A **and** B", "A와 B 둘 다", "**복수**"],
            ["**either** A **or** B", "A 또는 B", "**B**에 맞춤"],
            ["**neither** A **nor** B", "A도 B도 아닌", "**B**에 맞춤"],
            ["**not** A **but** B", "A가 아니라 B", "**B**에 맞춤"],
            ["**not only** A **but also** B = B **as well as** A", "A뿐만 아니라 B도", "**B**에 맞춤"],
        ],
        widths=[44, 30, 26], center=[2], caption="상관접속사 (짝으로 다니는 접속사)",
    ),
    PILGI([
        "상관접속사 수일치는 {{B}}에 맞춘다. 단, both A and B는 {{복수}}",
        "B as well as A → 동사는 {{B}}에 맞춤 (앞에 있는 쪽)",
        "and / but / or 앞뒤는 {{같은 형태}} (병렬)",
        "비교 than / as 앞뒤도 {{병렬}}",
    ]),
    FIG(F.parallel_board([
        (True, "reading", "and", "writing"),
        (True, "to read", "and", "(to) write"),
        (False, "reading", "and", "to write"),
        (True, "kind", "and", "honest"),
        (False, "kind", "and", "honesty"),
    ]), "병렬: 접속사 앞뒤 모양 맞추기"),
    CHAIN([
        ("틀린 문장", "She likes reading and ~~to write~~.", None),
        ("동명사로", "She likes **reading and writing**.", "동명사 ↔ 동명사"),
        ("to V로", "She likes **to read and (to) write**.", "두 번째 to는 생략 가능"),
        ("상관접속사", "She likes **not only reading but also writing**.", "not only A but also B도 병렬"),
    ], title="She likes reading and writing"),
    TABLE(
        ["의미", "접속사 (+ S + V)", "같은 뜻 전치사 (+ 명사)"],
        [
            ["시간", "when, while, before, after, until, since", "during (~동안)"],
            ["이유", "because, since, as", "because of, due to"],
            ["양보", "although, though, even though", "despite, in spite of"],
            ["조건", "if, unless (= if ~ not)", "–"],
            ["목적·결과", "so that (~하도록) / so ~ that (너무 ~해서)", "–"],
        ],
        widths=[14, 50, 36], caption="종속접속사 vs 전치사",
    ),
    QUICK([
        "상관접속사 수일치 → **뒤쪽(B)** 확인 (both만 복수)",
        "병렬 문제 → ① and·but·or 찾기 ② 앞 덩어리 모양 확인 ③ 뒤 모양 맞추기",
        "뒤에 S + V → **접속사** / 명사만 → **전치사** (although ↔ despite)",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Either you or Jake (has / have) to clean the room.", "has", "B(Jake)에 맞춤"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Both Mina and Sora (is / are) my friends.", "are", "both → 복수"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Although / Despite) the rain, we went out.", "Despite", "뒤에 명사만"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  He enjoys swimming, hiking, and (to ride / riding) a bike.", "riding", "병렬"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The students as well as the teacher (was / were) excited.", "were",
              "B as well as A → B(The students)"),
            Q("다음 중 어법상 틀린 것은?", "④", "병렬: 형용사 ↔ 형용사 → smart and kind",
              options=["Not only he but also I am tired.", "Neither my sister nor my parents know it.",
                       "She studied hard so that she could pass.", "My teacher is smart and kindness."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("같은 뜻이 되도록 바꾸시오.  Jake as well as his friends likes soccer. (not only ~ but also)",
              "Not only his friends but also Jake likes soccer.", "동사는 B(Jake)에 맞춰 likes", lines=1),
            Q("어법상 틀린 부분을 고치시오.  I like to swim and playing tennis.", "playing → (to) play (또는 to swim → swimming)",
              "병렬", lines=1),
            Q("같은 뜻이 되도록 바꾸시오.  Although it was cold, we went swimming. (Despite)",
              "Despite the cold (weather), we went swimming.", "전치사 + 명사", lines=1),
        ]),
    ]),
]
