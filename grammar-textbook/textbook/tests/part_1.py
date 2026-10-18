"""PART 1 문장의 뼈대 종합 TEST (Unit 01~05 / 20문항, 객관식 12 / 서술형 8, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "Unit 01~05 종합",
    "time": "45분",
    "items": [
        MC("밑줄 친 fast의 품사가 나머지와 다른 하나는?",
           ["He is a ==fast== learner.", "She drives too ==fast==.", "The train runs very ==fast==.",
            "Don't eat so ==fast==.", "He swims ==fast==."],
           1, "①은 명사 learner를 꾸미는 형용사, 나머지는 동사를 꾸미는 부사", level="기본"),
        MC("밑줄 친 부분의 문장성분이 <보기>와 같은 것은?  <보기> The soup tastes ==salty==.",
           ["I bought ==a new phone==.", "He gave me ==a pen==.", "She became ==a lawyer==.",
            "We arrived ==late==.", "I met ==her== yesterday."],
           3, "<보기>와 ③은 주어를 설명하는 보어(C). ①②⑤ 목적어 ④ 수식어", level="기본"),
        MC("빈칸에 들어갈 말로 알맞지 않은 것은?  My mom ______ me to clean my room.",
           ["told", "asked", "wanted", "made", "allowed"],
           4, "사역동사 make는 목적격보어로 동사원형 → made me clean"),
        MC("다음 문장을 3형식으로 바르게 바꾼 것은?  Dad bought me a new bike.",
           ["Dad bought a new bike to me.", "Dad bought a new bike for me.", "Dad bought for me a new bike.",
            "Dad bought me for a new bike.", "Dad bought a new bike of me."],
           2, "buy는 3형식 전환 시 for"),
        MC("다음 중 어법상 옳은 것은?",
           ["The cookies on the plate is delicious.", "She looked sadly after the game.", "He made me to wait outside.",
            "We discussed about the plan.", "I had my hair cut yesterday."],
           5, "① 주어 cookies → are ② 보어 → sad ③ wait ④ discussed the plan ⑤ 머리가 '잘린' → have + O + p.p."),
        MC("다음 중 5형식 문장을 모두 고른 것은?",
           ["ⓐ, ⓑ", "ⓑ, ⓒ", "ⓑ, ⓒ, ⓔ", "ⓐ, ⓓ, ⓔ", "ⓒ, ⓓ, ⓔ"],
           3, "ⓑ her = happy ⓒ 사역 + 동사원형 ⓔ him = captain → 5형식 / ⓐ 4형식 ⓓ 3형식",
           passage="ⓐ I made her a doll.\nⓑ I made her happy.\nⓒ I made her clean the room.\n"
                   "ⓓ I made a doll for her.\nⓔ They elected him captain."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "사역 make + O + 동사원형 feel 뒤 보어 자리 → 형용사 happy",
           passage="Last weekend, I helped my grandmother ==ⓐ plant== flowers in her garden. The garden looked "
                   "==ⓑ beautiful== after we finished. She made me ==ⓒ a cup of tea== and told me ==ⓓ an interesting "
                   "story== about her childhood. It made me feel ==ⓔ happily==."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "수식어 on the top shelf를 지우면 주어는 The book(단수) → was",
           passage="The members of our book club ==ⓐ meet== every Friday. Each member ==ⓑ chooses== a book to "
                   "share. The book on the top shelf ==ⓒ were== recommended by our teacher. Reading books with "
                   "friends ==ⓓ is== a lot of fun. One of my favorite books ==ⓔ is== about space."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "get은 사역 의미여도 to V → got my sister to check",
           level="상",
           passage="My older sister wanted me ==ⓐ to help== her with her science project. She had me "
                   "==ⓑ collect== some leaves in the park. While I was working, I watched birds ==ⓒ flying== over "
                   "the lake. When I came home, I got my sister ==ⓓ check== the leaves. She let me ==ⓔ use== her "
                   "microscope."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["sad – us the situation – keep", "sad – the situation to us – to keep",
            "sadly – the situation to us – to keep", "sadly – us the situation – keep",
            "sad – the situation to us – keep"],
           2, "(A) 5형식 목적격보어 → 형용사 (B) explain은 4형식 불가 → explain A to B (C) ask + O + to V",
           level="상",
           passage="Yesterday our school's old gym closed. The news made everyone (A) [sad / sadly]. In the "
                   "morning assembly, the principal explained (B) [us the situation / the situation to us] calmly. "
                   "She asked us (C) [keep / to keep] calm because a new gym would open next year."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ 지각동사 능동 → knock(knocking) ⓓ reach는 타동사 → reached the station",
           level="상", hard=True,
           passage="ⓐ He looks like his father.\nⓑ I heard someone to knock on the door.\nⓒ She found the box "
                   "empty.\nⓓ They reached to the station at noon.\nⓔ My parents let me stay up late."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 옳은 것끼리 짝지어진 것은?",
           ["ⓐ, ⓑ", "ⓐ, ⓒ, ⓔ", "ⓑ, ⓓ", "ⓒ, ⓓ, ⓔ", "ⓐ, ⓑ, ⓒ, ⓔ"],
           2, "ⓑ 동사 greets를 꾸밈 → warmly ⓓ ask + O + to V → to join / ⓐ -ly 형용사 ⓒ 자전거가 수리됨 → p.p. ⓔ make + O + 동사원형",
           level="상", hard=True,
           passage="Jimin is a ==ⓐ friendly== student. She always greets people ==ⓑ warm==. Yesterday she got "
                   "her bike ==ⓒ repaired==. She also asked her friends ==ⓓ join== her volunteer club. Her kindness "
                   "makes everyone ==ⓔ smile==."),

        WR("다음 문장을 3형식으로 바꿔 쓰시오.  Can you show me your ID card?",
           "Can you show your ID card to me?", "show는 3형식 전환 시 to",
           level="기본", points=6, lines=1),
        WR("다음 문장을 <조건>에 맞게 바꿔 쓰시오.  My mom said to me, \"Clean your room.\"",
           "(1) My mom told me to clean my room. (2) My mom made me clean my room.",
           "tell + O + to V / 사역 make + O + 동사원형",
           points=7, lines=2, conditions=["(1) told를 사용할 것", "(2) made를 사용할 것"]),
        WR("다음 문장에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.  The flowers in the vase smells sweetly.",
           "smells → smell / sweetly → sweet",
           "주어 The flowers(복수) / 감각동사 smell 뒤 보어 → 형용사",
           points=6, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  나는 그 시험이 쉽다는 것을 알았다.",
           "I found the test easy.", "find + O + 형용사(목적격보어) → 5형식",
           points=6, lines=1, conditions=["find, test, easy를 활용할 것", "5단어로 쓸 것"]),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "I heard someone call my name.", "지각동사 hear + O + 동사원형 (calling도 정답)",
           points=7, lines=1, conditions=["hear, someone, call, my name을 활용할 것", "6단어로 쓸 것"],
           passage="Last night, I couldn't sleep. ==나는 누군가 내 이름을 부르는 것을 들었다.== But when I opened the "
                   "door, nobody was there."),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "realistically → realistic / display → displayed",
           "look 뒤 보어 → 형용사 / 사진이 '전시되는' 대상 → have + O + p.p.",
           level="상", points=7, lines=2,
           passage="My uncle is a photographer. He travels around the world and takes beautiful pictures. Last "
                   "year, he sent a photo book to me. In the book, there was a picture of a lion. It looked so "
                   "realistically that I felt scared. He also had his photos display at a gallery in Seoul."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "So I got an expert to fix it.", "get + O + to V (전문가가 직접 고침 → 능동)",
           level="상", hard=True, points=7, lines=1,
           conditions=["So로 시작할 것", "get, an expert, fix, it을 활용할 것"],
           passage="My computer suddenly stopped working last week. I couldn't fix it by myself. ==그래서 나는 "
                   "전문가에게 그것을 고치게 했다.== Now it works perfectly."),
        WR("다음 문장을 S / V / O / C / M으로 끊어 표시하고, 문장의 형식을 쓰시오.\n"
           "The students in the classroom kept the windows open during the class.",
           "The students in the classroom (S) / kept (V) / the windows (O) / open (C) / during the class (M) → 5형식",
           "the windows = open → 목적격보어 / 전치사구 during the class는 수식어",
           level="상", points=6, lines=2),
    ],
}
