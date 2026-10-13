from textbook.blocks import *

GOALS = [
    "부사절을 분사구문으로 바꾸는 3단계를 익힌다.",
    "V-ing / p.p. / having p.p. 중 알맞은 형태를 고른다.",
]

INTRO = "분사구문은 **부사절을 짧게 줄인 것**. 만드는 순서 3단계만 기억하면 됩니다."

BLOCKS = [
    TABLE(
        ["만드는 순서", "설명"],
        [
            ["**1**", "접속사를 지운다. (필수 아님)"],
            ["**2**", "주절의 주어와 부사절의 주어가 같으면 부사절의 주어를 지운다."],
            ["**3**", "동사를 V-ing로 바꾼다. 필요하면 having p.p., being p.p.도 가능"],
        ],
        widths=[16, 84], center=[0],
    ),
    EX([
        ("When he broke the window, he ran away.", "부사절"),
        ("→ **Breaking** the window, he ran away.", "분사구문"),
    ], title="예시"),
    PILGI([
        "주의: 자동사·타동사·수동 여부에 따라 {{V-ing}} / {{p.p.}} 선택이 달라질 수 있습니다.",
        "주어가 다르면 주어를 {{지우지 않는다}} (독립분사구문).",
        "부사절이 주절보다 먼저 일어났으면 {{having p.p.}}",
    ]),
    CHAIN([
        ("부사절", "**When he broke** the window, he ran away.", None),
        ("① 접속사 X", "~~When~~ he broke the window, he ran away.", None),
        ("② 주어 X", "~~he~~ broke the window, he ran away.", "주절 주어 he와 같음"),
        ("③ V-ing", "**Breaking** the window, he ran away.", None),
        ("먼저 일어남", "**Having broken** the window, he ran away.", "깬 것 → 도망 (순서 강조)"),
        ("수동", "**(Being) Broken**, the window was replaced.", "창문이 '깨진' 것 → p.p."),
    ], title="When he broke the window, he ran away."),
    QUICK([
        "주절의 주어를 분사 앞에 넣어 본다 → **주어가 하면 V-ing, 당하면 p.p.**",
        "부정 → **Not / Never** + 분사",
    ]),
    LINK(7, "Having eaten lunch, I'm full now. (준동사 완료형)"),
    LINK(10, "분사의 능동/수동 기준과 같다."),

    STEPUP(),
    TABLE(
        ["의미", "원래 접속사", "예문"],
        [
            ["시간", "when, while, after", "**Walking** down the street, I met an old friend."],
            ["이유", "because, as", "**Feeling** tired, I went to bed early."],
            ["조건", "if", "**Turning** left, you'll find the bank."],
            ["양보", "although", "**Though living** next door, I rarely see him."],
            ["동시동작", "and, as", "She sat on the bench, **reading** a book."],
        ],
        widths=[14, 22, 64],
    ),
    WARN([
        ("~~Seeing~~ from the sky, the island looks like a heart.", "++Seen++ from the sky, …", "섬이 '보여지는' 것"),
        ("~~Having not~~ eaten breakfast, I'm hungry.", "++Not having eaten++ breakfast, …", "not은 맨 앞"),
    ]),
    EX([
        ("**It being** sunny, we went on a picnic.", "독립분사구문 (주어가 다름)"),
        ("**Generally speaking**, / **Judging from** ~", "비인칭 독립분사구문"),
        ("He listened to music **with his eyes closed**.", "with + O + p.p. (눈이 감긴 채)"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("분사구문으로 바꾸시오.  When he broke the window, he ran away.", "Breaking the window, he ran away.", ""),
            Q("분사구문으로 바꾸시오.  Because I was sick, I stayed home.", "(Being) Sick, I stayed home.", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Leaving / Left) alone, the baby started to cry.", "Left", "아기가 남겨진"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  (Having lost / Losing) my key yesterday, I can't open the door now.",
              "Having lost", "먼저 일어남"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Not knowing / Knowing not) his address, I couldn't write.", "Not knowing", ""),
            Q("밑줄 친 분사구문과 의미가 같은 것은?  ==Turning to the right==, you will see the post office.", "②", "조건",
              options=["Because you turn to the right", "If you turn to the right",
                       "Although you turn to the right", "After you turned to the right"]),
        ]),
        ("STEP 3", "서술형", [
            Q("부사절로 바꾸시오.  Having read the book before, I know the story.",
              "Because(As) I have read the book before, I know the story.", "", lines=1),
            Q("with를 활용하여 영작하시오.  그는 TV를 켜 둔 채로 잠이 들었다.", "He fell asleep with the TV turned on.", "",
              lines=1),
        ]),
    ]),
]
