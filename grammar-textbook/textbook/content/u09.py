from textbook.blocks import *
from textbook import figs as F

GOALS = [
    "to V / V-ing에 따라 뜻이 바뀌는 동사 4개를 확실히 구별한다.",
    "동명사만 목적어로 쓰는 동사와 관용 표현을 익힌다.",
]

INTRO = "동명사 단원의 핵심은 표 하나. **to V는 앞으로 할 일(미래), V-ing는 이미 한 일(과거)** 입니다."

BLOCKS = [
    ANCHOR("I remember calling her last night.", "나는 어젯밤 그녀에게 전화했던 것을 기억한다.", "remember to call ↔ remember calling — to V와 V-ing를 바꾸면 시간이 바뀝니다."),
    FIG(F.gerund_venn(), "to부정사 vs 동명사: 목적어로 무엇을 쓰는가 (교집합 = 둘 다 가능)"),
    TABLE(
        ["동사", "to V", "V-ing"],
        [
            ["**forget**", "할 일을 잊다", "했던 일을 잊다"],
            ["**remember**", "할 일을 기억하다", "했던 일을 기억하다"],
            ["**regret**", "~하게 되어 유감이다", "~했던 것을 후회하다"],
            ["**stop**", "~하기 위해 멈추다", "~하는 것을 멈추다"],
        ],
        widths=[20, 40, 40], center=[1, 2],
    ),
    PILGI([
        "to V = {{앞으로}} 할 일 (미래) / V-ing = {{이미}} 한 일 (과거)",
        "stop + to V의 to V는 목적어가 아니라 {{부사적}} 용법(~하기 위해)",
        "동명사는 {{명사}} 역할만 한다 → 주어·목적어·보어·전치사의 목적어",
    ]),
    CHAIN([
        ("remember to V", "**Remember to call** her tonight.", None),
        ("remember V-ing", "I **remember calling** her last night.", "어젯밤 이미 전화한 일"),
        ("forget V-ing", "I'll never **forget meeting** you.", "만났던 일 → 과거"),
        ("stop V-ing", "He **stopped smoking**.", "담배를 끊었다 (목적어)"),
        ("stop to V", "He **stopped to smoke**.", "담배 피우려고 멈췄다 (부사적)"),
    ], title="to V ↔ V-ing 바꿔 보기"),
    QUICK([
        "시간 표현이 미래(tonight, tomorrow) → **to V**",
        "과거 표현(last night, ago, for the first time) → **V-ing**",
        "전치사 뒤 → 무조건 **V-ing**",
    ]),
    LINK(8, "to부정사만 목적어로 쓰는 동사(want, decide…)와 비교."),

    STEPUP(),
    TABLE(
        ["목적어", "동사"],
        [
            ["**동명사만**", "mind, enjoy, give up, avoid, finish, escape, practice, postpone, consider, deny"],
            ["**to부정사만**", "want, hope, wish, plan, decide, promise, expect, agree, refuse"],
            ["**둘 다 (뜻 같음)**", "like, love, hate, begin, start, continue"],
        ],
        widths=[20, 80],
    ),
    TIP("MEGAFEPS", ["mind · enjoy · give up · avoid · finish · escape · practice/postpone · stop → 동명사만"]),
    TABLE(
        ["동명사 관용 표현", "의미"],
        [
            ["look forward to V-ing", "~하기를 고대하다"],
            ["be used to V-ing", "~하는 데 익숙하다"],
            ["be worth V-ing", "~할 가치가 있다"],
            ["cannot help V-ing", "~하지 않을 수 없다"],
            ["spend 시간 V-ing", "~하는 데 시간을 쓰다"],
            ["feel like V-ing", "~하고 싶다"],
        ],
        widths=[50, 50],
    ),
    NOTE("used to 3형제", [
        "used to V: ~하곤 했다 / be used to V-ing: ~에 익숙하다 / be used to V: ~하는 데 사용되다",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Don't forget (to bring / bringing) your passport tomorrow.", "to bring", "미래"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I remember (to meet / meeting) him last year.", "meeting", "과거"),
            Q("괄호 안에서 알맞은 것을 고르시오.  Would you mind (opening / to open) the window?", "opening", "mind + V-ing"),
            Q("괄호 안에서 알맞은 것을 고르시오.  He is good at (draw / drawing).", "drawing", "전치사 뒤"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("밑줄 친 부분의 의미를 쓰시오.  He ==stopped to drink== some water.", "물을 마시기 위해 멈췄다", "부사적 용법"),
            Q("밑줄 친 부분의 의미를 쓰시오.  I ==regret telling== you the truth.", "진실을 말한 것을 후회한다", ""),
            Q("다음 중 어법상 틀린 문장은?", "②", "finish + V-ing",
              options=["I gave up trying to convince him.", "I finished to do my homework.",
                       "She avoided answering the question.", "They began singing together."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("한 문장으로 바꾸시오.  I called her last night. I remember it. (remember)",
              "I remember calling her last night.", "이미 한 일 → V-ing", lines=1),
            Q("한 문장으로 바꾸시오.  I must call her tonight. Don't forget it. (forget)",
              "Don't forget to call her tonight.", "앞으로 할 일 → to V", lines=1),
            Q("어법상 틀린 부분을 고치시오.  I'm looking forward to hear from you.", "hear → hearing", "to는 전치사", lines=1),
        ]),
    ]),
]
