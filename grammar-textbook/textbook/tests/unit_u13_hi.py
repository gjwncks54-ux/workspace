"""Unit 16 가주어·가목적어 / 강조구문 고등 실전 TEST (모듈 u13 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "가주어·가목적어 / 강조구문 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "think의 목적어 자리 명사절(완전한 절)을 이끄는 접속사 → that",
           level="상", points=8,
           passage="Many people find ==ⓐ it== difficult to stay focused for long periods. ==ⓑ It== is believed that "
                   "the average attention span has decreased. Some experts think ==ⓒ it== smartphones are partly to "
                   "blame. However, ==ⓓ it== is not the phones themselves ==ⓔ that== cause the problem, but the way "
                   "we use them."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["it – for – that", "that – of – where", "it – of – that", "that – for – that", "it – for – where"],
           1, "(A) make + 가목적어 it + 명사 + to V (B) important → for (C) 강조구문 It was ~ that",
           level="상", hard=True, points=8,
           passage="My parents made (A) [it / that] a rule to have dinner together every evening. They believe it "
                   "is important (B) [for / of] families to spend time together. Looking back, it was at the dinner "
                   "table (C) [that / where] I learned the most about my parents' lives."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ necessary → for you ⓔ 가목적어 it 생략 불가 → made it possible",
           level="상", hard=True, points=8,
           passage="ⓐ It was careless of him to lose the key.\nⓑ I think it important to keep promises.\n"
                   "ⓒ It is necessary of you to see a doctor.\nⓓ It was in 1998 that my parents got married.\n"
                   "ⓔ She made possible for us to finish on time."),
        MC("밑줄 친 It의 쓰임이 나머지 넷과 다른 것은?",
           ["==It== is easy to make mistakes.", "==It== is strange that he didn't call.",
            "==It== was Jake who broke the vase.", "==It== is necessary for you to rest.", "==It== is true that she won."],
           3, "③은 It was와 who를 지우면 완전한 문장 → 강조구문. 나머지는 가주어", points=8),
        MC("밑줄 친 부분을 강조한 문장으로 알맞은 것은?  Mina met Jake ==at the station== yesterday.",
           ["It was at the station that Mina met Jake yesterday.", "It was at the station what Mina met Jake yesterday.",
            "It was at the station which Mina met Jake yesterday.", "That was at the station it Mina met Jake yesterday.",
            "It was Mina that met Jake at the station yesterday."],
           1, "It was + 강조 대상(부사구) + that + 나머지. ⑤는 Mina를 강조", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "find + 가목적어 it + 형용사 + to V → find it hard",
           level="상", points=8,
           passage="Some people think it ==ⓐ strange== that cats sleep so much. In fact, it is natural ==ⓑ for "
                   "cats== to sleep up to 16 hours a day. Their ancestors found ==ⓒ it== necessary to save energy "
                   "for hunting. It is at night ==ⓓ that== cats become most active. That is why some owners find "
                   "==ⓔ that== hard to sleep well."),

        WR("가주어 It을 사용하여 다음 문장을 바꿔 쓰시오.  That he passed the exam is surprising.",
           "It is surprising that he passed the exam.", "진주어가 that절 → 가주어 It + that절을 뒤로", points=13, lines=1),
        WR("다음 문장을 <조건>에 맞게 같은 뜻으로 바꿔 쓰시오.  Jake thinks that learning Chinese is difficult.",
           "Jake thinks it difficult to learn Chinese.", "think + 가목적어 it + 형용사 + 진목적어 to V",
           points=13, lines=1, conditions=["가목적어 it을 사용할 것", "to부정사를 사용할 것"]),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "find difficult → find it difficult / what → that",
           "가목적어 it 생략 불가 / 강조구문 It is ~ that",
           level="상", hard=True, points=13, lines=2,
           passage="Many teenagers find difficult to wake up early in the morning. It is not laziness what causes "
                   "this problem. Scientists say that teenagers' biological clocks are different from adults'. It "
                   "is important for schools to consider this fact."),
        WR("다음 대화의 밑줄 친 문장을 Mina를 강조하는 문장으로 바꿔 쓰시오.",
           "It was Mina that(who) broke the window.", "It was + 강조 대상(주어) + that(who) + 나머지",
           level="상", points=13, lines=1,
           passage="A: Did Jake break the window in the classroom?\nB: No, he didn't. ==Mina broke the window.== She "
                   "already told the teacher."),
    ],
}
