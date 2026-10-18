"""고등 실전 모의고사 2회 (mock_4 / 전 범위 Unit 01~20 / 25문항, 객관식 15 / 서술형 10, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "수능형 어법 · 서술형",
    "time": "50분",
    "items": [
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "10대들이 SNS를 '사용하는' 능동 → using (본동사는 are) [Unit 12]",
           points=3,
           passage="Social media has changed the way people ==ⓐ communicate==. Users can share photos and messages "
                   "==ⓑ instantly== with friends around the world. However, spending too much time online can make "
                   "people ==ⓒ feel== lonely. Studies show that teenagers ==ⓓ used== social media for more than "
                   "three hours a day are more likely to feel anxious. It is important ==ⓔ to balance== online and "
                   "offline activities."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "all of + 복수명사(its members) → 복수동사 work [Unit 02]",
           points=3,
           passage="Honeybees live in large colonies. Each colony ==ⓐ has== one queen and thousands of workers. "
                   "The workers do most of the jobs, and ==ⓑ the others==, called drones, mate with the queen. Most "
                   "of the honey that the bees make ==ⓒ is== stored for winter. Bees communicate with ==ⓓ one "
                   "another== through special dances. A colony can survive only if all of its members ==ⓔ works== "
                   "together."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "과거 기준점(finally learned)보다 이전 → had tried [Unit 06]",
           points=3,
           passage="When I was a child, I ==ⓐ used to== be afraid of water. My parents ==ⓑ have tried== many times "
                   "to teach me to swim before I finally learned at the age of ten. Since then, swimming ==ⓒ has "
                   "been== my favorite sport. If I ==ⓓ hadn't overcome== my fear, I would never have joined the swim "
                   "team. Now I wish I ==ⓔ had started== swimming earlier."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["write – rewrite – displayed", "write – to rewrite – were displayed", "written – to rewrite – were displayed",
            "written – rewrite – displayed", "write – to rewrite – displayed"],
           2, "(A) have + O(사람) + 동사원형 (B) 사역 수동태 → be made to V (C) 에세이는 '전시되는' 대상 [Unit 05·08]",
           points=3,
           passage="Our English teacher had the students (A) [write / written] an essay about their dreams. Some "
                   "students were made (B) [rewrite / to rewrite] their essays several times. At the end of the "
                   "semester, the best essays (C) [displayed / were displayed] in the hallway."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["what – that – in which", "that – what – which", "what – what – in which", "that – that – which",
            "what – that – which"],
           1, "(A) do의 목적어 없음 → what (B) 선행사 X + 완전 → that (C) 뒤가 완전한 절 → 전치사 + 관계대명사 [Unit 13·14]",
           points=3,
           passage="Jake asked his teacher (A) [what / that] he should do to improve his writing. She told him "
                   "(B) [that / what] reading widely was the key. She also recommended a book (C) [which / in which] "
                   "the author explains how to write clearly."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["Although – very – work", "Despite – very – works", "Although – much – work", "Despite – much – works",
            "Despite – much – work"],
           4, "(A) 뒤에 명사구만 → Despite (B) 비교급 강조 → much (C) not only A but also B → B(its heart)에 수일치 [Unit 15·18]",
           points=3,
           passage="(A) [Despite / Although] its small size, the hummingbird is one of the most amazing birds. Its "
                   "heart beats (B) [much / very] faster than a human's. Not only its wings but also its heart "
                   "(C) [work / works] extremely hard to keep it in the air."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓓ / ⓑ 가목적어 it 필요 → found it difficult ⓔ 진짜 주어 several paintings → hang [Unit 16·19]",
           level="상", points=3,
           passage="ⓐ It was careless of you to leave your bag on the bus.\nⓑ I found difficult to answer the "
                   "question.\nⓒ Little did I expect to win the prize.\nⓓ It was not Jake but Mina who solved the "
                   "problem.\nⓔ On the wall hangs several paintings."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "주절 주어 UNICEF가 '지원받는' 것 → Supported [Unit 17]",
           points=3,
           passage="==ⓐ Founded== in 1946, UNICEF helps children in need around the world. ==ⓑ Working== in more "
                   "than 190 countries, it provides food, medicine, and education. ==ⓒ Having helped== millions of "
                   "children, it won the Nobel Peace Prize in 1965. Its staff often work in dangerous areas, "
                   "==ⓓ risking== their own lives. ==ⓔ Supporting== by donations from individuals and governments, "
                   "UNICEF continues its work today."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "전치사 by 뒤 → 동명사 staying [Unit 11]",
           points=3,
           passage="Many people dream of ==ⓐ traveling== around the world. However, they often give up ==ⓑ planning== "
                   "their trips because of money. In fact, it is possible ==ⓒ to travel== cheaply. You can save money "
                   "by ==ⓓ stay== in hostels instead of hotels. It is also a good idea ==ⓔ to book== flights early."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "간접의문문 어순 → where the ship was going [Unit 14]",
           points=3,
           passage="Archaeologists found a 2,000-year-old ship at the bottom of the sea. They believe it ==ⓐ must "
                   "have sunk== during a storm. The ship ==ⓑ may have carried== wine and olive oil. Nobody knows "
                   "exactly ==ⓒ where was the ship going==. ==ⓓ What== the researchers want to find out next is who "
                   "owned the ship. They hope they ==ⓔ will be able to== learn more about ancient trade."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳은 것끼리 짝지어진 것은?",
           ["ⓐ, ⓑ, ⓒ", "ⓑ, ⓒ, ⓔ", "ⓑ, ⓓ, ⓔ", "ⓐ, ⓒ, ⓓ", "ⓒ, ⓓ, ⓔ"],
           2, "ⓐ one of the + 최상급 + 복수명사 → problems ⓓ ways를 꾸미는 형용사적 용법 → to break / ⓑ 복수 ⓒ 계속적 which ⓔ what [Unit 10·13·18]",
           level="상", points=4,
           passage="Plastic pollution is ==ⓐ one of the most serious problem== today. Millions of tons of plastic "
                   "==ⓑ enter== the ocean every year. Sea animals often mistake plastic for food, ==ⓒ which== can "
                   "kill them. Scientists are trying to find ways ==ⓓ breaking== down plastic faster. ==ⓔ What== we "
                   "really need, however, is less plastic in the first place."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ(if 생략 도치) ⓒ ⓓ ⓔ / ⓑ neither A nor B → B(the students) → know [Unit 10·15·17·19·20]",
           level="상", hard=True, points=4,
           passage="ⓐ Should you have any questions, feel free to ask.\nⓑ Neither the teacher nor the students knows "
                   "the answer.\nⓒ Having been invited to the party, she bought a new dress.\nⓓ No sooner had he "
                   "arrived than it started to snow.\nⓔ He is said to have lived in Paris when he was young."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["who – that – Whether", "whom – what – If", "who – what – Whether", "whom – that – If", "who – that – If"],
           1, "(A) walked의 주어 자리 → 주격 who (B) 선행사 X + 완전 → that (C) 주어 자리 명사절 → Whether [Unit 13·14]",
           level="상", points=4,
           passage="Have you ever noticed that you feel more creative after a walk? In one study, people (A) [who / "
                   "whom] walked for a short time came up with more ideas than those who sat at a desk. The "
                   "researchers concluded (B) [that / what] walking increases the flow of ideas. (C) [Whether / If] "
                   "the walk takes place inside or outside does not seem to matter."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "부정어 Never가 앞에 오면 의문문 어순 → should we underestimate [Unit 19]",
           level="상", hard=True, points=4,
           passage="Laughter is often called the best medicine. When we laugh, our bodies ==ⓐ release== chemicals "
                   "that make us feel good. Laughing also helps ==ⓑ lower== blood pressure. People who laugh often "
                   "are ==ⓒ much healthier== than those who rarely laugh. Some hospitals even have clowns "
                   "==ⓓ visit== sick children. Never ==ⓔ we should underestimate== the power of a smile."),
        MC("다음 중 두 문장의 의미가 같은 것은?",
           ["As he is busy, he can't come. = If he were not busy, he could come.",
            "As I didn't know, I didn't call you. = If I knew, I would call you.",
            "I'm sorry I'm not tall. = I wish I am tall.",
            "Without water, nothing could live. = If it had not been for water, nothing could have lived.",
            "He talks like a doctor, but he isn't one. = He talks as if he is a doctor."],
           1, "② 과거 반대 → If I had known, I would have called ③ I wish I were ④ 현재 가정 → If it were not for ⑤ as if he were [Unit 20]",
           level="상", points=4),

        WR("다음 글을 읽고, 요약문의 빈칸 (A), (B)에 들어갈 말을 <보기>의 단어를 알맞은 형태로 바꿔 쓰시오.\n"
           "<요약문> Older adults (A) ______ regularly showed better memory than those who only (B) ______.\n"
           "<보기> walk / stretch",
           "(A) walking (B) stretched", "노인들이 '걷는' 능동 → 현재분사 후치수식 / 관계사절 속 과거시제 동사 [Unit 06·12]",
           points=5, lines=1,
           passage="In a recent study, older adults who walked for forty minutes three times a week showed improved "
                   "memory after a year. Their brains also grew in the area related to memory. In contrast, those "
                   "who only stretched did not show the same improvement."),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "Discovering → Discovered / could explain → could be explained",
           "무덤이 '발견된' 것 → p.p. / 죽음은 '설명되는' 대상 → 조동사 수동 [Unit 08·17]",
           level="상", hard=True, points=5, lines=2,
           passage="Discovering in 1922, the tomb of Tutankhamun was full of treasures. Archaeologists spent ten "
                   "years removing the objects. Many people believed that anyone who entered the tomb was cursed. "
                   "However, scientists say the deaths could explain by natural causes."),
        WR("if를 생략하여 다음 문장을 다시 쓰시오.  If I had known about the traffic, I would have taken the subway.",
           "Had I known about the traffic, I would have taken the subway.", "if 생략 → had + S + p.p. [Unit 20]",
           points=5, lines=1),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "She found it difficult to talk in Korean.", "find + 가목적어 it + 형용사 + to V [Unit 16]",
           points=5, lines=1, conditions=["find, difficult, talk in Korean을 활용할 것", "가목적어 it을 쓸 것"],
           passage="Mina recently moved to Korea from Canada. Her Korean classes are fun, but real conversations are "
                   "another story. ==그녀는 한국어로 대화하는 것이 어렵다는 것을 알게 되었다.=="),
        WR("두 문장을 한 문장으로 바꿔 쓰시오.  Do you think? + Why did she quit her job?",
           "Why do you think she quit her job?", "think류 → 의문사가 맨 앞, 뒤는 S + V (did 사라지고 quit) [Unit 14]",
           points=5, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "forests → forest / protecting → protects",
           "any other + 단수명사 / produces, stores, and protects 병렬 [Unit 15·18]",
           level="상", points=5, lines=2,
           passage="The Amazon is the largest rainforest in the world. It is home to more species than any other "
                   "forests on Earth. The rainforest produces oxygen, stores carbon, and protecting countless "
                   "animals. Sadly, it is shrinking faster than ever."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He got his bike repaired yesterday.", "자전거가 '수리되는' 것 → get + O + p.p. [Unit 05]",
           level="상", points=5, lines=1, conditions=["get, his bike, repair, yesterday를 활용할 것", "6단어로 쓸 것"],
           passage="Jake's bike had a flat tire, so he couldn't ride it to school. ==그는 어제 자전거를 수리받았다.== "
                   "Now he can ride it again."),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  그 손님들 중 일부는 일찍 떠났고, 나머지는 자정까지 머물렀다.",
           "Some of the guests left early, and the others stayed until midnight.",
           "정해진 전체 중 일부 / 나머지 전부 → some ~ the others [Unit 02]",
           level="상", points=5, lines=2, conditions=["Some of the guests로 시작할 것", "stay, midnight을 활용할 것"]),
        WR("다음 대화의 밑줄 친 문장을 at the bookstore를 강조하는 문장으로 바꿔 쓰시오.",
           "It was at the bookstore that I met him.", "It was + 강조 대상(부사구) + that + 나머지 [Unit 16]",
           level="상", points=5, lines=1,
           passage="A: Did you meet Jake at the library yesterday?\nB: No. ==I met him at the bookstore.== We bought "
                   "some comic books together."),
        WR("관계대명사를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  My uncle lives in Jeju, and it is famous for its beautiful beaches.",
           "My uncle lives in Jeju, which is famous for its beautiful beaches.",
           "and + it → 계속적 용법 , which (that 불가) [Unit 13]", level="상", points=5, lines=1),
    ],
}
