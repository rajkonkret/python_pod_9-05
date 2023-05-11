class A:
    def method(self):
        print("Metoda kalsy A")


class B:
    def method(self):
        print("Metoda kalsy B")


class C(A, B):
    """
    klasa C
    """

    def method(self):
        # super().method()
        A.method(self)

c = C()
c.method()
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.__mro__)