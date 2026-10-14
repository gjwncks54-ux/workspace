"""Unit 11 관계사 실전 TEST (모듈 u12 / ★★★ → 20문항, 객관식 12 / 서술형 8, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "관계사",
    "time": "40분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  I have a friend ______ father is a pilot.",
           ["who", "whom", "whose", "which", "what"],
           3, "a friend의 아버지 → 소유격 whose (뒤 명사 father)", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  ______ you need now is a good rest.",
           ["That", "What", "Which", "Who", "Whose"],
           2, "선행사 X + 불완전(need의 목적어 없음) → What", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  This is the town ______ I grew up.",
           ["which", "what", "who", "where", "whose"],
           4, "I grew up은 완전한 절 + 장소 선행사 → 관계부사 where", level="기본"),
        MC("빈칸에 that을 쓸 수 없는 것은?",
           ["He is the funniest person ___ I know.", "I think ___ she is right.", "The bag ___ I lost was expensive.",
            "This is the house in ___ he lived.", "The man ___ lives next door is kind."],
           4, "전치사 뒤에는 that 불가 → in which", level="기본"),
        MC("밑줄 친 that의 쓰임이 나머지와 다른 하나는?",
           ["The book ==that== I borrowed is interesting.", "I know the girl ==that== is singing.",
            "This is the movie ==that== I told you about.", "The cake ==that== Mom made was delicious.",
            "She said ==that== she was tired."],
           5, "⑤는 선행사 X + 완전한 절 → 접속사. 나머지는 관계대명사"),
        MC("다음 중 어법상 틀린 것은?",
           ["Tell me the way how you solved it.", "I don't understand what you mean.", "This is the reason why I came.",
            "I remember the day when we first met.", "The girl whose bag was stolen cried."],
           1, "the way와 how는 함께 쓰지 않는다 → the way 또는 how"),
        MC("두 문장을 한 문장으로 연결한 것 중 어법상 틀린 것은?  I still remember the café. We first met in it.",
           ["I still remember the café which we first met in.", "I still remember the café in that we first met.",
            "I still remember the café in which we first met.", "I still remember the café where we first met.",
            "I still remember the café that we first met in."],
           2, "전치사 + 관계대명사에서 that 불가 → in which"),
        MC("빈칸에 공통으로 들어갈 말로 알맞은 것은?  I can't believe ___ he said. / ___ matters most is your health.",
           ["that", "which", "what", "who", "how"],
           3, "선행사 X + 불완전(said의 목적어·matters의 주어 없음) → what"),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "선행사 X + 불완전(liked의 목적어 없음) → What",
           passage="Last summer, I visited Gangneung, a city ==ⓐ which== is famous for its beautiful beaches. I "
                   "stayed at a small hotel ==ⓑ where== my uncle works. He showed me a café ==ⓒ whose== coffee is "
                   "the best in town. The café is in a building ==ⓓ that== was built 100 years ago. ==ⓔ That== I "
                   "liked most was the sunrise over the sea."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "콤마 뒤 계속적 용법에는 that 불가 → which",
           level="상",
           passage="My grandmother lives in a village ==ⓐ where== people grow apples. Every autumn, I visit her "
                   "house, ==ⓑ that== has a big garden. She has a dog ==ⓒ whose== name is Bori. I love the stories "
                   "==ⓓ which== she tells me at night. She is the person ==ⓔ who== I respect most."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ visit의 목적어 없음 → which(that) ⓔ 이유 → why(for which)",
           level="상", hard=True,
           passage="ⓐ This is the house in which I was born.\nⓑ He passed the exam, which surprised everyone.\n"
                   "ⓒ Seoul is the city where I want to visit.\nⓓ I know the man that you are talking about.\n"
                   "ⓔ The reason which he left is still unknown."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["which – which – that", "which – where – what", "where – where – what",
            "where – which – that", "which – where – that"],
           2, "(A) visited의 목적어 없음 → which (B) 뒤가 완전 → where (C) 선행사 X + 불완전(wore의 목적어 없음) → what",
           level="상", hard=True,
           passage="The museum (A) [which / where] I visited last week was amazing. It has a special room "
                   "(B) [which / where] visitors can try on old costumes. The guide also showed us (C) [that / what] "
                   "people wore 500 years ago."),

        WR("두 문장을 <조건>에 맞게 한 문장으로 바꿔 쓰시오.  This is the library. I studied in it every day.",
           "(1) This is the library which I studied in every day. (2) This is the library in which I studied every day. "
           "(3) This is the library where I studied every day.",
           "it → which(전치사는 끝에) / 전치사를 앞으로 → in which / in which = where",
           points=7, lines=3,
           conditions=["(1) which를 쓰고 전치사는 문장 끝에 둘 것", "(2) in which를 쓸 것", "(3) 관계부사를 쓸 것"]),
        WR("두 문장을 관계대명사를 사용하여 한 문장으로 바꿔 쓰시오.  I met a boy. His dream is to be an astronaut.",
           "I met a boy whose dream is to be an astronaut.", "His → 소유격 관계대명사 whose",
           points=6, lines=1),
        WR("밑줄 친 부분을 한 단어로 바꿔 문장을 다시 쓰시오.  ==The thing that== I want for my birthday is a new bike.",
           "What I want for my birthday is a new bike.", "the thing that(which) = what (선행사를 품은 관계대명사)",
           points=6, lines=1),
        WR("다음 문장을 계속적 용법의 관계대명사를 사용하여 바꿔 쓰시오.  I have two sisters, and they live in Canada.",
           "I have two sisters, who live in Canada.", "and + they → , who (계속적 용법, that 불가)",
           points=6, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  이것이 그가 그 문제를 푼 방법이다.",
           "This is how he solved the problem.", "방법 → how 또는 the way (둘을 함께 쓰지 않음)",
           points=7, lines=1, conditions=["how를 사용할 것", "solve, problem을 활용할 것", "7단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  Jeju is the island where I want to visit someday.",
           "where → which(또는 that) / visit의 목적어가 빠진 불완전한 절이므로 관계부사가 아니라 관계대명사를 써야 한다.",
           "장소 선행사라도 뒤 절이 불완전하면 관계대명사", level="상", points=7, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "whom → whose / which → where (또는 in which)",
           "a boy의 꿈 → 소유격 whose / there was no airport는 완전한 절 → 관계부사 where",
           level="상", hard=True, points=7, lines=2,
           passage="Last weekend, I watched a movie that my friend recommended. It was about a boy whom dream was to "
                   "become a pilot. He lived in a small town which there was no airport. He worked hard, and finally "
                   "he became a pilot. The ending was what I liked most."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "What he tells us is always helpful.", "선행사 X + tells의 직접목적어 없음 → What이 이끄는 명사절 주어",
           level="상", points=6, lines=1, conditions=["what을 사용할 것", "tell, helpful을 활용할 것", "7단어로 쓸 것"],
           passage="Mr. Han is my homeroom teacher. ==그가 우리에게 말하는 것은 항상 도움이 된다.== He also listens "
                   "to us carefully."),
    ],
}
