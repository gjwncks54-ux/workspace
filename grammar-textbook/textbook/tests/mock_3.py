"""고등 실전 모의고사 1회 (mock_3 / 전 범위 Unit 01~20 / 25문항, 객관식 15 / 서술형 10, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "수능형 어법 · 서술형",
    "time": "50분",
    "items": [
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "관계사절 who spend time gardening을 지우면 주어는 people(복수) → feel [Unit 03·13]",
           points=3,
           passage="Urban gardens are becoming popular in many cities around the world. People ==ⓐ living== in "
                   "apartments can grow vegetables on rooftops or balconies. These gardens not only provide fresh "
                   "food but also ==ⓑ help== reduce stress. Studies show that people who spend time gardening "
                   "==ⓒ feels== happier and healthier. In addition, urban gardens give neighbors a chance to meet "
                   "==ⓓ one another==. This is the reason ==ⓔ why== many city governments support such projects."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "in 1912 = 명백한 과거 → hit (현재완료 불가) [Unit 06]",
           points=3,
           passage="The Titanic ==ⓐ was considered== unsinkable when it was built. However, on its first voyage in "
                   "1912, it ==ⓑ has hit== an iceberg and sank. More than 1,500 people ==ⓒ died== in the disaster. "
                   "Experts say many lives ==ⓓ could have been saved== if there had been enough lifeboats. Since "
                   "then, safety rules for ships ==ⓔ have become== much stricter."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "avoid는 동명사만 목적어 → avoid checking [Unit 11]",
           points=3,
           passage="Many students find ==ⓐ it== hard to manage their time. One effective method is ==ⓑ making== a "
                   "to-do list every morning. Writing down tasks helps you ==ⓒ focus== on what is important. "
                   "Experts also advise students to avoid ==ⓓ to check== their phones while studying. ==ⓔ Having "
                   "finished== a task, you can reward yourself with something small."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["that – who – What", "what – whom – That", "that – whom – What", "what – who – That", "that – who – That"],
           1, "(A) 선행사 X + 완전 → that (B) had caught의 주어 자리 → 주격 who (C) 선행사 X + 불완전 → What [Unit 13·14]",
           points=3,
           passage="Scientists have discovered (A) [that / what] some birds can recognize human faces. In one "
                   "experiment, crows remembered the people (B) [who / whom] had caught them and reacted angrily "
                   "whenever they saw them. (C) [What / That] surprised the researchers most was that the crows "
                   "taught this to their young."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["Building – shocked – loving", "Built – shocked – loved", "Built – shocking – loving",
            "Building – shocking – loved", "Built – shocking – loved"],
           5, "(A) 탑이 '지어진' 것 → Built (B) 탑이 충격을 '일으키는' 쪽 → shocking (C) 상징이 '사랑받는' 것 → loved [Unit 12·17]",
           points=3,
           passage="(A) [Built / Building] in 1889, the Eiffel Tower was once the tallest structure in the world. "
                   "Many Parisians found it (B) [shocking / shocked] at first and called it ugly. Today, however, it "
                   "is a symbol (C) [loving / loved] by people all over the world."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["hotter – as – scientists send", "the hottest – than – do scientists send",
            "the hottest – as – do scientists send", "hotter – than – scientists send",
            "the hottest – than – scientists send"],
           2, "(A) of all ~ → 최상급 (B) 비교급 + than (C) 부정어 Rarely → 의문문 어순 [Unit 18·19]",
           points=3,
           passage="Of all the planets in our solar system, Venus is (A) [the hottest / hotter]. It is even hotter "
                   "(B) [than / as] Mercury, which is closer to the sun. Rarely (C) [scientists send / do scientists "
                   "send] probes there because the extreme heat destroys them quickly."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓓ ⓔ / ⓒ 현재 이룰 수 없는 소망 → I wish I could travel [Unit 07·20]",
           level="상", points=3,
           passage="ⓐ If I had known the answer, I would have told you.\nⓑ He must have been sleeping when I called.\n"
                   "ⓒ I wish I can travel around the world.\nⓓ Were I in your position, I would accept the offer.\n"
                   "ⓔ You should have told me earlier; now it's too late."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "neither A nor B → B(schools, 복수)에 수일치 → provide [Unit 02·15]",
           points=3,
           passage="Recycling is important, but many people do it incorrectly. Some put dirty containers in the "
                   "recycling bin, and ==ⓐ others== mix plastic with paper. Each of these mistakes ==ⓑ makes== "
                   "recycling harder. ==ⓒ Although== most people want to help, they don't know the rules. Neither "
                   "the government nor schools ==ⓓ provides== enough education about it. Both clear rules and "
                   "public education ==ⓔ are== necessary."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "사역동사 make + O + 동사원형 → make patients feel [Unit 05]",
           points=3,
           passage="Music therapy is used to help patients ==ⓐ recover== from illness. Therapists have patients "
                   "==ⓑ listen== to calm music or play simple instruments. This can make patients ==ⓒ to feel== "
                   "less anxious. Doctors have also noticed patients ==ⓓ sleep== better after music sessions. Some "
                   "hospitals even allow patients ==ⓔ to choose== their own music."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "find + 가목적어 it + 형용사 + to V → find it important [Unit 16]",
           points=3,
           passage="==ⓐ It== was in 1928 that Alexander Fleming discovered penicillin. He had left some bacteria "
                   "in a dish, and ==ⓑ to his surprise==, mold had killed them. Never ==ⓒ had anyone imagined== "
                   "that mold could be so useful. ==ⓓ It== is thanks to this discovery that millions of lives have "
                   "been saved. Today, doctors find ==ⓔ that== important to use antibiotics carefully."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳은 것끼리 짝지어진 것은?",
           ["ⓐ, ⓑ, ⓒ", "ⓑ, ⓒ, ⓓ", "ⓑ, ⓓ, ⓔ", "ⓐ, ⓒ, ⓔ", "ⓒ, ⓓ, ⓔ"],
           2, "ⓐ 선행사 people(복수) → who work ⓔ advise + O + to V → to take / ⓑ 동명사 주어 → 단수 ⓒ 가목적어 it ⓓ 명사절 that [Unit 05·13·16]",
           level="상", points=4,
           passage="The number of people ==ⓐ who works== from home has increased sharply. Working from home "
                   "==ⓑ saves== time spent on commuting. However, some workers find ==ⓒ it== difficult to separate "
                   "work from personal life. Experts say ==ⓓ that== workers should set clear working hours. They "
                   "also advise workers ==ⓔ taking== regular breaks."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓓ / ⓒ visit의 목적어 없음 → which(that) ⓔ suggest는 4형식 불가 → suggested to me that ~ [Unit 04·13·17·18·19]",
           level="상", hard=True, points=4,
           passage="ⓐ The more you read, the wider your vocabulary becomes.\nⓑ Not until I lost my phone did I "
                   "realize how much I depended on it.\nⓒ This is the place where I want to visit.\nⓓ Having been "
                   "written in a hurry, the report had many errors.\nⓔ She suggested me that I should see a doctor."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["have been damaged – that – will disappear", "have damaged – that – disappear",
            "have been damaged – what – will disappear", "have damaged – what – disappear",
            "have been damaged – that – disappear"],
           1, "(A) 산호초는 '손상된' 대상 → 현재완료 수동 (B) 선행사 the algae + 불완전 → that (C) 조건절은 현재, 주절은 미래 [Unit 06·08·13]",
           level="상", points=4,
           passage="Coral reefs cover less than 1% of the ocean floor, but they are home to about 25% of all marine "
                   "species. Sadly, many reefs (A) [have damaged / have been damaged] by rising sea temperatures. "
                   "When the water becomes too warm, corals lose the tiny algae (B) [that / what] give them their "
                   "color. If ocean temperatures continue to rise, most reefs (C) [disappear / will disappear] by "
                   "2050."),
        MC("다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "학생들이 잠이 '부족한' 능동 → lacking (본동사는 have) [Unit 12]",
           level="상", hard=True, points=4,
           passage="Sleep deprivation is a serious problem among teenagers. Most teenagers need about nine hours of "
                   "sleep, but few of them ==ⓐ get== enough. Staying up late ==ⓑ using== smartphones is one of the "
                   "main causes. The blue light from screens makes it harder for the brain ==ⓒ to fall== asleep. "
                   "Students ==ⓓ lacked== sleep often have trouble concentrating in class. If schools started later, "
                   "students ==ⓔ would get== more sleep."),
        MC("밑줄 친 that의 쓰임이 같은 것끼리 짝지어진 것은?",
           ["ⓐ – ⓑ", "ⓐ – ⓒ", "ⓑ – ⓔ", "ⓒ – ⓓ", "ⓒ – ⓔ"],
           3, "ⓑ ⓔ 선행사 O + 불완전 → 관계대명사 / ⓐ ⓓ 명사절 접속사 / ⓒ 강조구문 [Unit 13·14·16]",
           level="상", points=4,
           passage="ⓐ It is clear ==that== he lied to us.\nⓑ The book ==that== I borrowed was boring.\n"
                   "ⓒ It was Jake ==that== called you last night.\nⓓ I know ==that== she is right.\n"
                   "ⓔ This is the house ==that== my grandfather built."),

        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "If he had followed his doctor's advice last year, he would be healthier now.",
           "과거(last year) 사실의 반대 → 현재(now) 결과 → 혼합가정법 [Unit 20]",
           level="상", points=5, lines=2,
           conditions=["If로 시작할 것", "follow, his doctor's advice, last year, healthier, now를 활용할 것"],
           passage="Jake's doctor told him to exercise and eat less fast food, but he ignored the advice. Now he "
                   "often feels tired. ==그가 작년에 의사의 충고를 따랐더라면, 지금 더 건강할 텐데.=="),
        WR("다음 글을 읽고, 요약문의 빈칸 (A), (B)에 들어갈 말을 <보기>의 단어를 알맞은 형태로 바꿔 쓰시오.\n"
           "<요약문> Children praised for their effort were more willing (A) ______ difficult tasks than children (B) ______ for their intelligence.\n"
           "<보기> try / praise",
           "(A) to try (B) praised", "be willing + to V / 아이들이 '칭찬받은' 것 → 과거분사 후치수식 [Unit 10·12]",
           points=5, lines=1,
           passage="Researchers studied two groups of children. Children in the first group were praised for being "
                   "smart. Children in the second group were praised for working hard. Later, both groups were "
                   "given a very difficult puzzle. The children who had been praised for their effort kept trying "
                   "longer and enjoyed the challenge more."),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "why do leaves change → why leaves change / that → which",
           "간접의문문 어순 / 앞 내용을 받는 계속적 용법에는 that 불가 [Unit 13·14]",
           level="상", hard=True, points=5, lines=2,
           passage="Have you ever wondered why do leaves change color in autumn? Leaves contain a green pigment "
                   "called chlorophyll. In autumn, trees stop producing chlorophyll, that reveals other colors such "
                   "as yellow and orange. This is the reason why we see colorful leaves in the fall."),
        WR("다음 문장을 분사구문으로 바꿔 쓰시오.  As there was no bus service, we had to walk home.",
           "There being no bus service, we had to walk home.", "there 구문의 독립분사구문 → There being ~ [Unit 17]",
           points=5, lines=1),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "It was his grandmother that(who) made him what he is today.",
           "강조구문 It was ~ that + 관계대명사 what(~하는 것) [Unit 13·16]",
           level="상", points=5, lines=2,
           conditions=["It was ~ that 강조구문을 쓸 것", "make, what he is today를 활용할 것"],
           passage="Jake's parents passed away when he was very young, so his grandmother raised him. Now he is a "
                   "successful doctor. ==그를 오늘날의 그로 만든 사람은 바로 그의 할머니였다.=="),
        WR("Only after로 시작하는 같은 뜻의 문장으로 바꿔 쓰시오.  I realized the value of health only after I got sick.",
           "Only after I got sick did I realize the value of health.", "Only + 부사절이 앞으로 → 주절 도치 [Unit 19]",
           points=5, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "feeling → feel / contribute → contributes",
           "to meet, (to) learn, and (to) feel 병렬 / each of ~ → 단수동사 [Unit 02·15]",
           level="상", points=5, lines=2,
           passage="Volunteering offers many benefits. It allows people to meet new friends, learn new skills, and "
                   "feeling useful. Each of these benefits contribute to a happier life. Moreover, volunteers as "
                   "well as the people they help gain a strong sense of community."),
        WR("any other를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  No other student in our class speaks English as fluently as Mina.",
           "Mina speaks English more fluently than any other student in our class.",
           "비교급 + than any other + 단수명사 = 최상급 의미 [Unit 18]", level="상", points=5, lines=1),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He must have gone to bed early.", "과거에 대한 강한 추측 → must have p.p. [Unit 07]",
           level="상", points=5, lines=1, conditions=["must, go to bed, early를 활용할 것", "7단어로 쓸 것"],
           passage="The lights in Jake's room were off all evening, and he didn't answer any of my messages. ==그는 "
                   "일찍 잠자리에 들었음에 틀림없다.=="),
        WR("The painting으로 시작하는 같은 뜻의 문장으로 바꿔 쓰시오.  People believe that the painting was stolen during the war.",
           "The painting is believed to have been stolen during the war.",
           "believe(현재)보다 was stolen(과거)이 이전 → be believed to have been p.p. [Unit 08·10]",
           level="상", points=5, lines=1),
    ],
}
