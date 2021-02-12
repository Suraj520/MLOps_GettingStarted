#imports
import uvicorn
from fastapi import FastAPI
Calculator = FastAPI()
#describing the get requests
@Calculator.get('/')
def function1():
    return {'message':'Welcome to the Binary Calculator page!'}
#second get request : fetch input from UI
@Calculator.get('/fetch_input')
def FetchInput(num1: int, num2: int):
    sum = num1 + num2
    multiply = num1 - num2
    if num2!=0:
        divide = num1//num2
    else:
        divide ="Division not possible"
    modulus = num1 % num2
    substract = num1-num2
    return {'The sum is {0}, diff is {1}, product is {2}, division is {3} and modulus is {4}'.format(sum,substract,multiply,divide,modulus)}
#running the app
# if __name__ == "__main__":
#     uvicorn.run(Calculator,host= '127.0.0.1') #Assigning the by default port

uvicorn.run(Calculator,host= '127.0.0.1') #Assigning the by default port
