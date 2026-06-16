def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {
        "BMI": round(bmi, 2),
        "Category": category
    }


if __name__ == "__main__":

    result = calculate_bmi(70, 1.75)

    print("BMI:", result["BMI"])
    print("Category:", result["Category"])