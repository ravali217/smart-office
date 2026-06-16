def convert_units(query):

    query = query.lower()

    try:

        parts = query.split()

        value = float(parts[0])

        from_unit = parts[1]

        to_unit = parts[3]

        # KM → M

        if from_unit == "km" and to_unit == "meters":

            result = value * 1000

        # M → KM

        elif from_unit == "meters" and to_unit == "km":

            result = value / 1000

        # KG → G

        elif from_unit == "kg" and to_unit == "grams":

            result = value * 1000

        # G → KG

        elif from_unit == "grams" and to_unit == "kg":

            result = value / 1000

        else:

            return "Conversion not supported."

        return f"{value} {from_unit} = {result} {to_unit}"

    except Exception as e:

        return f"Error: {e}"


if __name__ == "__main__":

    print(
        convert_units("10 km to meters")
    )

    print(
        convert_units("5000 meters to km")
    )

    print(
        convert_units("2 kg to grams")
    )