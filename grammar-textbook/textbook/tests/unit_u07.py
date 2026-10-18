"""Unit 09 준동사 개관 실전 TEST (★ → 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "준동사 개관",
    "time": "20분",
    "items": [
        MC("밑줄 친 부분의 준동사 종류가 나머지와 다른 하나는?",
           ["==Reading== books is my hobby.", "I enjoy ==swimming== in the sea.", "He finished ==cleaning== his room.",
            "==Walking== every day is good for you.", "Look at the ==sleeping== baby."],
           5, "⑤는 명사 baby를 꾸미는 분사(형용사 역할). 나머지는 주어·목적어 자리의 동명사(명사 역할)",
           level="기본", points=8),
        MC("빈칸에 들어갈 말로 알맞은 것은?  She decided ______ the party.",
           ["not to go to", "not go to", "to not going", "not going to", "to go not to"],
           1, "준동사의 부정: not은 to부정사 바로 앞 → not to V", level="기본", points=8),
        MC("빈칸에 들어갈 말이 나머지와 다른 하나는?",
           ["It is hard ___ me to wake up early.", "It was kind ___ you to help me.",
            "It is important ___ us to exercise.", "It is easy ___ him to solve the problem.",
            "It is dangerous ___ children to swim here."],
           2, "성격 형용사(kind) 뒤 의미상 주어 → of. 나머지는 for", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["Exercising regularly helps you stay healthy.", "I hate being treated like a child.",
            "He seems to have been rich.", "Eat too much fast food is bad for your health.",
            "Having eaten lunch, I'm full now."],
           4, "본동사는 is 하나 → 주어 자리 동사는 준동사: Eating too much fast food is ~", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "본동사 made가 이미 있음 → '축하하기 위해' 부사적 용법 to celebrate",
           points=8,
           passage="==ⓐ To become== a chef is my dream. ==ⓑ Cooking== for others makes me happy. Last week, I made "
                   "a cake ==ⓒ celebrate== my sister's birthday. It was a little ==ⓓ burned==, but she enjoyed "
                   "==ⓔ eating== it."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓒ ⓓ / ⓔ 본동사는 take 하나여야 함 → Learning foreign languages takes",
           level="상", hard=True, points=8,
           passage="ⓐ It is nice of you to say so.\nⓑ She seems to have been sick last week.\n"
                   "ⓒ I'm sorry for not calling you earlier.\nⓓ Not having eaten breakfast, I'm hungry now.\n"
                   "ⓔ Learn foreign languages take a lot of time."),

        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  Because I have already seen the movie, I don't want to see it again.",
           "Having already seen the movie, I don't want to see it again.",
           "영화를 본 것이 원하지 않는 것보다 먼저 → having p.p.",
           points=13, lines=2),
        WR("두 문장의 뜻이 같도록 바꿔 쓰시오.  It seems that he was a famous actor. → He seems ______.",
           "He seems to have been a famous actor.",
           "seems(현재)보다 was(과거)가 이전 → 완료 부정사 to have p.p.",
           points=13, lines=1),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  Keep a diary every day helps you remember your life.",
           "Keep → Keeping (또는 To keep) / 한 절에 본동사는 helps 하나뿐이므로 주어 자리의 동사는 준동사로 써야 한다.",
           "주어 자리 동사 → to V / V-ing", level="상", points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "walk → walking (또는 to walk) / of → for",
           "that절의 본동사는 is → 주어 자리는 준동사 / important는 성격 형용사가 아니므로 의미상 주어 for",
           level="상", hard=True, points=13, lines=2,
           passage="My grandfather is 80 years old, but he looks very healthy. He says that walk every morning is "
                   "his secret. It is important of old people to stay active. I hope to be as healthy as he is "
                   "when I get old."),
    ],
}
