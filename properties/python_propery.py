class Foo(object):
    # deault constructor
    def __init__(self):
        self._bar = 0

    @property # propery converts class method into a read only attribute
    def Bar(self):
        return self._bar

    @Bar.setter # setter gets called while setting values
    def Bar(self, value):
        self._bar = value


foo = Foo()
print(foo.Bar)  # called Bar getter --> 0
foo.Bar = 10  # called Bar setter
print(foo.Bar)  # called Bar getter --> 10