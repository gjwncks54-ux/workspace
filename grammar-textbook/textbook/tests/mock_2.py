"""실전 모의고사 2회 (전 범위 / 25문항, 객관식 15 / 서술형 10, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "전 범위 (기본 15단원)",
    "time": "50분",
    "items": [
        MC("밑줄 친 late의 품사가 나머지와 다른 하나는?",
           ["He came home ==late==.", "I woke up ==late== today.", "We had a ==late== lunch.",
            "Don't stay up ==late==.", "She arrived ==late== for class."],
           3, "③은 명사 lunch를 꾸미는 형용사, 나머지는 동사를 꾸미는 부사 [Unit 01]", level="기본", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  The pictures in this book ______ very old.",
           ["is", "are", "was", "has", "be"],
           2, "수식어 in this book을 지우면 주어는 The pictures(복수) → are [Unit 03]", level="기본", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Thank you for ______ me.",
           ["help", "to help", "helped", "helping", "helps"],
           4, "전치사 for 뒤 → 동명사 [Unit 11]", level="기본", points=3),
        MC("다음 중 어법상 틀린 것은?",
           ["This cake tastes sweet.", "She became a famous writer.", "He gave a present to his mom.",
            "The idea sounds great.", "I'll introduce you my friend."],
           5, "introduce는 4형식 불가 → I'll introduce my friend to you. [Unit 04]", points=3),
        MC("다음 문장을 수동태로 바르게 바꾼 것은?  We must protect the environment.",
           ["The environment must protect.", "The environment must be protected.", "The environment must protected.",
            "The environment must being protected.", "The environment is must protected."],
           2, "조동사 수동태 → 조동사 + be + p.p. [Unit 08]", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  I heard my name ______ in the hallway.",
           ["call", "calling", "called", "to call", "to be called"],
           3, "이름은 '불리는' 대상 → 지각동사 + O + p.p. [Unit 05·12]", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  He lent me his bike, ______ was very kind of him.",
           ["which", "that", "what", "who", "where"],
           1, "앞 문장 전체를 받는 계속적 용법 → which (콤마 뒤 that 불가) [Unit 13]", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Not until he lost his health ______ how important it was.",
           ["he realized", "did he realize", "he did realize", "realized he", "does he realized"],
           2, "Not until ~ 가 앞으로 → 주절 도치 did + S + 동사원형 [Unit 19]", points=3),
        MC("대화의 빈칸에 들어갈 말로 알맞은 것은?",
           ["If you knew", "Have you known", "If you know", "Were you known", "Had you known"],
           5, "주절 would have p.p. → If you had known에서 if 생략 → Had you known [Unit 20]",
           points=3,
           passage="A: I didn't know about the exam, so I didn't study at all.\nB: ______ about it, you would have "
                   "studied hard."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "본동사는 is → 주어 자리는 동명사 Sleeping [Unit 09·11]",
           points=3,
           passage="It is not easy ==ⓐ for students== to get enough sleep. Many students stay up late ==ⓑ to study== "
                   "for exams. But ==ⓒ sleep== well is important for memory. Experts say it is better ==ⓓ to sleep== "
                   "at least seven hours. They also advise students not ==ⓔ to use== phones in bed."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "내가 실망을 '느끼는' 쪽 → disappointed [Unit 05·12]",
           level="상", points=4,
           passage="Last Sunday, I had my hair ==ⓐ cut== at a new salon. The hairdresser asked me ==ⓑ to sit== in a "
                   "chair. While she was cutting my hair, I heard someone ==ⓒ singing== in the next room. When I "
                   "looked in the mirror, I was ==ⓓ disappointing== with my new hairstyle. But my friends said it "
                   "made me ==ⓔ look== older."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["which – that – What", "where – that – What", "where – which – That", "which – which – That",
            "where – that – That"],
           2, "(A) I was born은 완전한 절 → where (B) 강조구문 It was ~ that (C) 선행사 X + 불완전 → What [Unit 13·16]",
           level="상", points=4,
           passage="Jeonju is the city (A) [which / where] I was born. It was there (B) [that / which] I learned to "
                   "ride a bike. (C) [What / That] I miss most about Jeonju is my grandmother's cooking."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ when I was a child(특정 과거) → knew ⓔ 문제는 '해결되는' 대상 → has already been solved [Unit 06·08·17]",
           level="상", hard=True, points=4,
           passage="ⓐ Having lived in Japan for five years, she speaks Japanese well.\nⓑ The thief was arrested "
                   "yesterday.\nⓒ I have known him when I was a child.\nⓓ Seen from far away, the rock looks like a "
                   "lion.\nⓔ The problem has already solved."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           1, "부정어 Rarely가 앞에 오면 의문문 어순 → do I get [Unit 19·20]",
           level="상", hard=True, points=4,
           passage="Rarely ==ⓐ I get== angry, but yesterday I did. My little brother broke my favorite cup. If he "
                   "==ⓑ had been== more careful, it wouldn't have broken. On the floor ==ⓒ were== pieces of the cup "
                   "everywhere. I wish he ==ⓓ were== more careful. Never again ==ⓔ will I leave== my things on the "
                   "table."),
        MC("다음 글에서 어법상 틀린 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           1, "틀린 것: ⓒ advise + O + to V → advised me to take (나머지는 모두 옳음) [Unit 05·10·17]",
           level="상", points=4,
           passage="ⓐ Not knowing the way, I asked a police officer for help. ⓑ He was kind enough to show me the "
                   "map. ⓒ He also advised me taking a taxi. ⓓ I was too tired to walk any more. ⓔ Thanking him, I "
                   "got into a taxi."),

        WR("두 문장의 뜻이 같도록 문장을 완성하시오.  She is a fluent speaker of English. → She speaks ______.",
           "She speaks English fluently.", "명사를 꾸미던 형용사 fluent → 동사를 꾸미는 부사 fluently [Unit 01]",
           level="기본", points=5, lines=1),
        WR("다음 문장을 A new jacket으로 시작하는 수동태로 바꿔 쓰시오.  My aunt bought me a new jacket.",
           "A new jacket was bought for me by my aunt.", "buy는 직접목적어만 주어, 간접목적어 앞에 for [Unit 08]",
           points=5, lines=1),
        WR("두 문장을 remember를 사용하여 한 문장으로 바꿔 쓰시오.  I sent the email. I remember it.",
           "I remember sending the email.", "이미 한 일을 기억 → remember + V-ing [Unit 11]",
           points=5, lines=1),
        WR("밑줄 친 부분을 한 단어로 바꿔 문장을 다시 쓰시오.  ==The thing which== surprised me was his answer.",
           "What surprised me was his answer.", "the thing which = what [Unit 13]",
           points=5, lines=1),
        WR("밑줄 친 부분을 강조하는 문장으로 바꿔 쓰시오.  My brother fixed my bike ==yesterday==.",
           "It was yesterday that my brother fixed my bike.", "It was + 강조 대상 + that + 나머지 [Unit 16]",
           points=5, lines=1),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "We saw a panda sleeping in the tree.", "판다가 '자고 있는' 능동·진행 → V-ing [Unit 05·12]",
           points=5, lines=1, conditions=["see, a panda, sleep, in the tree를 활용할 것", "8단어로 쓸 것"],
           passage="Last Saturday, we went to the zoo. ==우리는 나무에서 자고 있는 판다를 보았다.== It was so cute "
                   "that we took many pictures."),
        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  Because I have eaten too much, I feel sick now.",
           "Having eaten too much, I feel sick now.", "먹은 것이 아픈 것보다 먼저 → having p.p. [Unit 09·17]",
           level="상", points=5, lines=1),
        WR("다음 글의 밑줄 친 문장을 as if를 사용하여 한 문장으로 바꿔 쓰시오.",
           "He talks as if he were a doctor.", "현재 사실의 반대 → as if + 과거형 (be는 were) [Unit 20]",
           level="상", points=5, lines=1,
           passage="Jake always gives his friends advice about their health. ==He talks like a doctor, but in fact "
                   "he isn't a doctor.== Sometimes his advice is wrong."),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "stands → stand / finding → to find",
           "장소 도치의 진짜 주어 many tall hotels(복수) / too ~ to V [Unit 10·19]",
           level="상", hard=True, points=5, lines=2,
           passage="Welcome to Haeundae Beach! Along the beach stands many tall hotels. Every summer, the beach is "
                   "full of people enjoying the sea. Never have I seen so many people in one place. It was too "
                   "crowded for us finding a place to sit. Only at night does the beach become quiet."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "When I arrived at school, all the posters had already been put up.",
           "과거 기준점(arrived)보다 이전 + 포스터는 '붙여지는' 대상 → had been p.p. [Unit 06·08]",
           level="상", points=5, lines=2,
           conditions=["When으로 시작할 것", "arrive at school, all the posters, put up, already를 활용할 것",
                       "과거완료 수동태로 쓸 것"],
           passage="Our school festival was held last Friday. I came to school early to help, but I was too late. "
                   "==내가 학교에 도착했을 때, 모든 포스터가 이미 붙여져 있었다.== My friends had worked very hard."),
    ],
}
