"""원본 손필기 노트의 도식을 HTML/SVG로 다시 그린 것.
색은 단원 파트 색(var(--c))을 따라간다."""

C = "var(--c)"
INK = "#1E2433"
SUB = "#5B6475"
MUTE = "#8A93A6"
RED = "#D64545"
FONT = 'font-family="Pretendard, sans-serif"'


def _svg(w, h, body):
    return (f'<svg class="fig-svg" viewBox="0 0 {w} {h}" width="100%" {FONT} '
            f'xmlns="http://www.w3.org/2000/svg">'
            f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            f'<marker id="ahc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:{C}"/></marker></defs>'
            f'{body}</svg>')


def _axis(y=100, x1=30, x2=610):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{INK}" stroke-width="1.6" marker-end="url(#ah)"/>'
            f'<text x="{x1}" y="{y + 30}" font-size="11" fill="{MUTE}">과거</text>'
            f'<text x="{x2 - 22}" y="{y + 30}" font-size="11" fill="{MUTE}">미래</text>')


def _now(x, y=100, label="현재"):
    return (f'<circle cx="{x}" cy="{y}" r="5.5" fill="{INK}"/>'
            f'<text x="{x}" y="{y + 24}" font-size="12" font-weight="800" text-anchor="middle" fill="{INK}">{label}</text>')


# ---------- 시제 타임라인 (Unit 05) ----------

def timeline_present_perfect():
    body = _axis()
    # 끊긴 과거 시점 (yesterday) — 과거시제
    body += (f'<circle cx="95" cy="100" r="5" fill="none" stroke="{RED}" stroke-width="1.6"/>'
             f'<text x="95" y="76" font-size="11" text-anchor="middle" fill="{RED}">yesterday</text>'
             f'<text x="95" y="62" font-size="10" text-anchor="middle" fill="{RED}">끊긴 점 → 과거시제</text>')
    # 선: since ~ 현재
    body += (f'<rect x="200" y="93" width="260" height="14" rx="3" style="fill:{C}" opacity=".85"/>'
             f'<line x1="200" y1="84" x2="200" y2="116" style="stroke:{C}" stroke-width="2.4"/>'
             f'<text x="200" y="134" font-size="12" font-weight="700" text-anchor="middle" style="fill:{C}">since + 시점</text>'
             f'<text x="200" y="149" font-size="10.5" text-anchor="middle" fill="{SUB}">(~부터)</text>'
             f'<path d="M200,78 L200,66 L460,66 L460,78" fill="none" stroke="{INK}" stroke-width="1.3"/>'
             f'<text x="330" y="58" font-size="12" font-weight="700" text-anchor="middle" fill="{INK}">for + 기간 (~동안)</text>')
    body += _now(460)
    body += (f'<text x="330" y="22" font-size="12.5" font-weight="800" text-anchor="middle" style="fill:{C}">'
             f'현재완료 = 지금까지 이어진 선 (have p.p.)</text>')
    return _svg(640, 160, body)


def timeline_past_perfect():
    body = _axis()
    pts = [(170, "e1", "had p.p.", True), (360, "e2", "V-ed", False)]
    for x, e, form, main in pts:
        col = f'style="fill:{C}"' if main else f'fill="{SUB}"'
        body += (f'<circle cx="{x}" cy="100" r="6" {col}/>'
                 f'<text x="{x}" y="86" font-size="13" font-weight="800" text-anchor="middle" fill="{INK}">{e}</text>'
                 f'<text x="{x}" y="126" font-size="12" font-weight="700" text-anchor="middle" {col}>({form})</text>')
    body += (f'<path d="M176,92 Q265,40 352,92" fill="none" style="stroke:{C}" stroke-width="1.6" marker-end="url(#ahc)"/>'
             f'<text x="265" y="48" font-size="11.5" text-anchor="middle" style="fill:{C}" font-weight="700">더 먼저 일어난 일</text>'
             f'<text x="360" y="146" font-size="10.5" text-anchor="middle" fill="{SUB}">과거 기준점</text>')
    body += _now(540)
    body += (f'<text x="320" y="22" font-size="12.5" font-weight="800" text-anchor="middle" style="fill:{C}">'
             f'과거완료 = 과거 기준점보다 더 이전 (had p.p.)</text>')
    return _svg(640, 160, body)


