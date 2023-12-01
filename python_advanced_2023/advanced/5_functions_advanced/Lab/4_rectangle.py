def rectangle(length, width):
    if isinstance(length, int) and isinstance(width, int):
        def area():
            return length*width

        def perimeter():
            return (length+width)*2

        result = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
        return result
    else:
        return f"Enter valid values!"


print(rectangle(420, 69))
