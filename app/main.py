from fastapi import FastAPI
from app.calculator import Calculator

app = FastAPI()
calculator = Calculator()


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/calculator")
def cal(
    num1: int,
    num2: int,
    operation: str,
):
    operation = operation.lower()

    if operation == "add":
        return {"result is: ": f"{calculator.Add(num1, num2)}"}

    elif operation.lower == "subtract":
        return {"result is: ": f"{calculator.Subtract(num1, num2)}"}

    elif operation.lower == "divide":
        return {"result is: ": f"{calculator.Divide(num1, num2)}"}

    elif operation.lower == "multiply":
        return {"result is: ": f"{calculator.Multiply(num1, num2)}"}

    else:
        "Please put in a valid operation, and valid integers"
