import math

def calculate_angle(index_of_refraction_1, index_of_refraction_2):
    return math.degrees(math.asin(index_of_refraction_2 / index_of_refraction_1))

angle = calculate_angle(1.0003, 1.333)
print(f"Угол ломания света в дожде: {angle:.2f} градусов")
