class Calculator:
    def __init__(self, exp) -> None:
        self.exp = exp
        self.offset = 0

    def at(self, index):
        if index < len(self.exp):
            return self.exp[index]
        return '\0'

    def value(self):
        length = 0
        while self.at(self.offset + length).isdigit():
            length += 1

        offset = self.offset
        self.offset += length
        return int(self.exp[offset:][:length])

    def skip_space(self):
        while self.at(self.offset) == ' ':
            self.offset += 1

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

calc = Calculator("6 + 2 * 3 - 7")
print(calc.calculate()) # 17
