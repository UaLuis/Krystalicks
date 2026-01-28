code = []
vals = {}
with open('test.pk', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        code.append(parts)

def analyze(code):
    fun, als, var = code

    if fun == 'var':
        vals[als] = var
    elif fun == 'print':
        if als == 'var':
            print(vals[var])

for i in range(len(code)):
    print(code[i])
    analyze(code[i])
