"""Unit 12 분사 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "분사 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "결말이 놀라움을 '일으키는' 쪽 → surprising",
           level="상", points=8,
           passage="The documentary ==ⓐ released== last month has become very popular. It tells the story of a girl "
                   "==ⓑ living== in a small village in Africa. Viewers were deeply ==ⓒ moved== by her courage, and "
                   "many found the ending ==ⓓ surprised==. The film has encouraged people to help children "
                   "==ⓔ affected== by poverty."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["disappointing – taking – confused", "disappointed – taken – confusing", "disappointing – taken – confused",
            "disappointed – taking – confused", "disappointing – taking – confusing"],
           1, "(A) 결과가 실망을 일으킴 → -ing (B) 학생들이 시험을 '보는' 능동 → taking (C) 선생님이 혼란을 느낌 → confused",
           level="상", hard=True, points=8,
           passage="The results of the final test were (A) [disappointing / disappointed]. Most of the students "
                   "(B) [taking / taken] the test failed to pass. The teacher, (C) [confusing / confused] by the "
                   "results, decided to review the questions again."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓑ ⓔ / ⓒ 영화가 지루함을 일으킴 → boring ⓓ 문이 '닫힌' 상태 → closed",
           level="상", hard=True, points=8,
           passage="ⓐ I found the window broken.\nⓑ The man standing at the door is my uncle.\n"
                   "ⓒ The movie was so bored that I fell asleep.\nⓓ Leave the door closing, please.\n"
                   "ⓔ We saw a building destroyed by the earthquake."),
        MC("빈칸에 들어갈 말로 알맞은 것은?  There are many people ______ for the bus.",
           ["wait", "waits", "waiting", "waited", "to waiting"],
           3, "사람들이 '기다리는' 능동·진행 → 현재분사 후치수식", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["The lost child was found safe.", "It was an exhausting day.", "She looked frightened.",
            "The language spoken in Brazil is Portuguese.", "I'm interesting in Korean history."],
           5, "내가 흥미를 '느끼는' 쪽 → interested", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "벌이 먹이를 '찾은' 능동 → finding (본동사는 performs)",
           level="상", points=8,
           passage="Bees are ==ⓐ fascinating== insects. A bee ==ⓑ found== a good source of food performs a special "
                   "dance. Other bees ==ⓒ watching== the dance can find the food. Scientists ==ⓓ interested== in "
                   "animal communication have studied this dance for years. The results have been truly "
                   "==ⓔ amazing==."),

        WR("분사를 이용하여 다음 문장을 바꿔 쓰시오.  The bridge which was built in 1900 is still in use.",
           "The bridge built in 1900 is still in use.", "관계대명사 + be 생략 → 과거분사 후치수식",
           points=13, lines=1),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.\nEveryone was exciting about the news that the school trip would be held in Jeju.",
           "exciting → excited / 주어 Everyone(사람)이 흥분을 '느끼는' 쪽이므로 과거분사를 쓴다.",
           "일으키면 -ing, 느끼면 p.p.", points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "frightened → frightening / shocking → shocked",
           "영화가 공포를 '일으키는' 쪽 → -ing / 친구가 충격을 '받은' 쪽 → p.p.",
           level="상", hard=True, points=13, lines=2,
           passage="Last night I watched a horror movie with my friends. It was so frightened that I couldn't sleep. "
                   "The scene showing a ghost walking down a dark hallway was the scariest. My friend, shocking by "
                   "the ending, screamed loudly."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He found his dog sleeping on the sofa.", "개가 '자고 있는' 능동·진행 → 목적격보어 V-ing",
           level="상", points=13, lines=1, conditions=["find, his dog, sleep, on the sofa를 활용할 것", "8단어로 쓸 것"],
           passage="Jake came home late after soccer practice. The house was very quiet. ==그는 그의 개가 소파 위에서 "
                   "자고 있는 것을 발견했다.=="),
    ],
}
