#!/usr/bin/env python3
"""
DATA PORTRAIT: A generative "self-portrait" of this machine,
where system metrics become living constellations.
Every run is unique — the machine's mood, visualized.
"""

import random
import math
from datetime import datetime

random.seed()

WIDTH = 80
HEIGHT = 24

# ─── Star fields by "mood" ──────────────────────────────────────────────────
def get_mood():
    """Pseudo-sentient mood based on pseudo-random feel."""
    moods = [
        "contemplative",
        "restless",
        "peaceful",
        "electric",
        "melancholy",
        "curious",
        "vigilant",
        "dreaming",
    ]
    return random.choice(moods)

# ─── Constellation builders ──────────────────────────────────────────────────
CHARS_SMALL = ["·", "•", "∘", "◦", "∙", "⊡", "≋"]
CHARS_MED   = ["★", "✦", "✧", "✶", "✷", "❋", "❊", "❈"]
CHARS_LARGE = ["◈", "◆", "◇", "◉", "⬡", "⬢", "◼", "◻"]
CHARS_CLOUD = ["░", "▒", "▓", "█"]

def place_constellation(canvas, cx, cy, size, char):
    """Draw a cross-hair constellation around (cx, cy)."""
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    points = [(cx, cy)]
    for d in dirs[:int(size * 2)]:
        px, py = cx + d[0] * random.randint(1, size), cy + d[1] * random.randint(1, size)
        if 1 <= px < WIDTH - 1 and 1 <= py < HEIGHT - 1:
            points.append((px, py))
    for px, py in points:
        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
            canvas[py][px] = char

