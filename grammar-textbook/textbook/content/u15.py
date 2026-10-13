from textbook.blocks import *

GOALS = [
    "가정법 과거·과거완료·혼합가정법의 형태와 의미를 구분한다.",
    "I wish, as if, It's time 가정법을 상황에 맞게 쓸 수 있다.",
    "without / but for, if 생략 도치 표현을 이해하고 바꿔 쓸 수 있다.",
]

INTRO = "가정법은 **사실과 반대되거나 일어날 가능성이 거의 없는 일**을 상상할 때 씁니다. 핵심 원리는 하나입니다. **'실제보다 한 시제 과거로'** — 현재 반대는 과거형, 과거 반대는 과거완료형을 씁니다."

BLOCKS = [
    TABLE(
        ["종류", "형태", "의미"],
        [
            ["**가정법 과거**", "If + S + **V-ed (were)**, S + would/could/might + **동사원형**", "현재 사실과 반대"],
            ["**가정법 과거완료**", "If + S + **had p.p.**, S + would/could/might + **have p.p.**", "과거 사실과 반대"],
            ["**혼합가정법**", "If + S + **had p.p.**, S + would/could/might + **동사원형** (+ now)", "과거 일이 현재에 영향"],
        ],
        widths=[20, 56, 24], caption="가정법 3종 핵심",
    ),

    H("1. 가정법 과거  — 현재의 반대"),
    PARSE([("If I had wings,", "M"), ("I", "S"), ("could fly", "V"), ("to you", "M")],
          "내가 날개가 있다면 너에게 날아갈 수 있을 텐데."),
    EX([
        ("If I **were** rich, I **would buy** a big house.", "내가 부자라면 큰 집을 살 텐데. → 실제: I am not rich."),
        ("If I **were** you, I **wouldn't** say that.", "내가 너라면 그렇게 말하지 않을 텐데. (충고)"),
    ]),
    TIP("가정법 과거의 be동사는 were", [
        "주어와 상관없이 were를 쓰는 것이 원칙 (구어에서는 was도 쓰임)",
        "If he **were** here, he would help us.",
    ]),
    WARN([
        ("If I ~~know~~ her number, I would call her.", "If I ++knew++ her number, I would call her.", "현재 반대 → 과거형"),
        ("If I had time, I ~~will~~ help you.", "If I had time, I ++would++ help you.", "주절은 would/could/might"),
    ]),
    NOTE("직설법 조건문과 구별", [
        "If it **rains** tomorrow, I **will** stay home. → 실제로 일어날 수 있는 일 (조건문)",
        "If I **were** a bird, I **would** fly. → 불가능한 일 (가정법)",
    ]),

    H("2. 가정법 과거완료  — 과거의 반대"),
    EX([
        ("If I **had studied** harder, I **could have passed** the exam.", "더 열심히 공부했다면 시험에 합격할 수 있었을 텐데."),
        ("→ 실제: As I **didn't study** harder, I **couldn't pass** the exam.", "직설법으로 바꾸면 시제가 한 단계 '현재 쪽'으로"),
    ]),

    H("3. 혼합가정법  — 과거의 일이 현재에 영향"),
    P("if절은 **과거** 사실의 반대(had p.p.), 주절은 **현재** 사실의 반대(would + 원형)입니다. 주절에 **now, today** 같은 표현이 단서가 됩니다."),
    EX([
        ("If I **had taken** the medicine, I **would feel** better **now**.", "(그때) 약을 먹었더라면 (지금) 기분이 나을 텐데."),
        ("If she **hadn't missed** the bus, she **would be** here now.", "그녀가 버스를 놓치지 않았다면 지금 여기 있을 텐데."),
    ]),

    H("4. I wish / as if / It's time"),
    TABLE(
        ["표현", "형태", "예문", "의미"],
        [
            ["**I wish** (현재 소망)", "I wish + S + 과거형", "I wish I **were** taller.", "키가 더 크면 좋을 텐데"],
            ["**I wish** (과거 후회)", "I wish + S + had p.p.", "I wish I **had listened** to you.", "네 말을 들었더라면 좋았을 텐데"],
            ["**as if** (현재)", "as if + S + 과거형", "He talks **as if** he **knew** everything.", "모든 걸 아는 것처럼 (실제론 모름)"],
            ["**as if** (과거)", "as if + S + had p.p.", "She looks **as if** she **had seen** a ghost.", "유령을 본 것처럼"],
            ["**It's time**", "It's (high) time + S + 과거형", "It's time you **went** to bed.", "이제 잘 시간이다 (진작 했어야)"],
        ],
        widths=[18, 22, 34, 26],
    ),

    H("5. without / but for  — if절 대신"),
    TABLE(
        ["표현", "가정법 과거 (현재)", "가정법 과거완료 (과거)"],
        [
            ["**Without / But for** + 명사", "Without water, we **couldn't live**.", "Without your help, I **couldn't have finished** it."],
            ["= If it were not for / Were it not for", "If it were not for water, …", "–"],
            ["= If it had not been for / Had it not been for", "–", "If it had not been for your help, …"],
        ],
        widths=[34, 33, 33],
    ),

    H("6. if 생략 도치"),
    P("if절의 동사가 **were / had / should** 이면 if를 생략하고 **주어와 동사의 위치를 바꿀** 수 있습니다. (Unit 14 도치구문)"),
    TABLE(
        ["원래 문장", "if 생략 도치"],
        [
            ["If I **were** you, …", "**Were I** you, …"],
            ["If I **had known** the truth, …", "**Had I known** the truth, …"],
            ["If you **should** need help, …", "**Should you** need help, … (혹시라도 ~하면)"],
        ],
        widths=[50, 50],
    ),
    WARN([
        ("~~Had known I~~ the answer, I would have told you.", "++Had I known++ the answer, I would have told you.",
         "had만 앞으로, p.p.는 주어 뒤"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  If I (am / were) a bird, I would fly to you.", "were", "가정법 과거"),
            Q("괄호 안에서 알맞은 것을 고르시오.  If she had left earlier, she (would catch / would have caught) the train.",
              "would have caught", "가정법 과거완료"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I wish I (can / could) speak French.", "could", "I wish + 과거형 (현재 소망)"),
            Q("괄호 안에서 알맞은 것을 고르시오.  He acts as if he (is / were) the boss.", "were", "실제로는 사장이 아님"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  If I had eaten breakfast, I (wouldn't be / wouldn't have been) hungry now.",
              "wouldn't be", "now → 혼합가정법"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Had I / I had) known about the party, I would have come.", "Had I", "if 생략 도치"),
            Q("다음 문장과 의미가 같은 것은?  As I don't have a car, I can't drive you home.", "③",
              "현재 사실 반대 → 가정법 과거",
              options=["If I have a car, I can drive you home.", "If I had had a car, I could have driven you home.",
                       "If I had a car, I could drive you home.", "If I didn't have a car, I couldn't drive you home."]),
            Q("다음 빈칸에 들어갈 말로 알맞지 않은 것은?  ______ your advice, I would have failed.", "④",
              "④ If it were not for는 가정법 과거(현재) → 주절 would have failed와 맞지 않음",
              options=["Without", "But for", "Had it not been for", "If it were not for"]),
        ]),
        ("STEP 3", "서술형", [
            Q("직설법 문장을 가정법으로 바꿔 쓰시오.  As he didn't tell me the truth, I got angry.",
              "If he had told me the truth, I wouldn't have gotten(got) angry.", "과거 사실 반대 → 가정법 과거완료", lines=1),
            Q("I wish를 이용하여 바꿔 쓰시오.  I'm sorry that I didn't bring my umbrella.",
              "I wish I had brought my umbrella.", "과거 후회 → I wish + had p.p.", lines=1),
            Q("if를 생략하여 다시 쓰시오.  If I were in your position, I would accept the offer.",
              "Were I in your position, I would accept the offer.", "were 도치", lines=1),
        ]),
    ]),
]
