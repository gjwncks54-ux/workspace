"""Unit 05 5형식 심화 / 사역·지각동사 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "5형식 심화 / 사역·지각동사 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "사역동사 have + O + 동사원형 → have students present",
           level="상", points=8,
           passage="Good teachers do not simply tell students ==ⓐ to memorize== facts. They encourage students "
                   "==ⓑ to ask== questions and let them ==ⓒ explore== ideas on their own. When students see their "
                   "classmates ==ⓓ solve== problems creatively, they become motivated. Teachers also have students "
                   "==ⓔ to present== their findings to the class."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["repair – wear – use", "repaired – wear – to use", "repaired – to wear – to use",
            "repair – to wear – use", "repaired – wear – use"],
           2, "(A) 다리가 '수리되는' 것 → have + O + p.p. (B) make + O + 동사원형 (C) be allowed to V",
           level="상", hard=True, points=8,
           passage="The city had the old bridge (A) [repair / repaired] last year. During the work, engineers made "
                   "workers (B) [wear / to wear] safety gear at all times. Residents were finally allowed "
                   "(C) [use / to use] the bridge again in March."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ cause + O + to V → caused the river to overflow ⓓ 사역 수동태 → was made to clean",
           level="상", hard=True, points=8,
           passage="ⓐ I heard my name called from behind.\nⓑ The heavy rain caused the river overflow.\n"
                   "ⓒ She got her friends to help her move.\nⓓ He was made clean the bathroom.\n"
                   "ⓔ We watched the sun rising over the sea."),
        MC("빈칸에 들어갈 말로 알맞지 않은 것은?  The coach ______ the players to practice harder.",
           ["encouraged", "told", "made", "wanted", "forced"],
           3, "사역동사 make는 목적격보어로 동사원형 → made the players practice", points=8),
        MC("다음 중 어법상 옳은 것은?",
           ["They kept the door locked all night.", "I had the package deliver to my office.",
            "She helped me finding my keys.", "The teacher let us to leave early.",
            "I noticed him to leave the room."],
           1, "문이 '잠긴' 상태 → keep + O + p.p. / ② delivered ③ find(to find) ④ leave ⑤ leave(leaving)", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "cause + O + to V → cause your heart to work",
           level="상", points=8,
           passage="Have you ever had your blood pressure ==ⓐ checked==? Doctors advise adults ==ⓑ to check== it "
                   "regularly. High blood pressure can cause your heart ==ⓒ work== harder than normal. Regular "
                   "exercise helps people ==ⓓ keep== it under control. Simple changes in diet also matter, so don't "
                   "let small habits ==ⓔ ruin== your health."),

        WR("다음 문장을 <조건>에 맞게 같은 뜻의 문장으로 바꿔 쓰시오.  I asked a mechanic to repair my car.",
           "(1) I had a mechanic repair my car. (2) I got my car repaired.",
           "have + O(사람) + 동사원형 / get + O(사물) + p.p.",
           points=13, lines=2,
           conditions=["(1) have와 a mechanic을 사용할 것", "(2) get을 사용하고 my car를 목적어로 쓸 것"]),
        WR("다음 문장을 The man으로 시작하는 수동태로 바꿔 쓰시오.  Neighbors saw the man enter the building at midnight.",
           "The man was seen to enter the building at midnight (by neighbors).", "지각동사 수동태 → 동사원형이 to V로",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "become → to become / to attend → attend",
           "want + O + to V / 사역 make + O + 동사원형",
           level="상", hard=True, points=13, lines=2,
           passage="Many parents want their children become successful. Some of them make their kids to attend "
                   "several academies after school. However, experts warn that too much pressure can cause "
                   "children to lose interest in learning. Instead, parents should let children choose what they "
                   "want to study."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He had his computer checked before the presentation.", "컴퓨터가 '점검되는' 것 → have + O + p.p.",
           level="상", points=13, lines=1,
           conditions=["have, his computer, check, before the presentation을 활용할 것"],
           passage="Jake had an important presentation on Monday. His computer had been slow for weeks. ==그는 "
                   "발표 전에 컴퓨터를 점검받았다.== Everything went smoothly."),
    ],
}
