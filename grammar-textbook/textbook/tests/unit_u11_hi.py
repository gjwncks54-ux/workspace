"""Unit 17 분사구문 고등 실전 TEST (모듈 u11 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "분사구문",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "주절 주어 the old castle이 '지어진' 것 → Built",
           level="상", points=8,
           passage="==ⓐ Located== on the coast, the city attracts many tourists every summer. ==ⓑ Walking== along "
                   "the beach, visitors can enjoy beautiful sunsets. ==ⓒ Building== in the 16th century, the old "
                   "castle is the city's most famous landmark. ==ⓓ Having been== damaged during the war, it was "
                   "restored in the 1960s. The weather ==ⓔ being== warm all year round, the city is a perfect place "
                   "to relax."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["Seeing – Taking – closing", "Seen – Taking – closed", "Seen – Taken – closed",
            "Seeing – Taken – closing", "Seen – Taking – closing"],
           2, "(A) 마을이 '보여지는' 것 → Seen (B) 내가 숨을 '쉰' 능동 → Taking (C) 눈이 '감긴' 상태 → with + O + p.p.",
           level="상", hard=True, points=8,
           passage="(A) [Seeing / Seen] from the mountain top, the village looked like a painting. (B) [Taking / "
                   "Taken] a deep breath, I enjoyed the fresh air. Then I sat on a rock for a while with my eyes "
                   "(C) [closing / closed]."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓒ / ⓓ not은 맨 앞 → Not having finished ⓔ 그녀가 '놀란' 것 → Surprised",
           level="상", hard=True, points=8,
           passage="ⓐ Not knowing what to do, she called her mother.\nⓑ Written in simple English, the book is easy "
                   "to read.\nⓒ It being Sunday, the shops were closed.\nⓓ Having not finished his homework, he "
                   "couldn't go out.\nⓔ Surprising by the news, she dropped her cup."),
        MC("밑줄 친 부분과 의미가 같은 것은?  ==Having lived in Japan for years==, he speaks Japanese fluently.",
           ["Because he has lived in Japan for years", "Although he lived in Japan for years",
            "If he lives in Japan for years", "When he will live in Japan for years", "Unless he lived in Japan for years"],
           1, "having p.p. → 주절(현재)보다 이전부터 / 이유 → Because he has lived", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["Feeling tired, I went to bed early.", "Left alone, the child began to cry.",
            "Generally speaking, women live longer than men.", "Judging from his accent, he must be from Busan.",
            "Exhausting after the long trip, she fell asleep quickly."],
           5, "그녀가 '지친' 상태 → Exhausted", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "주절 주어 we가 이야기를 '듣는' 능동 → Listening",
           level="상", points=8,
           passage="My grandfather is a great storyteller. ==ⓐ Sitting== in his favorite chair, he tells us stories "
                   "about his childhood. ==ⓑ Born== in a small village, he grew up very poor. ==ⓒ Having lost== his "
                   "father at an early age, he had to work to support his family. He always talks with his eyes "
                   "==ⓓ shining==. ==ⓔ Listened== to his stories, we learn a lot about life."),

        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  Because he was injured in the game, he couldn't play last week.",
           "(Being) Injured in the game, he couldn't play last week.", "수동 분사구문 → (Being) p.p. (being은 생략 가능)",
           points=13, lines=1),
        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  As the weather was fine, we went on a picnic.",
           "The weather being fine, we went on a picnic.", "부사절 주어(the weather) ≠ 주절 주어(we) → 주어를 남긴 독립분사구문",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "Arrived → Arriving / crossing → crossed",
           "Jake가 '도착한' 능동 → Arriving / 다리가 '꼬인' 상태 → with + O + p.p.",
           level="상", hard=True, points=13, lines=2,
           passage="Waking up late, Jake rushed to the station. Arrived at the platform, he saw the train leaving. "
                   "Having missed the train, he had to wait for an hour. Feeling bored, he sat on a bench and read a "
                   "book with his legs crossing."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He listened to the speech with his arms folded.", "팔이 '접힌(낀)' 상태 → with + O + p.p.",
           level="상", points=13, lines=1, conditions=["with를 사용할 것", "listen to the speech, arms, fold를 활용할 것"],
           passage="The principal gave a long speech at the ceremony. Jake didn't agree with some of her ideas. ==그는 "
                   "팔짱을 낀 채로 그 연설을 들었다.=="),
    ],
}
