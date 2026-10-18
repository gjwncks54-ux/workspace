"""Unit 14 명사절 / 간접의문문 고등 실전 TEST (모듈 u18 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "명사절 / 간접의문문 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "선행사 X + 완전한 절(dreams are just random signals) → that",
           level="상", points=8,
           passage="Scientists have long wondered ==ⓐ why== we dream. Some believe ==ⓑ that== dreams help us process "
                   "emotions. Others think ==ⓒ what== dreams are just random signals from the brain. "
                   "==ⓓ Whether== dreams have a real purpose is still unclear. However, ==ⓔ what== we know for sure "
                   "is that sleep is essential for health."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["if – Whether – why he didn't", "that – If – why didn't he", "if – If – why he didn't",
            "that – Whether – why he didn't", "if – Whether – why didn't he"],
           1, "(A) '~인지' → if (B) 주어 자리 → Whether만 가능 (C) 간접의문문 → 의문사 + S + V",
           level="상", hard=True, points=8,
           passage="I wonder (A) [if / that] Jake will come to my party. (B) [Whether / If] he comes or not doesn't "
                   "matter much. But I really want to know (C) [why he didn't / why didn't he] reply to my message."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ 간접의문문 → where she lives ⓓ 뒤가 완전 → that",
           level="상", hard=True, points=8,
           passage="ⓐ What do you think he wants for his birthday?\nⓑ Do you know where does she live?\n"
                   "ⓒ I'm not sure whether or not she will agree.\nⓓ I believe what he is honest.\n"
                   "ⓔ That the earth is round is a fact."),
        MC("밑줄 친 if의 쓰임이 나머지 넷과 다른 것은?",
           ["I wonder ==if== it will rain.", "Ask him ==if== he can help.", "I'm not sure ==if== she is at home.",
            "==If== it rains tomorrow, we'll stay home.", "Do you know ==if== the store is open?"],
           4, "④는 조건의 부사절(만약 ~라면). 나머지는 '~인지'라는 명사절(목적어)", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["I don't know why she left early.", "Who do you think broke the window?", "Tell me what you want.",
            "I asked him where was he going.", "What she said made me cry."],
           4, "간접의문문 어순 → where he was going", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "선행사 X + 불완전(주어 없음) → What",
           level="상", points=8,
           passage="Many people ask me ==ⓐ how== I learned English so quickly. The truth is ==ⓑ that== I watched "
                   "American TV shows every day. At first, I couldn't understand ==ⓒ what== the characters were "
                   "saying. But I didn't care ==ⓓ if== I understood everything. ==ⓔ That== matters most is "
                   "practicing every day."),

        WR("두 문장을 한 문장으로 바꿔 쓰시오.  Do you believe? + Who will win the election?",
           "Who do you believe will win the election?", "believe류 동사 → 의문사가 맨 앞 (의문사가 주어이므로 뒤는 will win)",
           points=13, lines=1),
        WR("다음 문장을 Whether로 시작하는 같은 뜻의 문장으로 바꿔 쓰시오.  It is not certain whether he will come.",
           "Whether he will come is not certain.", "주어 자리 명사절 → whether (if 불가)", points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "why was I → why I was / what → that",
           "간접의문문 어순 / 선행사 X + 완전한 절 → 접속사 that",
           level="상", hard=True, points=13, lines=2,
           passage="Yesterday my teacher asked me why was I late. I explained what the bus had broken down on the "
                   "way. She said that being on time was important. She just wanted me to leave home earlier."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He asked her where the nearest subway station was.", "간접의문문: 의문사 + S + V (과거 → was)",
           level="상", points=13, lines=1,
           conditions=["ask, the nearest subway station을 활용할 것", "간접의문문으로 쓸 것"],
           passage="Jake is new to this city. He got lost and stopped a woman on the street. ==그는 그녀에게 가장 가까운 "
                   "지하철역이 어디인지 물었다.== She kindly showed him the way."),
    ],
}
