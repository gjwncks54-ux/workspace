from textbook.blocks import *

TITLE = "부록"

IRREGULAR = [
    ("A-A-A", [("cut", "cut", "cut", "자르다"), ("put", "put", "put", "놓다"), ("set", "set", "set", "놓다, 정하다"),
               ("hit", "hit", "hit", "치다"), ("let", "let", "let", "~하게 하다"), ("read", "read[red]", "read[red]", "읽다"),
               ("cost", "cost", "cost", "(비용이) 들다"), ("hurt", "hurt", "hurt", "다치게 하다"), ("shut", "shut", "shut", "닫다")]),
    ("A-B-A", [("come", "came", "come", "오다"), ("become", "became", "become", "~이 되다"), ("run", "ran", "run", "달리다")]),
    ("A-B-B", [("bring", "brought", "brought", "가져오다"), ("buy", "bought", "bought", "사다"), ("catch", "caught", "caught", "잡다"),
               ("teach", "taught", "taught", "가르치다"), ("think", "thought", "thought", "생각하다"), ("feel", "felt", "felt", "느끼다"),
               ("find", "found", "found", "찾다"), ("have", "had", "had", "가지다"), ("hear", "heard", "heard", "듣다"),
               ("keep", "kept", "kept", "유지하다"), ("leave", "left", "left", "떠나다"), ("lose", "lost", "lost", "잃다"),
               ("make", "made", "made", "만들다"), ("meet", "met", "met", "만나다"), ("pay", "paid", "paid", "지불하다"),
               ("say", "said", "said", "말하다"), ("sell", "sold", "sold", "팔다"), ("send", "sent", "sent", "보내다"),
               ("sit", "sat", "sat", "앉다"), ("sleep", "slept", "slept", "자다"), ("spend", "spent", "spent", "쓰다"),
               ("stand", "stood", "stood", "서다"), ("tell", "told", "told", "말하다"), ("understand", "understood", "understood", "이해하다"),
               ("win", "won", "won", "이기다"), ("hang", "hung", "hung", "걸다"), ("lay", "laid", "laid", "놓다, 낳다")]),
    ("A-B-C", [("be", "was/were", "been", "~이다"), ("begin", "began", "begun", "시작하다"), ("break", "broke", "broken", "깨다"),
               ("choose", "chose", "chosen", "고르다"), ("do", "did", "done", "하다"), ("drink", "drank", "drunk", "마시다"),
               ("drive", "drove", "driven", "운전하다"), ("eat", "ate", "eaten", "먹다"), ("fall", "fell", "fallen", "떨어지다"),
               ("fly", "flew", "flown", "날다"), ("forget", "forgot", "forgotten", "잊다"), ("get", "got", "got(ten)", "얻다"),
               ("give", "gave", "given", "주다"), ("go", "went", "gone", "가다"), ("grow", "grew", "grown", "자라다"),
               ("know", "knew", "known", "알다"), ("lie", "lay", "lain", "눕다"), ("ride", "rode", "ridden", "타다"),
               ("rise", "rose", "risen", "오르다"), ("see", "saw", "seen", "보다"), ("show", "showed", "shown", "보여 주다"),
               ("sing", "sang", "sung", "노래하다"), ("speak", "spoke", "spoken", "말하다"), ("steal", "stole", "stolen", "훔치다"),
               ("swim", "swam", "swum", "수영하다"), ("take", "took", "taken", "가져가다"), ("throw", "threw", "thrown", "던지다"),
               ("wear", "wore", "worn", "입다"), ("write", "wrote", "written", "쓰다")]),
]

BLOCKS = [H("A. 불규칙 동사 변화표")]
for kind, rows in IRREGULAR:
    BLOCKS.append(TABLE(["원형", "과거", "과거분사", "뜻"], [list(r) for r in rows],
                        widths=[25, 25, 25, 25], caption=f"{kind}형", center=[0, 1, 2]))
BLOCKS.append(NOTE("헷갈리는 동사 쌍", [
    "lie(눕다) – lay – lain  /  lay(놓다, 낳다) – laid – laid  /  lie(거짓말하다) – lied – lied",
    "rise(오르다, 자동사) – rose – risen  /  raise(올리다, 타동사) – raised – raised",
    "find(찾다) – found – found  /  found(설립하다) – founded – founded",
]))

BLOCKS += [
    H("B. 문법 용어 사전"),
    TABLE(
        ["용어", "영어", "뜻", "관련 단원"],
        [
            ["주어 (S)", "Subject", "문장의 주체", "2"],
            ["동사 (V)", "Verb", "동작·상태", "1, 2"],
            ["목적어 (O)", "Object", "동작의 대상", "2, 3"],
            ["보어 (C)", "Complement", "주어·목적어를 설명", "2, 3"],
            ["수식어 (M)", "Modifier", "꾸며 주는 말", "2"],
            ["간접목적어 / 직접목적어", "Indirect / Direct Object", "~에게 / ~을", "3"],
            ["목적격보어 (O.C)", "Object Complement", "목적어를 설명", "3, 4"],
            ["자동사 / 타동사", "Intransitive / Transitive Verb", "목적어 X / 목적어 O", "3"],
            ["사역동사", "Causative Verb", "~하게 시키다", "4"],
            ["지각동사", "Perception Verb", "보다·듣다·느끼다", "4"],
            ["시제", "Tense", "동작의 시간", "5"],
            ["완료", "Perfect", "have p.p.", "5"],
            ["진행", "Progressive", "be V-ing", "5"],
            ["능동태 / 수동태", "Active / Passive Voice", "하다 / 당하다", "6"],
            ["준동사", "Verbal", "to부정사·동명사·분사", "7"],
            ["의미상 주어", "Sense Subject", "준동사의 행위자", "7, 13"],
            ["to부정사", "To-infinitive", "to + 동사원형", "8"],
            ["원형부정사", "Bare Infinitive", "to 없는 동사원형", "4, 8"],
            ["동명사", "Gerund", "V-ing (명사 역할)", "9"],
            ["현재분사 / 과거분사", "Present / Past Participle", "V-ing / p.p.", "10"],
            ["분사구문", "Participle Clause", "부사절 축약", "11"],
            ["선행사", "Antecedent", "관계사가 꾸미는 명사", "12"],
            ["관계대명사 / 관계부사", "Relative Pronoun / Adverb", "who·which / when·where", "12"],
            ["가주어 / 진주어", "Dummy / Real Subject", "it / to V·that절", "13"],
            ["강조구문", "Cleft Sentence", "It is ~ that", "13"],
            ["도치", "Inversion", "주어-동사 순서 바뀜", "14"],
            ["가정법", "Subjunctive Mood", "사실과 반대 가정", "15"],
        ],
        widths=[28, 32, 26, 14], center=[3],
    ),
]
