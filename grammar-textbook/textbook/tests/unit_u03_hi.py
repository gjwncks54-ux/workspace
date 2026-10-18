"""Unit 04 문장의 5형식 / 자동사·타동사 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "문장의 5형식 / 자동사·타동사 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "become(~이 되다) 뒤 보어 자리 → 형용사 tense",
           level="상", points=8,
           passage="When we feel stressed, our bodies ==ⓐ react== in various ways. Our hearts beat faster, and our "
                   "muscles ==ⓑ become tensely==. A short walk can make us ==ⓒ feel calmer==. Experts also "
                   "recommend ==ⓓ a few simple techniques==, such as deep breathing. These methods keep our minds "
                   "==ⓔ clear== during difficult times."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["impressive – us the history – informative", "impressively – the history to us – informatively",
            "impressive – the history to us – informative", "impressive – the history to us – informatively",
            "impressively – us the history – informative"],
           3, "(A) look 뒤 보어 → 형용사 (B) explain은 4형식 불가 → explain A to B (C) 5형식 목적격보어 → 형용사",
           level="상", hard=True, points=8,
           passage="The museum's new exhibition looks (A) [impressive / impressively]. The guide explained "
                   "(B) [us the history / the history to us] in detail. Many visitors found the exhibition "
                   "(C) [informative / informatively] and planned to come back."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ resemble은 타동사 → resembles her mother ⓓ introduce는 4형식 불가 → introduced his new girlfriend to me",
           level="상", hard=True, points=8,
           passage="ⓐ The committee discussed the issue for hours.\nⓑ She resembles with her mother.\n"
                   "ⓒ The milk turned sour overnight.\nⓓ He introduced me his new girlfriend.\n"
                   "ⓔ They named their daughter Grace."),
        MC("다음 중 어법상 틀린 것은?",
           ["Please remain seated.", "Could you explain me how it works?", "The rumor proved false.",
            "The leaves turned yellow.", "I'll get you a drink."],
           2, "explain은 4형식 불가 → explain to me how it works", points=8),
        MC("다음 중 문장의 형식이 나머지 넷과 다른 것은?",
           ["He found the movie boring.", "The plan sounds great.", "She kept silent during the meeting.",
            "The weather grew colder.", "Your idea seems reasonable."],
           1, "①은 the movie = boring → 5형식. 나머지는 주어를 설명하는 2형식", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "buy는 3형식 전환 시 for → bought a small gift for him",
           level="상", points=8,
           passage="Last month, my grandfather sent a letter ==ⓐ to me==. In it, he told ==ⓑ me== a story about his "
                   "childhood. He also asked a favor ==ⓒ of me==: to visit him more often. So I bought a small gift "
                   "==ⓓ to him== and visited him last weekend. He cooked a wonderful dinner ==ⓔ for me==."),

        WR("다음 두 문장을 각각 3형식으로 바꿔 쓰시오.\n(1) The waiter brought us the menu.\n(2) Could you get me a glass of water?",
           "(1) The waiter brought the menu to us. (2) Could you get a glass of water for me?",
           "bring → to / get → for", points=13, lines=2),
        WR("다음 문장에서 어법상 틀린 부분 2개를 찾아 고치고, 그 이유를 쓰시오.\nWe need to discuss about the matter before we reach to a decision.",
           "discuss about → discuss / reach to → reach / discuss와 reach는 타동사이므로 전치사 없이 목적어를 쓴다.",
           "전치사를 쓰면 틀리는 타동사: discuss, reach, marry, enter, resemble", points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "explained us → explained to us / calmly → calm",
           "explain은 4형식 불가 / stay 뒤 보어 → 형용사",
           level="상", hard=True, points=13, lines=2,
           passage="Some people think that rainy days make them depressed. However, the sound of rain can make "
                   "others feel relaxed. Scientists explained us that the sound works like 'white noise.' It helps "
                   "the brain stay calmly by blocking out other sounds."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "She made a cake for him on his birthday.", "make는 3형식 전환 시 for",
           level="상", points=13, lines=1, conditions=["3형식으로 쓸 것", "make, cake, birthday를 활용할 것"],
           passage="Jake's mother is a great cook. ==그녀는 그의 생일에 그에게 케이크를 만들어 주었다.== It was the best "
                   "cake he had ever eaten."),
    ],
}
