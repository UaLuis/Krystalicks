import os, time

def var(name, arg):
    varS[name] = arg

def prinK(name1, name2=None):
    if name1 in varS and name2 in varS:
        print(varS[name1], varS[name2])
    elif name1 in varS and name2 not in varS:
        print(varS[name1], name2)
    elif name1 not in varS and name2 in varS:
        print(name1, varS[name2])
    elif name1 not in varS and name2 not in varS:
        print(name1, name2)
    elif name1 in varS and name2 == None:
        print(name1)
    elif name1 not in varS and name2 == None:
        print(name1)

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

def ifK(arg0, arg1, arg2, arg3, arg4, funLine, arg6):
    if arg1 and arg3 in varS:
        var1, var2 = varS[arg1], varS[arg3]
    elif arg1 in varS and agr3 not in varS:
        var1, var2 = varS[arg1], arg3
    elif arg3 in varS and agr1 not in varS:
        var2, var1 = varS[arg3], arg1
    elif arg1 and arg3 not in varS:
        var1, var2 = arg1, arg2

    if arg2 == "=" and arg0 == "int":
        if int(var1) == int(var2):
            fun[funLine](arg6)

    elif arg2 == "=" and arg0 == "str":
        if var1 == var2:
            fun[funLine](arg6)

    elif arg2 == ">" and arg0 == "int":
        if int(var1) > int(var2):
            fun[funLine](arg6)

    elif arg2 == "<" and arg0 == "int":
        if int(var1) < int(var2):
            fun[funLine](arg6)

    elif arg0 == None or int:
        print("ERROR, not have data of type!")

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
    if len(code) == 8:
        funLine, arg0, agr1, arg2, arg3, arg4, arg5, arg6 = code
        fun[funLine](arg0, arg1, arg2, arg3, arg4, arg5, arg6)

    elif len(code) == 4:
        funLine, arg1, arg2, arg3 = code
        fun[funLine](arg1, arg2, arg3)

    elif len(code) == 3:
        funLine, arg1, arg2 = code
        fun[funLine](arg1, arg2)

    elif len(code) == 2:
        funLine, arg1 = code
        fun[funLine](arg1)
