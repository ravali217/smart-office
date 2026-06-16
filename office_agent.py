import ollama

from calculator_tool import calculator
from weather_tool import weather


def select_tool(user_query):

    prompt = f"""
You are an AI Office Assistant.

Available Tools:

1. calculator
   For mathematical calculations.

2. weather
   For weather-related questions.

Return ONLY in one of these formats:

calculator:<expression>

OR

weather:<city>

User Query:
{user_query}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()


def office_agent(user_query):

    decision = select_tool(user_query)

    print("\nReasoning:")
    print(decision)

    if decision.lower().startswith("calculator:"):

        expression = decision.split(
            ":",
            1
        )[1].strip()

        observation = calculator(
            expression
        )

    elif decision.lower().startswith("weather:"):

        city = decision.split(
            ":",
            1
        )[1].strip()

        observation = weather(
            city
        )

    else:

        observation = "Unable to determine tool."

    final_prompt = f"""
User Question:
{user_query}

Tool Output:
{observation}

Generate a short and helpful answer.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return response["message"]["content"]


print("=" * 50)
print("SMART OFFICE ASSISTANT")
print("=" * 50)

while True:

    query = input("\nEmployee: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    answer = office_agent(query)

    print("\nAssistant:")
    print(answer)