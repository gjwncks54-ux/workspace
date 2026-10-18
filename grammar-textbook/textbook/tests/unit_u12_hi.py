"""Unit 13 관계사 고등 실전 TEST (모듈 u12 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "관계사",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "콤마 뒤 계속적 용법에는 that 불가 → which",
           level="상", points=8,
           passage="Antarctica is a continent ==ⓐ where== few people live permanently. Scientists ==ⓑ who== work "
                   "there study climate change and wildlife. The ice, ==ⓒ which== covers about 98% of the land, "
                   "holds most of the world's fresh water. Penguins, ==ⓓ that== cannot fly, are the most famous "
                   "animals there. ==ⓔ What== scientists worry about most is the melting ice."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["which – which – that", "where – in which – which", "where – which – which",
            "which – in which – that", "where – in which – that"],
           2, "(A) 완전한 절 → where (B) 완전한 절 → 전치사 + 관계대명사 (C) 콤마 뒤 → which",
           level="상", hard=True, points=8,
           passage="This is the town (A) [which / where] I spent my childhood. I still remember the house "
                   "(B) [which / in which] my family lived. Recently I visited the town, (C) [that / which] had "
                   "changed a lot since then."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ the way와 how는 함께 쓰지 않는다 ⓓ where 뒤는 완전한 절 → in 삭제 (또는 which we stayed in)",
           level="상", hard=True, points=8,
           passage="ⓐ The reason why he quit is unknown.\nⓑ This is the way how I solved the problem.\n"
                   "ⓒ I have a friend whose sister is a pilot.\nⓓ The hotel where we stayed in was clean.\n"
                   "ⓔ He said nothing, which made me angry."),
        MC("빈칸에 that을 쓸 수 없는 것은?",
           ["The first thing ___ I did was call my mom.", "She is the only person ___ understands me.",
            "The bag, ___ I bought yesterday, is broken.", "All ___ you need is love.",
            "He is the best player ___ I have ever seen."],
           3, "콤마 뒤 계속적 용법 → which (that 불가)", points=8),
        MC("두 문장을 한 문장으로 바르게 연결한 것은?  I'll never forget the day. We first met on that day.",
           ["I'll never forget the day which we first met.", "I'll never forget the day when we first met.",
            "I'll never forget the day where we first met.", "I'll never forget the day on that we first met.",
            "I'll never forget the day what we first met."],
           2, "시간 선행사 + 완전한 절 → when (= on which)", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "visitors can enjoy ~는 완전한 절 → where(in which)",
           level="상", points=8,
           passage="The Louvre is a famous museum in Paris ==ⓐ which== attracts millions of visitors every year. "
                   "The building, ==ⓑ which== was once a royal palace, became a museum in 1793. The Mona Lisa, "
                   "==ⓒ whose== painter was Leonardo da Vinci, is its most famous work. Many visitors wait in long "
                   "lines to see the painting ==ⓓ which== they have seen only in books. The museum is also a place "
                   "==ⓔ which== visitors can enjoy beautiful architecture."),

        WR("두 문장을 <조건>에 맞게 한 문장으로 바꿔 쓰시오.  This is the chair. Jake used to sit on it.",
           "(1) This is the chair on which Jake used to sit. (2) This is the chair which(that) Jake used to sit on.",
           "전치사를 앞으로 → on which (that 불가) / 전치사를 끝에 남기면 which·that 가능",
           points=13, lines=2,
           conditions=["(1) on which를 쓸 것", "(2) 전치사를 문장 끝에 둘 것"]),
        WR("관계대명사를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  He passed the exam, and it surprised everyone.",
           "He passed the exam, which surprised everyone.", "앞 문장 전체를 받는 계속적 용법 which",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "that → which / which → why (또는 for which)",
           "콤마 뒤 계속적 용법에 that 불가 / 이유 선행사 + 완전한 절 → why",
           level="상", hard=True, points=13, lines=2,
           passage="Seoul is a city which has a long history. It has many palaces that were built during the Joseon "
                   "Dynasty. Gyeongbokgung, that is the largest palace, attracts many tourists. There is also a "
                   "market in which tourists can buy traditional crafts. This is the reason which I love Seoul."),
        WR("다음 글의 밑줄 친 두 문장을 관계대명사를 사용하여 한 문장으로 바꿔 쓰시오.",
           "Yesterday, Jake met a girl whose father is a famous writer.", "Her → 소유격 관계대명사 whose",
           level="상", points=13, lines=1,
           passage="==Yesterday, Jake met a girl. Her father is a famous writer.== She showed him some of her "
                   "father's books."),
    ],
}
