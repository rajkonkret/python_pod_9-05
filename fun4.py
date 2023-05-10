# funkcja zagnieżdzona
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest funkacja fun2")

    return fun2  # bez nawiasów bo nie chcemy wykonania funkcji fun2 tylko chcemy adres gdzie jest w pamieci


xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000019EC4EB8D60>
print(type(xFun))  # <class 'function'>
xFun()
# xFun - nazwa funkcji
# xFun() - wywołanie(uruchomienie) funkcji zawartej w xFun
