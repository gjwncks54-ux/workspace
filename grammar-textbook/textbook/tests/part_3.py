"""PART 3 준동사 종합 TEST (Unit 07~10 / 20문항, 객관식 12 / 서술형 8, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "Unit 07~10 종합",
    "time": "45분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  I enjoy ______ to music in my free time.",
           ["listen", "to listen", "listening", "listened", "listens"],
           3, "enjoy는 동명사만 목적어", level="기본"),
        MC("빈칸에 들어갈 말로 알맞은 것은?  She hopes ______ a doctor in the future.",
           ["become", "becoming", "became", "to become", "becomes"],
           4, "hope는 to부정사만 목적어 (미래·소망)", level="기본"),
        MC("밑줄 친 부분의 쓰임이 <보기>와 같은 것은?  <보기> My hobby is ==collecting== stamps.",
           ["The baby ==crying== in the room is my cousin.", "I saw him ==running== in the park.",
            "==Swimming== in the sea is fun.", "She is ==reading== a book.", "Who is the boy ==wearing== a cap?"],
           3, "<보기>와 ③은 명사 역할의 동명사. 나머지는 형용사 역할의 현재분사"),
        MC("다음 중 어법상 틀린 것은?",
           ["I'm looking forward to meeting you.", "He decided not to go abroad.", "The broken window was fixed.",
            "It is easy for me to cook ramyeon.", "I don't mind to wait for you."],
           5, "mind는 동명사만 목적어 → I don't mind waiting"),
        MC("다음 문장과 의미가 같은 것은?  I remember that I locked the door.",
           ["I remember to lock the door.", "I remember locking the door.", "I forget locking the door.",
            "I remember lock the door.", "I remembered to lock the door."],
           2, "이미 한 일을 기억 → remember + V-ing"),
        MC("빈칸 (A), (B)에 들어갈 말이 바르게 짝지어진 것은?  The ending of the movie was (A) ______, so everyone in the theater was (B) ______.",
           ["surprising – surprised", "surprised – surprising", "surprising – surprising",
            "surprised – surprised", "surprise – surprised"],
           1, "결말이 놀라움을 '일으키는' 쪽 → -ing / 관객이 '느끼는' 쪽 → p.p."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "개가 두려움을 '느끼는' 쪽 → frightened",
           passage="Last Saturday, I volunteered at an animal shelter. My job was ==ⓐ to feed== the dogs. There "
                   "was a small dog ==ⓑ hiding== under the table. It looked ==ⓒ frightening==, so I sat next to it "
                   "quietly. After a while, it stopped ==ⓓ shaking== and came to me. I'm planning ==ⓔ to visit== it "
                   "again next week."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "지난겨울 이미 함께 한 일을 잊지 않겠다 → forget making",
           passage="I want to tell you about my grandmother. She is good at ==ⓐ making== kimchi. She taught me how "
                   "==ⓑ to make== it last winter. It was not easy, but it was worth ==ⓒ trying==. I'll never forget "
                   "==ⓓ to make== kimchi with her. I hope ==ⓔ to learn== more recipes from her."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["using – tired – using", "to use – tired – using", "using – tiring – to use",
            "to use – tiring – to use", "using – tired – to use"],
           1, "(A) '사용하는 것을' 멈추다 → stop V-ing (B) 내가 피곤함을 느낌 → tired (C) avoid는 동명사만 목적어",
           level="상",
           passage="Many people can't stop (A) [using / to use] their smartphones. Spending too much time on them "
                   "can make you feel (B) [tiring / tired]. Experts advise us to avoid (C) [using / to use] our "
                   "phones for an hour before bed."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "동명사 주어(Walking ~)는 단수 → helps",
           level="상",
           passage="==ⓐ Having== a pet has many benefits. Studies show that people ==ⓑ living== with pets feel less "
                   "lonely. Walking a dog every day ==ⓒ help== you stay healthy. It is also good for children "
                   "==ⓓ to take== care of animals. They learn ==ⓔ to be== responsible."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           2, "옳은 것: ⓐ ⓓ / ⓑ 성격 형용사 foolish → of him ⓒ 본동사는 is → sitting ⓔ play with friends → to play with",
           level="상", hard=True,
           passage="ⓐ I'm sorry for not keeping my promise.\nⓑ It was foolish for him to believe the rumor.\n"
                   "ⓒ The man sat on the bench is my uncle.\nⓓ He seems to have been a famous singer.\n"
                   "ⓔ She has no friends to play."),
        MC("밑줄 친 to부정사의 용법이 같은 것끼리 짝지어진 것은?",
           ["ⓐ – ⓑ", "ⓐ – ⓓ", "ⓑ – ⓒ", "ⓒ – ⓔ", "ⓓ – ⓔ"],
           2, "ⓐ ⓓ 명사를 꾸미는 형용사적 용법 / ⓑ 목적 ⓔ 감정의 원인 → 부사적 / ⓒ 보어 → 명사적",
           level="상", hard=True,
           passage="ⓐ I need something ==to drink==.\nⓑ He went to the store ==to buy== milk.\n"
                   "ⓒ My plan is ==to travel== to Europe.\nⓓ She has a lot of work ==to do==.\n"
                   "ⓔ I was happy ==to hear== the news."),

        WR("밑줄 친 부분을 동명사로 바꿔 문장을 다시 쓰시오.  ==To exercise== every day is good for your health.",
           "Exercising every day is good for your health.", "주어 자리 to부정사 = 동명사 (단수 취급)",
           level="기본", points=6, lines=1),
        WR("두 문장을 분사를 이용하여 한 문장으로 바꿔 쓰시오.  Do you know the girl? She is talking to Mr. Kim.",
           "Do you know the girl talking to Mr. Kim?", "소녀가 '말하고 있는' 능동·진행 → 현재분사 후치수식",
           points=7, lines=1),
        WR("다음 문장을 so ~ that 구문으로 바꿔 쓰시오.  The river was too cold for us to swim in.",
           "The river was so cold that we couldn't swim in it.", "too ~ to V = so ~ that S can't V (that절엔 it 필요)",
           points=6, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  그는 휴대폰을 확인하기 위해 멈췄다.",
           "He stopped to check his phone.", "stop + to V = ~하기 위해 멈추다 (부사적 용법)",
           points=6, lines=1, conditions=["stop, check, phone을 활용할 것", "6단어로 쓸 것"]),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "The documentary was really interesting.", "다큐멘터리가 흥미를 '일으키는' 쪽 → -ing",
           points=7, lines=1, conditions=["documentary, interest, really를 활용할 것", "5단어로 쓸 것"],
           passage="Our class watched a documentary about the ocean. ==그 다큐멘터리는 정말 흥미로웠다.== Now I want "
                   "to be a marine biologist someday."),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  He avoided to answer my question.",
           "to answer → answering / avoid는 동명사만 목적어로 쓰는 동사이다.",
           "mind, enjoy, give up, avoid, finish … + V-ing", level="상", points=7, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "exciting → excited / to cook → cooking",
           "내가 흥분을 '느끼는' 쪽 → p.p. / enjoy는 동명사만 목적어",
           level="상", hard=True, points=7, lines=2,
           passage="Last summer, my family went camping. It was my first time sleeping in a tent. I was so exciting "
                   "that I couldn't sleep. My dad showed me how to make a fire, and I enjoyed to cook sausages over "
                   "it. The stars shining in the sky were amazing."),
        WR("다음 문장을 <조건>에 맞게 바꿔 쓰시오.  It seems that she was sick yesterday.",
           "She seems to have been sick yesterday.", "seems(현재)보다 was(과거)가 이전 → 완료 부정사 to have p.p.",
           level="상", points=6, lines=1, conditions=["She로 시작할 것"]),
    ],
}
