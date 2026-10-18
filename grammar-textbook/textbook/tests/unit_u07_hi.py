"""Unit 09 준동사 개관 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "준동사 개관",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "that절의 본동사는 can reduce → 주어 자리는 준동사 reading",
           level="상", points=8,
           passage="==ⓐ Reading== books regularly has many benefits. It is important ==ⓑ for children== to develop "
                   "this habit early. Research shows that people who read often seem ==ⓒ to have== better memory. "
                   "Some experts even say that ==ⓓ read== for just six minutes a day can reduce stress. Parents "
                   "should encourage their children ==ⓔ to read== instead of playing games."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["to be – having – for", "to have been – having – of", "to have been – to have – of",
            "to be – to have – of", "to have been – having – for"],
           2, "(A) seems(현재)보다 이전 → to have been (B) 전치사 of 뒤 동명사 완료형 (C) 성격 형용사 careless → of",
           level="상", hard=True, points=8,
           passage="Jake's grandfather seems (A) [to be / to have been] a famous athlete when he was young. He is "
                   "still proud of (B) [having / to have] won a gold medal in 1988. But he admits it was careless "
                   "(C) [for / of] him to ignore his injuries back then."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓒ ⓔ / ⓓ 본동사는 makes → 주어 자리 Exercising(To exercise)",
           level="상", hard=True, points=8,
           passage="ⓐ She decided not to accept the offer.\nⓑ I hate being told what to do.\n"
                   "ⓒ Not having slept well, he felt tired all day.\nⓓ Exercise every day makes you healthier.\n"
                   "ⓔ He seems to have lost his wallet yesterday."),
        MC("다음 중 의미상 주어가 바르게 쓰인 것은?",
           ["It is hard of me to wake up early.", "It was wise of you to save money.", "It is necessary of us to rest.",
            "It was rude for him to say so.", "It is important of students to read."],
           2, "성격 형용사(wise, rude) → of / 그 외(hard, necessary, important) → for", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["I'm sorry for not keeping my promise.", "She pretended not to know me.",
            "Having finished the work, he went home.", "He is said to have been rich.",
            "Having not eaten breakfast, I felt hungry."],
           5, "준동사의 부정은 not을 맨 앞에 → Not having eaten breakfast", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "본동사는 can be → 주어 자리 동사는 준동사 Finding(To find)",
           level="상", points=8,
           passage="Many people dream of ==ⓐ living== in a big city. However, city life is not always easy. "
                   "==ⓑ Find== an affordable apartment can be very difficult. It is also common ==ⓒ for workers== "
                   "to spend hours commuting. ==ⓓ Having lived== in Seoul for ten years, my uncle finally moved to "
                   "the countryside. He says he doesn't regret ==ⓔ leaving== the city."),

        WR("다음 문장을 He로 시작하는 같은 뜻의 문장으로 바꿔 쓰시오.  It seems that he was a soccer player in his youth.",
           "He seems to have been a soccer player in his youth.", "seems(현재)보다 was(과거)가 이전 → 완료 부정사",
           points=13, lines=1),
        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  Because I didn't study for the test, I'm worried now.",
           "Not having studied for the test, I'm worried now.", "부정(not 맨 앞) + 공부하지 않은 일이 먼저 → Not having p.p.",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "Learn → Learning (또는 To learn) / of them → for them",
           "본동사는 has → 주어 자리 준동사 / good은 성격 형용사가 아님 → for + 목적격",
           level="상", hard=True, points=13, lines=2,
           passage="Learn a musical instrument has many advantages. It helps children develop patience and focus. "
                   "It is also good of them to work with others in a band. Not having played an instrument before, "
                   "I started taking piano lessons last year."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He hates being treated like a child.", "동명사의 수동형 → being p.p.",
           level="상", points=13, lines=1, conditions=["hate, treat, like a child를 활용할 것", "동명사의 수동형을 쓸 것"],
           passage="Jake is seventeen, but his parents still check his homework every night. ==그는 아이처럼 대우받는 "
                   "것을 싫어한다.== He wants them to trust him more."),
    ],
}
