"""PART 4 문장의 확장 종합 TEST (Unit 11~13 / 20문항, 객관식 12 / 서술형 8, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "Unit 11~13 종합",
    "time": "45분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  This is the girl ______ won the race.",
           ["who", "whom", "whose", "which", "what"],
           1, "선행사 사람 + 주어가 빠진 절 → 주격 who", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  ______ is important to be honest.",
           ["This", "It", "That", "What", "There"],
           2, "진주어 to be honest를 받는 가주어 It", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  ______ the news, she started to cry.",
           ["Hear", "Heard", "Hearing", "To hearing", "Hears"],
           3, "When she heard the news → 그녀가 '들은' 능동 → Hearing", level="기본"),
        MC("밑줄 친 that의 쓰임이 <보기>와 같은 것은?  <보기> It was in the park ==that== I lost my phone.",
           ["I know ==that== he is honest.", "This is the book ==that== I bought.", "It was Tom ==that== broke the window.",
            "It is true ==that== she moved to Busan.", "He said ==that== he was tired."],
           3, "<보기>와 ③은 It was ~ that 강조구문. ①⑤ 접속사 ② 관계대명사 ④ 가주어 It의 진주어 that절"),
        MC("다음 중 어법상 틀린 것은?",
           ["What I need is your advice.", "This is the place where we first met.", "It was kind of you to help me.",
            "Written in easy English, the book is popular.", "I found difficult to solve the problem."],
           5, "가목적어 it 생략 불가 → I found it difficult to solve the problem."),
        MC("밑줄 친 부분과 의미가 같은 것은?  ==Not knowing what to say==, I kept silent.",
           ["Because I didn't know what to say", "Although I knew what to say", "If I don't know what to say",
            "When I knew what to say", "Unless I knew what to say"],
           1, "말할 것을 몰라서 침묵 → 이유(Because), 분사구문의 not → 부정"),
        MC("빈칸에 공통으로 들어갈 말로 알맞은 것은?  This is the house ___ my grandfather was born. / I'll never forget the city ___ I studied for a year.",
           ["which", "where", "that", "when", "what"],
           2, "뒤 절이 완전 + 장소 선행사 → 관계부사 where"),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "visits의 목적어가 빠진 불완전한 절 → which(that)",
           passage="Sejong is a city ==ⓐ which== was built as a new administrative center. Many government offices "
                   "==ⓑ that== used to be in Seoul moved there. The lake park ==ⓒ where== my family often visits is "
                   "very large. ==ⓓ It== is easy for people to walk around the city. ==ⓔ What== I like most about "
                   "the city is its clean air."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "주절 주어 the cat이 '놀란' 것 → Surprised",
           passage="==ⓐ Having finished== her homework, Sora went out for a walk. ==ⓑ Walking== along the river, she "
                   "saw a cat ==ⓒ sitting== under a bench. ==ⓓ Surprising== by her, the cat ran away. ==ⓔ Feeling== "
                   "sorry, she left some food for it."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["that – Living – where", "what – Living – which", "that – Lived – which", "what – Lived – where",
            "that – Living – which"],
           1, "(A) 강조구문 It was ~ that (B) 할아버지가 '사는' 능동 → Living (C) he fished는 완전한 절 → where",
           level="상",
           passage="It was my grandfather (A) [that / what] taught me how to fish. (B) [Living / Lived] near a "
                   "river, he went fishing almost every day. The river (C) [which / where] he fished is now part "
                   "of a beautiful park."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓒ ⓔ / ⓓ 이유 + 완전한 절 → the reason why(for which)",
           level="상", hard=True,
           passage="ⓐ I have a friend whose father is a firefighter.\nⓑ It was in 2020 that I first met her.\n"
                   "ⓒ Seen from the plane, the city looked like a toy.\nⓓ That's the reason which I left early.\n"
                   "ⓔ He made it clear that he would not come."),
        MC("다음 중 It is[was] ~ that 강조구문을 모두 고른 것은?",
           ["ⓐ, ⓑ", "ⓐ, ⓒ", "ⓑ, ⓓ", "ⓐ, ⓒ, ⓔ", "ⓒ, ⓓ, ⓔ"],
           4, "It was와 that을 지워도 완전한 문장이 남으면 강조구문(ⓐ ⓒ ⓔ). ⓑ ⓓ는 가주어 It + 진주어 that절",
           level="상", hard=True,
           passage="ⓐ It was Mina that called you last night.\nⓑ It is true that he won the prize.\n"
                   "ⓒ It was at the library that I met him.\nⓓ It is important that you exercise regularly.\n"
                   "ⓔ It was yesterday that the package arrived."),

        WR("두 문장을 관계대명사를 사용하여 한 문장으로 바꿔 쓰시오.  I have a cousin. She lives in New York.",
           "I have a cousin who(that) lives in New York.", "She → 주격 관계대명사 who",
           level="기본", points=6, lines=1),
        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  After she had read the letter, she burst into tears.",
           "Having read the letter, she burst into tears.", "편지를 읽은 것이 먼저 → having p.p.",
           points=7, lines=1),
        WR("밑줄 친 부분을 강조하는 문장으로 바꿔 쓰시오.  My dad bought me ==this watch== at the mall.",
           "It was this watch that my dad bought me at the mall.", "It was + 강조 대상 + that + 나머지",
           points=6, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  나는 영어로 일기를 쓰는 것이 재미있다는 것을 알았다.",
           "I found it fun to keep a diary in English.", "find + 가목적어 it + 형용사 + 진목적어 to V",
           points=6, lines=1, conditions=["find, fun, keep a diary, in English를 활용할 것", "가목적어 it을 쓸 것"]),
        WR("다음 대화의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "What I really want is new sneakers.", "선행사 X + want의 목적어 없음 → What이 이끄는 명사절 주어",
           points=7, lines=1, conditions=["what, really, want, new sneakers를 활용할 것", "7단어로 쓸 것"],
           passage="A: Which gift do you want for Christmas?\nB: ==내가 정말 원하는 것은 새 운동화야.=="),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  This is the house which my grandmother lived.",
           "which → where(또는 in which) / lived는 목적어가 필요 없는 자동사여서 뒤 절이 완전하므로 관계부사를 쓴다.",
           "또는 전치사를 남겨 which my grandmother lived in", level="상", points=7, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "Knowing not → Not knowing / buying → to buy",
           "분사구문의 not은 맨 앞 / too ~ for 의미상 주어 + to V (너무 ~해서 …할 수 없다)",
           level="상", hard=True, points=7, lines=2,
           passage="Yesterday I visited a bookstore that has been open for 50 years. It was the owner's grandfather "
                   "who opened it. Built of old wood, the building looked very cozy. The owner showed me a book whose "
                   "cover was made of leather. Knowing not its price, I asked him. It was too expensive for me buying."),
        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  As it was very cold outside, we stayed inside.",
           "It being very cold outside, we stayed inside.", "부사절 주어 it ≠ 주절 주어 we → 주어를 남긴 독립분사구문",
           level="상", points=6, lines=1),
    ],
}
