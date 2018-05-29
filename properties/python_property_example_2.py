class C(object):
    def __init__(self):
        self._x = None

    @property # property makes class method into a read only attribute
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called-->"+self._x) # here underscore(_) at the beginning used to denote private variables in python.
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x


c = C()
c.x = 'foo'  # setter called
var2 = c.x    # getter called
del c.x      # deleter called