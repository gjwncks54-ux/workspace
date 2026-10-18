"""Unit 02 대명사 실전 TEST (모듈 u19 / ★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "대명사",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  She introduced ______ to her new classmates.",
           ["her", "hers", "herself", "she", "herselves"],
           3, "주어(She) = 목적어 → 재귀대명사 herself", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  I have two cats. One is white, and ______ is black.",
           ["another", "the other", "other", "others", "the others"],
           2, "2개 중 나머지 하나 → the other", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Each of the students ______ a different hobby.",
           ["have", "having", "are having", "has", "to have"],
           4, "each (of ~) → 단수동사", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Some people like summer, and ______ like winter.",
           ["others", "other", "the other", "another", "the another"],
           1, "정해지지 않은 사람들 중 일부 / 다른 일부 → some ~ others", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["Both of my brothers are tall.", "Most of the water is clean.", "Help yourself to the snacks.",
            "Half of the cookies are gone.", "Every child need love."],
           5, "every + 단수명사 → 단수동사 needs", points=6),
        MC("밑줄 친 재귀대명사의 쓰임이 나머지와 다른 하나는?",
           ["She made the dress ==herself==.", "I fixed the bike ==myself==.", "He looked at ==himself== in the mirror.",
            "The president ==himself== came to the party.", "We painted the wall ==ourselves==."],
           3, "③은 주어 = 목적어인 재귀 용법(생략 X). 나머지는 '직접'을 뜻하는 강조 용법(생략 O)", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "가리키는 명사는 세 마리 반려동물(복수) → them",
           points=6,
           passage="Jake has three pets. ==ⓐ One== is a dog, ==ⓑ another== is a cat, and ==ⓒ the other== is a "
                   "hamster. Every morning, he feeds ==ⓓ it== by ==ⓔ himself== before school."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "the others(나머지 학생들 전부)는 복수 → were",
           level="상", points=6,
           passage="Our class went on a field trip last Friday. Each of the students ==ⓐ was== given a map. Some "
                   "of the students ==ⓑ were== excited, but the others ==ⓒ was== tired. Most of the food at the "
                   "restaurant ==ⓓ was== delicious. Both of our teachers ==ⓔ were== kind to us."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           2, "옳은 것: ⓐ ⓓ / ⓑ 주어 = 목적어 → myself ⓒ of 뒤 money(셀 수 없음) → was ⓔ The dog(단수) → its tail",
           level="상", hard=True, points=6,
           passage="ⓐ Neither of the answers is correct.\nⓑ I hurt me while I was playing soccer.\n"
                   "ⓒ Some of the money were stolen.\nⓓ One of my friends lives in Busan.\n"
                   "ⓔ The dog wagged their tail."),

        WR("우리말과 같도록 <조건>에 맞게 문장을 완성하시오.  나는 셔츠 두 장을 샀다. 하나는 내 것이고, 나머지 하나는 Jake의 것이다.\n"
           "I bought two shirts. ______",
           "One is mine, and the other is Jake's.", "2개: one – the other",
           points=7, lines=1, conditions=["one, the other를 사용할 것"]),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  그녀는 혼자서 그 문제를 풀었다.",
           "She solved the problem by herself.", "by oneself = 혼자서",
           points=7, lines=1, conditions=["solve, problem, by를 활용할 것", "6단어로 쓸 것"]),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  학생들 중 몇 명은 집에 갔고, 나머지는 모두 남았다.",
           "Some of the students went home, and the others stayed.",
           "정해진 전체 중 일부 / 나머지 전부 → some ~ the others",
           points=8, lines=2, conditions=["Some of the students로 시작할 것", "stay를 활용할 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  Every student in the class have to wear a uniform.",
           "have → has / every + 단수명사는 단수 취급하므로 단수동사를 쓴다.",
           "수식어 in the class를 지우면 주어는 Every student", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "another → the other / have → has",
           "2개 중 나머지 하나 → the other / each of ~ → 단수동사",
           level="상", hard=True, points=8, lines=2,
           passage="My grandparents have two dogs. One is big, and another is small. Every morning, my grandfather "
                   "walks them in the park. Each of the dogs have a special toy. My grandmother made the toys "
                   "herself."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "Half of the students don't eat breakfast.", "half of + 복수명사 → 복수동사 (do not도 정답)",
           level="상", points=8, lines=1,
           conditions=["Half, the students, eat breakfast를 활용할 것", "현재시제로 쓸 것"],
           passage="Our school did a survey about breakfast. ==학생들 중 절반이 아침을 먹지 않는다.== The teachers "
                   "were surprised at the result."),
    ],
}
