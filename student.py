class Students:
    kind ="human"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_kind(cls):
        cls.kind = "asd"

s1 = stundent("Test1")
s1 = stundent("Test2")
print(s1.kind)
print(s2.kind)
s1.change_king()
print(s1.kind)
print(s2.kind)
