from textbook.blocks import *

GOALS = [
    "부사절을 분사구문으로 바꾸는 3단계를 익힌다.",
    "분사구문의 의미(시간·이유·조건·양보·동시동작)를 문맥에 맞게 해석한다.",
    "완료형·수동형·독립분사구문, with + O + 분사 구문을 정확히 쓴다.",
]

INTRO = "분사구문은 **'접속사 + 주어 + 동사'로 된 부사절을 분사로 짧게 줄인 것**입니다. 글을 간결하게 만들어 주기 때문에 수능·내신 독해 지문에 매우 자주 등장합니다."

BLOCKS = [
    H("1. 분사구문 만드는 3단계"),
    TABLE(
        ["단계", "방법", "예시"],
        [
            ["**①**", "접속사를 지운다 (의미를 분명히 하려면 남겨도 됨)", "~~When~~ he saw me, he ran away."],
            ["**②**", "주절과 주어가 같으면 부사절의 주어를 지운다", "~~he~~ saw me, he ran away."],
            ["**③**", "동사를 V-ing로 바꾼다 (be동사 → Being, 보통 생략)", "**Seeing** me, he ran away."],
        ],
        widths=[10, 48, 42], center=[0],
    ),
    PARSE([("Seeing me,", "M"), ("he", "S"), ("ran away", "V")], "나를 보자, 그는 도망쳤다."),
    TIP("주어가 다르면 지우지 않는다", [
        "주절과 부사절의 주어가 다르면 주어를 남긴다 → 독립분사구문 (아래 5번)",
    ]),

    H("2. 분사구문의 의미"),
    TABLE(
        ["의미", "원래 접속사", "예문"],
        [
            ["**시간**", "when, while, after, as", "**Walking** down the street, I met an old friend. (= While I was walking …)"],
            ["**이유**", "because, as, since", "**Feeling** tired, I went to bed early. (= Because I felt tired …)"],
            ["**조건**", "if", "**Turning** left, you'll find the bank. (= If you turn left …)"],
            ["**양보**", "although, though", "**Living** next door, I rarely see him. (= Although I live next door …)"],
            ["**동시동작·연속**", "and, as", "She sat on the bench, **reading** a book. (= and she read …)"],
        ],
        widths=[16, 22, 62],
    ),
    NOTE("양보의 분사구문", ["양보의 의미는 문맥만으로 알기 어려워 접속사를 남기는 경우가 많습니다.",
                       "**Though** living next door, I rarely see him."]),

    H("3. 부정 · 완료형 · 수동형"),
    TABLE(
        ["형태", "언제 쓰나", "예문"],
        [
            ["**Not / Never** + V-ing", "부정", "**Not knowing** what to do, I called my mom."],
            ["**Having p.p.**", "부사절이 주절보다 **이전** 시제", "**Having finished** my work, I went out. (= After I had finished …)"],
            ["**(Being) p.p.**", "주어가 동작을 **당함** (Being 생략)", "**(Being) Written** in easy English, the book sells well."],
            ["**(Having been) p.p.**", "수동 + 이전 시제", "**(Having been) Built** long ago, the house needs repair."],
        ],
        widths=[22, 30, 48],
    ),
    WARN([
        ("~~Seeing~~ from the sky, the island looks like a heart.", "++Seen++ from the sky, the island looks like a heart.",
         "섬이 '보여지는' 것 → 수동 p.p."),
        ("~~Writing~~ in a hurry, the letter had many mistakes.", "++Written++ in a hurry, the letter had many mistakes.",
         "편지가 '쓰인' 것 → p.p."),
        ("~~Having not~~ eaten breakfast, I'm hungry.", "++Not having eaten++ breakfast, I'm hungry.",
         "부정어는 분사 맨 앞"),
    ]),
    TIP("능동(V-ing)인가 수동(p.p.)인가?", [
        "주절의 주어를 분사구문의 주어로 놓고 판단!",
        "(The island) **is seen** from the sky → 수동 → Seen",
        "(I) **saw** the island → 능동 → Seeing",
    ]),

    H("4. 접속사를 남긴 분사구문"),
    EX([
        ("**While staying** in London, I visited the British Museum.", "런던에 머무는 동안, 나는 대영박물관을 방문했다."),
        ("**After finishing** the test, he left the room.", "시험을 마친 후, 그는 교실을 나갔다."),
        ("**When asked** about it, she just smiled.", "그것에 대해 질문을 받자, 그녀는 그냥 웃었다. (수동)"),
    ]),

    H("5. 독립분사구문 / 비인칭 독립분사구문"),
    P("부사절과 주절의 주어가 **다르면** 분사 앞에 주어를 남깁니다."),
    EX([
        ("**It being** sunny, we went on a picnic.", "날씨가 화창해서 우리는 소풍을 갔다. (= Because it was sunny …)"),
        ("**The work done**, we went home.", "일이 끝나서 우리는 집에 갔다. (= After the work was done …)"),
    ]),
    TABLE(
        ["비인칭 독립분사구문 (주어가 일반인 → 생략)", "의미"],
        [
            ["**Generally speaking**", "일반적으로 말하면"],
            ["**Frankly speaking**", "솔직히 말하면"],
            ["**Judging from** ~", "~로 판단하건대"],
            ["**Considering** ~", "~을 고려하면"],
            ["**Speaking of** ~", "~에 대해 말하자면"],
        ],
        widths=[50, 50],
    ),

    H("6. with + 목적어 + 분사  (~한 채로)"),
    P("동시에 일어나는 상황을 묘사합니다. 목적어와 분사가 **능동이면 V-ing, 수동이면 p.p.** 를 씁니다."),
    EX([
        ("He was listening to music **with his eyes closed**.", "그는 눈을 감은 채 음악을 듣고 있었다. (눈이 감긴 → p.p.)"),
        ("She stood there **with her hair blowing** in the wind.", "그녀는 머리카락을 바람에 날리며 서 있었다. (머리가 날리는 → V-ing)"),
        ("Don't speak **with your mouth full**.", "입에 음식을 가득 넣은 채 말하지 마. (형용사도 가능)"),
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("밑줄 친 부분을 분사구문으로 바꾸시오.  ==Because I was sick==, I stayed home.", "(Being) Sick, I stayed home.",
              "be동사 → Being (생략 가능)"),
            Q("밑줄 친 부분을 분사구문으로 바꾸시오.  ==When she heard the news==, she cried.", "Hearing the news, she cried.", ""),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Leaving / Left) alone, the baby started to cry.", "Left",
              "아기가 '홀로 남겨진' 것 → 수동"),
            Q("괄호 안에서 알맞은 것을 고르시오.  He sat with his legs (crossing / crossed).", "crossed", "다리가 '꼬인' 상태"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  (Having lost / Losing) my key yesterday, I can't open the door now.", "Having lost",
              "잃어버린 것(어제)이 문을 못 여는 것(지금)보다 이전"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Not knowing / Knowing not) his address, I couldn't write to him.", "Not knowing",
              "부정어는 분사 앞"),
            Q("다음 문장의 밑줄 친 분사구문과 의미가 같은 것은?  ==Turning to the right==, you will see the post office.", "②",
              "명령·미래 주절 → 조건",
              options=["Because you turn to the right", "If you turn to the right",
                       "Although you turn to the right", "After you turned to the right"]),
            Q("다음 중 어법상 틀린 문장은?", "③",
              "③ 날씨(The weather)와 주절의 주어 we가 다르므로 주어를 남겨야 함 → The weather being fine, we went hiking.",
              options=["Generally speaking, boys are taller than girls.", "Built in 1900, the bridge is very old.",
                       "Being fine, we went hiking.", "Walking along the beach, I found a shell."]),
        ]),
        ("STEP 3", "서술형", [
            Q("분사구문을 부사절로 바꿔 쓰시오.  Having read the book before, I know the story.",
              "Because(As) I have read(had read / read) the book before, I know the story.",
              "완료 분사구문 → 주절보다 이전 시제", lines=1),
            Q("어법상 틀린 부분을 찾아 고쳐 쓰시오.  Compared to last year, the prices have risen. Comparing with hers, my essay is short.",
              "Comparing → Compared", "my essay가 '비교되는' 것 → 수동 p.p.", lines=1),
            Q("우리말과 같도록 with를 활용하여 영작하시오.  그는 TV를 켜 둔 채로 잠이 들었다. (fall asleep, turn on)",
              "He fell asleep with the TV turned on.", "TV가 '켜진' 상태 → p.p.", lines=1),
        ]),
    ]),
]
