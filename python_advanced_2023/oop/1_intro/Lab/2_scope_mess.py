x = 'global'


def outer():
    x = 'local'

    def inner():
        nonlocal x  # this is added

        x = 'nonlocal'
        print('inner:', x)

    def change_global():
        global x  # this is added

        x = 'global: changed!'

    print('outer:', x)
    inner()

    print('outer:', x)
    change_global()


print(x)
outer()
print(x)
