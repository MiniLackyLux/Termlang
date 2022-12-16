import subprocess
import sys
import py_compile

term_files = [sys.argv[1]]

with open(term_files[0], 'r') as file:
    file: str = file.read()

file = file.replace("String", "str")
file = file.replace("Int", "int")
file = file.replace("Float", "float")
file = file.replace("Boolean", "bool")
file = file.replace(" then", ":")
file = file.replace("else if", "elif")
file = file.replace("|", "#")
file = file.replace("String", "str")
file = file.replace(";", "")
file = file.replace("\\;", ";")
file = file.replace("true", "True")
file = file.replace("false", "False")
file = file.replace("fnc", "def")
file = file.replace(" do", ":")
file = file.replace("include", "import")
file = file.replace("use", "from")
file = file.replace("array", "list")
file = file.replace("tup", "tuple")
file = file.replace("map", "dict")
file = file.replace("readline", "input()")
file = file.replace("catch", "except")
file = file.replace("attempt", "try:")
file = file.replace("take", "import")
file = file.replace("ceiling", "ceil")
file = file.replace("everything", "*")
file = file.replace("all", "*")
file = file.replace("formats", "f")
file = file.replace("frmt", "f")
file = file.replace("///program///", """'''
This is a program in Termlang!
Consider supporting our website and go to https://termoxers.ml/
This language is made for making games for the termlang platform (And also as a little challenge)
-- MiniLackyLux'''""")
file = file.replace("import this", "You tried to get away didn't you?")
file = file.replace("0init0", "__init__")



with open(".run.py", "w") as run:
    run.write(file)

if sys.argv[2] == "inter":
    subprocess.run(f"python3 .run.py", shell=True)
elif sys.argv[2] == "compile":
    try:
        py_compile.compile(".run.py")
    except Exception:
        print("An Error has occured")
elif sys.argv[2] == "python":
    with open("out.py", "w") as out:
        out.write(file)
else:
    print("Invalid Second Argument")
