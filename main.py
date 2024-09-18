

class Calculator:

    @staticmethod
    def add(num1: float, num2: float):
        return num1 + num2

    @staticmethod
    def subtract(num1: float, num2: float):
        return num1 - num2

    @staticmethod
    def multiply(num1: float, num2: float):
        return num1 * num2

    @staticmethod
    def divide(num1: float, num2: float):
        pass

    def calculate(self, inp: str):
        OPERATIONS = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }
        num1 = ""
        num2 = ""
        operation = None
        for char in inp:
            if char.isnumeric() or char == ".":
                if operation is None:
                    num1 += char
                else:
                    num2 += char
            elif char in OPERATIONS and num1 != "" and operation is None:
                operation = OPERATIONS[char]
            else:
                return "Error"
        if operation is not None and num1 != "" and num2 != "":
            return operation(float(num1), float(num2))
        else:
            return num1

    def run(self):
        while True:
            print("\n##### CALCULATOR APP ####")
            inp = input("-> ")
            if inp.lower() == 'q':
                print("Closing Calculator... Goodbye!")
                return
            output = self.calculate(inp)
            print(f" = {output}")


if __name__ == "__main__":
    Calculator().run()
