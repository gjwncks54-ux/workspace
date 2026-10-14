"""Unit 04 5형식 심화 / 사역·지각동사 실전 TEST (★★★ → 20문항, 객관식 12 / 서술형 8, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "5형식 심화 / 사역·지각동사",
    "time": "40분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  My parents let me ______ to the concert.",
           ["go", "to go", "going", "gone", "went"],
           1, "사역동사 let + 목적어 + 동사원형", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  The doctor advised him ______ smoking.",
           ["stop", "stopping", "to stop", "stopped", "stops"],
           3, "advise + 목적어 + to V", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  I had my bike ______ yesterday.",
           ["fix", "fixing", "to fix", "fixed", "fixes"],
           4, "자전거는 '수리되는' 대상 → have + 목적어 + p.p.", level="기본"),
        MC("빈칸에 들어갈 말로 알맞지 않은 것은?  I ______ my brother clean his room.",
           ["made", "had", "let", "helped", "got"],
           5, "get은 사역 의미여도 to V → got my brother to clean", level="기본"),
        MC("다음 중 어법상 틀린 것은?",
           ["I heard someone call my name.", "Mom wanted me be home by six.", "She saw the boy crossing the street.",
            "They named the baby Ella.", "He helped me carry the boxes."],
           2, "want + 목적어 + to V → wanted me to be home"),
        MC("다음 중 어법상 옳은 것은?",
           ["I got my sister wash the dishes.", "The teacher made us to write an essay.",
            "I'll have the mechanic check the engine.", "She heard her name calling.", "My boss let me to leave early."],
           3, "① to wash ② write ④ 이름은 '불리는' 대상 → called ⑤ leave"),
        MC("두 문장의 뜻이 같도록 할 때 빈칸에 알맞은 것은?  I made her clean the room. ≒ I got her ______ the room.",
           ["cleaned", "to clean", "clean", "cleaning", "to cleaning"],
           2, "make는 동사원형, get은 to V"),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "사역동사 make + 동사원형 → make him feel",
           passage="My brother's birthday is next week, so my parents are planning a surprise party. Mom asked me "
                   "==ⓐ to keep== it a secret. Dad had the bakery ==ⓑ make== a big chocolate cake. Yesterday, I "
                   "heard Mom ==ⓒ talking== on the phone about the party. She wanted all his friends ==ⓓ to come==. "
                   "I hope the party will make him ==ⓔ to feel== special."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "자전거는 '수리되는' 대상 → get + 목적어 + p.p. (repaired)",
           passage="Last week, my bike broke, so I took it to a repair shop. The man there let me ==ⓐ wait== inside. "
                   "I watched him ==ⓑ fix== the chain carefully. It took only twenty minutes to get my bike "
                   "==ⓒ repair==. He also advised me ==ⓓ to check== the tires every month. His kindness made me "
                   "==ⓔ want== to visit the shop again."),
        MC("빈칸에 공통으로 들어갈 말로 알맞은 것은?  I ______ my hair cut. / I ______ the plumber fix the sink.",
           ["got", "had", "made", "let", "helped"],
           2, "have + O + p.p.(머리가 잘림) / have + O + 동사원형(배관공이 고침). got은 뒤 문장에서 to fix가 필요",
           level="상"),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓑ ⓒ ⓓ / ⓐ 지각동사 능동 → enter ⓔ cause + O + to V → caused people to panic",
           level="상", hard=True,
           passage="ⓐ I saw him to enter the building.\nⓑ He was seen to enter the building.\n"
                   "ⓒ We were made to wait for an hour.\nⓓ She had her purse stolen on the subway.\n"
                   "ⓔ The news caused people panic."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["ask – use – moving", "to ask – use – moving", "to ask – to use – moving",
            "to ask – use – moved", "ask – to use – moved"],
           2, "(A) encourage + O + to V (B) let + O + 동사원형 (C) 곤충이 '움직이는' 중 → 지각동사 + V-ing",
           level="상", hard=True,
           passage="Our science teacher always encourages us (A) [ask / to ask] questions. Last Friday, she let us "
                   "(B) [use / to use] the new microscopes. Through the lens, I watched a tiny insect "
                   "(C) [moving / moved] its legs. It was amazing!"),

        WR("다음 문장을 <조건>에 맞게 바꿔 쓰시오.  I made her clean the room.",
           "(1) I had her clean the room. (2) I got her to clean the room.",
           "have는 동사원형, get은 to V", points=7, lines=2,
           conditions=["(1) have를 사용할 것", "(2) get을 사용할 것"]),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  나는 어제 휴대폰을 수리 받았다.",
           "I got my phone repaired yesterday.", "휴대폰은 '수리되는' 대상 → get + O + p.p.",
           points=6, lines=1, conditions=["get, repair를 활용할 것", "6단어로 쓸 것"]),
        WR("다음 두 문장을 지각동사를 이용하여 한 문장으로 쓰시오.  I saw a man. He was running down the street.",
           "I saw a man running down the street.", "진행 중인 동작 → 지각동사 + O + V-ing",
           points=6, lines=1),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  The coach made us to run around the field ten times.",
           "to run → run / 사역동사 make는 목적격보어로 동사원형을 쓴다.",
           "make·let·have + O + 동사원형", points=6, lines=2),
        WR("다음 문장을 We를 주어로 하는 능동태 문장으로 바꿔 쓰시오.  A man was seen to run down the street.",
           "We saw a man run down the street.", "지각동사 수동태의 to V → 능동태에서는 동사원형",
           points=6, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "use → to use / check → checked",
           "allow + O + to V / 에세이는 '검토되는' 대상 → have + O + p.p.",
           level="상", hard=True, points=7, lines=2,
           passage="Ms. Lee is my favorite teacher. She never makes us feel nervous in class. When I had trouble with "
                   "math, she helped me understand the problems step by step. She also allowed me use her books "
                   "after school. Before the speech contest, she even had my essay check by a native speaker."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "I made her stop crying.", "사역동사 make + O + 동사원형",
           level="상", points=7, lines=1, conditions=["make, stop을 활용할 것", "5단어로 쓸 것"],
           passage="My little sister was crying because her doll was broken. ==나는 그녀가 울음을 멈추게 했다.== "
                   "I told her a funny story, and she finally smiled."),
        WR("다음 문장을 수동태로 바꿔 쓰시오.  My parents let me go to the concert.",
           "I was allowed to go to the concert (by my parents).", "let은 수동태로 쓰지 않고 be allowed to로 바꿔 쓴다",
           level="상", points=7, lines=1),
    ],
}
