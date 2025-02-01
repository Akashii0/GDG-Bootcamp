class Calculator():

    def Add(self, num1, num2):
        return int(num1) + int(num2)

    # This function subtract two  numbers
    def Subtract(self, num1, num2):
        return int(num1) - int(num2)

    # This function multiplies two  numbers
    def Multiply(self, num1, num2):
        return int(num1) * int(num2)

    # This function divides two  numbers
    def Divide(self, num1, num2):
        return int(num1) / int(num2)

    def main(self):
        print("Bootcamp Project 1: Calculator")
        print("""
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        """)

        while True:
            choice = input("Enter choice(1 or add, 2 or subtract, 3 or multiply, 4 or divide, q to quit): ")

            if choice.lower() == 'q':
                break

            if choice in ('1', '2', '3', '4', 'add', 'subtract', 'multiply', 'divide'):
                num1 = input("Enter first number: ")
                num2 = input("Enter second number: ")

                if choice == '1' or choice.lower() == 'add':
                    print("The result is: ", self.Add(num1, num2))

                elif choice == '2' or choice.lower() == 'subtract':
                    print("The result is: ", self.Subtract(num1, num2))

                elif choice == '3' or choice.lower() == 'multiply':
                    print("The result is: ", self.Multiply(num1, num2))

                elif choice == '4' or choice.lower() == 'divide':
                    print("The result is: ", self.Divide(num1, num2))
            else:
                print("Invalid Input")
# Description: A simple calculator that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.


calculator = Calculator()
calculator.main()
