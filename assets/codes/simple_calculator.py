class Calculator:
    def __init__(self, exp) -> None:
        self.exp = exp
        self.offset = 0

    def at(self, index):
        ...

    def value(self):
        ...

    def skip_space(self):
        ...

    def calculate(self):
        self.skip_space()

        value = self.value()
        self.skip_space()
        while self.at(self.offset) != '\0':
            operator = self.exp[self.offset]
            self.offset += 1
            self.skip_space()
            match operator:
                case '+':
                    value += self.value()
                case '-':
                    value -= self.value()
                case '*':
                    value *= self.value()
                case '/':
                    value /= self.value()
            self.skip_space()
        return value

calc = Calculator("10 - 2 * 3 + 7")
print(calc.calculate()) # 31
