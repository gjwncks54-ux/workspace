"""Unit 07 조동사 고등 실전 TEST (모듈 u16 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "조동사 (고등)",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "충돌 이후(과거)에 대한 강한 추측 → must have blocked",
           level="상", points=8,
           passage="Many scientists believe that dinosaurs ==ⓐ must have died== out after a huge asteroid hit the "
                   "Earth. The impact ==ⓑ may have caused== giant fires and tsunamis. Dust in the air ==ⓒ must "
                   "block== sunlight for years after the impact, so plants could not grow. Without plants, "
                   "plant-eating dinosaurs ==ⓓ could not survive==. Some scientists say we ==ⓔ should study== "
                   "asteroids more carefully to protect our planet."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["should practice – must be – will can", "should have practiced – must have been – will be able to",
            "should have practiced – must be – will be able to", "should practice – must have been – will can",
            "should have practiced – must have been – will can"],
           2, "(A) 과거에 하지 않은 일에 대한 후회 (B) 시험 때(과거)에 대한 추측 (C) 조동사 연달아 X → will be able to",
           level="상", hard=True, points=8,
           passage="Jake failed his driving test yesterday. He (A) [should practice / should have practiced] more "
                   "before the test. His instructor said he (B) [must be / must have been] too nervous during the "
                   "test. Next time, he (C) [will can / will be able to] do better."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓓ ⓔ / ⓒ would는 과거 '상태'에 쓰지 않는다 → There used to be",
           level="상", hard=True, points=8,
           passage="ⓐ You don't have to finish it today; tomorrow is fine.\nⓑ He can't have seen me; I was in Busan "
                   "then.\nⓒ There would be a bakery on this corner.\nⓓ You had better not tell anyone about it.\n"
                   "ⓔ She need not have bought so much food."),
        MC("다음 문장과 의미가 같은 것은?  It is possible that she missed the bus.",
           ["She must have missed the bus.", "She may have missed the bus.", "She should have missed the bus.",
            "She can't have missed the bus.", "She needn't have missed the bus."],
           2, "과거 일에 대한 약한 추측(~했을지도 모른다) → may have p.p.", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["You must not park here.", "I used to be shy, but now I'm outgoing.", "We will have to wait for an hour.",
            "He must have forgotten our appointment.", "You'd better to take an umbrella."],
           5, "had better + 동사원형 → You'd better take an umbrella.", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "would는 과거의 '동작'만 → 과거 상태는 There used to be",
           level="상", points=8,
           passage="When I was young, my family ==ⓐ used to== spend every summer at my grandparents' farm. I "
                   "==ⓑ would== wake up early to feed the chickens. There ==ⓒ would be== a big apple tree next to "
                   "the house. My grandfather ==ⓓ would== tell me stories under that tree. I ==ⓔ should have "
                   "visited== them more often when they were alive."),

        WR("must를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  I'm sure that Jake left his umbrella at school.",
           "Jake must have left his umbrella at school.", "과거에 대한 강한 확신 → must have p.p.",
           points=13, lines=1),
        WR("should를 사용하여 같은 뜻의 문장으로 바꿔 쓰시오.  I'm sorry that I ate so much last night.",
           "I shouldn't have eaten so much last night.", "과거에 한 일에 대한 후회 → shouldn't have p.p.",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "must leave → must have left / will can → will be able to",
           "어제(과거)에 대한 강한 추측 → must have p.p. / 조동사 두 개 연달아 X",
           level="상", hard=True, points=13, lines=2,
           passage="Mina lost her phone yesterday. It was found in the library this morning. She must leave it there "
                   "after class. She was in such a hurry that she didn't notice it. She will can pick it up after "
                   "school today."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "He should have checked the weather forecast.", "과거에 하지 않은 일에 대한 후회 → should have p.p.",
           level="상", points=13, lines=1, conditions=["should, check, the weather forecast를 활용할 것", "7단어로 쓸 것"],
           passage="Jake didn't bring an umbrella this morning, and now it's raining heavily. ==그는 일기예보를 "
                   "확인했어야 했다.== He has to wait at the station until the rain stops."),
    ],
}
