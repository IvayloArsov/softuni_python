import math

user_vector_1 = [float(input()) for _ in range(2)]
user_vector_2 = [float(input()) for _ in range(2)]


def center_point_comparison(vector1, vector2):
    vector_1 = [abs(math.floor(vec)) for vec in vector1]
    vector_2 = [abs(math.floor(vec)) for vec in vector2]
    vec1_position = sum(vector_1) / len(vector1)
    vec2_position = sum(vector_2) / len(vector2)

    if vec1_position <= vec2_position:
        return tuple(math.floor(vec) for vec in vector1)
    return tuple(math.floor(vec) for vec in vector2)


result = center_point_comparison(user_vector_1, user_vector_2)
print(result)