def timeline_future_perfect():
    body = _axis()
    body += (f'<rect x="250" y="88" width="250" height="24" rx="4" fill="none" style="stroke:{C}" '
             f'stroke-width="2" stroke-dasharray="6 4"/>'
             f'<line x1="250" y1="100" x2="500" y2="100" style="stroke:{C}" stroke-width="5" opacity=".55"/>'
             f'<line x1="500" y1="80" x2="500" y2="120" style="stroke:{C}" stroke-width="2.4"/>'
             f'<text x="500" y="72" font-size="12" font-weight="700" text-anchor="middle" style="fill:{C}">미래 기준점</text>'
             f'<text x="500" y="138" font-size="11.5" font-weight="700" text-anchor="middle" fill="{INK}">by / by the time / when</text>')
    body += _now(250)
    body += (f'<text x="320" y="22" font-size="12.5" font-weight="800" text-anchor="middle" style="fill:{C}">'
             f'미래완료 = 미래 기준점까지 완료 (will have p.p.)</text>')
    return _svg(640, 160, body)


# ---------- 마네킹 + 옷 (Unit 05·06) ----------

def mannequin_board():
    return '''<div class="mq">
  <div class="mq-col"><div class="mq-h">마네킹 <small>(시제)</small></div>
    <div class="mq-i">현재 <b>Vs</b></div><div class="mq-i">과거 <b>V-ed</b></div><div class="mq-i">미래 <b>will</b></div></div>
  <div class="mq-plus">+</div>
  <div class="mq-col"><div class="mq-h">옷 <small>(겹쳐 입기)</small></div>
    <div class="mq-i">완료 <b>have p.p.</b></div><div class="mq-i">진행 <b>be V-ing</b></div><div class="mq-i">수동태 <b>be V p.p.</b></div></div>
  <div class="mq-rule">입히는 법: 위 줄의 <b>뒷부분 모양</b>이 아래 줄 <b>첫 단어</b>의 모양을 정한다<br>
  (과거 + have → <b>had</b> / have p.p. + be → <b>been</b> / be V-ing + be → <b>being</b>)</div>
</div>'''


def stack(title, layers, result, ex=None, ko=None):
    """layers: 위에서부터 겹쳐 입는 옷 목록 (첫 줄은 마네킹)"""
    rows = "".join(f'<div class="st-r" style="padding-left:{i * 1.6}em">{l}</div>' for i, l in enumerate(layers))
    exs = f'<div class="st-ex">{ex}</div>' if ex else ""
    kos = f'<div class="st-ko">{ko}</div>' if ko else ""
    return (f'<div class="st"><div class="st-t">{title}</div><div class="st-body"><span class="st-plus">+</span>'
            f'<div class="st-rows">{rows}</div></div><div class="st-sum">{result}</div>{exs}{kos}</div>')


def stacks(*items):
    return '<div class="st-grid">' + "".join(items) + "</div>"


# ---------- 4형식 → 3형식 (Unit 03) ----------

def _chip(x, y, w, label, sub=None, color=None):
    style = f'style="fill:{color}"' if color else f'style="fill:{C}"'
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="6" {style}/>'
         f'<text x="{x + w / 2}" y="{y + 20}" font-size="13.5" font-weight="800" text-anchor="middle" fill="#fff">{label}</text>')
    if sub:
        s += f'<text x="{x + w / 2}" y="{y - 6}" font-size="11" text-anchor="middle" fill="{SUB}">{sub}</text>'
    return s


def dative_shift():
    b = (f'<text x="0" y="40" font-size="12.5" font-weight="800" fill="{INK}">4형식</text>'
         f'<text x="0" y="140" font-size="12.5" font-weight="800" fill="{INK}">3형식</text>')
    b += _chip(60, 20, 50, "S", color=INK) + _chip(120, 20, 50, "V", color=INK)
    b += _chip(180, 20, 90, "I.O", "~에게") + _chip(280, 20, 90, "D.O", "~을/를", "#2C9C6A")
    b += _chip(60, 120, 50, "S", color=INK) + _chip(120, 120, 50, "V", color=INK)
    b += _chip(180, 120, 90, "D.O", None, "#2C9C6A")
    b += (f'<rect x="280" y="120" width="110" height="30" rx="6" fill="#fff" style="stroke:{C}" stroke-width="2"/>'
          f'<text x="335" y="140" font-size="13" font-weight="800" text-anchor="middle" style="fill:{C}">to / for / of</text>')
    b += _chip(400, 120, 90, "I.O")
    b += (f'<path d="M325,52 C325,90 225,80 225,118" fill="none" stroke="#2C9C6A" stroke-width="2" marker-end="url(#ah)"/>'
          f'<path d="M225,52 C260,100 440,70 445,118" fill="none" style="stroke:{C}" stroke-width="2" marker-end="url(#ahc)"/>'
          f'<text x="510" y="100" font-size="11.5" fill="{SUB}">give·send·show·tell → <tspan font-weight="800" fill="{INK}">to</tspan></text>'
          f'<text x="510" y="118" font-size="11.5" fill="{SUB}">make·buy·cook → <tspan font-weight="800" fill="{INK}">for</tspan></text>'
          f'<text x="510" y="136" font-size="11.5" fill="{SUB}">ask → <tspan font-weight="800" fill="{INK}">of</tspan></text>')
    return _svg(660, 160, b)


