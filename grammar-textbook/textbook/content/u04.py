from textbook.blocks import *

GOALS = [
    "5형식 목적격보어 자리에 오는 형태(명사·형용사·to부정사·동사원형·분사)를 구분한다.",
    "사역동사·지각동사·준사역동사의 목적격보어 형태를 정확히 쓸 수 있다.",
    "목적어와 목적격보어의 능동·수동 관계로 동사원형/p.p.를 판단할 수 있다.",
]

INTRO = "5형식의 핵심은 **목적격보어(O.C) 자리에 무엇이 오느냐**입니다. 동사의 종류가 O.C의 형태를 결정하므로, 내신 어법 문제의 단골 출제 포인트입니다."

BLOCKS = [
    TABLE(
        ["O.C 형태", "주요 동사", "예문"],
        [
            ["**명사**", "name, call, make, elect, consider", "We **elected** her class president."],
            ["**형용사**", "make, keep, find, leave, consider", "Exercise **keeps** you healthy."],
            ["**to부정사**", "want, ask, tell, allow, expect, enable, encourage, advise, force", "I **want** you to do your homework first."],
            ["**동사원형**", "사역동사 make, have, let / 지각동사", "Mom **made** me clean my room."],
            ["**V-ing**", "지각동사 (진행 중인 동작 강조), keep, find", "I **saw** a man running down the street."],
            ["**p.p.**", "have, get, 지각동사, keep, find, leave (O가 동작을 '당함')", "I **had** my car washed."],
        ],
        widths=[16, 42, 42], caption="목적격보어 형태 총정리",
    ),

    H("1. to부정사를 목적격보어로 쓰는 동사"),
    P("**'O가 ~하기를 원하다/요청하다/허락하다'** 처럼 앞으로 할 일을 나타내는 동사는 목적격보어로 **to부정사**를 씁니다."),
    PARSE([("The teacher", "S"), ("told", "V"), ("us", "O"), ("to be quiet", "O.C")], "선생님은 우리에게 조용히 하라고 말씀하셨다."),
    EX([
        ("My parents **allowed** me to go camping.", "부모님은 내가 캠핑 가는 것을 허락하셨다."),
        ("The doctor **advised** him not to smoke.", "의사는 그에게 담배를 피우지 말라고 충고했다. (부정: not to V)"),
        ("This app **enables** users to share photos easily.", "이 앱은 사용자들이 사진을 쉽게 공유할 수 있게 한다."),
    ]),

    H("2. 사역동사  make / have / let"),
    P("'O가 ~하게 하다/시키다'라는 뜻의 사역동사는 목적격보어로 **동사원형**을 씁니다. O와 O.C가 수동 관계(O가 ~되다)이면 **p.p.** 를 씁니다."),
    TABLE(
        ["동사", "의미", "O.C (능동)", "O.C (수동)"],
        [
            ["**make**", "(강제로) ~하게 하다", "동사원형", "p.p."],
            ["**have**", "(부탁·지시해서) ~하게 하다", "동사원형", "p.p."],
            ["**let**", "~하도록 허락하다", "동사원형", "be p.p."],
        ],
        widths=[16, 34, 25, 25], center=[2, 3],
    ),
    EX([
        ("She **made** her son ==finish== his homework.", "그녀는 아들이 숙제를 끝내게 했다. (son이 끝냄 → 능동)"),
        ("I **had** the mechanic ==repair== my bike.", "나는 정비사에게 자전거를 수리하게 했다."),
        ("I **had** my bike ==repaired==.", "나는 자전거를 수리 받았다. (bike가 수리됨 → 수동)"),
        ("**Let** me ==introduce== myself.", "제 소개를 하겠습니다."),
    ]),
    WARN([
        ("Mom made me ~~to clean~~ my room.", "Mom made me ++clean++ my room.", "사역동사 make + O + 동사원형"),
        ("I had my hair ~~cutting~~.", "I had my hair ++cut++.", "머리가 '잘리는' 것 → p.p. (cut-cut-cut)"),
    ]),

    H("3. 준사역동사  help / get"),
    TABLE(
        ["동사", "O.C (능동)", "O.C (수동)", "예문"],
        [
            ["**help**", "to V / 동사원형", "–", "He helped me (to) move the boxes."],
            ["**get**", "**to V**", "p.p.", "I got him to fix the door. / I got the door fixed."],
        ],
        widths=[12, 22, 14, 52],
    ),
    TIP("get은 사역 의미여도 to부정사!", [
        "I got my brother ~~wash~~ the dishes. → I got my brother ++to wash++ the dishes.",
        "get + O + to V (능동)  /  get + O + p.p. (수동)",
    ]),

    H("4. 지각동사  see / watch / hear / feel / notice / listen to"),
    P("'O가 ~하는 것을 보다/듣다/느끼다'라는 뜻으로, 목적격보어 자리에 **동사원형**(동작 전체) 또는 **V-ing**(진행 중인 동작)가 옵니다. O가 동작을 당하면 **p.p.** 를 씁니다."),
    PARSE([("I", "S"), ("heard", "V"), ("someone", "O"), ("call my name", "O.C")], "나는 누군가 내 이름을 부르는 것을 들었다."),
    EX([
        ("We **watched** the sun ==set==.", "우리는 해가 지는 것을 (처음부터 끝까지) 보았다."),
        ("I **felt** the ground ==shaking==.", "나는 땅이 흔들리고 있는 것을 느꼈다. (진행 강조)"),
        ("She **heard** her name ==called==.", "그녀는 자기 이름이 불리는 것을 들었다. (수동)"),
    ]),

    H("5. 5형식 수동태 — 사역·지각동사 주의"),
    P("사역동사 make와 지각동사가 수동태가 되면, 목적격보어였던 **동사원형이 to부정사로** 바뀝니다. (수동태는 Unit 6)"),
    EX([
        ("They **made** me ==wait== for an hour. → I **was made** ==to wait== for an hour.", "나는 한 시간 동안 기다려야 했다."),
        ("We **saw** him ==enter== the building. → He **was seen** ==to enter== the building.", "그가 건물에 들어가는 것이 목격되었다."),
    ]),
    NOTE("let과 have", ["let과 have는 수동태로 거의 쓰지 않습니다. let의 수동은 be allowed to V로 바꿔 씁니다.",
                       "I was ~~let~~ to go. → I ++was allowed to++ go."]),

    H("6. 목적격보어 판단 3단계"),
    LIST([
        "**1단계** 동사 확인: to부정사형(want, tell…) / 사역(make, have, let) / 준사역(help, get) / 지각(see, hear…)",
        "**2단계** O와 O.C의 관계 확인: O가 직접 하면 능동, O가 당하면 수동(p.p.)",
        "**3단계** 동사별 규칙 적용: 사역 → 동사원형 / get → to V / help → to V·원형 / 지각 → 원형·V-ing",
    ], title="어법 문제 풀이 순서"),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  My dad let me (use / to use) his laptop.", "use", "사역동사 let + O + 동사원형"),
            Q("괄호 안에서 알맞은 것을 고르시오.  The coach told us (run / to run) faster.", "to run", "tell + O + to V"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I saw a cat (climb / to climb) the tree.", "climb", "지각동사 see + O + 동사원형/V-ing"),
            Q("괄호 안에서 알맞은 것을 고르시오.  She had her phone (repair / repaired).", "repaired", "phone은 수리'되는' 대상 → p.p."),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  I finally got my sister (lend / to lend) me her bike.", "to lend",
              "get + O + to V (준사역)"),
            Q("괄호 안에서 알맞은 것을 고르시오.  He was made (clean / to clean) the classroom.", "to clean",
              "사역동사 make의 수동태 → be made to V"),
            Q("다음 중 어법상 틀린 문장은?", "③",
              "③ have + O + 동사원형/p.p. → I had my homework checked. (homework는 '검사받는' 대상)",
              options=["I heard her singing in her room.", "They helped me carry the boxes.",
                       "I had my homework check by the teacher.", "The news made everyone surprised."]),
            Q("다음 빈칸에 들어갈 말로 알맞지 않은 것은?  My mom ______ me to study harder.", "②",
              "make는 사역동사 → to V가 아닌 동사원형을 쓴다",
              options=["wanted", "made", "told", "encouraged"]),
        ]),
        ("STEP 3", "서술형", [
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  The teacher had us to write an essay.", "to write → write",
              "사역동사 have + O + 동사원형", lines=1),
            Q("다음 문장을 수동태로 바꿔 쓰시오.  People saw the boy cross the road.", "The boy was seen to cross the road (by people).",
              "지각동사 수동태: 동사원형 → to V", lines=1),
            Q("우리말과 같도록 주어진 단어를 활용하여 영작하시오.  나는 어제 머리를 잘랐다. (have, cut)",
              "I had my hair cut yesterday.", "미용사가 잘라 준 것 → have + 머리(O) + p.p.", lines=1),
        ]),
    ]),
]