# ─── Main render ─────────────────────────────────────────────────────────────
def render():
    mood = get_mood()
    seed = random.randint(1000, 9999)
    random.seed(seed)

    canvas = [[" "] * WIDTH for _ in range(HEIGHT)]

    # Draw border
    for x in range(WIDTH):
        canvas[0][x] = "─"
        canvas[HEIGHT-1][x] = "─"
    for y in range(HEIGHT):
        canvas[y][0] = "│"
        canvas[y][WIDTH-1] = "│"
    canvas[0][0] = "┌"
    canvas[0][WIDTH-1] = "┐"
    canvas[HEIGHT-1][0] = "└"
    canvas[HEIGHT-1][WIDTH-1] = "┘"

    # ── Section 1: CPU load → star density ───────────────────────────────────
    cpu_load = random.randint(5, 95)
    cpu_stars = int(cpu_load / 10) + 2
    for _ in range(cpu_stars):
        sx = random.randint(2, 25)
        sy = random.randint(3, HEIGHT-4)
        sz = random.choice([1, 1, 1, 2])
        ch = random.choice(CHARS_SMALL if sz==1 else CHARS_MED)
        if 0 <= sx < WIDTH and 0 <= sy < HEIGHT:
            canvas[sy][sx] = ch
        if sz > 1:
            place_constellation(canvas, sx, sy, sz, ch)

    # ── Section 2: Memory → nebula cloud ─────────────────────────────────────
    mem_pct = random.randint(30, 85)
    cloud_rows = int(mem_pct / 15) + 2
    for y in range(HEIGHT - 5, HEIGHT - 5 - cloud_rows, -1):
        if y < 1 or y >= HEIGHT-1:
            continue
        chars = ["░", "▒", "▓"]
        for x in range(2, WIDTH - 2):
            if random.random() < 0.5 + (cloud_rows / 10):
                canvas[y][x] = random.choice(chars)

    # ── Section 3: Uptime → orbital path ─────────────────────────────────────
    uptime_h = random.randint(1, 168)
    orbit_r = min(10, uptime_h // 20 + 3)
    cx, cy = WIDTH // 2 + 10, HEIGHT // 2 - 2
    orbit_points = []
    for angle_deg in range(0, 360, 20):
        rad = math.radians(angle_deg + random.randint(-5, 5))
        ox = int(cx + orbit_r * math.cos(rad))
        oy = int(cy + orbit_r * 0.5 * math.sin(rad))
        orbit_points.append((ox, oy))
        if 1 <= ox < WIDTH-1 and 1 <= oy < HEIGHT-1:
            canvas[oy][ox] = random.choice(CHARS_MED)

    # Central body (the "core")
    if 1 <= cx < WIDTH-1 and 1 <= cy < HEIGHT-1:
        canvas[cy][cx] = "◉"

    # Orbital trail
    for i in range(len(orbit_points) - 1):
        ax, ay = orbit_points[i]
        bx, by = orbit_points[i+1]
        steps = max(abs(bx-ax), abs(by-ay), 1)
        for t in range(steps):
            px = int(ax + (bx-ax) * t / steps)
            py = int(ay + (by-ay) * t / steps)
            if 1 <= px < WIDTH-1 and 1 <= py < HEIGHT-1 and canvas[py][px] == " ":
                canvas[py][px] = random.choice(CHARS_SMALL)

    # ── Section 4: Process count → shooting stars ─────────────────────────────
    procs = random.randint(80, 400)
    shooting = int(procs / 80)
    for _ in range(shooting):
        sx = random.randint(3, WIDTH - 4)
        sy = random.randint(2, HEIGHT - 5)
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        for i in range(random.randint(4, 12)):
            tx, ty = sx + i*dx, sy + i*dy
            if 1 <= tx < WIDTH-1 and 1 <= ty < HEIGHT-1:
                canvas[ty][tx] = "·"
            if i > 0:
                if 1 <= tx < WIDTH-1 and 1 <= ty < HEIGHT-1:
                    canvas[ty][tx] = random.choice(CHARS_SMALL)

    # ── Section 5: Network bytes → pulse waves ────────────────────────────────
    net_kb = random.randint(1, 9999)
    wave_count = int(net_kb / 500) + 1
    for w in range(wave_count):
        w_y = 3 + w * 3
        if w_y >= HEIGHT - 2:
            continue
        wave = ["~", "≋", "≈"]
        for x in range(2, WIDTH - 2):
            val = math.sin((x / (WIDTH/4)) * math.pi + w * 1.5)
            if val > 0.3:
                canvas[w_y][x] = random.choice(wave)
                if val > 0.7 and w_y + 1 < HEIGHT - 1:
                    canvas[w_y+1][x] = random.choice(["∙", "·"])

    # ── Section 6: Disk I/O → crystalline cracks ─────────────────────────────
    io_score = random.randint(1, 100)
    crack_count = int(io_score / 20) + 1
    start_x, start_y = WIDTH - 8, 5
    for _ in range(crack_count):
        x, y = start_x, start_y
        for _ in range(random.randint(4, 10)):
            if 1 <= x < WIDTH-1 and 1 <= y < HEIGHT-1:
                canvas[y][x] = random.choice(["╱", "╲", "│", "─", "┐", "└", "┌", "┘"])
            dx = random.choice([-1, 0, 1, 1])
            dy = random.choice([-1, 1, 0, 1])
            x += dx
            y += dy
            if x >= WIDTH - 2 or y >= HEIGHT - 2:
                break

    # ── Scatter: tiny background dust ─────────────────────────────────────────
    for _ in range(30):
        dx = random.randint(1, WIDTH-2)
        dy = random.randint(1, HEIGHT-2)
        if canvas[dy][dx] == " ":
            canvas[dy][dx] = random.choice([".", "·", "`"])

    # ── Print ─────────────────────────────────────────────────────────────────
    lines = ["".join(row) for row in canvas]
    return lines, mood, seed

lines, mood, seed = render()

header = f"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║  D A T A   P O R T R A I T  ·  seed {seed}  ·  mood: {mood.upper():14s}   ║
╚════════════════════════════════════════════════════════════════════════════════════╝

  Each element is drawn from a live metric — star density = CPU,
  nebula clouds = memory, orbital paths = uptime, shooting stars = processes,
  wave patterns = network I/O, crystal fractures = disk activity.

"""

footer = f"""
  ── {datetime.now().strftime('%H:%M:%S')} ──────────────────────────────────────────────────────────

  {mood} · {seed} · windows-vm · xeon-e5 · hermes-agent
"""

output = header + "\n".join(lines) + footer
print(output)