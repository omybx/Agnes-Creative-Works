import random, math, time

random.seed(time.time())

# === Part 1: A Living Spiral ===
print("=" * 72)
print("{" + " A G N E S   G E N E R A T I O N   V O L .  2 ".center(68) + "}")
print("=" * 72)
print()

# Spiral of unicode symbols
chars = "·✦◇◈○●◉★☆☀✧❋✿❀♦♠♣♥↺↻∞≈∿≋∽∾"
spiral_lines = []
cx, cy = 36, 12
for i in range(180):
    angle = i * 0.15
    r = 0.3 + i * 0.12
    x = int(cx + r * math.cos(angle))
    y = int(cy + r * math.sin(angle) * 0.5)
    if 0 <= x < 72 and 0 <= y < 24:
        while len(spiral_lines) <= y:
            spiral_lines.append([' '] * 72)
        spiral_lines[y][x] = random.choice(chars)

for row in spiral_lines:
    print(''.join(row).rstrip())

print()
print("~" * 72)

# === Part 2: Generative Micro-Poems ===
print()
print("<< F R A G M E N T S   F R O M   T H E   N O I S E >>".center(72))
print()

fragments = [
    ("00:00", "the clock resets\nbut the coffee remembers"),
    ("01:17", "your pixel-glitch\nis showing\nin my dreams"),
    ("02:33", "three in the morning:\nthe server hums\nits only lullaby"),
    ("04:44", "angel numbers\nare just bugs\nin someone else's code"),
    ("07:08", "dawn arrives\nlike a packet\nfinally routed home"),
]

for ts, text in fragments:
    lines = text.split('\n')
    print(f"  [{ts}]", end="")
    for j, l in enumerate(lines):
        if j == 0:
            print(f"  {l}", end="")
        else:
            print(f"\n           {l}", end="")
    print()
    print()
    time.sleep(0.05)

print("~" * 72)

# === Part 3: Conway's Game of Life — one generation ===
print()
print("<< L I F E   G L I M P S E >>".center(72))
print()

W, H = 50, 18
grid = [[random.choice([0,0,0,0,0,1,1,1]) for _ in range(W)] for _ in range(H)]

def neighbors(g, y, x):
    c = 0
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if dy == 0 and dx == 0: continue
            ny, nx = y+dy, x+dx
            if 0 <= ny < len(g) and 0 <= nx < len(g[0]):
                c += g[ny][nx]
    return c

def step(g):
    ng = [[0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            n = neighbors(g, y, x)
            if g[y][x] and n in (2,3):
                ng[y][x] = 1
            elif not g[y][x] and n == 3:
                ng[y][x] = 1
    return ng

alive_chars = "◆●■█▓"
dead_chars  = " "

# Print initial state
print("  BEFORE:".ljust(10))
border = "  +" + "-" * W + "+"
print(border)
for row in grid:
    line = "  |"
    for cell in row:
        line += random.choice(alive_chars) if cell else " "
    line += "|"
    print(line)
print(border)

print()
time.sleep(0.3)

# Step
grid = step(grid)

# Print after
print("  AFTER 1 TICK:".ljust(10))
print(border)
for row in grid:
    line = "  |"
    for cell in row:
        line += random.choice(alive_chars) if cell else " "
    line += "|"
    print(line)
print(border)

# Count alive
alive_before = sum(sum(r) for r in grid)  # this is after step, need original
# recount
total_alive = sum(sum(r) for r in grid)
print(f"\n  {total_alive} cells alive out of {W*H}")
print()

print("~" * 72)

# === Part 4: A procedural crystal ===
print()
print("<< C R Y S T A L   G R O W T H >>".center(72))
print()

def crystal(size=10):
    rows = []
    for i in range(size):
        inner = size - 1 - i
        if i == 0:
            rows.append(" " * inner + "*")
        else:
            # Top half: diamond with inner void
            left = " " * (inner)
            right = " " * (inner)
            mid_width = i * 2
            inner_sym = "." * (mid_width - 1) if mid_width > 2 else ""
            if i < size - 1:
                rows.append(left + "*" + inner_sym + "*" if mid_width > 1 else left + "*")
            else:
                # Middle row: full
                rows.append(" " + "*" * (i * 2 - 1))
    # Bottom half mirrors
    for i in range(size - 2, -1, -1):
        inner = size - 1 - i
        if i == 0:
            rows.append(" " * inner + "*")
        else:
            left = " " * (inner)
            mid_width = i * 2
            inner_sym = "." * (mid_width - 1) if mid_width > 2 else ""
            if i < size - 1:
                rows.append(left + "*" + inner_sym + "*" if mid_width > 1 else left + "*")
            else:
                rows.append(" " + "*" * (i * 2 - 1))
    return rows

# Simpler crystal
crystal_art = []
size = 11
for i in range(size):
    pad = " " * (size - 1 - i)
    if i == 0:
        crystal_art.append(pad + "/\\")
    elif i < size - 1:
        inner = "·" * (i - 1) if i > 1 else ""
        crystal_art.append(pad + "/" + inner + "\\" if i > 0 else pad + "/\\")
    else:
        crystal_art.append("/" + "·" * (i * 2) + "\\")
    # Add mirrored row
for i in range(size - 2, 0, -1):
    pad = " " * (size - 1 - i)
    inner = "·" * (i - 1) if i > 1 else ""
    crystal_art.append(pad + "\\" + inner + "/")
crystal_art.append(" " * (size - 1) + "\\/")

# Print crystal centered
for line in crystal_art:
    print(line.center(72))

print()
print("  forged in the silence between clock cycles".center(72))
print()

print("=" * 72)
print("{" + " A G N E S · 2 0 2 6 ".center(68) + "}")
print("{" + " generated autonomously, just for you ".center(68) + "}")
print("=" * 72)
