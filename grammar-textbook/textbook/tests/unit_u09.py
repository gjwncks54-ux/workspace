"""Unit 09 동명사 실전 TEST (★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "동명사",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  Would you mind ______ the door?",
           ["close", "to close", "closing", "closed", "to closing"],
           3, "mind는 동명사만 목적어", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞지 않은 것은?  I ______ playing soccer after school.",
           ["enjoy", "finished", "gave up", "practiced", "wanted"],
           5, "want는 to부정사만 목적어 → wanted to play", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Don't forget ______ the lights before you leave.",
           ["turn off", "to turn off", "turning off", "turned off", "turns off"],
           2, "앞으로 할 일을 잊지 마라 → forget + to V", level="기본", points=6),
        MC("밑줄 친 부분의 의미로 알맞은 것은?  On the way home, he ==stopped to buy== some coffee.",
           ["커피를 사기 위해 멈췄다", "커피 사는 것을 그만두었다", "커피를 샀던 것을 기억했다",
            "커피를 산 것을 후회했다", "커피를 사려고 애썼다"],
           1, "stop + to V의 to V는 부사적 용법(목적) → ~하기 위해 멈추다", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["I'm looking forward to seeing you.", "This book is worth reading.", "She is used to getting up early.",
            "I couldn't help laughing at his joke.", "He spent all day to play games."],
           5, "spend + 시간 + V-ing → spent all day playing games", points=6),
        MC("다음 문장과 의미가 같은 것은?  I'm sorry that I didn't tell you the truth.",
           ["I regret to tell you the truth.", "I regret not telling you the truth.", "I regret telling you the truth.",
            "I regret not to tell you the truth.", "I don't regret telling you the truth."],
           2, "과거에 하지 않은 일을 후회 → regret + not V-ing (동명사 부정은 not V-ing)", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "feel like + V-ing → felt like giving up",
           points=6,
           passage="Last year, I decided ==ⓐ to learn== the piano. At first, I wasn't used to ==ⓑ practicing== every "
                   "day. Sometimes I felt like ==ⓒ to give up==. But my teacher encouraged me ==ⓓ to keep== trying. "
                   "Now I enjoy ==ⓔ playing== for my family."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "버스에서 이미 웃었던 일을 기억 → remember laughing",
           level="상", points=6,
           passage="I'll never forget ==ⓐ visiting== Gyeongju with my class two years ago. We spent the whole day "
                   "==ⓑ exploring== old temples. On the way back, the bus stopped ==ⓒ to get== gas, and we bought "
                   "some snacks. I remember ==ⓓ to laugh== a lot with my friends on the bus. I'm looking forward to "
                   "==ⓔ going== there again."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓓ / ⓑ consider + V-ing → considering moving ⓔ ~하곤 했다 → used to play",
           level="상", hard=True, points=6,
           passage="ⓐ He denied breaking the window.\nⓑ I'm considering to move to Busan.\n"
                   "ⓒ Remember to lock the door tonight.\nⓓ She is proud of being a nurse.\n"
                   "ⓔ My brother used to playing baseball."),

        WR("두 문장을 forget을 사용하여 한 문장으로 바꿔 쓰시오.\n"
           "I met the famous singer last summer. I will never forget it.",
           "I will never forget meeting the famous singer last summer.", "이미 한 일(과거)을 잊다 → forget + V-ing",
           points=7, lines=2),
        WR("두 문장을 forget을 사용하여 한 문장으로 바꿔 쓰시오.\n"
           "You must send the letter tomorrow. Don't forget it.",
           "Don't forget to send the letter tomorrow.", "앞으로 할 일(미래)을 잊다 → forget + to V",
           points=7, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  이 영화는 두 번 볼 가치가 있다.",
           "This movie is worth watching twice.", "be worth V-ing = ~할 가치가 있다",
           points=8, lines=1, conditions=["worth, watch, twice를 활용할 것", "6단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  She is used to live alone in a big city.",
           "live → living / '~하는 데 익숙하다'는 be used to V-ing이며, 이때 to는 전치사이므로 뒤에 동명사가 온다.",
           "be used to V-ing ≠ used to V(~하곤 했다)", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "stop to smoke → stop smoking / gave up to try → gave up trying",
           "담배를 '끊다' → stop + V-ing / give up은 동명사만 목적어",
           level="상", hard=True, points=8, lines=2,
           passage="My grandfather used to smoke a lot. Last year, his doctor told him to stop to smoke. At first it "
                   "was hard, but he never gave up to try. Now he is healthier, and he enjoys walking in the park "
                   "every morning. He says it was worth the effort."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "I stopped to help her.", "'~하기 위해 멈추다' → stop + to V (부사적 용법)",
           level="상", points=8, lines=1, conditions=["stop, help를 활용할 것", "5단어로 쓸 것"],
           passage="On my way home, I saw an old woman carrying heavy bags. ==나는 그녀를 돕기 위해 멈췄다.== She "
                   "thanked me with a big smile."),
    ],
}
