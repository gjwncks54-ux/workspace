from textbook.blocks import *

GOALS = [
    "기본·진행·완료 시제의 형태와 의미를 구분한다.",
    "현재완료의 4가지 용법을 이해하고 과거시제와 구분한다.",
    "과거완료·미래완료를 시간 순서에 맞게 쓸 수 있다.",
]

INTRO = "시제는 **'언제' 일어난 일인지**와 **'어떤 상태'(진행·완료)인지**를 동사 형태로 나타냅니다. 3개의 시간(현재·과거·미래) × 4개의 모습(기본·진행·완료·완료진행) = 12시제로 정리됩니다."

BLOCKS = [
    TABLE(
        ["", "현재", "과거", "미래"],
        [
            ["**기본**", "do / does", "did", "will do"],
            ["**진행**", "am/is/are doing", "was/were doing", "will be doing"],
            ["**완료**", "have/has done", "had done", "will have done"],
            ["**완료진행**", "have/has been doing", "had been doing", "will have been doing"],
        ],
        widths=[16, 28, 28, 28], center=[0, 1, 2, 3], caption="12시제 한눈에 보기 (동사 do 기준)",
    ),

    H("1. 기본 시제"),
    TABLE(
        ["시제", "핵심 의미", "예문"],
        [
            ["**현재**", "습관·반복, 현재 상태, 불변의 진리", "I **get up** at 7. / Water **boils** at 100℃."],
            ["**과거**", "과거에 끝난 일, 역사적 사실", "Columbus **discovered** America in 1492."],
            ["**미래**", "미래의 일, 의지, 예측", "I **will call** you tonight. / It **is going to** rain."],
        ],
        widths=[14, 36, 50],
    ),
    WARN([
        ("Our teacher said that the earth ~~moved~~ around the sun.", "...the earth ++moves++ around the sun.",
         "불변의 진리는 시제 일치와 상관없이 항상 현재시제"),
        ("If it ~~will rain~~ tomorrow, I'll stay home.", "If it ++rains++ tomorrow, I'll stay home.",
         "시간·조건 부사절(when, if, before…)에서는 현재가 미래를 대신함"),
    ]),

    H("2. 진행 시제  be + V-ing"),
    P("특정 시점에 **진행 중인 동작**을 나타냅니다. 단, 상태·감정·소유·인식 동사(know, like, want, have(소유), belong, resemble 등)는 진행형으로 쓰지 않습니다."),
    EX([
        ("I **was taking** a shower when you called.", "네가 전화했을 때 나는 샤워 중이었다. (과거진행)"),
        ("This time tomorrow, I **will be flying** to Paris.", "내일 이맘때 나는 파리로 날아가고 있을 것이다. (미래진행)"),
        ("I ~~am knowing~~ → I **know** the answer.", "know는 상태동사 → 진행형 X"),
    ]),

    H("3. 현재완료  have/has + p.p."),
    P("**과거에 일어난 일이 현재까지 영향을 주는 것**을 나타냅니다. 과거와 현재를 잇는 '다리' 시제입니다."),
    TABLE(
        ["용법", "의미", "함께 쓰는 말", "예문"],
        [
            ["**완료**", "막 ~했다", "just, already, yet", "I **have** just **finished** my homework."],
            ["**경험**", "~한 적이 있다", "ever, never, before, once, ~times", "**Have** you ever **been** to Jeju?"],
            ["**계속**", "(지금까지) 계속 ~해 왔다", "for + 기간, since + 시점, how long", "She **has lived** here since 2015."],
            ["**결과**", "~해서 (지금) …하다", "go, lose, leave 등", "He **has gone** to London. (지금 여기 없음)"],
        ],
        widths=[12, 22, 28, 38],
    ),
    FORMULA("현재완료 + 명백한 과거 표현 (X)", "yesterday, last week, ~ ago, in 2020, when I was young 등은 과거시제와 함께"),
    WARN([
        ("I ~~have seen~~ the movie yesterday.", "I ++saw++ the movie yesterday.", "yesterday = 명백한 과거"),
        ("When ~~have you finished~~ it?", "When ++did you finish++ it?", "의문사 when은 현재완료와 쓰지 않음"),
        ("I have lived here ~~since~~ three years.", "I have lived here ++for++ three years.", "for + 기간 / since + 시작 시점"),
    ]),
    TIP("have been to vs have gone to", [
        "have been to: ~에 가 본 적 있다 (경험) — I have been to Japan twice.",
        "have gone to: ~에 가 버렸다 (결과, 지금 없음) → 1·2인칭 주어에는 쓰지 않음",
    ]),

    H("4. 과거완료  had + p.p."),
    P("과거의 어느 시점(기준점)보다 **더 이전**에 일어난 일을 나타냅니다. 이를 **대과거**라고도 합니다. 문장 안에 반드시 **과거 기준점**이 있어야 합니다."),
    PARSE([("When I arrived at the station,", "M"), ("the train", "S"), ("had already left", "V")],
          "내가 역에 도착했을 때, 기차는 이미 떠나 버렸다. (떠남 → 도착 순서)"),
    EX([
        ("I lost the watch that my father **had given** me.", "나는 아버지가 주셨던 시계를 잃어버렸다. (준 것 → 잃어버린 것)"),
        ("She **had lived** in Seoul for ten years before she moved to Busan.", "그녀는 부산으로 이사하기 전 10년간 서울에 살았었다. (계속)"),
    ]),

    H("5. 미래완료  will have + p.p."),
    P("미래의 특정 시점까지 **완료·경험·계속**될 일을 나타냅니다. **by + 시점, by the time, next ~** 등과 자주 씁니다."),
    EX([
        ("I **will have finished** the report by Friday.", "금요일까지는 보고서를 끝냈을 것이다."),
        ("By next year, we **will have been** married for 20 years.", "내년이면 우리는 결혼한 지 20년이 될 것이다."),
    ]),

    H("6. 완료진행  have been + V-ing"),
    P("과거부터 시작된 동작이 **지금(또는 기준 시점)까지 계속 진행 중**임을 강조합니다."),
    EX([
        ("It **has been raining** since this morning.", "아침부터 비가 계속 내리고 있다."),
        ("He **had been waiting** for two hours when she finally came.", "그녀가 마침내 왔을 때 그는 두 시간째 기다리고 있었다."),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  I (lost / have lost) my wallet last night.", "lost", "last night = 명백한 과거"),
            Q("괄호 안에서 알맞은 것을 고르시오.  She has been sick (for / since) last Monday.", "since", "since + 시작 시점"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Call me when you (will arrive / arrive) at the airport.", "arrive",
              "시간 부사절에서는 현재시제가 미래를 대신함"),
            Q("밑줄 친 현재완료의 용법을 쓰시오.  I ==have never seen== such a beautiful sunset.", "경험", "never와 함께 쓰여 '~한 적이 없다'"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  When I got home, my brother (already ate / had already eaten) all the pizza.",
              "had already eaten", "집에 온 것(과거)보다 먹은 것이 더 이전 → 과거완료"),
            Q("괄호 안에서 알맞은 것을 고르시오.  By the end of this month, I (will finish / will have finished) the book.",
              "will have finished", "by + 미래 시점 → 미래완료"),
            Q("다음 중 어법상 틀린 문장은?", "②",
              "② ago는 명백한 과거 표현 → I met him two years ago.",
              options=["I have known her since childhood.", "I have met him two years ago.",
                       "Have you ever tried Thai food?", "He has just left the office."]),
            Q("다음 두 문장의 의미가 같도록 할 때 빈칸에 알맞은 것은?  Tom went to Canada. He is not here now. = Tom ______ to Canada.",
              "③", "가서 지금 없음 → 현재완료 결과 용법 has gone",
              options=["has been", "had gone", "has gone", "went"]),
        ]),
        ("STEP 3", "서술형", [
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  The teacher said that light traveled faster than sound.",
              "traveled → travels", "불변의 진리는 현재시제", lines=1),
            Q("두 문장을 현재완료 문장 하나로 바꿔 쓰시오.  I started learning English in 2019. I still learn it.",
              "I have learned (been learning) English since 2019.", "since + 시작 시점 → 계속", lines=1),
            Q("우리말과 같도록 주어진 단어를 활용하여 영작하시오.  내가 극장에 도착했을 때, 영화는 이미 시작했었다. (start, already)",
              "When I arrived at the theater, the movie had already started.", "도착(과거) 이전에 시작 → 과거완료", lines=1),
        ]),
    ]),
]
