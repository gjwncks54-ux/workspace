"""Unit 06 시제 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "시제",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "In 2007 = 명백한 과거 → changed",
           level="상", points=8,
           passage="The first smartphone ==ⓐ was introduced== in the 1990s. In 2007, a new model ==ⓑ has changed== "
                   "the market completely. Since then, the number of smartphone users ==ⓒ has grown== rapidly. When "
                   "smartwatches appeared, many people ==ⓓ had already owned== smartphones for years. Experts "
                   "predict that by 2030, wearable devices ==ⓔ will have replaced== many traditional phones."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["had lived – studied – passes", "has lived – has studied – will pass", "had lived – has studied – passes",
            "had lived – has studied – will pass", "has lived – studied – passes"],
           3, "(A) 과거 기준점(moved in 2020)보다 이전 → had lived (B) since then → 현재완료 (C) 조건 부사절 → 현재가 미래 대신",
           level="상", hard=True, points=8,
           passage="Jake (A) [had lived / has lived] in Tokyo for three years before he moved to Seoul in 2020. He "
                   "(B) [studied / has studied] Korean since then. If he (C) [passes / will pass] the language exam "
                   "next month, he will get a job at a Korean company."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓑ ⓒ(불변의 진리 → 현재) ⓓ / ⓐ in 2019 → visited ⓔ 시간 부사절 → when she comes back",
           level="상", hard=True, points=8,
           passage="ⓐ I have visited Paris in 2019.\nⓑ By the end of this year, she will have worked here for a "
                   "decade.\nⓒ He told us that light travels faster than sound.\nⓓ When did you finish the project?\n"
                   "ⓔ I will tell her the news when she will come back."),
        MC("다음 중 어법상 틀린 것은?",
           ["I've known Jake since we were kids.", "It has been raining since this morning.",
            "We had finished dinner before he arrived.", "How long have you been waiting?",
            "I am belonging to the drama club."],
           5, "belong(소속 상태)은 상태동사 → 진행형 X: I belong to the drama club.", points=8),
        MC("밑줄 친 부분의 용법이 <보기>와 같은 것은?  <보기> She ==has lived== in Busan for ten years.",
           ["I ==have== just ==finished== my report.", "He ==has gone== to Canada.", "==Have== you ever ==ridden== a horse?",
            "We ==have been== friends since childhood.", "I ==have lost== my wallet."],
           4, "<보기>와 ④는 계속. ① 완료 ② 결과 ③ 경험 ⑤ 결과", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "지난여름(과거)에 끝난 일 → taught",
           level="상", points=8,
           passage="Last summer, I ==ⓐ went== on a volunteer trip to Cambodia. Before the trip, I ==ⓑ had never "
                   "traveled== abroad. When we arrived at the village, the children ==ⓒ were waiting== for us. I "
                   "==ⓓ have taught== them English for two weeks. Since I came back, I ==ⓔ have kept== in touch "
                   "with some of them."),

        WR("두 문장을 현재완료를 사용하여 한 문장으로 바꿔 쓰시오.\nJake started to work at this company in 2018. He still works there.",
           "Jake has worked at this company since 2018.", "과거에 시작해 지금도 계속 → 현재완료 + since 시점 (has been working도 정답)",
           points=13, lines=1),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.\nI will call you as soon as I will arrive at the airport.",
           "will arrive → arrive / 시간을 나타내는 부사절(as soon as ~)에서는 현재시제가 미래를 대신한다.",
           "시간·조건 부사절 → 현재시제", points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "has discovered → discovered / saved → have saved",
           "in 1928 = 명백한 과거 / Since then → 현재완료",
           level="상", hard=True, points=13, lines=2,
           passage="Penicillin is one of the most important discoveries in medical history. Alexander Fleming has "
                   "discovered it in 1928. Before that, many people had died from simple infections. Since then, "
                   "antibiotics saved millions of lives. Today, however, scientists are worried that bacteria are "
                   "becoming resistant to these drugs."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "By the end of this week, he will have finished the book.", "미래의 특정 시점(by ~)까지 완료 → will have p.p.",
           level="상", points=13, lines=2,
           conditions=["By the end of this week로 시작할 것", "finish, the book을 활용하여 미래완료로 쓸 것"],
           passage="Jake started reading a long novel last week. He reads fifty pages every night. ==이번 주말까지 그는 "
                   "그 책을 다 읽었을 것이다.== Then he will start a new one."),
    ],
}
