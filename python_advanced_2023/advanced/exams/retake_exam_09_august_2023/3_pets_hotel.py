def accommodate_new_pets(available_capacity, weight_limit, *pets):
    accommodated_pets = {}
    result = []
    for pet_type, pet_weight in pets:
        if available_capacity <= 0:
            result.append('You did not manage to accommodate all pets!')
            break
        if pet_weight > weight_limit:
            continue
        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        available_capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")

    result.append('Accommodated pets:')
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(accommodated_pets.items())]
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))