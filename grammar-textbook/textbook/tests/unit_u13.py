"""Unit 12 가주어·가목적어 / 강조구문 실전 TEST (모듈 u13 / ★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "가주어·가목적어 / 강조구문",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  ______ is important to drink enough water.",
           ["This", "That", "It", "What", "There"],
           3, "진주어 to drink ~를 뒤로 보내고 빈 주어 자리에 가주어 It", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  It was very careless ______ you to lose your passport.",
           ["for", "of", "to", "with", "by"],
           2, "사람의 성격·태도 형용사(careless) → of + 목적격", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  I found ______ hard to sleep in the noisy room.",
           ["that", "this", "what", "its", "it"],
           5, "find + 가목적어 it + 형용사 + to V", level="기본", points=6),
        MC("밑줄 친 It의 쓰임이 나머지와 다른 하나는?",
           ["==It== is fun to learn new things.", "==It== is true that he won the race.",
            "==It== was in the library that I met her.", "==It== is necessary for you to rest.",
            "==It== is strange that she didn't come."],
           3, "③은 It was와 that을 지우면 완전한 문장(I met her in the library) → 강조구문. 나머지는 가주어",
           points=6),
        MC("밑줄 친 부분을 강조한 문장으로 알맞은 것은?  Minho broke the window ==yesterday==.",
           ["It was yesterday Minho broke that the window.", "It was yesterday that Minho broke the window.",
            "That was yesterday it Minho broke the window.", "It was Minho that broke the window yesterday.",
            "It was yesterday what Minho broke the window."],
           2, "It was + 강조 대상(yesterday) + that + 나머지. ④는 Minho를 강조한 문장", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["It is impossible for me to finish it today.", "She made it possible for us to win.",
            "I think it difficult to learn Chinese.", "He made a rule to take a walk every morning.",
            "It was Jenny that I met at the library."],
           4, "가목적어 it 생략 불가 → He made it a rule to take a walk every morning.", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "진주어 to go ~를 받는 가주어 자리 → it (Experts say it is a good idea ~)",
           points=6,
           passage="Many students think ==ⓐ it== hard to wake up early. But ==ⓑ it== is important for teenagers "
                   "==ⓒ to get== enough sleep. Experts say ==ⓓ that== is a good idea to go to bed at the same time "
                   "every night. ==ⓔ It== was my homeroom teacher that taught me this tip."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["it – for – that", "it – of – that", "that – for – what", "it – for – what", "that – of – that"],
           1, "(A) make + 가목적어 it + 명사 + to V (B) hard → for (C) 강조구문 It was ~ that",
           level="상", points=6,
           passage="My dad made (A) [it / that] a rule to read for an hour every night. At first, it was hard "
                   "(B) [for / of] me to follow the rule. But it was this habit (C) [that / what] helped me get "
                   "better grades."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ 가목적어 it 필요 → found it difficult ⓓ necessary → for him",
           level="상", hard=True, points=6,
           passage="ⓐ It is kind of you to help the old man.\nⓑ I found difficult to understand his words.\n"
                   "ⓒ It was in 2010 that my family moved to Seoul.\nⓓ It is necessary of him to see a doctor.\n"
                   "ⓔ I did finish my homework before dinner."),

        WR("다음 문장의 밑줄 친 부분을 각각 강조하는 문장으로 바꿔 쓰시오.\n"
           "==(1) Mina== gave me ==(2) this necklace== on my birthday.",
           "(1) It was Mina that(who) gave me this necklace on my birthday. "
           "(2) It was this necklace that Mina gave me on my birthday.",
           "It was + 강조 대상 + that + 나머지 (과거 문장이므로 was)",
           points=7, lines=2),
        WR("가주어 It을 사용하여 다음 문장을 바꿔 쓰시오.  To learn a new language takes a lot of time.",
           "It takes a lot of time to learn a new language.", "긴 to부정사 주어를 뒤로 보내고 가주어 It",
           points=7, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  나는 그 책을 이해하기 쉽다는 것을 알았다.",
           "I found it easy to understand the book.", "find + 가목적어 it + 형용사 + 진목적어 to V",
           points=8, lines=1, conditions=["find, easy, understand, the book을 활용할 것", "가목적어 it을 쓸 것",
                                          "8단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  It is very nice for you to invite me to the party.",
           "for → of / nice는 사람의 성격·태도를 나타내는 형용사이므로 의미상 주어를 of + 목적격으로 쓴다.",
           "kind, nice, wise, careless, rude → of", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "thinks fun → thinks it fun / what → that",
           "think + 가목적어 it + 형용사 + to V / 강조구문은 It was ~ that",
           level="상", hard=True, points=8, lines=2,
           passage="My best friend Sora is good at drawing. She thinks fun to draw cartoons. Last month, it was her "
                   "cartoon what won first prize in the school contest. It is amazing for a 15-year-old girl to "
                   "draw so well. I'm really proud of her."),
        WR("다음 대화의 밑줄 친 문장을 at the shopping mall을 강조하는 문장으로 바꿔 쓰시오.",
           "It was at the shopping mall that I lost it.", "부사구도 강조 가능: It was + 부사구 + that + 나머지",
           level="상", points=8, lines=1,
           passage="A: Did you lose your wallet on the bus?\nB: No. ==I lost it at the shopping mall.== I'm going "
                   "back there to look for it."),
    ],
}
