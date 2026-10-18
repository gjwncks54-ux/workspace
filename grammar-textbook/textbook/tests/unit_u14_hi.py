"""Unit 19 도치구문 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "도치구문",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "부정어 Little이 앞에 오면 의문문 어순 → did scientists know",
           level="상", points=8,
           passage="Deep in the forest ==ⓐ lives== a rare species of owl. Rarely ==ⓑ do people see== it during the "
                   "day. Only at night ==ⓒ does it come== out to hunt. Little ==ⓓ scientists knew== about its habits "
                   "until recently. Among the owl's favorite foods ==ⓔ are== mice and small insects."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["I have – stands – I realized", "have I – stand – did I realize", "have I – stands – did I realize",
            "I have – stand – did I realize", "have I – stand – I realized"],
           2, "(A) 부정어 도치 (B) 장소 도치, 진짜 주어 two old trees(복수) (C) Not until ~ → 주절 도치",
           level="상", hard=True, points=8,
           passage="Never (A) [I have / have I] seen such a beautiful sunset. On the hill (B) [stand / stands] two "
                   "old trees, glowing in the evening light. Not until I came home (C) [I realized / did I realize] "
                   "that I had left my camera there."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ 진짜 주어 several old coins → were ⓔ 부정어 도치 → will I forget",
           level="상", hard=True, points=8,
           passage="ⓐ Here she comes.\nⓑ Seldom does he complain about anything.\nⓒ In the box was several old "
                   "coins.\nⓓ No sooner had I sat down than the phone rang.\nⓔ Never I will forget your kindness."),
        MC("대화의 빈칸에 들어갈 말로 알맞은 것은?  A: I haven't finished my homework yet.  B: ______ It's too difficult.",
           ["So have I.", "Neither have I.", "Neither I have.", "So I haven't.", "Neither did I."],
           2, "부정문(현재완료)에 동의 → Neither + have + 주어", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["Only then did I understand her feelings.", "Under the table was a sleeping cat.",
            "Little did she know about the plan.", "Here comes the bus.", "Rarely he eats breakfast."],
           5, "부정어 Rarely가 앞에 오면 의문문 어순 → Rarely does he eat breakfast.", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "Only + 부사구가 앞에 오면 도치 → does it become",
           level="상", points=8,
           passage="Our town has a beautiful park. In the middle of the park ==ⓐ stands== a huge fountain. Around "
                   "it ==ⓑ are== many benches. Never ==ⓒ have I seen== such a peaceful place. Rarely ==ⓓ do people "
                   "leave== trash there. Only on weekends ==ⓔ it becomes== crowded."),

        WR("부정어를 문장 맨 앞으로 보내 다시 쓰시오.  I had never seen such a big crowd.",
           "Never had I seen such a big crowd.", "과거완료 → had + S + p.p.", points=13, lines=1),
        WR("Not until로 시작하는 같은 뜻의 문장으로 바꿔 쓰시오.  I didn't know the truth until he told me.",
           "Not until he told me did I know the truth.", "Not until ~ 가 앞으로 → 주절 도치 did + S + 동사원형",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "stand → stands / visitors go → do visitors go",
           "장소 도치의 진짜 주어 an old temple(단수) / 부정어 Rarely → 의문문 어순",
           level="상", hard=True, points=13, lines=2,
           passage="On the top of the mountain stand an old temple. Rarely visitors go there because the path is "
                   "steep. But the view from the temple is amazing. Only after reaching the top do people realize "
                   "why the climb was worth it."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "On the second floor are thousands of books.", "장소 도치 → 장소 표현 + V + S (주어 복수 → are)",
           level="상", points=13, lines=1,
           conditions=["On the second floor로 시작할 것", "thousands of books를 활용할 것"],
           passage="Welcome to our new library! On the first floor, you can find a café and study rooms. ==수천 권의 "
                   "책이 2층에 있다.== Please enjoy your visit."),
    ],
}
