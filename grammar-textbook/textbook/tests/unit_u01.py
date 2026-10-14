"""Unit 01 8품사 실전 TEST (★ → 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "8품사",
    "time": "20분",
    "items": [
        MC("밑줄 친 hard의 품사가 나머지와 다른 하나는?",
           ["She works ==hard== every day.", "The math test was ==hard==.", "It rained ==hard== last night.",
            "He studied ==hard== for the exam.", "Don't hit the ball too ==hard==."],
           2, "②는 be동사 뒤 보어 → 형용사(어려운), 나머지는 동사를 꾸미는 부사(열심히·세게)",
           level="기본", points=8),
        MC("빈칸에 들어갈 말로 알맞지 않은 것은?  The cake smells ______.",
           ["sweet", "delicious", "wonderful", "nicely", "good"],
           4, "smell(~한 냄새가 나다) 뒤 보어 자리 → 형용사. nicely는 부사",
           level="기본", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["I could hardly believe the news.", "She has been very busy lately.", "He gave me a friendly smile.",
            "It's nearly ten o'clock.", "The bird flew highly in the sky."],
           5, "'높이' 날다 → high. highly는 '매우'라는 뜻의 부사",
           points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "smell 뒤 보어 자리 → 형용사 fresh",
           points=8,
           passage="Last Saturday, my family went camping ==ⓐ near== a lake. The weather was ==ⓑ perfect==, and the "
                   "air smelled ==ⓒ freshly==. My little brother ran ==ⓓ quickly== to the water, and my dad cooked a "
                   "==ⓔ delicious== dinner for us."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 품사가 나머지 넷과 다른 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           1, "Lately(최근에)는 부사. lonely, lovely, friendly, costly는 -ly로 끝나는 형용사",
           level="상", points=8,
           passage="==ⓐ Lately==, my grandmother has felt a little ==ⓑ lonely== because my grandfather passed away "
                   "last year. She lives alone in a ==ⓒ lovely== house in the country. She is ==ⓓ friendly== to "
                   "everyone in her village, but she still misses him. So we visit her every weekend, even though "
                   "the train tickets are ==ⓔ costly==."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           2, "옳은 것: ⓒ ⓓ / ⓐ because of 뒤에 절 → because ⓑ very good → very well ⓔ careful → carefully",
           level="상", hard=True, points=8,
           passage="ⓐ I stayed home because of it rained.\nⓑ She speaks English very good.\n"
                   "ⓒ He hardly ate anything at the party.\nⓓ The movie was surprisingly interesting.\n"
                   "ⓔ The students listened careful to the teacher."),

        WR("두 문장의 뜻이 같도록 <조건>에 맞게 문장을 완성하시오.  He is a good swimmer. → He ______.",
           "He swims well.", "명사(swimmer)를 꾸미던 형용사 good → 동사(swims)를 꾸미는 부사 well",
           points=13, lines=1, conditions=["swim을 활용할 것", "부사를 사용할 것", "3단어로 쓸 것"]),
        WR("밑줄 친 부분을 접속사를 사용한 절로 바꿔 다시 쓰시오.  The game was cancelled ==because of the heavy rain==.",
           "The game was cancelled because it rained heavily.",
           "접속사 because 뒤에는 주어 + 동사. 명사 rain을 꾸미던 heavy → 동사 rained를 꾸미는 heavily",
           points=13, lines=1, conditions=["because, it, rain을 활용할 것"]),
        WR("다음 문장에 <보기>의 두 부사를 알맞은 자리에 넣어 다시 쓰시오.  I made him sad.  <보기> really / yesterday",
           "I really made him sad yesterday.",
           "really는 동사 앞에서 동사를 꾸미고, 시간 부사 yesterday는 문장 끝(또는 문장 맨 앞). 부사는 빼도 문장이 성립하는 수식어",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "wonderfully → wonderful / hard → hardly",
           "taste 뒤 보어 자리 → 형용사 / '거의 ~할 수 없었다' → hardly (hard는 '열심히·딱딱한')",
           level="상", hard=True, points=13, lines=2,
           passage="My cousin Tom is a talented cook. Last weekend, he made a special dinner for my family. The pasta "
                   "tasted wonderfully, and the salad looked fresh. We were so full that we could hard move after "
                   "the meal. It was a really great evening."),
    ],
}
