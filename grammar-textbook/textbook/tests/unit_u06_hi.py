"""Unit 08 수동태 고등 실전 TEST (10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "수동태",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "만리장성은 '방문되는' 대상 → is visited",
           level="상", points=8,
           passage="The Great Wall of China ==ⓐ was built== over many centuries. It ==ⓑ is believed== to be more "
                   "than 20,000 kilometers long. Millions of workers ==ⓒ were involved== in its construction. Today, "
                   "it ==ⓓ visits== by millions of tourists every year. Some parts of the wall ==ⓔ are being "
                   "repaired== to protect them from further damage."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["discovered – has named – is destroying", "was discovered – has been named – is being destroyed",
            "was discovered – has named – is being destroyed", "discovered – has been named – is destroying",
            "was discovered – has been named – is destroying"],
           2, "(A) '발견된' 대상 + last year (B) '이름 붙여진' 대상 → 현재완료 수동 (C) '파괴되고 있는' 대상 → 진행 수동",
           level="상", hard=True, points=8,
           passage="A new species of frog (A) [discovered / was discovered] in the Amazon rainforest last year. It "
                   "(B) [has named / has been named] after the scientist who found it. Unfortunately, its habitat "
                   "(C) [is destroying / is being destroyed] by illegal logging."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓓ / ⓑ happen은 자동사 → happened ⓔ buy는 간접목적어 앞에 for → was bought for me",
           level="상", hard=True, points=8,
           passage="ⓐ The meeting was put off until next week.\nⓑ The accident was happened on the highway.\n"
                   "ⓒ He is said to have been a great athlete.\nⓓ The children were taken care of by their aunt.\n"
                   "ⓔ A gift was bought to me by my uncle."),
        MC("다음 문장과 의미가 같은 것은?  People say that the castle was built in the 12th century.",
           ["The castle is said to be built in the 12th century.",
            "The castle is said to have been built in the 12th century.",
            "It is said that the castle is built in the 12th century.",
            "The castle says to have been built in the 12th century.",
            "It said that the castle was built in the 12th century."],
           2, "say(현재)보다 was built(과거)가 이전 → be said to have been p.p.", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["The bottle was filled with water.", "This song is known to everyone.", "The road will be closed tomorrow.",
            "The room has already been cleaned.", "The book is consisted of ten chapters."],
           5, "consist는 자동사 → 수동태 불가: The book consists of ten chapters.", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           2, "become은 자동사 → 수동태 불가: became",
           level="상", points=8,
           passage="According to legend, coffee ==ⓐ was first discovered== in Ethiopia. A goat herder noticed that "
                   "his goats ==ⓑ were become== energetic after eating certain berries. Later, coffee ==ⓒ was "
                   "introduced== to the Middle East and Europe. Today, more than two billion cups of coffee "
                   "==ⓓ are consumed== every day. Coffee beans ==ⓔ are grown== in more than 70 countries."),

        WR("다음 문장을 두 가지 수동태로 바꿔 쓰시오.  The school offered Jake a scholarship.",
           "Jake was offered a scholarship (by the school). / A scholarship was offered to Jake (by the school).",
           "4형식 → 간접·직접목적어 모두 주어 가능, 직접목적어가 주어면 offer → to", points=13, lines=2),
        WR("다음 문장을 The players로 시작하는 수동태로 바꿔 쓰시오.  The coach made the players run ten laps.",
           "The players were made to run ten laps (by the coach).", "사역동사 수동태 → 동사원형이 to V로",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "has used → has been used / must solve → must be solved",
           "플라스틱은 '사용되는' 대상 → 현재완료 수동 / 문제는 '해결되는' 대상 → 조동사 수동",
           level="상", hard=True, points=13, lines=2,
           passage="Plastic was invented in the early 1900s. Since then, it has used in almost every industry. "
                   "However, most plastic is not recycled. Every year, millions of tons of plastic waste are thrown "
                   "into the ocean, and many sea animals are harmed by it. This problem must solve as soon as "
                   "possible."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "The house is said to be haunted.", "People say that ~ → S + be said to V",
           level="상", points=13, lines=1, conditions=["The house로 시작할 것", "say, haunted를 활용할 것"],
           passage="There is an old empty house at the end of our street. ==사람들은 그 집에 유령이 나온다고 말한다.== "
                   "Nobody goes near it at night."),
    ],
}
