from textbook.blocks import *
from textbook import figs as F

GOALS = []
INTRO = ""

BLOCKS = [
    TABLE(
        ["구분", "형태", "예문"],
        [
            ["**원급**", "as + 원급 + as", "Tom is **as tall as** his father.\nTom은 아버지만큼 키가 크다."],
            ["**비교급**", "-er / more ~ + than", "Tom is **taller than** his father.\nTom은 아버지보다 키가 크다."],
            ["**최상급**", "the -est / most ~ + in / of", "Tom is **the tallest** in his class.\nTom은 반에서 가장 키가 크다."],
        ],
        widths=[14, 30, 56], caption="비교 3종",
    ),
    PILGI([
        "as ___ as 사이에는 {{원급}}  /  than 앞에는 {{비교급}}",
        "비교급 강조: {{much}}, even, still, far, a lot  (very ✗)",
        "The + 비교급 ~, the + 비교급 … = ~할수록 더 …하다",
        "최상급 = 비교급 + than any other + {{단수}}명사",
        "in + 장소·집단 / of + {{복수}}명사 (of the three, of all)",
    ]),
    CHAIN([
        ("최상급", "Seoul is **the biggest** city in Korea.", "서울은 한국에서 가장 큰 도시이다."),
        ("비교급 ①", "Seoul is **bigger than any other city** in Korea.", "any other + 단수명사"),
        ("비교급 ②", "Seoul is **bigger than all the other cities** in Korea.", "all the other + 복수명사"),
        ("부정 + 비교급", "**No other city** in Korea is **bigger than** Seoul.", "No other + 단수명사"),
        ("부정 + 원급", "**No other city** in Korea is **as big as** Seoul.", "as ~ as"),
    ], title="최상급 바꿔 쓰기 5단"),
    TABLE(
        ["표현", "뜻", "예문"],
        [
            ["as ~ as **possible** = as ~ as S **can**", "가능한 한 ~하게", "Come as soon as possible.\n가능한 한 빨리 와."],
            ["**배수** + as ~ as / 배수 + 비교급 than", "~보다 몇 배 …한", "This room is **twice as big as** that one.\n이 방은 저 방의 두 배다."],
            ["**The** 비교급, **the** 비교급", "~할수록 더 …하다", "**The more** you practice, **the better** you get.\n연습할수록 더 잘하게 된다."],
            ["비교급 **and** 비교급", "점점 더 ~한", "It is getting **colder and colder**.\n점점 더 추워지고 있다."],
        ],
        widths=[36, 20, 44], caption="비교 관용 표현",
    ),
    QUICK([
        "**than**이 보이면 → 비교급  /  **as ___ as** → 원급  /  **the ___ in·of** → 최상급",
        "비교급 앞 very → ✗ → **much**",
        "any other / No other 뒤 → **단수**명사",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  This box is as (heavy / heavier) as that one.", "heavy", "as ~ as 사이 원급"),
            Q("괄호 안에서 알맞은 것을 고르시오.  My bag is (much / very) bigger than yours.", "much", "비교급 강조"),
            Q("괄호 안에서 알맞은 것을 고르시오.  She is the smartest (in / of) all the students.", "of", "of + 복수명사"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Mt. Everest is higher than any other (mountain / mountains).", "mountain",
              "any other + 단수"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The (hard / harder) you study, the better grades you get.", "harder",
              "The 비교급, the 비교급"),
            Q("다음 중 의미가 나머지와 다른 것은?", "④", "①②③은 모두 '서울이 가장 크다', ④는 '서울이 다른 도시만큼 크지 않다'",
              options=["Seoul is the biggest city in Korea.", "No other city in Korea is bigger than Seoul.",
                       "Seoul is bigger than any other city in Korea.", "Seoul is not as big as other cities in Korea."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("같은 뜻이 되도록 바꾸시오.  Jake is the fastest runner in his class. (No other)",
              "No other runner in his class is faster than Jake.", "No other + 단수명사 + 비교급 than", lines=1),
            Q("같은 뜻이 되도록 바꾸시오.  Read as many books as possible. (can)", "Read as many books as you can.", "", lines=1),
        ]),
    ]),
]
