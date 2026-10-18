"""실전 모의고사 1회 (전 범위 Unit 01~20 / 25문항, 객관식 15 / 서술형 10, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "Unit 01~20 전 범위",
    "time": "50분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞지 않은 것은?  She looked ______ when she heard the news.",
           ["happy", "upset", "calmly", "nervous", "surprised"],
           3, "look(~하게 보이다) 뒤 보어 자리 → 형용사. calmly는 부사 [Unit 01·04]", level="기본", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  He ______ to Canada last year.",
           ["has moved", "moved", "moves", "had moved", "has been moving"],
           2, "last year = 명백한 과거 → 과거시제 [Unit 06]", level="기본", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Every student in the class ______ a tablet PC.",
           ["have", "having", "are having", "to have", "has"],
           5, "every + 단수명사 → 단수동사 has [Unit 02]", level="기본", points=3),
        MC("빈칸 (A), (B)에 들어갈 말이 바르게 짝지어진 것은?  I decided (A) ______ more books. / I gave up (B) ______ sweets.",
           ["to read – eating", "reading – to eat", "to read – to eat", "reading – eating", "read – eat"],
           1, "decide + to V / give up + V-ing [Unit 10·11]", points=3),
        MC("다음 중 어법상 틀린 것은?",
           ["I wonder if he will call me.", "Whether she likes it is not important.", "Do you know where he lives?",
            "I believe what he told me the truth.", "What do you think she wants?"],
           4, "선행사 X + 완전한 절 → 접속사 that: I believe that he told me the truth. [Unit 14]", points=3),
        MC("다음 중 어법상 옳은 것은?",
           ["I had my car wash.", "She let me to use her pen.", "I saw him enter the room.",
            "He got me fix the computer.", "They made us to stay late."],
           3, "① washed ② use ④ to fix ⑤ stay / 지각동사 + O + 동사원형 [Unit 05]", points=3),
        MC("빈칸에 들어갈 말로 알맞은 것은?  The street is all wet. It ______ last night.",
           ["must rain", "must have rained", "should rain", "should have rained", "can't have rained"],
           2, "과거(last night)에 대한 강한 추측 → must have p.p. [Unit 07]", points=3),
        MC("밑줄 친 부분을 강조한 문장으로 알맞은 것은?  Jisu found my wallet ==in the classroom==.",
           ["It was in the classroom what Jisu found my wallet.", "It is the classroom in that Jisu found my wallet.",
            "It was Jisu that found my wallet in the classroom.", "In the classroom it was Jisu found my wallet.",
            "It was in the classroom that Jisu found my wallet."],
           5, "It was + 강조 대상(부사구) + that + 나머지. ③은 Jisu를 강조 [Unit 16]", points=3),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "내가 감탄을 '느끼는' 쪽 → amazed [Unit 12·17]",
           points=3,
           passage="==ⓐ Located== in the heart of Seoul, Gyeongbokgung is a popular place. Visitors ==ⓑ wearing== "
                   "hanbok can enter for free. ==ⓒ Walking== around the palace, you can see many old buildings. I "
                   "was ==ⓓ amazing== by its beauty. ==ⓔ Having visited== it once, I want to go back again."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "부정어 Little이 앞에 오면 의문문 어순 → did I know [Unit 19]",
           points=3,
           passage="In front of the library ==ⓐ stands== a statue of King Sejong. Never ==ⓑ had I seen== such a "
                   "big statue. Little ==ⓒ I knew== that it was so famous. Around it ==ⓓ are== many benches. People "
                   "say, \"Here ==ⓔ it is==, the heart of our city!\""),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "look 뒤 보어 자리 → 형용사 confident [Unit 01·04]",
           level="상", points=4,
           passage="My best friend Yuna ==ⓐ looks like== a model. She is tall and always ==ⓑ looks confidently==. "
                   "Her dream is ==ⓒ to become== a designer. Yesterday she showed me ==ⓓ the sketches== she made. "
                   "They made me ==ⓔ want== to draw too."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["built – has been – closing", "was built – was – to close", "was built – has been – to close",
            "built – was – closing", "was built – has been – closing"],
           3, "(A) 다리는 '지어진' 대상 (B) Since then → 현재완료 (수동) (C) decide + to V [Unit 06·08·10]",
           level="상", points=4,
           passage="The old bridge in my town (A) [built / was built] 100 years ago. Since then, it (B) [has been / "
                   "was] repaired many times. Last month, the city decided (C) [closing / to close] it for safety."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓒ ⓓ / ⓔ the way와 how는 함께 쓰지 않는다 [Unit 13·17]",
           level="상", hard=True, points=4,
           passage="ⓐ This is the restaurant where my parents first met.\nⓑ Feeling hungry, I ordered a big pizza.\n"
                   "ⓒ Everything that he said was true.\nⓓ Compared with his brother, he is quiet.\n"
                   "ⓔ I don't like the way how he talks."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "주절 would + 동원 → 가정법 과거, if절은 과거형 had [Unit 16·20]",
           level="상", hard=True, points=4,
           passage="Our teacher told us, \"It is important ==ⓐ for you== to read every day.\" At first, I found "
                   "==ⓑ it== boring to read long books. But it was a mystery novel ==ⓒ that== changed my mind. Now "
                   "I wish I ==ⓓ had started== reading earlier. If I ==ⓔ have== more time, I would read a book "
                   "every day."),
        MC("다음 글에서 어법상 틀린 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           2, "틀린 것: ⓒ enjoy + V-ing → enjoy learning ⓔ 내가 흥미를 느낌 → interested [Unit 09·11·12]",
           level="상", points=4,
           passage="ⓐ Learning a new language is not easy. ⓑ It takes a lot of time to master it. ⓒ But many "
                   "people enjoy to learn new words. ⓓ I want to visit Spain someday to use my Spanish. ⓔ I'm "
                   "interesting in Spanish culture these days."),

        WR("Although를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  Despite the bad weather, we enjoyed the trip.",
           "Although the weather was bad, we enjoyed the trip.", "전치사 despite + 명사구 → 접속사 although + S + V [Unit 15]",
           level="기본", points=5, lines=1),
        WR("다음 문장을 수동태로 바꿔 쓰시오.  Someone stole my bike last night.",
           "My bike was stolen last night.", "과거 수동 was + p.p. / 막연한 행위자 someone은 생략 [Unit 08]",
           points=5, lines=1),
        WR("두 문장을 <조건>에 맞게 한 문장으로 바꿔 쓰시오.  The concert started. Then we arrived at the hall.",
           "When we arrived at the hall, the concert had already started.",
           "과거 기준점(arrived)보다 먼저 일어난 일 → had p.p. [Unit 06]",
           points=5, lines=2, conditions=["When으로 시작할 것", "already를 넣어 과거완료로 쓸 것"]),
        WR("No other로 시작하는 같은 뜻의 문장으로 바꿔 쓰시오.  Mina is the most diligent student in our class.",
           "No other student in our class is more diligent than Mina.", "No other + 단수명사 + 비교급 than [Unit 18]",
           points=5, lines=1),
        WR("두 문장을 관계대명사를 사용하여 한 문장으로 바꿔 쓰시오.  I have a friend. Her father is a famous chef.",
           "I have a friend whose father is a famous chef.", "Her → 소유격 관계대명사 whose [Unit 13]",
           points=5, lines=1),
        WR("다음 글의 밑줄 친 부분을 분사구문으로 바꿔 문장 전체를 다시 쓰시오.",
           "Having drunk too much coffee, I stayed awake until 3 a.m.",
           "커피를 마신 것이 먼저 → having p.p. (Drinking too much coffee, ~도 정답) [Unit 17]",
           points=5, lines=1,
           passage="Last night, I couldn't sleep at all. ==Because I had drunk too much coffee==, I stayed awake "
                   "until 3 a.m. I'll never drink coffee in the evening again."),
        WR("가주어 It을 사용하여 다음 문장을 바꿔 쓰시오.  To solve this puzzle in five minutes is impossible for me.",
           "It is impossible for me to solve this puzzle in five minutes.", "긴 to부정사 주어 → 가주어 It + 진주어 [Unit 16]",
           level="상", points=5, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "exciting → excited / to feed → feeding",
           "동생이 흥분을 '느끼는' 쪽 → p.p. / 이미 한 일을 잊다 → forget V-ing [Unit 11·12]",
           level="상", hard=True, points=5, lines=2,
           passage="Last weekend, my family visited a farm. My little sister was very exciting to see the cows. The "
                   "farmer let us feed the animals. I'll never forget to feed a baby goat that day. It was a really "
                   "amazing experience."),
        WR("다음 대화의 밑줄 친 문장을 if를 생략한 문장으로 바꿔 쓰시오.",
           "Had I not been sick, I would have come.", "if 생략 → Had + S + not + p.p. [Unit 20]",
           level="상", points=5, lines=1,
           passage="A: Why didn't you come to my birthday party?\nB: I'm sorry. I was sick. ==If I hadn't been sick, I "
                   "would have come.=="),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "My mom made me clean my room.", "사역동사 make + O + 동사원형 [Unit 05]",
           level="상", points=5, lines=1, conditions=["make, clean, my room을 활용할 것", "7단어로 쓸 것"],
           passage="My room was really messy because I hadn't cleaned it for weeks. ==엄마는 내가 방을 청소하게 "
                   "하셨다.== It took me three hours."),
    ],
}
