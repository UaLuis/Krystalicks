import analyze

code = []
vals = {}

with open('test.pk', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        code.append(parts)

for line in code:
    analyze.analyze(line)


