class Stack:
    data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True

    def __str__(self):
        return '[' + ', '.join(map(str, self.data[::-1])) + ']'


# test zero
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.top(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


# if __name__ == '__main__':
#     unittest.main()
#
# class StackTests(unittest.TestCase):
#     def test_zero(self):
#         stack = Stack()
#         stack.push("apple")
#         stack.push("carrot")
#         self.assertEqual(str(stack), '[carrot, apple]')
#         self.assertEqual(stack.pop(), 'carrot')
#         self.assertEqual(stack.top(), 'apple')
#         stack.push("cucumber")
#         self.assertEqual(str(stack), '[cucumber, apple]')
#         self.assertEqual(stack.is_empty(), False)
#
#
# if __name__ == '__main__':
#     unittest.main()