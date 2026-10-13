from textbook.blocks import *

GOALS = [
    "현재·과거·미래와 완료 시제의 핵심 의미를 표로 정리한다.",
    "현재완료와 과거시제를 시간 표현으로 구별한다.",
    "과거완료는 '과거 기준점'이 있어야 함을 안다.",
]

INTRO = "시제는 **기본 의미부터** 확실히. 완료 시제는 **기준점이 언제인지**만 잡으면 끝납니다."

BLOCKS = [
    ANCHOR("I have just eaten lunch.", "나는 방금 점심을 먹었다.", "eat lunch 하나로 현재 → 과거 → 완료 → 과거완료 → 미래완료를 따라갑니다."),
    TABLE(
        ["시제", "핵심 의미", "필기 메모"],
        [
            ["**현재**", "일상적 습관, 반복, 불변의 진리", "현재 시제는 가장 기본 의미부터 익힌다."],
            ["**과거**", "과거의 일, 역사적 사실", "명확히 끝난 일을 표현한다."],
            ["**미래**", "미래의 일, 의지, 확신", "will은 강한 확신·의지 표현으로도 쓰인다."],
            ["**현재완료** have p.p.", "완료 / 경험 / 결과 / 계속", "yesterday, when I was young 같은 특정 과거시점 표현과 함께 쓰지 않음"],
            ["**과거완료** had p.p.", "과거 기준점보다 더 이전", "연결된 문장에 과거 기준점이 필요"],
            ["**미래완료** will have p.p.", "미래의 특정 시점까지 완료", "by / by the time / when 등과 잘 어울림"],
        ],
        widths=[22, 30, 48],
    ),
    PILGI([
        "현재완료 = 과거의 일이 {{현재}}까지 이어짐.  과거시제 = 과거에 {{끝난}} 일.",
        "현재완료 4용법: 완료 · {{경험}} · 결과 · {{계속}}",
        "과거완료는 반드시 {{과거 기준점}}이 있어야 쓴다.",
        "미래완료 단서: {{by}} / by the time",
    ]),
    CHAIN([
        ("현재", "I **eat** lunch at 12.", "습관"),
        ("과거", "I **ate** lunch an hour ago.", "끝난 일 (ago = 명백한 과거)"),
        ("현재완료", "I **have** just **eaten** lunch.", "지금 막 끝남 → 지금 배부름"),
        ("과거완료", "When she called, I **had** already **eaten** lunch.", "기준점 = she called (과거)"),
        ("미래완료", "By 1 p.m., I **will have eaten** lunch.", "기준점 = by 1 p.m. (미래)"),
    ], title="eat lunch 하나로 시제 따라가기"),
    LINK(7, "Having eaten lunch, I'm full now. — 준동사의 완료형도 '본동사보다 이전'."),
    QUICK([
        "yesterday · ago · last ~ · in 2020 · When ~? → **과거시제** (현재완료 X)",
        "for + 기간 / since + 시점 / just · already · ever · never → **현재완료**",
        "'~했을 때 이미 …했었다' → **had p.p.**",
    ]),

    STEPUP(),
    H("현재완료 4용법"),
    TABLE(
        ["용법", "함께 쓰는 말", "예문"],
        [
            ["완료", "just, already, yet", "I **have** just **finished** my homework."],
            ["경험", "ever, never, before, ~times", "**Have** you ever **been** to Jeju?"],
            ["계속", "for, since, how long", "She **has lived** here since 2015."],
            ["결과", "go, lose, leave", "He **has gone** to London. (지금 없음)"],
        ],
        widths=[12, 32, 56],
    ),
    WARN([
        ("I ~~have seen~~ the movie yesterday.", "I ++saw++ the movie yesterday.", "yesterday = 명백한 과거"),
        ("If it ~~will rain~~ tomorrow, I'll stay home.", "If it ++rains++ tomorrow, …", "시간·조건 부사절은 현재가 미래 대신"),
        ("The teacher said the earth ~~moved~~ around the sun.", "… the earth ++moves++ …", "불변의 진리 → 항상 현재"),
    ]),
    H("진행형 · 완료진행"),
    EX([
        ("I **was taking** a shower when you called.", "과거진행"),
        ("It **has been raining** since this morning.", "현재완료진행: 지금까지 계속 진행 중"),
        ("I ~~am knowing~~ → I **know** the answer.", "상태동사(know, like, have 소유)는 진행형 X"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  I (lost / have lost) my wallet last night.", "lost", "last night"),
            Q("괄호 안에서 알맞은 것을 고르시오.  She has been sick (for / since) last Monday.", "since", "since + 시점"),
            Q("밑줄 친 현재완료의 용법을 쓰시오.  I ==have never seen== such a beautiful sunset.", "경험", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  Call me when you (will arrive / arrive).", "arrive", "시간 부사절"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  When I got home, my brother (already ate / had already eaten) the pizza.",
              "had already eaten", "기준점 got home보다 이전"),
            Q("괄호 안에서 알맞은 것을 고르시오.  By the end of this month, I (will finish / will have finished) the book.",
              "will have finished", "by + 미래 시점"),
            Q("다음 중 어법상 틀린 문장은?", "②", "② ago → 과거시제: I met him two years ago.",
              options=["I have known her since childhood.", "I have met him two years ago.",
                       "Have you ever tried Thai food?", "He has just left the office."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("괄호 안의 표현을 넣어 시제를 바꿔 쓰시오.  I eat lunch. (an hour ago)", "I ate lunch an hour ago.", "", lines=1),
            Q("괄호 안의 표현을 넣어 시제를 바꿔 쓰시오.  I eat lunch. (already, 현재완료)", "I have already eaten lunch.", "", lines=1),
            Q("괄호 안의 표현을 넣어 시제를 바꿔 쓰시오.  I eat lunch. (By 1 p.m., 미래완료)", "By 1 p.m., I will have eaten lunch.", "", lines=1),
            Q("어법상 틀린 부분을 고치시오.  When I was young, I have lived in Daegu.", "have lived → lived",
              "when I was young = 특정 과거시점", lines=1),
            Q("우리말과 같도록 영작하시오.  내가 극장에 도착했을 때, 영화는 이미 시작했었다.",
              "When I arrived at the theater, the movie had already started.", "", lines=1),
        ]),
    ]),
]
