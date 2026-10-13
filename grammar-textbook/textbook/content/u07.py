from textbook.blocks import *

GOALS = [
    "준동사(to부정사·동명사·분사)의 개념과 공통 성질을 이해한다.",
    "준동사의 의미상 주어, 부정, 완료형, 수동형을 구분한다.",
    "본동사와 준동사를 구별하여 문장 구조를 파악한다.",
]

INTRO = "준동사는 **동사에서 출발했지만 문장 안에서 명사·형용사·부사 역할을 하는 말**입니다. 동사의 성질(목적어, 수식어, 시제·태)은 그대로 갖고 있어 '반은 동사, 반은 다른 품사'라고 볼 수 있습니다."

BLOCKS = [
    TABLE(
        ["종류", "형태", "문장 안 역할", "예문"],
        [
            ["**to부정사**", "to + V", "명사 / 형용사 / 부사", "I want **to travel** abroad."],
            ["**동명사**", "V-ing", "명사", "**Swimming** is good exercise."],
            ["**분사**", "V-ing / p.p.", "형용사", "Look at the **sleeping** baby."],
        ],
        widths=[16, 18, 28, 38], caption="준동사 3총사",
    ),

    H("1. 본동사 vs 준동사"),
    P("한 문장(절)에는 시제를 가진 **본동사가 하나**만 있습니다. 나머지 동사 형태는 모두 준동사입니다. 어법 문제에서 '동사 자리인가, 준동사 자리인가'를 판단하는 것이 출발점입니다."),
    PARSE([("To keep a diary every day", "S"), ("is", "V"), ("not easy", "C")], "매일 일기를 쓰는 것은 쉽지 않다. (본동사는 is 하나)"),
    WARN([
        ("Exercise regularly ~~help~~ you stay healthy. (동사 2개 X)", "++Exercising++ regularly ++helps++ you stay healthy.",
         "주어 자리 동사 → 동명사/to부정사로 바꾸고 본동사는 하나만"),
    ]),

    H("2. 준동사의 공통 성질 ① 동사처럼 목적어·수식어를 가진다"),
    EX([
        ("I like **reading** ==comic books==.", "동명사 reading이 목적어 comic books를 가짐"),
        ("She decided **to study** ==harder==.", "to부정사가 부사 harder의 수식을 받음"),
    ]),

    H("3. ② 의미상 주어"),
    P("준동사의 행위자가 문장의 주어와 다를 때 **의미상 주어**를 표시합니다."),
    TABLE(
        ["준동사", "의미상 주어 형태", "예문"],
        [
            ["to부정사", "**for + 목적격** (일반)", "It is hard **for me** to wake up early."],
            ["", "**of + 목적격** (사람의 성격 형용사: kind, nice, wise, foolish…)", "It was kind **of you** to help me."],
            ["동명사", "**소유격** (또는 목적격)", "Do you mind **my(me)** opening the window?"],
        ],
        widths=[14, 42, 44],
    ),

    H("4. ③ 부정은 준동사 바로 앞에 not/never"),
    EX([
        ("He promised **not to be** late again.", "그는 다시는 늦지 않겠다고 약속했다."),
        ("I'm sorry for **not calling** you back.", "다시 전화하지 않아서 미안해."),
        ("**Not knowing** what to say, I kept silent.", "무슨 말을 해야 할지 몰라서 나는 침묵했다."),
    ]),

    H("5. ④ 완료형 — 본동사보다 앞선 시제"),
    TABLE(
        ["준동사", "단순형 (본동사와 같은 때)", "완료형 (본동사보다 이전)"],
        [
            ["to부정사", "to V", "**to have p.p.**"],
            ["동명사", "V-ing", "**having p.p.**"],
            ["분사(구문)", "V-ing", "**having p.p.**"],
        ],
        widths=[20, 40, 40], center=[1, 2],
    ),
    EX([
        ("He seems **to be** rich.  = It seems that he **is** rich.", "그는 (지금) 부자인 것 같다."),
        ("He seems **to have been** rich.  = It seems that he **was** rich.", "그는 (예전에) 부자였던 것 같다."),
        ("**Having eaten** lunch, I'm full now.", "점심을 먹어서 지금 배부르다. (먹은 것이 먼저)"),
    ]),

    H("6. ⑤ 수동형 — 의미상 주어가 '당할' 때"),
    TABLE(
        ["준동사", "수동형", "완료 수동형", "예문"],
        [
            ["to부정사", "to be p.p.", "to have been p.p.", "Everyone wants **to be loved**."],
            ["동명사", "being p.p.", "having been p.p.", "I hate **being treated** like a child."],
        ],
        widths=[16, 18, 22, 44],
    ),
    TIP("준동사 문제 접근법", [
        "① 본동사 자리인가? → 아니면 준동사",
        "② 의미상 주어와의 관계가 능동인가, 수동인가?",
        "③ 본동사와 같은 때인가, 더 이전인가?",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 부분의 준동사 종류를 쓰시오.  ==Learning== a new language takes time.", "동명사", "주어 역할 V-ing"),
            Q("밑줄 친 부분의 준동사 종류를 쓰시오.  I need something ==to drink==.", "to부정사 (형용사적 용법)", "something을 꾸밈"),
            Q("밑줄 친 부분의 준동사 종류를 쓰시오.  Who is the boy ==standing== by the door?", "분사 (현재분사)", "the boy를 꾸미는 형용사 역할"),
            Q("괄호 안에서 알맞은 것을 고르시오.  It is very nice (for / of) you to say so.", "of", "nice는 사람의 성격 형용사"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  She decided (not to go / to not go) to the party.", "not to go", "부정어는 준동사 바로 앞"),
            Q("괄호 안에서 알맞은 것을 고르시오.  He seems (to be / to have been) sick last week.", "to have been",
              "seems(현재)보다 last week(과거)가 이전 → 완료형"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I don't like (being told / telling) what to do.", "being told",
              "내가 '듣는(지시받는)' 입장 → 동명사 수동형"),
            Q("다음 중 어법상 틀린 문장은?", "①", "① 본동사가 make, is 두 개 → Making friends is not always easy.",
              options=["Make friends is not always easy.", "It is important for us to recycle.",
                       "I'm proud of having won the prize.", "She seems to know the answer."]),
        ]),
        ("STEP 3", "서술형", [
            Q("두 문장의 의미가 같도록 빈칸을 완성하시오.  It seems that she was a singer. = She seems ________ a singer.",
              "to have been", "that절이 본동사보다 이전 시제 → to have p.p.", lines=1),
            Q("우리말과 같도록 주어진 단어를 배열하시오.  나는 거짓말한 것이 부끄럽다. (ashamed / having / I'm / lied / of)",
              "I'm ashamed of having lied.", "부끄러운 것(현재)보다 거짓말이 먼저 → having p.p.", lines=1),
        ]),
    ]),
]
