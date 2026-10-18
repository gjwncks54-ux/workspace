"""Unit 19 도치구문 실전 TEST (★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "도치구문",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  Never ______ such a beautiful view.",
           ["I have seen", "have I seen", "I saw", "seen I have", "did I saw"],
           2, "부정어 Never가 앞으로 → 의문문 어순 (완료형은 have를 앞으로)", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  On the hill ______ an old castle.",
           ["standing", "stand", "stands", "to stand", "does stand"],
           3, "장소 도치 → V + S. 진짜 주어 an old castle(단수) → stands", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  Look! Here ______.",
           ["comes it", "does it come", "come it", "it comes", "it come"],
           4, "주어가 대명사이면 도치하지 않는다 → Here it comes.", level="기본", points=6),
        MC("다음 중 어법상 틀린 것은?",
           ["In the box was many old letters.", "Rarely does she eat breakfast.", "Under the tree sat an old man.",
            "Little did I know about it.", "Never has he been late for school."],
           1, "진짜 주어 many old letters(복수) → were", points=6),
        MC("대화의 빈칸에 들어갈 말로 알맞은 것은?  A: I can't swim very well.  B: ______ I'm afraid of water.",
           ["So can I.", "Neither can I.", "So I can.", "Neither I can.", "Neither can't I."],
           2, "부정문에 동의 → Neither + 조동사 + 주어 (도치)", points=6),
        MC("다음 문장과 의미가 같은 것은?  I didn't realize the truth until I read his letter.",
           ["Not until I read his letter I realized the truth.", "Not until did I read his letter I realized the truth.",
            "Until I read his letter did I realize the truth.", "Not until I read his letter I did realize the truth.",
            "Not until I read his letter did I realize the truth."],
           5, "Not until ~ 가 앞으로 나가면 주절이 도치 → did I realize", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "Only + 부사구가 앞에 오면 도치 → did I realize",
           points=6,
           passage="Last night, I went to a small concert in the park. Around the stage ==ⓐ were== many people. On "
                   "the stage ==ⓑ stood== a young singer with a guitar. Never ==ⓒ had I heard== such a beautiful "
                   "voice. Only after the concert ==ⓓ I realized== that she was my neighbor. Rarely ==ⓔ do I meet== "
                   "such a talented person."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "진짜 주어 two old trees(복수) → grow",
           level="상", points=6,
           passage="My grandfather lives in a small village. In front of his house ==ⓐ is== a big pond. Next to the "
                   "pond ==ⓑ grows== two old trees. Rarely ==ⓒ does he leave== the village. Never ==ⓓ has he been== "
                   "to Seoul. Only on holidays ==ⓔ do we visit== him."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓔ / ⓑ did 뒤 원형 → did I dream ⓓ Only then 뒤 도치 → did I understand",
           level="상", hard=True, points=6,
           passage="ⓐ Here comes the bus.\nⓑ Never did I dreamed that I would win.\n"
                   "ⓒ Among the guests were two famous actors.\nⓓ Only then I understood his words.\n"
                   "ⓔ No sooner had I arrived than it began to rain."),

        WR("다음 문장의 부정어를 문장 맨 앞으로 보내 다시 쓰시오.\n(1) She rarely eats fast food.\n(2) He has never told a lie.",
           "(1) Rarely does she eat fast food. (2) Never has he told a lie.",
           "일반동사 → does + S + 원형 / 완료형 → has + S + p.p.",
           points=7, lines=2),
        WR("장소 표현을 문장 맨 앞으로 보내 다시 쓰시오.  Two cute puppies were in the basket.",
           "In the basket were two cute puppies.", "장소 도치 → V + S (주어가 명사이므로 도치)",
           points=7, lines=1),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  그때서야 나는 내 실수를 깨달았다.",
           "Only then did I realize my mistake.", "Only + 부사가 앞으로 → 의문문 어순 did + S + 원형",
           points=8, lines=1, conditions=["Only then으로 시작할 것", "realize, mistake를 활용할 것", "7단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  Little did I knew about his plan.",
           "knew → know / 부정어 도치에서 조동사 did가 시제를 나타내므로 뒤에는 동사원형을 쓴다.",
           "did + S + 동사원형", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "stand → stands / I have seen → have I seen",
           "진짜 주어 a tall statue(단수) / 부정어 Never가 앞에 오면 의문문 어순",
           level="상", hard=True, points=8, lines=2,
           passage="Our school has a beautiful garden. In the middle of the garden stand a tall statue. Around it are "
                   "many colorful flowers. Never I have seen such a lovely garden. Students often eat lunch there."),
        WR("다음 글의 밑줄 친 문장에서 주어를 찾아 쓰고, 문장 전체를 우리말로 해석하시오.",
           "주어: the paintings of famous local artists / 해석: 2층에는 유명한 지역 화가들의 그림들이 있다.",
           "장소 도치 문장은 동사(are) 뒤에서 진짜 주어를 찾는다",
           level="상", points=8, lines=2,
           passage="Welcome to our town museum! ==On the second floor are the paintings of famous local artists.== "
                   "On the first floor, you can see old tools and clothes from 100 years ago."),
    ],
}
