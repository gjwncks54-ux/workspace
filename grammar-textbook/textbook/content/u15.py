from textbook.blocks import *
from textbook import figs as F

GOALS = [
    "가정법 과거·과거완료·혼합가정법을 형태로 구별한다.",
    "without / but for, if 생략 도치로 바꿔 쓴다.",
]

INTRO = "가정법의 원리는 하나. **실제보다 한 시제 과거로.** 현재 반대는 과거형, 과거 반대는 had p.p."

BLOCKS = [
    ANCHOR("If I were you, I wouldn't do that.", "내가 너라면 그렇게 하지 않을 텐데.", "If I were you → Were I you / If I had known → Had I known."),
    TABLE(
        ["If의 종류", "조건절", "가정법", "명사절 (= whether)"],
        [
            ["**해석**", "만약 ~라면", "만약 ~라면", "~인지 아닌지"],
            ["**시제**", "현재 (will X)", "과거, 대과거", "과거, 현재, 미래"],
            ["**역할**", "부사절", "부사절", "명사절 (주어 X)"],
            ["**실현 가능성**", "O", "X", "O"],
        ],
        widths=[19, 27, 27, 27], center=[1, 2, 3], caption="If의 종류 (수업 판서)",
    ),
    TABLE(
        ["형태", "의미"],
        [
            ["If + S + **Ved**, S + would/could + **동원**", "현재 사실과 반대인 가정"],
            ["If + S + **had p.p.**, S + would/could **have p.p.**", "과거 사실과 반대인 가정"],
            ["If + S + **had p.p.**, S + would/could + **동원**", "혼합가정법"],
        ],
        widths=[62, 38],
    ),
    FIG(F.subjunctive_formulas(), "가정법 3종: 절마다 '실제로 가리키는 때'를 밑에 적어 보면 혼합가정법 = 과 + 현"),
    TABLE(
        ["without / if 생략 표현", "비고"],
        [
            ["but for", "without과 유사"],
            ["if it were not for / were it not for", "현재 가정"],
            ["if it had not been for / had it not been for", "과거 가정"],
        ],
        widths=[62, 38],
    ),
    PILGI([
        "if 생략 도치",
        "- {{were}} / {{had}} / {{should}} 일 때 가능",
        "- if를 지우고 {{S ↔ V}}",
        "- 예: Were I you, ... / Had I known, ...",
    ]),
    CHAIN([
        ("사실", "I am not you, so I won't do that.", None),
        ("가정법 과거", "**If I were** you, I **wouldn't** do that.", "현재 반대 → 과거형 (be는 were)"),
        ("if 생략", "**Were I** you, I wouldn't do that.", "were를 앞으로"),
    ], title="Were I you, ..."),
    CHAIN([
        ("사실", "I didn't know the truth, so I didn't tell you.", None),
        ("가정법 과거완료", "**If I had known** the truth, I **would have told** you.", "과거 반대 → had p.p."),
        ("if 생략", "**Had I known** the truth, I would have told you.", "had만 앞으로"),
        ("혼합", "If I had known the truth, I **would be** happier **now**.", "과거 일 → 지금 영향"),
    ], title="Had I known, ..."),
    CHAIN([
        ("without", "**Without** water, we couldn't live.", None),
        ("if it were not for", "**If it were not for** water, we couldn't live.", "현재 가정"),
        ("도치", "**Were it not for** water, we couldn't live.", None),
    ], title="Without water, ..."),
    QUICK([
        "주절에 would **have p.p.** → if절은 **had p.p.**",
        "주절에 **now / today** → 혼합가정법 (would + 동원)",
        "If ~ will … 이면 가정법이 아니라 **조건문** (If it rains tomorrow, I will …)",
    ]),
    LINK(14, "if 생략 도치도 도치구문의 한 종류."),

    STEPUP(),
    TABLE(
        ["표현", "형태", "예문"],
        [
            ["I wish (현재)", "I wish + S + 과거형", "I wish I **were** taller."],
            ["I wish (과거)", "I wish + S + had p.p.", "I wish I **had listened** to you."],
            ["as if (현재)", "as if + S + 과거형", "He talks as if he **knew** everything."],
            ["as if (과거)", "as if + S + had p.p.", "She looks as if she **had seen** a ghost."],
            ["It's time", "It's time + S + 과거형", "It's time you **went** to bed."],
        ],
        widths=[20, 30, 50],
    ),
    WARN([
        ("If I ~~know~~ her number, I would call her.", "If I ++knew++ her number, …", "현재 반대 → 과거형"),
        ("~~Had known I~~ the answer, …", "++Had I known++ the answer, …", "had만 앞으로"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  If I (am / were) you, I wouldn't do that.", "were", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  If I had known the truth, I (would tell / would have told) you.",
              "would have told", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  I wish I (can / could) speak French.", "could", ""),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  If I had eaten breakfast, I (wouldn't be / wouldn't have been) hungry now.",
              "wouldn't be", "now → 혼합"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Had I / I had) known about the party, I would have come.", "Had I", ""),
            Q("빈칸에 들어갈 말로 알맞지 않은 것은?  ______ your advice, I would have failed.", "④",
              "If it were not for는 현재 가정",
              options=["Without", "But for", "Had it not been for", "If it were not for"]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("if를 생략하여 다시 쓰시오.  If I were you, I would accept the offer.", "Were I you, I would accept the offer.",
              "", lines=1),
            Q("가정법으로 바꾸시오.  As he didn't tell me the truth, I got angry.",
              "If he had told me the truth, I wouldn't have gotten angry.", "", lines=1),
            Q("Had it not been for를 이용하여 바꾸시오.  Without your help, I couldn't have finished it.",
              "Had it not been for your help, I couldn't have finished it.", "", lines=1),
        ]),
    ]),
]
