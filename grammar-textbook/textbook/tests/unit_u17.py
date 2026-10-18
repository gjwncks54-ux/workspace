"""Unit 18 비교 실전 TEST (모듈 u17 / ★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "비교",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  This bag is as ______ as that one.",
           ["heavy", "heavier", "heaviest", "more heavy", "the heaviest"],
           1, "as ~ as 사이에는 원급", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  My room is ______ bigger than yours.",
           ["very", "much", "many", "more", "most"],
           2, "비교급 강조 → much (very X)", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Jake is the tallest ______ the three boys.",
           ["in", "than", "of", "as", "to"],
           3, "최상급 + of + 복수명사 (the three boys)", level="기본", points=6),
        MC("다음 중 의미가 나머지 넷과 다른 것은?",
           ["Mt. Everest is the highest mountain in the world.",
            "No other mountain in the world is higher than Mt. Everest.",
            "Mt. Everest is higher than any other mountain in the world.",
            "No other mountain in the world is as high as Mt. Everest.",
            "Mt. Everest is as high as other mountains in the world."],
           5, "①~④는 모두 '에베레스트가 가장 높다', ⑤는 '다른 산들만큼 높다'", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["The more you practice, the better you get.", "It's getting colder and colder.",
            "This room is twice as big as that one.", "Jake is smarter than any other students in his class.",
            "Come as soon as possible."],
           4, "any other + 단수명사 → any other student", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  The ______ you read, the more you learn.",
           ["much", "more", "many", "most", "very"],
           2, "The 비교급 ~, the 비교급 … = ~할수록 더 …하다", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "비교급 강조는 much / even / far (very X)",
           points=6,
           passage="Jupiter is ==ⓐ the largest== planet in our solar system. It is about eleven times ==ⓑ as wide "
                   "as== Earth. It is ==ⓒ very== bigger than all the other planets. In general, ==ⓓ the closer== a "
                   "planet is to the sun, ==ⓔ the hotter== it is."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["more – as – in", "much – as – of", "more – so – in", "much – so – of", "more – as – of"],
           1, "(A) than 앞 비교급 → more outgoing (B) 긍정문 원급 비교 → as ~ as (C) 최상급 + in + 집단(my family)",
           level="상", points=6,
           passage="My brother and I are very different. He is (A) [more / much] outgoing than I am. I am "
                   "(B) [as / so] tall as he is, but I'm not as strong. He is the funniest person (C) [of / in] my "
                   "family."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓒ ⓔ / ⓓ as ~ as possible 또는 as ~ as you can",
           level="상", hard=True, points=6,
           passage="ⓐ Your phone is three times as expensive as mine.\nⓑ No other student in my class is taller "
                   "than Jake.\nⓒ This is the most interesting book of all the books.\nⓓ Please answer as quickly "
                   "as you possible.\nⓔ The older he grew, the wiser he became."),

        WR("다음 문장을 <조건>에 맞게 같은 뜻의 문장으로 바꿔 쓰시오.  The Nile is the longest river in the world.",
           "(1) The Nile is longer than any other river in the world. (2) No other river in the world is longer than the Nile.",
           "비교급 + than any other + 단수명사 / No other + 단수명사 + 비교급 than",
           points=7, lines=2, conditions=["(1) any other를 사용할 것", "(2) No other로 시작할 것"]),
        WR("possible을 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  Run as fast as you can.",
           "Run as fast as possible.", "as ~ as S can = as ~ as possible",
           points=7, lines=1),
        WR("'The 비교급, the 비교급' 구문을 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  If you exercise more, you will become healthier.",
           "The more you exercise, the healthier you will become.", "The 비교급 + S + V, the 비교급 + S + V",
           points=8, lines=1),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  This movie is very more exciting than the last one.",
           "very → much (또는 even, still, far, a lot) / very는 비교급을 강조할 수 없다.",
           "비교급 강조어", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "of her school → in her school / twice as more books as → twice as many books as",
           "최상급 + in + 장소·집단 / 배수 + as + 원급(many) + as",
           level="상", hard=True, points=8, lines=2,
           passage="Mina and her sister look alike, but they are very different. Mina is quieter than her sister. "
                   "Her sister is the most active student of her school. Mina reads twice as more books as her "
                   "sister. But they both love music."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "This laptop is twice as expensive as that one.", "배수 + as + 원급 + as",
           level="상", points=8, lines=1,
           conditions=["This laptop으로 시작할 것", "twice, expensive, that one을 활용할 것", "as ~ as를 사용할 것"],
           passage="Jake compared the prices of two laptops at the store. ==이 노트북은 저 노트북보다 두 배 비싸다.== "
                   "So he decided to buy the cheaper one."),
    ],
}
