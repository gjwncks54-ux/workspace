"""Unit 07 조동사 실전 TEST (모듈 u16 / ★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "조동사",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  Jake can ______ the guitar very well.",
           ["plays", "play", "playing", "to play", "played"],
           2, "조동사 + 동사원형 (3인칭 단수여도 -s X)", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  You ______ wear a uniform. It's a school rule.",
           ["may", "can", "must", "might", "would"],
           3, "규칙에 따른 의무 → must", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  I will ______ swim next year.",
           ["can", "could", "able to", "be able to", "am able to"],
           4, "조동사는 두 개 연달아 쓸 수 없다 → will be able to", level="기본", points=6),
        MC("대화의 빈칸에 들어갈 말로 알맞은 것은?",
           ["must not", "don't have to", "should", "had better", "can't"],
           2, "도시락이 제공됨 → 가져올 필요 없다 = don't have to (must not은 금지)",
           points=6,
           passage="A: Do I have to bring my own lunch?\nB: No, you ______. Lunch is provided by the school."),
        MC("밑줄 친 부분의 의미로 알맞은 것은?  He ==must have been== very tired.",
           ["그는 매우 피곤해야 했다", "그는 매우 피곤했을 리가 없다", "그는 매우 피곤했을지도 모른다",
            "그는 매우 피곤했어야 했다", "그는 매우 피곤했음에 틀림없다"],
           5, "must have p.p. = ~했음에 틀림없다 (과거에 대한 강한 추측)", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["There would be a big tree in front of my house.", "I used to play soccer after school.",
            "You had better not stay up late.", "She may have missed the bus.", "You must not run in the hallway."],
           1, "would는 과거의 '동작'만 → 과거 상태는 There used to be a big tree ~", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "조동사는 두 개 연달아 X → will be able to visit",
           points=6,
           passage="Yesterday Jake didn't come to school. He ==ⓐ must have been== sick because he looked pale the "
                   "day before. I ==ⓑ should have called== him last night, but I forgot. Today I ==ⓒ will can== "
                   "visit him after school. I ==ⓓ had better== bring him some soup. He ==ⓔ may feel== better soon."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["used to – would – must have been", "would – would – should have been",
            "used to – was used to – must have been", "would – was used to – must have been",
            "used to – would – should have been"],
           1, "(A) 과거 '상태'(be afraid) → used to (B) 과거의 반복 동작 → would (C) 과거에 대한 강한 추측 → must have p.p.",
           level="상", points=6,
           passage="When I was a child, I (A) [used to / would] be afraid of the dark. I (B) [would / was used to] "
                   "sleep with the light on every night. Now I'm not afraid at all. My mom says I (C) [must have "
                   "been / should have been] a very nervous child."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ 조동사는 -s X → must finish ⓔ had better + 동사원형 → had better leave",
           level="상", hard=True, points=6,
           passage="ⓐ She can't have said such a thing.\nⓑ You don't have to hurry. We have plenty of time.\n"
                   "ⓒ He musts finish his homework.\nⓓ I should have studied harder for the test.\n"
                   "ⓔ We had better to leave now."),

        WR("must를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  It is certain that Jake was angry.",
           "Jake must have been angry.", "과거에 대한 강한 추측 → must have p.p.",
           points=7, lines=1),
        WR("can't를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  It is impossible that she forgot your birthday.",
           "She can't have forgotten your birthday.", "과거에 대한 부정 추측 → can't have p.p.",
           points=7, lines=1),
        WR("should를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  I'm sorry that I didn't bring an umbrella.",
           "I should have brought an umbrella.", "과거에 하지 않은 일에 대한 후회 → should have p.p.",
           points=8, lines=1),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  You must not to use your phone during the test.",
           "to use → use / 조동사 뒤에는 동사원형을 쓴다.", "must not + 동사원형 = 금지",
           level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "must go → had to go / will can → will be able to",
           "must의 과거(의무) → had to / 조동사 두 개 연달아 X",
           level="상", hard=True, points=8, lines=2,
           passage="Last weekend, Jake and I went hiking. We should have checked the weather, but we didn't. It "
                   "started to rain heavily, and we must go back down. Jake slipped on a rock. He might have hurt "
                   "his leg, but luckily he was fine. Next time, we will can prepare better."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "It must have rained last night.", "과거(last night)에 대한 강한 추측 → must have p.p.",
           level="상", points=8, lines=1, conditions=["It, rain, last night, must를 활용할 것", "6단어로 쓸 것"],
           passage="The ground is all wet this morning, and there are puddles everywhere. ==어젯밤에 비가 왔음에 "
                   "틀림없다.=="),
    ],
}
