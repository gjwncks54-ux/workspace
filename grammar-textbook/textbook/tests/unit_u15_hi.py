"""Unit 20 가정법 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "가정법",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "현재 사실의 반대(가정법 과거) 주절 → would have to",
           level="상", points=8,
           passage="If the Internet ==ⓐ had not been== invented, our lives would be very different today. Without "
                   "it, we ==ⓑ will have to== send letters instead of emails. If I ==ⓒ had lived== in the 1980s, I "
                   "would have used a typewriter. Some people wish they ==ⓓ could live== without smartphones. But "
                   "==ⓔ were it not for== technology, modern society could not function."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["studied – would be – Had I", "had studied – would have been – I had", "studied – would have been – Had I",
            "had studied – would be – Had I", "had studied – would have been – Had I"],
           4, "(A) 과거 사실에 대한 아쉬움 → I wish + had p.p. (B) now → 혼합가정법 would + 동원 (C) if 생략 도치 → Had I",
           level="상", hard=True, points=8,
           passage="I wish I (A) [studied / had studied] harder when I was in middle school. If I had done so, I "
                   "(B) [would be / would have been] at a better high school now. (C) [Had I / I had] known how "
                   "important it was, I would have tried much harder."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ yesterday(과거) → wouldn't have missed ⓔ should 뒤 동사원형 → Should you need",
           level="상", hard=True, points=8,
           passage="ⓐ If it were not for your help, I would fail.\nⓑ He talks as if he knew everything.\n"
                   "ⓒ If I had left earlier, I wouldn't miss the bus yesterday.\nⓓ It's time you went to bed.\n"
                   "ⓔ Should you needed help, please call me."),
        MC("다음 문장과 의미가 같은 것은?  As I am not rich, I can't buy the house.",
           ["If I were rich, I could buy the house.", "If I am rich, I can buy the house.",
            "If I were not rich, I couldn't buy the house.", "If I had been rich, I could have bought the house.",
            "If I were rich, I couldn't buy the house."],
           1, "현재 사실의 반대 → If + 과거형, could + 동원 (긍정·부정을 뒤집는다)", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["I wish I had a sister.", "If I had known, I would have told you.", "She looks as if she had seen a ghost.",
            "But for your advice, I would have failed.", "If I am you, I would apologize."],
           5, "가정법 과거 → If I were you", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "현재 사실의 반대 → as if + 과거형 were",
           level="상", points=8,
           passage="Many people say, \"If I ==ⓐ had== more time, I would exercise more.\" However, time is not the "
                   "real problem. If they ==ⓑ had planned== their days better, they could have found time. Some "
                   "people act as if they ==ⓒ are== too busy to exercise. It's time we ==ⓓ changed== our attitude. "
                   "==ⓔ Had we started== earlier, we would be healthier now."),

        WR("다음 문장을 가정법 문장으로 바꿔 쓰시오.  Because I didn't eat breakfast, I'm hungry now.",
           "If I had eaten breakfast, I wouldn't be hungry now.", "과거 사실의 반대 → 현재 결과(now) → 혼합가정법",
           points=13, lines=1),
        WR("Had it not been for를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  Without your help, I couldn't have finished the project.",
           "Had it not been for your help, I couldn't have finished the project.",
           "과거 가정 without = if it had not been for → if 생략 도치", points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "studied → had studied / would pass → would have passed",
           "지난 학기(과거)에 대한 아쉬움 → I wish + had p.p. / 과거 사실의 반대 → would have p.p.",
           level="상", hard=True, points=13, lines=2,
           passage="Jake failed the final exam last week. He wishes he studied harder last semester. If he had paid "
                   "more attention in class, he would pass the exam. Now he tells his younger brother, \"If I were "
                   "you, I would start studying early.\""),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "She talks as if she had lived in Paris.", "과거 사실의 반대 → as if + had p.p.",
           level="상", points=13, lines=1, conditions=["as if를 사용할 것", "talk, live, Paris를 활용할 것"],
           passage="Mina has never been to France. But she knows a lot about French culture. ==그녀는 마치 파리에 살았던 "
                   "것처럼 말한다.=="),
    ],
}
