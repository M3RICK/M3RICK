#!/usr/bin/env python3
"""Generates assets/hexdump.svg: python3 assets/gen_hexdump.py > assets/hexdump.svg"""

ROWS = ["DFIR", "REVERSE", "SYSTEMS", "RUST/C"]  # 8 chars max per row
WIDTH = 8
DUR = 12.0    # full loop, seconds
STEP = 0.12   # delay between two bytes
END = 0.95    # fraction of the loop where everything resets

GRAY, PURPLE = "#8b949e", "#7C3AED"


def anim(*pairs):
    """Discrete opacity animation from (seconds, opacity) pairs."""
    times = ";".join(f"{t / DUR:.4f}" for t, _ in pairs)
    values = ";".join(str(v) for _, v in pairs)
    return (f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" '
            f'calcMode="discrete" keyTimes="{times}" values="{values}"/>')


def main():
    assert all(len(r) <= WIDTH for r in ROWS), "row longer than WIDTH"
    end = DUR * END
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 {len(ROWS) * 22 + 8}" '
           f'width="390" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" '
           f'font-size="13" role="img" aria-label="{" / ".join(ROWS)}">']
    t = 0.3
    for r, word in enumerate(ROWS):
        y = 20 + r * 22
        decode = t + WIDTH * STEP + 0.15  # ASCII column resolves once the row is complete
        out.append(f'<text x="0" y="{y}" fill="{GRAY}">{r * WIDTH:08x}</text>')
        out.append(f'<text x="286" y="{y}" fill="{GRAY}">|</text>'
                   f'<text x="{296 + WIDTH * 9}" y="{y}" fill="{GRAY}">|</text>')
        for i, byte in enumerate(word.encode().ljust(WIDTH, b"\0")):
            pad = byte == 0
            hx, ax = 82 + i * 25, 296 + i * 9
            out.append(f'<text x="{hx}" y="{y}" fill="{GRAY if pad else PURPLE}">{byte:02x}'
                       f'{anim((0, 0), (t, 0.4 if pad else 1), (end, 0))}</text>')
            # dot placeholder while the byte is "raw", then the decoded character
            out.append(f'<text x="{ax}" y="{y}" fill="{GRAY}" opacity="0">.'
                       f'{anim((0, 0), (t, 1), (decode, 1 if pad else 0), (end, 0))}</text>')
            if not pad:
                out.append(f'<text x="{ax}" y="{y}" fill="{PURPLE}" font-weight="bold">'
                           f'{chr(byte).replace("&", "&amp;").replace("<", "&lt;")}'
                           f'{anim((0, 0), (decode, 1), (end, 0))}</text>')
            t += STEP
        t = decode + 0.25
    assert t < end, "animation longer than the loop: raise DUR or lower STEP"
    out.append("</svg>")
    print("\n".join(out))


if __name__ == "__main__":
    main()
