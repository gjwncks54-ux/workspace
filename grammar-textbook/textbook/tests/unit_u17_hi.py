"""Unit 18 비교 고등 실전 TEST (모듈 u17 / 10문항, 객관식 6 / 서술형 4, 100점)"""
from textbook.blocks import MC, WR

TEST = {
    "title": "비교",
    "time": "25분",
    "items": [
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           3, "as ~ as 사이에는 원급 → as long as",
           level="상", points=8,
           passage="The cheetah is ==ⓐ the fastest== land animal in the world. It can run ==ⓑ much faster== than a "
                   "lion. However, it cannot keep its top speed ==ⓒ as longer as== other animals. The faster it "
                   "runs, ==ⓓ the more== energy it uses. In fact, a cheetah is ==ⓔ much weaker== than a lion in a "
                   "fight."),
        MC("다음 글의 (A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?",
           ["mountain – highest – as", "mountains – highest – more", "mountain – high – as", "mountains – high – as",
            "mountain – highest – more"],
           1, "(A) any other + 단수명사 (B) the second + 최상급 (C) not as ~ as",
           level="상", hard=True, points=8,
           passage="Mt. Everest is higher than any other (A) [mountain / mountains] in the world. K2 is the second "
                   "(B) [high / highest] mountain. It is not (C) [as / more] high as Everest, but it is much more "
                   "dangerous to climb."),
        MC("다음 중 어법상 옳은 문장의 개수는?",
           ["1개", "2개", "3개", "4개", "5개"],
           4, "옳은 것: ⓐ ⓑ ⓒ ⓔ / ⓓ as ~ as 사이 원급 → as tall as",
           level="상", hard=True, points=8,
           passage="ⓐ This room is three times as large as mine.\nⓑ The more you know, the humbler you become.\n"
                   "ⓒ She is the smartest of all the students.\nⓓ No other student in my class is as taller as Jake.\n"
                   "ⓔ It's getting more and more expensive."),
        MC("다음 중 의미가 나머지 넷과 다른 것은?",
           ["Time is the most precious thing.", "Nothing is more precious than time.", "Nothing is as precious as time.",
            "Time is more precious than anything else.", "Time is not as precious as anything else."],
           5, "①~④는 '시간이 가장 소중하다', ⑤는 '시간은 다른 어떤 것만큼 소중하지 않다'", points=8),
        MC("다음 중 어법상 틀린 것은?",
           ["He is far older than he looks.", "Seoul is bigger than any other cities in Korea.",
            "This is the best movie I've ever seen.", "Please come as early as possible.",
            "The harder you try, the more you'll succeed."],
           2, "any other + 단수명사 → any other city", points=8),
        MC("다음 글의 밑줄 친 ⓐ~ⓔ 중 어법상 틀린 것은?",
           ["ⓐ", "ⓑ", "ⓒ", "ⓓ", "ⓔ"],
           5, "원급 비교 as + 원급 + as → as important as",
           level="상", points=8,
           passage="Many people believe that ==ⓐ the more== money they earn, the happier they will be. However, "
                   "studies show that money is ==ⓑ less important== than relationships. People with strong "
                   "friendships are ==ⓒ much happier== than those without them. Close friends may be ==ⓓ the "
                   "most== valuable thing in life. Spending time with friends is ==ⓔ as more important as== earning "
                   "money."),

        WR("다음 문장을 <조건>에 맞게 같은 뜻으로 바꿔 쓰시오.  Lake Baikal is the deepest lake in the world.",
           "No other lake in the world is as deep as Lake Baikal.", "No other + 단수명사 + as 원급 as",
           points=13, lines=1, conditions=["No other로 시작할 것", "as ~ as를 사용할 것"]),
        WR("두 문장을 배수 표현을 사용하여 한 문장으로 바꿔 쓰시오.  This bridge is 200 meters long. That bridge is 600 meters long.",
           "That bridge is three times as long as this bridge(this one).", "배수 + as + 원급 + as (three times longer than도 정답)",
           points=13, lines=1),
        WR("다음 글에서 어법상 틀린 부분 2개를 찾아 바르게 고쳐 쓰시오.",
           "as wider as → as wide as / planet → planets",
           "as ~ as 사이 원급 / all the other + 복수명사",
           level="상", hard=True, points=13, lines=2,
           passage="Jupiter is the largest planet in our solar system. It is more than eleven times as wider as "
                   "Earth. It is also heavier than all the other planet combined. The closer we look at Jupiter, "
                   "the more mysteries we find."),
        WR("다음 글의 밑줄 친 우리말을 <조건>에 맞게 영작하시오.",
           "The more he practiced, the better he played.", "The 비교급 + S + V, the 비교급 + S + V (well → better)",
           level="상", points=13, lines=1,
           conditions=["'The 비교급, the 비교급' 구문을 쓸 것", "practice, play well을 활용할 것"],
           passage="Jake has been taking piano lessons for five years. ==그는 연습하면 할수록 더 잘 연주했다.== Now he "
                   "plays in the school orchestra."),
    ],
}
