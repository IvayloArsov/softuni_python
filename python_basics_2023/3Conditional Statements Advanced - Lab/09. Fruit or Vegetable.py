fruit = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable = ['tomato', 'cucumber', 'pepper', 'carrot']
userinput = input()

if userinput in fruit:
    print('fruit')
elif userinput in vegetable:
    print('vegetable')
else:
    print('unknown')