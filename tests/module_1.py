def full_name(a, b):
    name = a + " " + b
    name = name.title()
    return name


var = full_name

def indirect (func, arg1, agr2):
    print(func(arg1, agr2))


print(var("tal", "green"))

indirect(var, "gidi", "gov")
