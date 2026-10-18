"""Unit 12 분사 실전 TEST (★★ → 15문항, 객관식 9 / 서술형 6, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "분사",
    "time": "30분",
    "items": [
        MC("빈칸에 들어갈 말로 알맞은 것은?  The movie was really ______. I want to see it again.",
           ["excite", "exciting", "excited", "to excite", "excites"],
           2, "영화가 흥분을 '일으키는' 쪽 → -ing", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  The language ______ in Mexico is Spanish.",
           ["speak", "speaking", "spoken", "to speak", "spoke"],
           3, "언어는 '말해지는' 대상 → p.p. 후치수식", level="기본", points=6),
        MC("빈칸에 들어갈 말로 알맞은 것은?  There is a girl ______ under the tree.",
           ["sat", "sits", "sit", "sitting", "to sitting"],
           4, "소녀가 '앉아 있는' 능동·진행 → V-ing 후치수식", level="기본", points=6),
        MC("밑줄 친 부분이 어법상 틀린 것은?",
           ["The ==confusing== students asked many questions.", "The news was ==shocking==.",
            "I was ==satisfied== with the result.", "It was a ==boring== lecture.", "She looked ==surprised==."],
           1, "학생들이 혼란을 '느끼는' 쪽 → confused", points=6),
        MC("다음 중 어법상 옳은 것은?",
           ["I found the door lock.", "Don't leave the water running.", "The man stood there was my uncle.",
            "I heard my name calling.", "The students were interesting in the movie."],
           2, "① 문이 잠긴 → locked ③ 본동사는 was → standing ④ 이름이 불리는 → called ⑤ 흥미를 느낌 → interested",
           points=6),
        MC("다음 문장과 의미가 같은 것은?  Look at the boy who is playing the guitar.",
           ["Look at the boy played the guitar.", "Look at the boy is playing the guitar.",
            "Look at the boy to play the guitar.", "Look at the playing the guitar boy.",
            "Look at the boy playing the guitar."],
           5, "관계대명사 + be 생략 → 현재분사 후치수식 (꾸미는 말이 길면 명사 뒤)", points=6),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "노래가 감동을 '일으키는' 쪽 → moving",
           points=6,
           passage="Yesterday I went to a concert with my friends. The concert hall was full of ==ⓐ excited== fans. "
                   "The singer ==ⓑ standing== on the stage sang beautifully. Her new song was really ==ⓒ moved==. "
                   "After the concert, we bought a T-shirt ==ⓓ signed== by her. It was an ==ⓔ amazing== night."),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           4, "케이크는 '장식되는' 대상 → decorated",
           level="상", points=6,
           passage="My uncle has a small bakery ==ⓐ located== near the station. There are always many people "
                   "==ⓑ waiting== in line. The smell of bread ==ⓒ baking== in the oven makes everyone hungry. Last "
                   "week, he made a cake ==ⓓ decorating== with fresh strawberries. Customers were ==ⓔ satisfied== "
                   "with it."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           3, "옳은 것: ⓐ ⓒ ⓓ / ⓑ 본동사는 is → dancing ⓔ 경기가 흥분을 일으킴 → exciting",
           level="상", hard=True, points=6,
           passage="ⓐ I found the box broken.\nⓑ The girl danced on the stage is my sister.\n"
                   "ⓒ We were disappointed with the ending.\nⓓ Fallen leaves covered the road.\n"
                   "ⓔ The game was so excited that I couldn't sleep."),

        WR("분사를 이용하여 다음 문장을 바꿔 쓰시오.  The man who is waiting at the door is my uncle.",
           "The man waiting at the door is my uncle.", "관계대명사 + be 생략 → 현재분사 후치수식",
           points=7, lines=1),
        WR("두 문장을 분사를 이용하여 한 문장으로 바꿔 쓰시오.\n"
           "This is a letter. It was written by my grandfather 50 years ago.",
           "This is a letter written by my grandfather 50 years ago.", "편지는 '쓰여진' 대상 → p.p. 후치수식",
           points=7, lines=2),
        WR("우리말과 같도록 <조건>에 맞게 영작하시오.  그 결과는 실망스러웠다.",
           "The result was disappointing.", "결과가 실망을 '일으키는' 쪽 → -ing",
           points=8, lines=1, conditions=["disappoint, result를 활용할 것", "4단어로 쓸 것"]),
        WR("다음 문장에서 어법상 틀린 부분을 찾아 고치고, 그 이유를 쓰시오.  I was very boring during the long meeting.",
           "boring → bored / 주어 I가 지루함을 '느끼는' 쪽이므로 과거분사를 쓴다.",
           "일으키면 -ing, 느끼면 p.p.", level="상", points=8, lines=2),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "drawing → drawn / interesting → interested",
           "그림은 '그려진' 대상 → p.p. / 동생이 흥미를 '느끼는' 쪽 → p.p.",
           level="상", hard=True, points=8, lines=2,
           passage="Last weekend, I visited a museum with my family. We saw many paintings drawing by famous "
                   "artists. One painting showing a girl with a red umbrella was my favorite. My little brother was "
                   "so interesting in the old coins that he didn't want to leave. It was a satisfying day for all "
                   "of us."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "I found the window broken.", "창문이 '깨진' 상태 → 목적격보어 자리에 p.p.",
           level="상", points=8, lines=1, conditions=["find, the window, break를 활용할 것", "5단어로 쓸 것"],
           passage="When I came back home after the trip, I was shocked. ==나는 창문이 깨져 있는 것을 발견했다.== "
                   "Luckily, nothing was stolen."),
    ],
}
