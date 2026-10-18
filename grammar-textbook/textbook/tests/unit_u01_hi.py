"""Unit 01 8품사 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "8품사",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "feel(~하게 느끼다) 뒤 보어 자리 → 형용사 sleepy",
           level="상", points=8,
           passage="Sleep is far more ==ⓐ important== than many teenagers think. When we sleep ==ⓑ deeply==, the "
                   "brain sorts the information it collected during the day. Students who go to bed at "
                   "==ⓒ regular== times tend to remember what they study better. In contrast, those who stay up "
                   "==ⓓ late== often feel ==ⓔ sleepily== in class and have trouble focusing."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["modern – comfortable – hard", "modern – comfortably – hardly", "modernly – comfortably – hard",
            "modern – comfortably – hard", "modernly – comfortable – hardly"],
           2, "(A) look 뒤 보어 → 형용사 (B) 과거분사 arranged를 꾸밈 → 부사 (C) '거의 ~할 수 없다' → hardly",
           level="상", hard=True, points=8,
           passage="The new city library looks (A) [modern / modernly] from the outside. Inside, the chairs are "
                   "(B) [comfortable / comfortably] arranged near large windows. It has become so popular that "
                   "students can (C) [hard / hardly] find an empty seat during exam periods."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ '늦게' → late (lately는 '최근에') ⓔ 동사 have risen을 꾸밈 → sharply",
           level="상", hard=True, points=8,
           passage="ⓐ The plan sounds perfectly reasonable.\nⓑ She has been highly praised for her work.\n"
                   "ⓒ He arrived lately because of the heavy traffic.\nⓓ The costly mistake taught us a lesson.\n"
                   "ⓔ Prices have risen sharp this year."),
        MC("밑줄 친 단어의 품사가 나머지 넷과 다른 것은?",
           ["The movie was ==pretty== boring.", "She works ==hard== to support her family.",
            "It was a ==lovely== day for a picnic.", "He ==nearly== missed the last train.", "I ==hardly== know him."],
           3, "③ lovely는 -ly로 끝나는 형용사(명사 day 수식). 나머지는 부사 (pretty = 꽤)", points=8),
        MC("밑줄 친 since의 품사가 나머지 넷과 다른 것은?",
           ["I haven't seen him ==since== Monday.", "==Since== it was raining, we stayed home.",
            "She has lived here ==since== she was born.", "==Since== you're busy, I'll call later.",
            "We've been friends ==since== we met in 2015."],
           1, "①은 뒤에 명사(Monday)만 → 전치사. 나머지는 뒤에 S + V → 접속사", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 품사가 나머지 넷과 다른 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "ⓓ alarming은 명사 trend를 꾸미는 형용사. 나머지는 부사",
           level="상", points=8,
           passage="Bees are ==ⓐ extremely== important for farming. Without them, many plants could ==ⓑ hardly== "
                   "produce fruit. Sadly, the number of bees has dropped ==ⓒ sharply== in recent years. Scientists "
                   "say that this ==ⓓ alarming== trend is caused by pesticides and climate change. We must act "
                   "==ⓔ quickly== to protect them."),

        WR("두 문장을 <조건>에 맞게 한 문장으로 바꿔 쓰시오.  His explanation was clear. His answer was polite.",
           "He explained clearly and answered politely.",
           "명사(explanation, answer) → 동사(explained, answered) / 형용사 → 부사",
           points=13, lines=1, conditions=["He로 시작할 것", "explain, answer를 동사로 쓸 것", "6단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분 2개를 찾아 고치고, 그 이유를 쓰시오.  The soup smells wonderfully, but it tastes too saltily.",
           "wonderfully → wonderful / saltily → salty / smell, taste 같은 감각동사 뒤 보어 자리에는 형용사를 쓴다.",
           "감각동사 + 형용사 (부사 X)", points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "perfect → perfectly / hard → hardly",
           "형용사 edible을 꾸밈 → 부사 / '거의 ~할 수 없다' → hardly",
           level="상", hard=True, points=13, lines=2,
           passage="Honey never goes bad. Archaeologists have found jars of honey in ancient Egyptian tombs, and "
                   "the honey was still perfect edible. This is because honey contains very little water, so "
                   "bacteria can hard survive in it. However, it should be kept in a tightly closed container."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "But now he drives very carefully.", "동사 drives를 꾸밈 → 부사 carefully",
           level="상", points=13, lines=1,
           conditions=["But now로 시작할 것", "drive, careful을 활용하되 형태를 알맞게 바꿀 것", "6단어로 쓸 것"],
           passage="Jake used to be a very careless driver and got several tickets. ==그러나 지금 그는 매우 조심스럽게 "
                   "운전한다.== He hasn't had an accident in years."),
    ],
}
