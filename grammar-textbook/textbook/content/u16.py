from textbook.blocks import *
from textbook import figs as F

GOALS = []
INTRO = ""

BLOCKS = [
    TABLE(
        ["조동사", "의미", "바꿔 쓰기", "예문"],
        [
            ["**can**", "능력 / 허가 / 가능성", "be able to", "She **can** speak three languages.\n그녀는 3개 국어를 할 수 있다."],
            ["**may**", "허가 / 약한 추측", "–", "It **may** rain tonight.\n오늘 밤 비가 올지도 모른다."],
            ["**must**", "의무 / 강한 추측", "have to (의무)", "You **must** wear a seat belt.\n안전벨트를 매야 한다."],
            ["**should**", "의무 · 충고", "ought to", "You **should** see a doctor.\n병원에 가 보는 게 좋겠다."],
            ["**had better**", "~하는 게 낫다 (경고)", "–", "You **had better** hurry.\n서두르는 게 좋을 거야."],
            ["**used to**", "(예전에) ~하곤 했다 / ~였다", "would (동작만)", "I **used to** live in Busan.\n나는 예전에 부산에 살았다."],
        ],
        widths=[15, 25, 18, 42], caption="조동사 한눈에",
    ),
    PILGI([
        "조동사 + {{동사원형}}  (주어가 3인칭 단수여도 -s X)",
        "조동사는 두 개 연달아 X → will can ✗ → will {{be able to}}",
        "must의 과거 = {{had to}}  /  must not = ~하면 안 된다 (금지)  /  don't have to = ~할 {{필요 없다}}",
        "used to = 동작·상태 모두 / would = {{동작}}만 (과거 습관)",
    ]),
    H("조동사 + have p.p. = 과거에 대한 추측·후회"),
    FIG(F.stacks(
        F.stack("강한 추측", ["must", "have p.p."], "must have p.p.", "He <b>must have been</b> tired.", "그는 피곤했던 것이 틀림없다."),
        F.stack("약한 추측", ["may (might)", "have p.p."], "may have p.p.", "She <b>may have missed</b> the bus.", "그녀는 버스를 놓쳤을지도 모른다."),
        F.stack("부정 추측", ["can't", "have p.p."], "can't have p.p.", "He <b>can't have said</b> that.", "그가 그 말을 했을 리가 없다."),
        F.stack("후회·유감", ["should", "have p.p."], "should have p.p.", "I <b>should have studied</b> harder.", "더 열심히 공부했어야 했는데. (안 했다)"),
    ), "마네킹 + 옷 응용: 조동사(마네킹) + have p.p.(완료 옷) = 과거 쪽을 가리킨다"),
    TABLE(
        ["형태", "뜻"],
        [
            ["**must** have p.p.", "~했음에 틀림없다"],
            ["**may / might** have p.p.", "~했을지도 모른다"],
            ["**can't (cannot)** have p.p.", "~했을 리가 없다"],
            ["**should** have p.p.", "~했어야 했는데 (안 했다)"],
            ["**shouldn't** have p.p.", "~하지 말았어야 했는데 (했다)"],
            ["**need not** have p.p.", "~할 필요가 없었는데 (했다)"],
        ],
        widths=[40, 60],
    ),
    CHAIN([
        ("현재 추측", "He **must be** tired.", "그는 피곤한 게 틀림없다."),
        ("과거 추측", "He **must have been** tired yesterday.", "be → have been (과거로 보내기)"),
        ("부정", "He **can't have been** tired.", "must의 반대 → can't"),
        ("후회", "I **should have let** him rest.", "그를 쉬게 했어야 했는데."),
    ], title="He must be tired"),
    QUICK([
        "조동사 + have p.p. → 무조건 **과거 일**",
        "must / may / can't + have p.p. → **추측**  /  should(n't) + have p.p. → **후회**",
        "must not(금지) ≠ don't have to(불필요)",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  She can (speak / speaks) Chinese.", "speak", "조동사 + 동사원형"),
            Q("괄호 안에서 알맞은 것을 고르시오.  You (must not / don't have to) bring lunch. Lunch is free.", "don't have to",
              "~할 필요 없다"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I will (can / be able to) help you tomorrow.", "be able to", "조동사 연달아 X"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  The ground is wet. It (must rain / must have rained) last night.", "must have rained",
              "last night = 과거 추측"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I failed the test. I (should study / should have studied) harder.",
              "should have studied", "과거 일에 대한 후회"),
            Q("다음 중 어법상 틀린 것은?", "③", "would는 과거 '상태'에 쓰지 않는다 → There used to be a tree here.",
              options=["I used to play soccer after school.", "He can't have lied to me.",
                       "There would be a big tree here.", "You had better take an umbrella."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("과거 추측으로 바꾸시오.  She must be at home. (last night)", "She must have been at home last night.", "", lines=1),
            Q("우리말과 같도록 영작하시오.  그가 그 창문을 깼을 리가 없다. (break)", "He can't have broken the window.", "", lines=1),
            Q("같은 뜻이 되도록 완성하시오.  I'm sorry that I didn't call you. = I ______ you.", "should have called",
              "후회 → should have p.p.", lines=1),
        ]),
    ]),
]
