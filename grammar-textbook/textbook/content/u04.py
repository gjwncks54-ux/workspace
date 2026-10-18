from textbook.blocks import *
from textbook import figs as F

GOALS = [
    "5형식 목적격보어(O.C) 형태를 동사 유형별로 정리한다.",
    "사역·지각·준사역동사의 O.C를 정확히 고른다.",
    "사역·지각동사가 수동태가 되면 to V로 바뀌는 것을 안다.",
]

INTRO = "5형식 심화의 핵심은 **동사가 O.C의 모양을 정한다**는 것. 아래 표 한 장이 이 단원의 전부입니다."

BLOCKS = [
    ANCHOR("I made her clean the room.", "나는 그녀가 방을 청소하게 했다.", "사역 → have/get 바꿔 쓰기 → 수동태(Unit 6)까지 이어집니다."),
    TABLE(
        ["유형", "주요 동사", "O.C 형태", "예문"],
        [
            ["**명사**", "name / call / make", "명사", "I named my dog Buddy."],
            ["**형용사**", "keep / make", "형용사", "I made him sad."],
            ["**to부정사**", "want / ask / tell / allow / enable / encourage / discourage", "to V",
             "I want you to do your homework first."],
            ["**지각동사**", "watch / hear / see / feel / notice / listen to", "동사원형 / V-ing / p.p.",
             "I saw a man run / running down the street."],
            ["**사역동사**", "make / let / have", "make·let + 동원\nhave + 동원·p.p.",
             "I made her clean the room.\nI had my car washed."],
            ["**준사역동사**", "help / get", "help + to V·동원\nget + to V·p.p.",
             "He helped me (to) finish it.\nI got my phone repaired."],
        ],
        widths=[13, 30, 21, 36], caption="5형식 목적격보어 총정리",
    ),
    PILGI([
        "5형식은 어떤 {{V}}가 오느냐에 따라 {{O.C}} 형태가 바뀐다.",
        "사역동사에서 목적격보어가 동사원형이면, 수동태로 바꿀 때 {{to V}}로 바뀌는 경우가 많습니다.",
        "목적어가 직접 하면 동사원형, 목적어가 당하면 {{p.p.}}  (my car가 '세차되는' 것 → washed)",
        "get은 사역 의미여도 {{to V}}.  help는 to V, 동사원형 {{둘 다}} 가능.",
    ]),
    FIG(F.causative_board(), "사역동사 (시키다) · 준사역동사"),
    EX([
        ("I **made** Jake ==do== his homework.", "나는 Jake가 숙제를 하게 했다. (make + 동사원형)"),
        ("I **had** Jake ==do== his homework.", "나는 Jake에게 숙제를 하게 했다. (have + 동사원형)"),
        ("I **had** my car ==washed==.", "나는 세차를 맡겼다. (have + V p.p.: 차가 세차됨)"),
    ]),
    FIG(F.participle_flow(), "O.C 자리 분사 고르기: V-ing인가 V p.p.인가 (분사구문에서도 같은 흐름도를 쓴다)", width=110),
    CHAIN([
        ("사역 (능동)", "I made her **clean** the room.", None),
        ("수동태", "She was made **to clean** the room.", "동사원형 → to V (Unit 6 5형식 수동태)"),
    ], title="I made her clean the room"),
    CHAIN([
        ("have + 동원", "I had **the man wash** my car.", None),
        ("have + p.p.", "I had **my car washed**.", "목적어가 car로 바뀌면 '세차되는' 관계 → p.p."),
        ("get + p.p.", "I got **my phone repaired**.", "get도 수동이면 p.p."),
        ("get + to V", "I got **him to repair** my phone.", "get 능동은 to V"),
    ], title="have / get — 목적어에 따라 O.C가 바뀐다"),
    CHAIN([
        ("지각 + 동원", "I saw a man **run** down the street.", None),
        ("지각 + V-ing", "I saw a man **running** down the street.", "진행 중인 순간을 강조"),
        ("수동태", "A man was seen **to run** down the street.", "지각동사 수동태도 to V"),
    ], title="I saw a man run down the street"),
    QUICK([
        "① 동사 확인 → ② 목적어가 하나, 당하나 → ③ 동사별 규칙",
        "사역 make·let·have → **동사원형** / get → **to V** / help → **to V·동원** / 지각 → **동원·V-ing**",
    ]),
    LINK(6, "5형식 수동태: She was made to clean the room."),

    STEPUP(),
    WARN([
        ("Mom made me ~~to clean~~ my room.", "Mom made me ++clean++ my room.", "사역 make + 동사원형"),
        ("I got my brother ~~wash~~ the dishes.", "I got my brother ++to wash++ the dishes.", "get + to V"),
        ("I was ~~let~~ to go.", "I ++was allowed to++ go.", "let은 수동태 대신 be allowed to"),
    ]),
    TABLE(
        ["to V를 O.C로 쓰는 동사 더 보기"],
        [["expect, advise, force, order, persuade, require, cause, get"]],
    ),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  My dad let me (use / to use) his laptop.", "use", "let + 동원"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The coach told us (run / to run) faster.", "to run", "tell + to V"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I had my car (wash / washed).", "washed", "차가 세차됨 → p.p."),
            Q("괄호 안에서 알맞은 것을 고르시오.  I named my dog (Buddy / to Buddy).", "Buddy", "O.C 명사"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  I got my phone (repair / repaired).", "repaired", "get + p.p."),
            Q("괄호 안에서 알맞은 것을 고르시오.  She was made (clean / to clean) the room.", "to clean",
              "사역 수동태 → to V"),
            Q("다음 빈칸에 들어갈 말로 알맞지 않은 것은?  I ______ you to do your homework first.", "②",
              "make는 to V가 아니라 동사원형", options=["want", "make", "ask", "tell"]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("수동태로 바꾸시오.  I made her clean the room.", "She was made to clean the room (by me).", "", lines=1),
            Q("수동태로 바꾸시오.  People saw a man run down the street.", "A man was seen to run down the street (by people).",
              "", lines=1),
            Q("have를 이용하여 바꿔 쓰시오.  I made her clean the room. (have)", "I had her clean the room.",
              "have도 사역 → 동사원형", lines=1),
            Q("get을 이용하여 바꿔 쓰시오.  I made her clean the room. (get)", "I got her to clean the room.",
              "get은 to V", lines=1),
            Q("우리말과 같도록 영작하시오.  나는 어제 머리를 잘랐다. (have, cut)", "I had my hair cut yesterday.",
              "머리가 잘리는 것 → p.p.", lines=1),
        ]),
    ]),
]
