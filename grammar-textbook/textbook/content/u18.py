from textbook.blocks import *
from textbook import figs as F

GOALS = []
INTRO = ""

BLOCKS = [
    TABLE(
        ["접속사", "뒤 절", "해석", "예문"],
        [
            ["**that**", "완전", "~라는 것", "I know **that** he is honest.\n나는 그가 정직하다는 것을 안다."],
            ["**whether / if**", "완전", "~인지 (아닌지)", "I wonder **whether** he will come.\n그가 올지 궁금하다."],
            ["**의문사** (who, what, when, where, why, how)", "의문사 + S + V", "누가 / 무엇을 / 언제 … ~하는지",
             "Tell me **where** you live.\n어디 사는지 말해 줘."],
            ["**what** (관계대명사)", "불완전", "~하는 것", "**What** he said is true.\n그가 말한 것은 사실이다."],
        ],
        widths=[24, 14, 22, 40], caption="명사절 = 주어 · 목적어 · 보어 자리에 들어가는 절",
    ),
    FIG(F.decision([
        ("뒤 절이 불완전한가? (주어·목적어 빠짐)", "what (또는 의문사 who·what·which)", None),
        ("확실한 내용인가?", "that", "불확실하면 ↓"),
        ("'~인지 아닌지'인가?", "whether / if", "정보(누가·언제·어디·왜·어떻게)를 묻는다면 ↓"),
        ("빈칸에 의문사 의미가 필요한가?", "의문사 + S + V", None),
    ], "명사절 접속사 고르기")),
    PILGI([
        "명사절 접속사 = that / {{whether(if)}} / 의문사 / what",
        "that 뒤는 {{완전}}, what 뒤는 {{불완전}}",
        "if는 {{주어}} 자리·전치사 뒤 X → whether만 가능",
        "간접의문문 어순: 의문사 + {{S + V}}  (의문문 어순 X)",
        "think / believe / guess / suppose → 의문사가 문장 {{맨 앞}}",
    ]),
    CHAIN([
        ("의문문", "**Where does he live?**", "그는 어디 사니?"),
        ("간접의문문", "I don't know **where he lives**.", "의문사 + S + V (does 사라짐)"),
        ("의문문 안", "Do you know **where he lives**?", "그가 어디 사는지 아니? (Yes/No로 답함)"),
        ("think류", "**Where** do you think **he lives**?", "그가 어디 산다고 생각해? (의문사 맨 앞)"),
    ], title="Where does he live?"),
    CHAIN([
        ("Yes/No 의문문", "**Is he** at home?", None),
        ("간접의문문", "I wonder **whether(if) he is** at home.", "의문사가 없으면 whether / if"),
    ], title="Is he at home?"),
    QUICK([
        "의문사 뒤 → **S + V** (does·did 사라지고 동사 원래 모양)",
        "주어 자리 · 전치사 뒤 · or not 바로 앞 → **whether** (if X)",
        "Do you know ~? → 의문사 뒤로 / Do you think ~? → 의문사 **맨 앞**",
    ]),

    CHECK([
        ("STEP 1", "기본 확인", [
            Q("괄호 안에서 알맞은 것을 고르시오.  I believe (that / what) she is right.", "that", "뒤 절 완전"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (That / What) I want is a long vacation.", "What", "want의 목적어 없음"),
            Q("괄호 안에서 알맞은 것을 고르시오.  I don't know (when the store opens / when does the store open).",
              "when the store opens", "간접의문문 어순"),
        ]),
        ("STEP 2", "어법 선택", [
            Q("괄호 안에서 알맞은 것을 고르시오.  (Whether / If) he will come is not certain.", "Whether", "주어 자리 → whether"),
            Q("괄호 안에서 알맞은 것을 고르시오.  (Do you think who / Who do you think) will win?", "Who do you think",
              "think류 → 의문사 맨 앞"),
            Q("다음 중 어법상 틀린 것은?", "②", "간접의문문 → Can you tell me where the station is?",
              options=["I wonder if it will rain tomorrow.", "Can you tell me where is the station?",
                       "What he said surprised everyone.", "I'm not sure whether or not she knows."]),
        ]),
        ("STEP 3", "바꿔 쓰기", [
            Q("한 문장으로 바꾸시오.  I don't know. + Why was she late?", "I don't know why she was late.", "", lines=1),
            Q("한 문장으로 바꾸시오.  Do you think? + What does he want?", "What do you think he wants?", "think류 → 의문사 맨 앞", lines=1),
            Q("한 문장으로 바꾸시오.  I wonder. + Does she like me?", "I wonder whether(if) she likes me.", "", lines=1),
        ]),
    ]),
]
