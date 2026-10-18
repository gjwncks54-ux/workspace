"""Unit 11 동명사 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "동명사 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "be used to V-ing(~하는 데 익숙하다)의 to는 전치사 → asking",
           level="상", points=8,
           passage="Many people avoid ==ⓐ asking== for help because they are afraid of ==ⓑ looking== weak. However, "
                   "psychologists say that asking for help is worth ==ⓒ trying==. In one study, employees who were "
                   "used to ==ⓓ ask== for advice performed better at work. So next time you are stuck, stop "
                   "==ⓔ worrying== and ask someone."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["to visit – to bring – taking", "visiting – bringing – to take", "visiting – to bring – to take",
            "to visit – bringing – to take", "visiting – to bring – taking"],
           3, "(A) 10년 전 이미 한 일 → forget V-ing (B) remind + O + to V (C) '~하기 위해' 멈추다 → stop to V",
           level="상", hard=True, points=8,
           passage="I'll never forget (A) [to visit / visiting] the Grand Canyon with my father ten years ago. "
                   "Before we left, he reminded me (B) [to bring / bringing] a warm jacket. On the way, we stopped "
                   "(C) [to take / taking] pictures of the sunset."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ consider + V-ing → changing ⓓ spend + 시간 + V-ing → cleaning",
           level="상", hard=True, points=8,
           passage="ⓐ I regret not telling you the truth earlier.\nⓑ She is considering to change her major.\n"
                   "ⓒ Would you mind my opening the window?\nⓓ He spent the whole weekend to clean the garage.\n"
                   "ⓔ I'm looking forward to working with you."),
        MC("빈칸에 들어갈 말로 알맞지 않은 것은?  My brother ______ playing computer games.",
           ["decided", "enjoys", "gave up", "denied", "finished"],
           1, "decide는 to부정사만 목적어 → decided to play", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["Stop worrying about it.", "I used to playing the piano.", "He is used to living alone.",
            "This book is worth reading.", "I feel like eating pizza tonight."],
           2, "'~하곤 했다' → used to + 동사원형: I used to play the piano.", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "1965년(과거)에 이미 한 일을 기억 → remembers buying",
           level="상", points=8,
           passage="My grandmother has a special hobby: ==ⓐ collecting== old postcards. She started ==ⓑ doing== it "
                   "when she was a teenager. She still remembers ==ⓒ to buy== her first postcard in Paris in 1965. "
                   "Now she spends a lot of time ==ⓓ organizing== them. She is even thinking about ==ⓔ opening== a "
                   "small exhibition."),

        WR("regret을 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  I'm sorry that I didn't call you yesterday.",
           "I regret not calling you yesterday.", "과거 일을 후회 → regret V-ing, 동명사 부정은 not V-ing (not having called도 정답)",
           points=13, lines=1),
        WR("다음 문장을 <조건>에 맞게 같은 뜻으로 바꿔 쓰시오.  Living alone is not difficult for her anymore.",
           "She is used to living alone.", "be used to + V-ing = ~하는 데 익숙하다",
           points=13, lines=1, conditions=["She로 시작할 것", "be used to를 사용할 것"]),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "postpone to do → postpone doing / make → making",
           "postpone은 동명사만 목적어 / 전치사 of 뒤 → 동명사",
           level="상", hard=True, points=13, lines=2,
           passage="Some students postpone to do their homework until the last minute. They are afraid of make "
                   "mistakes, so they avoid starting at all. Experts recommend breaking big tasks into smaller ones. "
                   "This makes it easier to get started."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "The café is worth visiting.", "be worth V-ing = ~할 가치가 있다",
           level="상", points=13, lines=1, conditions=["worth, visit을 활용할 것", "5단어로 쓸 것"],
           passage="A new café opened near Jake's school last month. The coffee is excellent, and the view is "
                   "amazing. ==그 카페는 방문할 가치가 있다.=="),
    ],
}
