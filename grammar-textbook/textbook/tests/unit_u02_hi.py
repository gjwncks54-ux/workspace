"""Unit 03 구와 절 / 문장성분 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "구와 절 / 문장성분",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "수식어 used for packaging을 지우면 주어는 the boxes(복수) → create",
           level="상", points=8,
           passage="The growth of online shopping ==ⓐ has changed== the way people buy things. Products ordered "
                   "online ==ⓑ are== often delivered within a day or two. However, the boxes used for packaging "
                   "==ⓒ creates== a lot of waste. One of the biggest challenges for companies ==ⓓ is== to reduce "
                   "this waste. The number of companies using eco-friendly packaging ==ⓔ is== slowly increasing."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["is – tend – are", "are – tends – is", "is – tends – are", "are – tend – are", "is – tend – is"],
           1, "(A) 주어 The ability(단수) (B) 주어 People(복수), who ~ language는 수식어 (C) 주어 The benefits(복수)",
           level="상", hard=True, points=8,
           passage="The ability to speak several languages (A) [is / are] valuable in today's global society. "
                   "People who learn a second language (B) [tend / tends] to be better at solving problems. "
                   "The benefits of bilingualism (C) [is / are] not limited to communication."),
        MC("다음 중 밑줄 친 부분이 주격보어(C)인 것의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "주격보어: ⓐ ⓑ ⓔ (주어를 설명) / ⓒ 목적어 ⓓ 목적격보어",
           level="상", hard=True, points=8,
           passage="ⓐ My goal is ==to become a scientist==.\nⓑ The problem is ==that we don't have enough time==.\n"
                   "ⓒ I found ==the book== on the shelf.\nⓓ The news made her ==very happy==.\n"
                   "ⓔ She seemed ==a little nervous== before the test."),
        MC("다음 중 어법상 틀린 것은?",
           ["The keys to the front door are on the table.", "Each of the rooms has a balcony.",
            "What we need right now is more time.", "The teacher with many students were in the hall.",
            "Listening to music helps me relax."],
           4, "수식어 with many students를 지우면 주어는 The teacher(단수) → was", points=8),
        MC("밑줄 친 부분의 역할(품사)이 나머지 넷과 다른 것은?",
           ["==To learn English== is fun.", "I know ==that he is honest==.", "==What she said== surprised me.",
            "The girl ==with long hair== is my sister.", "My dream is ==to travel the world==."],
           4, "④는 명사 The girl을 꾸미는 형용사구. 나머지는 주어·목적어·보어 자리의 명사구·명사절", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 문장성분이 나머지 넷과 다른 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "ⓓ coffee = a way to wake up → 보어. 나머지는 동작의 대상인 목적어",
           level="상", points=8,
           passage="Many people drink ==ⓐ coffee== every morning. They love ==ⓑ its rich taste==. Some especially "
                   "enjoy ==ⓒ the smell of fresh beans==. For others, coffee is ==ⓓ a way to wake up==. However, "
                   "doctors recommend ==ⓔ drinking enough water== as well."),

        WR("다음 문장을 S / V / C / M으로 끊어 표시하시오.\nThe decision made by the committee last week seemed unfair to many students.",
           "The decision made by the committee last week (S) / seemed (V) / unfair (C) / to many students (M)",
           "긴 주어(분사구 수식 포함) 뒤 동사 seemed → 2형식", points=13, lines=2),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.\nThe results of the survey conducted among teenagers shows a surprising trend.",
           "shows → show / 수식어 of the survey conducted among teenagers를 지우면 주어는 The results(복수)이다.",
           "동사 바로 앞 명사가 아니라 진짜 주어에 수일치", points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "have → has / helps → help",
           "주어 The use(단수) / that절의 주어 phones(복수), when used properly는 삽입된 수식어",
           level="상", hard=True, points=13, lines=2,
           passage="The use of smartphones in classrooms have become a hot issue. Some teachers believe that phones "
                   "distract students. Others argue that phones, when used properly, helps students learn. The key "
                   "to solving this problem is clear rules."),
        WR("다음 글의 밑줄 친 구를 같은 뜻의 절로 바꿔 문장 전체를 다시 쓰시오.",
           "Jake met a woman who had a camera around her neck.",
           "형용사구 with ~ → 형용사절(관계대명사절) who had ~",
           level="상", points=13, lines=1, conditions=["who를 사용할 것"],
           passage="At the festival, ==Jake met a woman with a camera around her neck==. She turned out to be a "
                   "famous photographer. She showed him some of her best pictures."),
    ],
}
