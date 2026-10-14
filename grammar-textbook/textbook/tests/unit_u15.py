"""Unit 15 가정법 실전 TEST (★★★ → 20문항, 객관식 12 / 서술형 8, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "가정법",
    "time": "40분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  If I ______ more time, I would learn to play the guitar.",
           ["have", "had", "will have", "have had", "having"],
           2, "주절 would + 동원 → 가정법 과거, if절은 과거형", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  If she had studied harder, she ______ the test.",
           ["passes", "will pass", "would pass", "would have passed", "had passed"],
           4, "if절 had p.p. → 가정법 과거완료, 주절 would have p.p.", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  I wish I ______ taller.",
           ["am", "be", "were", "will be", "have been"],
           3, "현재 사실의 반대 소망 → I wish + 과거형 (be는 were)", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  ______ you, I wouldn't do that.",
           ["I were", "If I am", "Had I", "Were I", "Am I"],
           4, "If I were you에서 if 생략 → Were I you", level="기본"),
        MC("다음 문장과 의미가 같은 것은?  As I don't know her number, I can't call her.",
           ["If I knew her number, I could call her.", "If I know her number, I can call her.",
            "If I had known her number, I could have called her.", "If I didn't know her number, I couldn't call her.",
            "If I knew her number, I couldn't call her."],
           1, "현재 사실의 반대 → If + 과거형, would/could + 동원 (긍정·부정을 뒤집는다)"),
        MC("다음 문장과 의미가 같은 것은?  Without your help, I couldn't have finished the project.",
           ["If it were not for your help, I couldn't have finished the project.",
            "If it had not been for your help, I couldn't have finished the project.",
            "Were it not for your help, I couldn't have finished the project.",
            "But for your help, I can't finish the project.",
            "Had it been for your help, I couldn't have finished the project."],
           2, "주절 couldn't have p.p. → 과거 가정 → If it had not been for (①③은 현재 가정 형태)"),
        MC("다음 중 어법상 틀린 것은?",
           ["If I were you, I would accept the offer.", "He talks as if he knew everything.",
            "It's time you went to bed.", "If I had eaten breakfast, I wouldn't be hungry now.",
            "If it will rain tomorrow, I will stay home."],
           5, "가정법이 아닌 조건문, 조건 부사절은 현재가 미래 대신 → If it rains tomorrow"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  If I had taken the medicine last night, I ______ better now.",
           ["feel", "would feel", "would have felt", "had felt", "will feel"],
           2, "if절 과거(last night) + 주절 now → 혼합가정법 would + 동원"),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "어제(과거) 사실의 반대 → would have caught",
           passage="Yesterday I missed the school bus. If I ==ⓐ had woken== up earlier, I ==ⓑ would catch== it. "
                   "My mom said, \"If I ==ⓒ were== you, I ==ⓓ would set== an alarm.\" Now I wish I ==ⓔ had listened== "
                   "to her advice earlier."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "현재 사실의 반대 소망 → I wish + 과거형 could cook",
           level="상",
           passage="My friend Jun talks ==ⓐ as if== he were a famous chef. Last week, he cooked pasta for us. If he "
                   "==ⓑ had followed== the recipe, the pasta ==ⓒ would have tasted== better. Honestly, "
                   "==ⓓ had it not been== for the cheese, we couldn't have eaten it. I wish he ==ⓔ can cook== as well "
                   "as he talks."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓒ(혼합가정법) ⓓ / ⓔ 현재 반대 소망 → I wish I had",
           level="상", hard=True,
           passage="ⓐ Had I known the truth, I would have told you.\nⓑ She looks as if she had seen a ghost.\n"
                   "ⓒ If I had saved money, I could buy the bike now.\nⓓ Were it not for water, we couldn't live.\n"
                   "ⓔ I wish I have a younger brother."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["were – had – Had", "am – had – Had", "were – have had – Have", "were – had – Have", "am – have had – Had"],
           1, "(A) 현재 반대 → were (B) 주절 would have p.p. → had p.p. (C) if 생략 도치 → Had I known",
           level="상", hard=True,
           passage="If I (A) [were / am] a bird, I would fly to my grandmother's house right now. Last year, I "
                   "couldn't visit her at all. If I (B) [had / have had] more free time, I would have visited her. "
                   "(C) [Had / Have] I known she was sick, I would have called her every day."),

        WR("다음 두 문장을 각각 if를 생략한 문장으로 바꿔 쓰시오.\n"
           "(1) If I were you, I would apologize to her first.\n(2) If I had known her address, I would have visited her.",
           "(1) Were I you, I would apologize to her first. (2) Had I known her address, I would have visited her.",
           "if 생략 → were / had를 주어 앞으로 (had만 앞으로, known은 그대로)",
           points=7, lines=2),
        WR("다음 문장을 가정법 문장으로 바꿔 쓰시오.  As it is raining, we can't play soccer outside.",
           "If it were not raining, we could play soccer outside.",
           "현재 사실의 반대 → 가정법 과거 (긍정·부정을 뒤집는다, If it weren't raining도 정답)",
           points=6, lines=1),
        WR("다음 문장을 가정법 문장으로 바꿔 쓰시오.  Because I didn't bring my umbrella, I got wet.",
           "If I had brought my umbrella, I wouldn't have gotten wet.",
           "과거 사실의 반대 → 가정법 과거완료 (wouldn't have got wet도 정답)",
           points=6, lines=1),
        WR("I wish를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  I'm sorry that I can't speak English fluently.",
           "I wish I could speak English fluently.", "현재 이룰 수 없는 소망 → I wish + 과거형(can → could)",
           points=6, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  공기가 없다면, 우리는 살 수 없을 것이다.",
           "Were it not for air, we couldn't live.",
           "If it were not for에서 if 생략 → Were it not for",
           points=7, lines=1,
           conditions=["it, air, live를 활용할 것", "if를 생략한 도치 문장으로 쓸 것", "couldn't를 포함하여 8단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.\n"
           "If I had listened to my teacher, I would get a better grade on the last test.",
           "would get → would have gotten / 지난 시험(과거)의 사실과 반대되는 가정이므로 주절도 would have p.p.를 써야 한다.",
           "on the last test → 과거 → 가정법 과거완료", level="상", points=7, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "is → were / have → had",
           "현재 사실의 반대 → as if + 과거형 / I wish + 과거형",
           level="상", hard=True, points=7, lines=2,
           passage="Minji is my best friend. She speaks English as if she is a native speaker. She told me that she "
                   "had lived in Canada for five years. If I had lived abroad like her, I could speak English better "
                   "now. Sometimes I wish I have her talent."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "If I had gone to bed early last night, I wouldn't be tired now.",
           "과거(last night) 사실의 반대 → 현재(now)에 영향 → 혼합가정법",
           level="상", points=6, lines=2,
           conditions=["If로 시작할 것", "go to bed early, last night, tired, now를 활용할 것"],
           passage="Last night I stayed up late playing games. Now I feel so tired in class. ==내가 어젯밤 일찍 "
                   "잤더라면, 지금 피곤하지 않을 텐데.=="),
    ],
}
