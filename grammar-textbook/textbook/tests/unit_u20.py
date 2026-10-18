"""Unit 15 접속사 / 병렬 실전 TEST (모듈 u20 / ★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "접속사 / 병렬",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  Both Jake and Mina ______ good at math.",
           ["is", "are", "was", "has", "be"],
           2, "both A and B → 복수동사", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  ______ the heavy rain, the game was not cancelled.",
           ["Although", "Because", "Despite", "Though", "Even though"],
           3, "뒤에 명사(구)만 있음 + 양보 → 전치사 Despite", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Either you or Jake ______ to clean the room.",
           ["have", "having", "are", "to have", "has"],
           5, "either A or B → B(Jake)에 수일치 → has", level="기본", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["Neither my sister nor my parents know it.", "Not only he but also I am tired.",
            "She likes reading and to write stories.", "The students as well as the teacher were excited.",
            "I stayed home because of the storm."],
           3, "and 앞뒤 병렬 → reading and writing (또는 to read and (to) write)", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  I'll wait here ______ you come back.",
           ["until", "during", "despite", "because of", "in spite of"],
           1, "뒤에 S + V → 접속사, '~할 때까지' → until", points=6),
        MC("다음 문장을 B as well as A로 바르게 바꾼 것은?  Not only Jake but also his friends like soccer.",
           ["His friends as well as Jake likes soccer.", "Both Jake and his friends likes soccer.",
            "Jake as well as his friends like soccer.", "His friends as well as Jake like soccer.",
            "Not only his friends but also Jake like soccer."],
           4, "not only A but also B = B as well as A, 동사는 B(his friends, 복수)에 맞춤 → like", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "spent time 뒤 V-ing가 and로 나열 → 병렬: swimming",
           points=6,
           passage="My summer vacation was busy but fun. I spent time ==ⓐ reading== novels, ==ⓑ to swim== at the "
                   "beach, and ==ⓒ visiting== my grandparents. My grandmother is kind and ==ⓓ funny==. She taught me "
                   "not only how to cook ==ⓔ but also== how to fish."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "뒤에 S + V(we had)가 있음 → 접속사 Although",
           level="상", points=6,
           passage="Neither my brother nor I ==ⓐ am== good at cooking. So last weekend, both my brother and I "
                   "==ⓑ were== surprised when our mom asked us to make dinner. ==ⓒ Despite== we had a recipe, the "
                   "soup tasted strange. Not only the soup but also the rice ==ⓓ was== burnt. Still, our parents ate "
                   "everything ==ⓔ because== they wanted to encourage us."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           2, "옳은 것: ⓐ ⓓ / ⓑ 뒤에 명사만 → Despite ⓒ 형용사 병렬 → honest ⓔ could + 동사원형 → could pass",
           level="상", hard=True, points=6,
           passage="ⓐ Jake as well as his sisters is coming.\nⓑ Although the cold weather, we went hiking.\n"
                   "ⓒ She is smart, kind, and honesty.\nⓓ Either my parents or my sister is at home.\n"
                   "ⓔ He studied hard so that he could passed the exam."),

        WR("다음 문장의 틀린 부분을 <조건>에 맞게 두 가지 방법으로 고쳐 문장을 다시 쓰시오.  She likes reading and to write.",
           "(1) She likes reading and writing. (2) She likes to read and (to) write.",
           "and 앞뒤 병렬: 동명사 ↔ 동명사 / to V ↔ (to) V",
           points=7, lines=2, conditions=["(1) 동명사로 통일할 것", "(2) to부정사로 통일할 것"]),
        WR("as well as를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  Not only Jake but also Mina plays the piano.",
           "Mina as well as Jake plays the piano.", "not only A but also B = B as well as A (동사는 B에 맞춤)",
           points=7, lines=1),
        WR("다음 문장을 <조건>에 맞게 바꿔 쓰시오.  Although it rained heavily, we played soccer.",
           "Despite the heavy rain, we played soccer.", "접속사 although + 절 → 전치사 despite + 명사구",
           points=8, lines=1, conditions=["Despite, the heavy rain을 사용할 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  Neither Jake nor his friends was at the party.",
           "was → were / neither A nor B는 B(his friends, 복수)에 수일치한다.",
           "상관접속사 수일치는 B (both만 복수)", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "playing → play / was → were",
           "can 뒤 동사원형 병렬(sing, dance, and play) / both A and B → 복수동사",
           level="상", hard=True, points=8, lines=2,
           passage="My best friend Sora is very talented. She can sing, dance, and playing the piano. Last year, "
                   "both Sora and her brother was chosen for the school musical. During the show, she was nervous "
                   "but confident. Everyone loved her performance."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He got up early so that he could catch the first train.",
           "so that S could V = ~할 수 있도록 (목적) (woke up early도 정답)",
           level="상", points=8, lines=2,
           conditions=["so that을 사용할 것", "get up, early, catch, the first train을 활용할 것"],
           passage="Jake had an important job interview in Busan. ==그는 첫 기차를 탈 수 있도록 일찍 일어났다.== "
                   "Luckily, he arrived on time."),
    ],
}
