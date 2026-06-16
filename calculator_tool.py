# calculator_tool.py

def calculator(expression):

    try:
        result = eval(expression)
        return f"Calculation Result: {result}"

    except Exception as e:
        return f"Error: {e}"