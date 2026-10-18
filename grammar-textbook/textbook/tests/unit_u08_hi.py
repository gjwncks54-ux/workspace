"""Unit 10 to부정사 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "to부정사 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "명사 way를 꾸미는 형용사적 용법 → One good way to practice",
           level="상", points=8,
           passage="Many students want ==ⓐ to improve== their English, but they don't know ==ⓑ how to start==. One "
                   "good way ==ⓒ practicing== is keeping a diary in English. It is too difficult for beginners "
                   "==ⓓ to write== long entries, so they should start with a few sentences. They also need a quiet "
                   "place ==ⓔ to study== every day."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["to carry it – to help – to rely", "to carry – helping – to rely on", "to carry – to help – to rely on",
            "to carry it – helping – to rely on", "to carry – to help – to rely"],
           3, "(A) 주어 = carry의 목적어 → it 반복 X (B) 형용사 + enough to V (C) rely on someone → 전치사 남김",
           level="상", hard=True, points=8,
           passage="Mina's suitcase was too heavy for her (A) [to carry / to carry it] up the stairs. Luckily, a "
                   "stranger was kind enough (B) [to help / helping] her. In a foreign city with no one "
                   "(C) [to rely / to rely on], she felt truly grateful."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓑ ⓒ ⓔ / ⓐ enough는 형용사 뒤 → brave enough ⓓ 주어 = solve의 목적어 → it 삭제",
           level="상", hard=True, points=8,
           passage="ⓐ She was enough brave to tell the truth.\nⓑ I need something hot to drink.\n"
                   "ⓒ He promised not to be late again.\nⓓ The problem was too hard for me to solve it.\n"
                   "ⓔ I don't know where to go next."),
        MC("밑줄 친 to부정사의 용법이 <보기>와 같은 것은?  <보기> I was surprised ==to hear== the news.",
           ["He grew up ==to be== a famous actor.", "I'm glad ==to see== you again.", "She has no time ==to waste==.",
            "My plan is ==to study== abroad.", "He went to the store ==to buy== milk."],
           2, "<보기>와 ②는 감정의 원인(~해서). ① 결과 ③ 형용사적 ④ 명사적 ⑤ 목적", points=8),
        MC("두 문장의 의미가 같지 않은 것은?",
           ["He is so rich that he can buy the car. = He is rich enough to buy the car.",
            "I don't know what I should say. = I don't know what to say.",
            "The box was so heavy that I couldn't lift it. = The box was too heavy for me to lift.",
            "She studied hard so that she could pass. = She studied hard in order to pass.",
            "It seems that he is sick. = He seems to have been sick."],
           5, "seems와 is는 같은 시제 → He seems to be sick. (to have been은 더 이전)", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           1, "decide는 to부정사만 목적어 → decided to build",
           level="상", points=8,
           passage="Last year, our school decided ==ⓐ building== a garden on the roof. Students were asked "
                   "==ⓑ to bring== seeds from home. The roof was large enough ==ⓒ to grow== vegetables on. We also "
                   "needed some tools ==ⓓ to dig with==. Now the garden is a wonderful place ==ⓔ to relax== after "
                   "lunch."),

        WR("다음 문장을 so ~ that 구문으로 바꿔 쓰시오.  The math problem was too difficult for Jake to solve.",
           "The math problem was so difficult that Jake couldn't solve it.",
           "too ~ to V = so ~ that S can't V (that절은 완전한 절 → it 필요)", points=13, lines=1),
        WR("밑줄 친 부분을 '의문사 + to부정사'로 바꿔 문장을 다시 쓰시오.  Can you tell me ==how I should get== to the station?",
           "Can you tell me how to get to the station?", "의문사 + S + should V = 의문사 + to V", points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "to buy it → to buy / saving → to save",
           "주어(it = the laptop) = buy의 목적어 → it 반복 X / decide는 to부정사만 목적어",
           level="상", hard=True, points=13, lines=2,
           passage="Jake wanted a new laptop for school, but it was too expensive for him to buy it. So he decided "
                   "saving money. He found a part-time job at a café near his house. After six months, he finally "
                   "had enough money to buy the laptop."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "She is looking for a house to live in.", "a house를 꾸미는 형용사적 용법 + live in a house → 전치사 in을 남긴다",
           level="상", points=13, lines=1, conditions=["look for, a house, live를 활용할 것", "to부정사를 사용할 것"],
           passage="Mina got a job in Seoul and has to move next month. ==그녀는 살 집을 찾고 있다.== She hopes to find "
                   "one near her office."),
    ],
}
