"""Unit 02 대명사 고등 실전 TEST (모듈 u19 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "대명사 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "each (of ~) → 단수동사 suffers",
           level="상", points=8,
           passage="Most of the plastic we throw away ==ⓐ is== not recycled. Some of it ends up in landfills, and "
                   "==ⓑ the rest== flows into rivers and oceans. Each of these places ==ⓒ suffer== serious damage "
                   "as a result. Many sea animals mistake plastic bags for food and hurt ==ⓓ themselves==. If we "
                   "want to protect ==ⓔ them==, we need to use less plastic."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["another – was – were", "the other – was – was", "another – were – was", "the other – were – was",
            "the other – were – were"],
           4, "(A) 두 집단 중 나머지 하나 → the other (B) most of + 복수명사 → were (C) every + 단수명사 → was",
           level="상", hard=True, points=8,
           passage="Researchers divided 100 volunteers into two groups. One group exercised every morning, and "
                   "(A) [another / the other] did not. After a month, most of the volunteers in the first group "
                   "(B) [was / were] sleeping better. Every participant (C) [was / were] asked to keep a sleep diary."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           2, "옳은 것: ⓑ ⓓ / ⓐ of 뒤 information(셀 수 없음) → was ⓒ of 뒤 my classmates(복수) → have "
              "ⓔ 정해지지 않은 다른 사람들 → others",
           level="상", hard=True, points=8,
           passage="ⓐ Half of the information were false.\nⓑ Neither of my parents likes spicy food.\n"
                   "ⓒ Most of my classmates has a smartphone.\nⓓ The company announced its new policy.\n"
                   "ⓔ Some students walk to school, and the other take the bus."),
        MC("다음 중 어법상 틀린 것은?",
           ["Two-thirds of the land is covered with forest.", "Every one of the windows was broken.",
            "Both of the twins are good at music.", "The team lost its first game.",
            "The number of students are increasing."],
           5, "The number of ~ (~의 수) → 단수동사 is", points=8),
        MC("빈칸에 들어갈 말로 알맞은 것은?  There are many ways to relieve stress. One is exercising, ______ is listening to music, and still others include meditation.",
           ["other", "the other", "another", "others", "the others"],
           3, "여럿 중 하나 다음 '또 하나' → another (아직 남은 것이 있음)", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "두 명 중 나머지 한 명 → the other",
           level="상", points=8,
           passage="When I moved to a new school, I was nervous. I didn't know anyone, so I kept to ==ⓐ myself== "
                   "at first. Then two classmates introduced ==ⓑ themselves== to me. One of them ==ⓒ was== Jake, "
                   "and ==ⓓ another== was Mina. Since then, the three of us have helped ==ⓔ one another== a lot."),

        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  그 마을 사람들의 대부분은 농부이다.",
           "Most of the people in the village are farmers.", "most of + 복수명사 → 복수동사",
           points=13, lines=1, conditions=["Most of, the people, the village, farmer를 활용할 것", "현재시제로 쓸 것"]),
        WR("우리말과 같도록 <조건>에 맞게 문장을 완성하시오.  나는 세 언어를 한다. 하나는 한국어, 또 하나는 영어, 나머지 하나는 중국어이다.\n"
           "I speak three languages. ______",
           "One is Korean, another is English, and the other is Chinese.", "3개: one – another – the other",
           points=13, lines=1, conditions=["one, another, the other를 사용할 것"]),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "other → others / are → is",
           "정해지지 않은 다른 일부 → others / each of ~ → 단수동사",
           level="상", hard=True, points=13, lines=2,
           passage="Social media can be useful, but it has its risks. Some users share too much personal "
                   "information, and other become victims of online crime. Each of these problems are serious. "
                   "Experts advise users to protect themselves by checking their privacy settings regularly."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "She practiced by herself in front of the mirror.", "by oneself = 혼자서 (주어 She → herself)",
           level="상", points=13, lines=1,
           conditions=["practice, by, in front of the mirror를 활용할 것", "재귀대명사를 쓸 것"],
           passage="Mina had a speech contest the next day. ==그녀는 거울 앞에서 혼자서 연습했다.== After the contest, "
                   "she was proud of herself."),
    ],
}
