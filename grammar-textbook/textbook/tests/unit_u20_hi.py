"""Unit 15 접속사 / 병렬 고등 실전 TEST (모듈 u20 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "접속사 / 병렬",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "not only A but also B → B(laziness, 단수)에 수일치 → prevents",
           level="상", points=8,
           passage="Regular exercise improves ==ⓐ both== physical and mental health. It helps people sleep better, "
                   "==ⓑ reduce== stress, and feel more energetic. ==ⓒ Although== many people know this, they still "
                   "don't exercise. Not only lack of time but also laziness ==ⓓ prevent== them from exercising. "
                   "Experts suggest that people start small ==ⓔ so that== they can build a lasting habit."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["was – Despite – risk", "were – Although – risky", "were – Despite – risky", "was – Although – risky",
            "were – Despite – risk"],
           3, "(A) neither A nor B → B(the employees) (B) 뒤에 명사구만 → Despite (C) not only 형용사 but also 형용사 → 병렬",
           level="상", hard=True, points=8,
           passage="Neither the manager nor the employees (A) [was / were] satisfied with the new plan. (B) [Despite "
                   "/ Although] the long meeting, they couldn't reach an agreement. Most of them thought the plan "
                   "was not only expensive but also (C) [risk / risky]."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ 병렬 → painting ⓓ 뒤에 S + V → Because",
           level="상", hard=True, points=8,
           passage="ⓐ Either you or he has to go.\nⓑ She enjoys reading, writing, and to paint.\n"
                   "ⓒ The teacher as well as the students was surprised.\nⓓ Because of it was cold, we stayed inside.\n"
                   "ⓔ I like him not because he is rich but because he is kind."),
        MC("빈칸에 들어갈 말로 알맞은 것은?  ______ the traffic jam, we arrived on time.",
           ["In spite of", "Although", "Even though", "Because", "Since"],
           1, "뒤에 명사구만 + 양보 → 전치사 in spite of", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["Both my sister and I are tall.", "He is smart, funny, and kindness.",
            "Not only Jake but also his parents were invited.", "We left early so that we could avoid traffic.",
            "I'll wait until you come back."],
           2, "형용사 병렬 → smart, funny, and kind", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "encourage + O + to share ~ and (to) take → 병렬",
           level="상", points=8,
           passage="Good leaders listen carefully, ==ⓐ communicate== clearly, and ==ⓑ make== fair decisions. They "
                   "focus not on their own success ==ⓒ but on== the success of their team. In a good team, either "
                   "the leader or a team member ==ⓓ is== responsible for each task. Good leaders also encourage "
                   "their team members to share ideas and ==ⓔ taking== risks."),

        WR("as well as를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  Not only the students but also the teacher was moved by the story.",
           "The teacher as well as the students was moved by the story.",
           "not only A but also B = B as well as A (동사는 B인 the teacher에 맞춤)", points=13, lines=1),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.\nMy goals for this year are to read more books and exercising regularly.",
           "exercising → (to) exercise / and로 연결된 보어는 같은 형태(to부정사)로 병렬해야 한다.",
           "and 앞뒤 병렬", points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "Despite → Although (또는 Though, Even though) / is → are",
           "뒤에 S + V → 접속사 / both A and B → 복수동사",
           level="상", hard=True, points=13, lines=2,
           passage="Jake is not only a good student but also a talented athlete. Despite he has a busy schedule, he "
                   "practices soccer every day. He says that soccer teaches him teamwork and how to manage his "
                   "time. Both his coach and his teachers is proud of him."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "She could buy not only a laptop but also a camera.", "not only A but also B: A와 B는 같은 형태(명사구)",
           level="상", points=13, lines=1, conditions=["not only ~ but also를 사용할 것", "buy, laptop, camera를 활용할 것"],
           passage="Mina worked part-time and saved money for a whole year. ==그녀는 노트북뿐만 아니라 카메라도 살 수 "
                   "있었다.== She was very proud of herself."),
    ],
}
