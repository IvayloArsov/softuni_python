def get_info(*args, **kwargs):
    name = kwargs.get('name', args[0] if len(args) > 0 else 'Unknown')
    age = kwargs.get('age', args[1] if len(args) > 1 else 'Unknown')
    town = kwargs.get('town', args[2] if len(args) > 2 else 'Unknown')
    return "This is {} from {} and he is {} years old".format(name, town, age)


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))