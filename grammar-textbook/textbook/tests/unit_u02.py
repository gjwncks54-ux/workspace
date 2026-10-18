"""Unit 03 구와 절 / 문장성분 실전 TEST (★ → 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "구와 절 / 문장성분",
    "time": "20분",
    "items": [
        MC("밑줄 친 부분이 '절'인 것은?",
           ["I lost my umbrella ==on the bus==.", "==To learn English== is fun.", "Look at the girl ==with long hair==.",
            "I left early ==because I was tired==.", "He left the room ==in a hurry==."],
           4, "주어 + 동사(I was)가 있으면 절. 나머지는 주어 + 동사가 없는 구",
           level="기본", points=8),
        MC("밑줄 친 부분의 문장성분이 나머지와 다른 하나는?",
           ["My dream is ==a doctor==.", "She became ==a famous singer==.", "He met ==a doctor== yesterday.",
            "The man looked ==tired==.", "Her voice sounds ==sweet==."],
           3, "③은 He ≠ a doctor → 목적어. 나머지는 주어를 설명하는 보어",
           level="기본", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["The box of old books is heavy.", "The students in this class is very kind.",
            "One of my friends lives in Busan.", "The keys on the table are mine.",
            "The number of cars has increased."],
           2, "수식어 in this class를 지우면 주어는 The students(복수) → are",
           points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 문장성분이 나머지 넷과 다른 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "ⓑ He = a pilot → 보어. 나머지는 동작의 대상 → 목적어",
           points=8,
           passage="My uncle loves ==ⓐ airplanes==. He became ==ⓑ a pilot== at the age of 25. Now he flies "
                   "==ⓒ big planes== all over the world. Last month, he visited ==ⓓ Paris== and bought "
                   "==ⓔ a small gift== for me."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "주어는 One(단수) → helps. of the teachers는 수식어",
           level="상", points=8,
           passage="The students in my class ==ⓐ are== planning a school festival. Each of the groups ==ⓑ has== a "
                   "different job. The posters on the wall ==ⓒ were== made by Minho's group. The food from the "
                   "parents ==ⓓ looks== delicious. One of the teachers ==ⓔ help== us every day."),
        MC("다음 중 밑줄 친 부분이 수식어(M)인 것의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "수식어: ⓐ ⓒ ⓔ (빼도 문장 성립) / ⓑ is의 보어 ⓓ know의 목적어",
           level="상", hard=True, points=8,
           passage="ⓐ She left the room ==in a hurry==.\nⓑ My hobby is ==to read books==.\n"
                   "ⓒ I was very tired ==after the long trip==.\nⓓ I know ==that he is honest==.\n"
                   "ⓔ He came home ==late== last night."),

        WR("밑줄 친 부분의 문장성분을 각각 쓰고, 그렇게 판단한 이유를 쓰시오.\n"
           "ⓐ My English teacher is ==kind==.\nⓑ My English teacher loves ==music==.",
           "ⓐ 보어(C): teacher = kind / ⓑ 목적어(O): teacher ≠ music (동작의 대상)",
           "주어와 같으면(=) 보어, 다르면(≠) 동작의 대상인 목적어",
           points=13, lines=2),
        WR("밑줄 친 구를 같은 뜻의 절로 바꿔 문장을 다시 쓰시오.  I like the girl ==with long hair==.",
           "I like the girl who has long hair.", "형용사 역할의 구 with long hair → 형용사 역할의 절 who has long hair",
           points=13, lines=1, conditions=["who를 사용할 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.\n"
           "The cookies in the jar on the kitchen table is for the guests.",
           "is → are / 수식어 in the jar on the kitchen table을 지우면 주어는 The cookies(복수)이다.",
           "동사 바로 앞 명사(table)가 아니라 진짜 주어에 수일치",
           points=13, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "take → takes / are → is",
           "주어 The trip(단수) → takes / 주어 One(단수) → is",
           level="상", hard=True, points=13, lines=2,
           passage="My best friend Jiho lives in Daegu. The trip from Seoul to Daegu take about two hours by train. "
                   "Jiho and I talk on the phone every night. One of his hobbies are collecting old coins. He always "
                   "keeps his coins in a small wooden box."),
    ],
}