# ---------- 사역동사 묶음 (Unit 04) ----------

def causative_board():
    return '''<div class="cz">
  <div class="cz-row"><div class="cz-v"><div>Make</div><div>Let</div></div><div class="cz-br">&gt;</div>
    <div class="cz-o"><span class="cz-circ">V</span> 동사원형</div></div>
  <div class="cz-row"><div class="cz-v"><div>Have</div></div><div class="cz-br">—</div>
    <div class="cz-o"><span class="cz-circ">V</span> 동사원형 / <b>V p.p.</b></div></div>
  <div class="cz-sep">준사역</div>
  <div class="cz-row"><div class="cz-v"><div>Help</div></div><div class="cz-br">—</div><div class="cz-o"><b>to V</b> / 동사원형</div></div>
  <div class="cz-row"><div class="cz-v"><div>Get</div></div><div class="cz-br">—</div><div class="cz-o"><b>to V</b> / <b>V p.p.</b></div></div>
</div>'''


# ---------- 분사 판단 흐름도 (Unit 04·13) ----------

def participle_flow():
    def box(x, y, w, t, fill="#fff", tc=INK, stroke=True):
        st = f'style="stroke:{C}" stroke-width="1.8"' if stroke else 'stroke="none"'
        return (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="{fill}" {st}/>'
                f'<text x="{x + w / 2}" y="{y + 22}" font-size="13.5" font-weight="800" text-anchor="middle" fill="{tc}">{t}</text>')

    def ans(x, y, t):
        return (f'<rect x="{x}" y="{y}" width="96" height="32" rx="16" style="fill:{C}"/>'
                f'<text x="{x + 48}" y="{y + 21}" font-size="14" font-weight="800" text-anchor="middle" fill="#fff">{t}</text>')
    b = box(40, 8, 150, "자동사인가?")
    b += f'<line x1="80" y1="42" x2="70" y2="96" stroke="{INK}" stroke-width="1.5" marker-end="url(#ah)"/>'
    b += f'<text x="62" y="70" font-size="13" font-weight="800" fill="{INK}">Y</text>'
    b += ans(20, 98, "~ing")
    b += f'<line x1="150" y1="42" x2="230" y2="96" stroke="{INK}" stroke-width="1.5" marker-end="url(#ah)"/>'
    b += f'<text x="198" y="66" font-size="13" font-weight="800" fill="{INK}">N</text>'
    b += box(190, 98, 180, "목적어가 있는가?")
    b += f'<line x1="240" y1="132" x2="225" y2="186" stroke="{INK}" stroke-width="1.5" marker-end="url(#ah)"/>'
    b += f'<text x="220" y="162" font-size="13" font-weight="800" fill="{INK}">Y</text>'
    b += ans(170, 188, "~ing")
    b += f'<line x1="330" y1="132" x2="350" y2="186" stroke="{INK}" stroke-width="1.5" marker-end="url(#ah)"/>'
    b += f'<text x="350" y="162" font-size="13" font-weight="800" fill="{INK}">N</text>'
    b += ans(305, 188, "V p.p.")
    return f'<div style="max-width:330px;margin:0 auto">{_svg(420, 226, b)}</div>'


# ---------- to V vs V-ing 벤다이어그램 (Unit 09) ----------

