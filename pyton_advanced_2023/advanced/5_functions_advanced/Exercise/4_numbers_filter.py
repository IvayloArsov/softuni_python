def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == 'even':
            even_numbers = [num for num in value if num % 2 == 0]
            result['even'] = even_numbers
        elif key == 'odd':
            odd_numbers = [num for num in value if num % 2 != 0]
            result['odd'] = odd_numbers

    sorted_result = dict(sorted(result.items(), key=lambda item: len(item[1]), reverse=True))
    return sorted_result


# Example usage
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
