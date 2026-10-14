"""Unit 05 시제 실전 TEST (★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "시제",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  I ______ my homework two hours ago.",
           ["finish", "finished", "have finished", "had finished", "will finish"],
           2, "ago = 명백한 과거 → 과거시제", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  She has lived in Seoul ______ ten years.",
           ["since", "ago", "for", "when", "until"],
           3, "현재완료 계속 + 기간 → for (since는 시점 앞)", level="기본", points=6),
        MC("밑줄 친 부분의 용법이 <보기>와 같은 것은?  <보기> I ==have been== to Jeju twice.",
           ["He ==has== just ==finished== his homework.", "She ==has lost== her key.",
            "We ==have known== each other since 2015.", "I ==have== never ==seen== a ghost.",
            "They ==have gone== to Busan."],
           4, "<보기>와 ④는 경험. ① 완료 ② 결과 ③ 계속 ⑤ 결과", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Call me when you ______ home.",
           ["arrive", "will arrive", "arrived", "arriving", "to arrive"],
           1, "시간 부사절(when ~)은 현재시제가 미래를 대신한다", level="기본", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["I have known her since childhood.", "When did you finish the report?", "Water boils at 100°C.",
            "He has already left the office.", "I have seen the movie last Friday."],
           5, "last Friday = 명백한 과거 → I saw the movie last Friday.", points=6),
        MC("다음 중 어법상 옳은 것은?",
           ["She has been reading for two hours.", "I am knowing the answer.", "When have you met him?",
            "If it will snow tomorrow, we will stay home.", "My teacher said that the sun rose in the east."],
           1, "② 상태동사 → know ③ When은 과거시제 → did you meet ④ 조건 부사절 → snows ⑤ 불변의 진리 → rises",
           points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "Last month = 명백한 과거 → visited",
           points=6,
           passage="My family ==ⓐ moved== to Busan three years ago. Since then, I ==ⓑ have made== many new friends "
                   "here. Last month, my best friend Yuna ==ⓒ has visited== me from Seoul. We ==ⓓ went== to Haeundae "
                   "Beach together. I ==ⓔ have never seen== her so happy before."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "기준점 I arrived(과거)보다 이전에 시작 → had already started",
           level="상", points=6,
           passage="Yesterday was a terrible day. When I ==ⓐ got== to the bus stop, the bus ==ⓑ had already left==. "
                   "I ==ⓒ had to== walk to school. When I arrived, the class ==ⓓ has already started==. My teacher "
                   "asked me why I ==ⓔ was== late."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           2, "옳은 것: ⓐ ⓒ / ⓑ yesterday → lost ⓓ 기준점 came home보다 이전 → had already gone "
              "ⓔ 시간 부사절 → as soon as I finish",
           level="상", hard=True, points=6,
           passage="ⓐ By next year, I will have lived here for ten years.\nⓑ I have lost my phone yesterday.\n"
                   "ⓒ It has been raining since this morning.\nⓓ When I came home, my sister already went to bed.\n"
                   "ⓔ I will call you as soon as I will finish my work."),

        WR("다음 문장을 <조건>에 맞게 바꿔 쓰시오.  I eat lunch.",
           "(1) When she called, I had already eaten lunch. (2) By 1 p.m., I will have eaten lunch.",
           "과거 기준점보다 이전 → had p.p. / by + 미래 시점 → will have p.p.",
           points=7, lines=2,
           conditions=["(1) When she called로 시작하고 already를 넣어 과거완료로 쓸 것",
                       "(2) By 1 p.m.으로 시작하여 미래완료로 쓸 것"]),
        WR("두 문장을 현재완료를 사용하여 한 문장으로 바꿔 쓰시오.\n"
           "I started to learn the guitar three years ago. I still learn it.",
           "I have learned the guitar for three years.",
           "과거에 시작해 지금도 계속 → 현재완료 계속 + for 기간 (have been learning도 정답)",
           points=7, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  그는 런던에 가 버렸다. (그래서 지금 여기 없다)",
           "He has gone to London.", "현재완료 결과: have gone to = 가 버려서 지금 없음 (have been to는 경험)",
           points=8, lines=1, conditions=["go, London을 활용할 것", "현재완료로 쓸 것", "5단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  I have visited the museum when I was in Paris.",
           "have visited → visited / when I was in Paris는 특정 과거시점을 나타내므로 현재완료와 함께 쓸 수 없다.",
           "특정 과거시점 표현 + 과거시제", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "has won → won / will get → gets",
           "Last year = 명백한 과거 / 조건 부사절(if ~)은 현재시제가 미래를 대신",
           level="상", hard=True, points=8, lines=2,
           passage="Mina is my classmate. She has played the piano since she was five. Last year, she has won first "
                   "prize in a national contest. Before the contest, she had practiced for six hours every day. "
                   "Next month, she will perform at a concert if she will get permission from her parents."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "When he arrived at the station, the train had already left.",
           "기준점 arrived(과거)보다 이전에 떠남 → had already left",
           level="상", points=8, lines=2,
           conditions=["When으로 시작할 것", "arrive at, the station, leave, already를 활용할 것"],
           passage="Last Saturday, Jinho planned to visit his grandmother in Gwangju. He woke up late and took a "
                   "taxi, but the traffic was terrible. ==그가 역에 도착했을 때, 기차는 이미 떠났었다.== He had to "
                   "wait two hours for the next one."),
    ],
}
