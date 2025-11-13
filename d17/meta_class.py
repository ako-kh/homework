import types

class Meta(type):
    def __new__(mcls, name, bases, attrs):
        for kay, value in attrs.items():
            if isinstance(value, types.FunctionType) and kay[0] != '_':
                raise ValueError("class methods should be protected")

        return super().__new__(mcls, name, bases, attrs)

class With(metaclass=Meta):
    _some = 11
    def _test(self):
        return

class Without(metaclass=Meta):
    some = 11
    def test(self):
        return

with_ = With()
without_ = Without()