def gerund_venn():
    b = (f'<circle cx="190" cy="105" r="92" fill="none" style="stroke:{C}" stroke-width="2"/>'
         f'<circle cx="320" cy="105" r="92" fill="none" stroke="#2C9C6A" stroke-width="2"/>'
         f'<defs><pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<line x1="0" y1="0" x2="0" y2="7" stroke="{MUTE}" stroke-width="1.4"/></pattern>'
         f'<clipPath id="cl"><circle cx="190" cy="105" r="92"/></clipPath></defs>'
         f'<circle cx="320" cy="105" r="92" fill="url(#hatch)" clip-path="url(#cl)" opacity=".7"/>'
         f'<text x="70" y="30" font-size="16" font-weight="800" text-anchor="middle" style="fill:{C}">to V</text>'
         f'<text x="450" y="30" font-size="16" font-weight="800" text-anchor="middle" fill="#2C9C6A">V-ing</text>')
    left = ["want", "ask", "tell", "allow", "plan", "wish", "hope"]
    right = ["enjoy", "avoid", "mind", "quit", "finish", "deny"]
    for i, w in enumerate(left):
        b += f'<text x="150" y="{50 + i * 18}" font-size="13" text-anchor="middle" fill="{INK}">{w}</text>'
    for i, w in enumerate(right):
        b += f'<text x="362" y="{55 + i * 19}" font-size="13" text-anchor="middle" fill="{INK}">{w}</text>'
    b += (f'<path d="M255,180 L255,215 L300,215" fill="none" stroke="{INK}" stroke-width="1.4" marker-end="url(#ah)"/>'
          f'<text x="310" y="212" font-size="13" font-weight="800" fill="{INK}">둘 다 OK</text>'
          f'<text x="390" y="200" font-size="12.5" font-weight="800" style="fill:{C}">\'사랑\'</text>'
          f'<text x="390" y="218" font-size="12" fill="{INK}">love · like · hate</text>'
          f'<text x="510" y="200" font-size="12.5" font-weight="800" style="fill:{C}">\'시작\'</text>'
          f'<text x="510" y="218" font-size="12" fill="{INK}">start · begin · continue</text>')
    return _svg(660, 232, b)


# ---------- 수동태 변환 화살표 (Unit 06) ----------

def passive_arrow():
    b = _chip(40, 20, 60, "S", color=INK) + _chip(110, 20, 60, "V", color=INK) + _chip(180, 20, 60, "O", color="#0E8A7E")
    b += _chip(40, 110, 60, "O", color="#0E8A7E")
    b += (f'<rect x="110" y="110" width="130" height="30" rx="6" fill="#fff" style="stroke:{C}" stroke-width="2"/>'
          f'<text x="175" y="130" font-size="13.5" font-weight="800" text-anchor="middle" style="fill:{C}">be V p.p.</text>'
          f'<text x="262" y="130" font-size="13.5" font-weight="800" fill="{SUB}">by</text>')
    b += _chip(290, 110, 60, "S", color=INK)
    b += (f'<path d="M210,52 C210,90 70,80 70,108" fill="none" stroke="#0E8A7E" stroke-width="2" marker-end="url(#ah)"/>'
          f'<path d="M70,52 C110,95 300,70 318,108" fill="none" stroke="{INK}" stroke-width="2" marker-end="url(#ah)"/>'
          f'<text x="390" y="40" font-size="12" fill="{SUB}">① 목적어 → 주어 자리로</text>'
          f'<text x="390" y="62" font-size="12" fill="{SUB}">② 동사 → be + p.p.</text>'
          f'<text x="390" y="84" font-size="12" fill="{SUB}">③ 주어 → by + 목적격 (생략 가능)</text>')
    return _svg(640, 156, b)


# ---------- 가정법 공식 (Unit 15) ----------

def subjunctive_formulas():
    def seg(t, lab):
        return f'<span class="sj-seg"><span class="sj-w">{t}</span><span class="sj-l">{lab}</span></span>'
    rows = [
        ("가정법 과거", [("If S", None), ("V-ed", "현"), (", S", None), ("would/could 동원", "현")]),
        ("가정법 과거완료", [("If S", None), ("had p.p.", "과"), (", S", None), ("would/could have p.p.", "과")]),
        ("혼합가정법", [("If S", None), ("had p.p.", "과"), (", S", None), ("would/could 동원", "현")]),
    ]
    out = ['<div class="sj">']
    for name, parts in rows:
        out.append(f'<div class="sj-row"><span class="sj-name">{name}</span><span class="sj-f">')
        for t, lab in parts:
            out.append(seg(t, lab) if lab else f'<span class="sj-plain">{t}</span>')
        out.append("</span></div>")
    out.append('<div class="sj-note">밑줄 아래 글자 = 실제로 가리키는 때 (현 = 현재, 과 = 과거)</div></div>')
    return "".join(out)
