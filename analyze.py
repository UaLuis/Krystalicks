import os, time

def var(name, arg):
    varS[name] = arg

def prinK(arg, name):
    if arg == "var":
        print(varS[name])

def add(var1, var2, name):
    if var1 in varS and var2 in varS:
        varS[name] = int(varS[var1]) + int(varS[var2])

def sub(var1, var2, name):
    if var1 in varS and var in varS:
        varsS[name] = int(varS[var1]) - int(varS[var2])

def mul(var1, var2, name):
    if var1 in varS and var2 in varS:
        varS[name] = int(varS[var1]) * int(varS[var2])

def div(var1, var2, name):
    if var1 in varS and vars in varS:
        varS[name] = int(varS[var1]) / int(varS[var2])

def ifK(arg1, arg2, fun):
    pass

def inputK(name):
    varS[name] = input()

def systemCalls(arg):
    os.system(arg)

def sleep(arg):
    time.sleep(int(arg))

fun = {
    "var": var,
    "print": prinK,
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "if": ifK,
    "input": inputK,
    "systemCalls": systemCalls,
    "sleep": sleep,
}
varS = {}

def analyze(code):
    if len(code) == 4:
        funLine, arg1, arg2, arg3 = code
        fun[funLine](arg1, arg2, arg3)
    elif len(code) == 3:
        funLine, arg1, arg2 = code
        fun[funLine](arg1, arg2)
    elif len(code) == 2:
        funLine, arg1 = code
        fun[funLine](arg1)
