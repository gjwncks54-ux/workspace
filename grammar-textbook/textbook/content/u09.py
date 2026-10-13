from textbook.blocks import *

GOALS = [
    "동명사의 형태와 명사적 역할(주어·목적어·보어·전치사의 목적어)을 이해한다.",
    "동명사만 목적어로 쓰는 동사와 to부정사만 쓰는 동사를 구분한다.",
    "목적어 형태에 따라 의미가 달라지는 동사와 동명사 관용 표현을 익힌다.",
]

INTRO = "동명사는 **V-ing** 형태로 **'~하는 것, ~하기'** 라는 명사 역할을 합니다. to부정사의 명사적 용법과 비슷하지만, **전치사 뒤**에 올 수 있고 **과거·경험**의 느낌이 강하다는 차이가 있습니다."

BLOCKS = [
    H("1. 동명사의 역할"),
    TABLE(
        ["역할", "예문", "해석"],
        [
            ["**주어**", "**Reading** books makes me happy.", "책 읽는 것은 나를 행복하게 한다."],
            ["**목적어**", "I enjoy **playing** the guitar.", "나는 기타 치는 것을 즐긴다."],
            ["**보어**", "My hobby is **taking** pictures.", "내 취미는 사진 찍기이다."],
            ["**전치사의 목적어**", "Thank you for **inviting** me.", "초대해 줘서 고마워."],
        ],
        widths=[18, 46, 36],
    ),
    WARN([
        ("Thank you for ~~invite~~ me.", "Thank you for ++inviting++ me.", "전치사 뒤 동사 → 동명사 (to부정사 X)"),
        ("Reading books ~~make~~ me happy.", "Reading books ++makes++ me happy.", "동명사 주어는 단수 취급"),
    ]),

    H("2. 목적어로 동명사 vs to부정사"),
    TABLE(
        ["목적어 형태", "동사", "느낌"],
        [
            ["**동명사만**", "enjoy, finish, mind, avoid, give up, quit, practice, keep, consider, deny, postpone, put off, suggest",
             "이미 하고 있는 일, 반복, 중단·회피"],
            ["**to부정사만**", "want, hope, wish, plan, decide, promise, expect, agree, refuse, learn, manage",
             "앞으로 할 일 (미래·의지)"],
            ["**둘 다 (의미 같음)**", "like, love, hate, begin, start, continue, prefer", "어느 쪽이든 OK"],
        ],
        widths=[18, 54, 28],
    ),
    TIP("동명사만 목적어로 쓰는 동사 외우기", [
        "**MEGAFEPS**: mind, enjoy, give up, avoid, finish, escape, practice/postpone, stop(그만두다)",
        "공통 느낌: 이미 하고 있던 일을 즐기거나, 끝내거나, 피한다",
    ]),

    H("3. 목적어에 따라 의미가 달라지는 동사"),
    TABLE(
        ["동사", "+ to V (미래: 앞으로 할 일)", "+ V-ing (과거: 이미 한 일)"],
        [
            ["**remember**", "~할 것을 기억하다", "~했던 것을 기억하다"],
            ["**forget**", "~할 것을 잊다", "~했던 것을 잊다"],
            ["**regret**", "~하게 되어 유감이다", "~했던 것을 후회하다"],
            ["**try**", "~하려고 애쓰다", "(시험 삼아) 한번 ~해 보다"],
            ["**stop**", "~하기 위해 멈추다 (부사적 용법)", "~하는 것을 멈추다 (목적어)"],
        ],
        widths=[18, 41, 41],
    ),
    EX([
        ("**Remember to lock** the door when you leave.", "나갈 때 문 잠그는 것 기억해. (앞으로)"),
        ("I **remember locking** the door.", "나는 문을 잠갔던 것을 기억한다. (이미)"),
        ("He **stopped to smoke**.", "그는 담배를 피우기 위해 멈췄다."),
        ("He **stopped smoking**.", "그는 담배를 끊었다."),
        ("**Try pressing** this button.", "이 버튼을 한번 눌러 봐."),
    ]),

    H("4. 동명사 관용 표현"),
    TABLE(
        ["표현", "의미", "표현", "의미"],
        [
            ["**look forward to** V-ing", "~하기를 고대하다", "**be used to** V-ing", "~하는 데 익숙하다"],
            ["**feel like** V-ing", "~하고 싶다", "**be busy** V-ing", "~하느라 바쁘다"],
            ["**be worth** V-ing", "~할 가치가 있다", "**spend** 시간/돈 V-ing", "~하는 데 시간/돈을 쓰다"],
            ["**cannot help** V-ing", "~하지 않을 수 없다", "**have trouble** V-ing", "~하는 데 어려움을 겪다"],
            ["**How about** V-ing?", "~하는 게 어때?", "**On** V-ing", "~하자마자"],
            ["**It is no use** V-ing", "~해도 소용없다", "**There is no** V-ing", "~하는 것은 불가능하다"],
        ],
        widths=[25, 22, 27, 26],
    ),
    WARN([
        ("I'm looking forward to ~~see~~ you.", "I'm looking forward to ++seeing++ you.", "이때 to는 전치사"),
        ("I'm used to ~~get~~ up early.", "I'm used to ++getting++ up early.", "be used to V-ing (~에 익숙하다)"),
    ]),
    NOTE("헷갈리는 used to 3형제", [
        "**used to V**: (과거에) ~하곤 했다 — I **used to play** soccer.",
        "**be used to V-ing**: ~하는 데 익숙하다 — I **am used to playing** soccer.",
        "**be used to V**: ~하는 데 사용되다 (수동태) — Wood **is used to make** paper.",
    ]),

    H("5. 동명사 vs 현재분사"),
    P("둘 다 V-ing 형태지만, 동명사는 **용도·목적**(~하기 위한), 현재분사는 **동작·상태**(~하고 있는)를 나타냅니다."),
    EX([
        ("a **sleeping** bag  =  a bag for sleeping", "침낭 (동명사: 잠자기 위한 가방)"),
        ("a **sleeping** baby  =  a baby who is sleeping", "잠자고 있는 아기 (현재분사)"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Would you mind (opening / to open) the window?", "opening", "mind + V-ing"),
            Q("괄호 안에서 알맞은 것을 고르시오.  She decided (studying / to study) abroad.", "to study", "decide + to V"),
            Q("괄호 안에서 알맞은 것을 고르시오.  He is good at (draw / drawing).", "drawing", "전치사 at 뒤 → 동명사"),
            Q("괄호 안에서 알맞은 것을 고르시오.  This movie is worth (watching / to watch).", "watching", "be worth V-ing"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  Don't forget (to bring / bringing) your passport tomorrow.", "to bring",
              "tomorrow → 앞으로 할 일"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I'll never forget (to meet / meeting) him for the first time.", "meeting",
              "처음 만났던 일 → 과거"),
            Q("다음 중 어법상 틀린 문장은?", "②", "② finish는 동명사만 목적어로 → finished doing",
              options=["I gave up trying to convince him.", "I finished to do my homework.",
                       "She avoided answering the question.", "They began singing together."]),
            Q("다음 중 밑줄 친 부분의 쓰임이 나머지와 다른 것은?", "④",
              "④는 현재분사(진행형), 나머지는 동명사",
              options=["==Swimming== is fun.", "My job is ==teaching== kids.", "I enjoy ==cooking==.",
                       "She is ==cooking== dinner now."]),
        ]),
        ("STEP 3", "서술형", [
            Q("두 문장의 의미가 같도록 빈칸을 완성하시오.  I couldn't help laughing. = I couldn't but ______.",
              "laugh", "cannot but + 동사원형 = cannot help V-ing", lines=1),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  I'm looking forward to hear from you soon.", "hear → hearing",
              "look forward to의 to는 전치사", lines=1),
            Q("우리말과 같도록 주어진 단어를 활용하여 영작하시오.  나는 그 게임을 하는 데 3시간을 썼다. (spend, play)",
              "I spent three hours playing the game.", "spend + 시간 + V-ing", lines=1),
        ]),
    ]),
]
