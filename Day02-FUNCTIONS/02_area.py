#Area of rectangle
def calculate_area(length, width):
    return length * width

length = float(input("Length : "))
width = float(input("Breadth : "))
print(f"AREA OF RECTANGLE : {calculate_area(length, width)}")