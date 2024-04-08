class Stack:
    def __init__(self):
        self.data = []

    # def validate_if_string(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError('Only strings can be appended to StringStack')

    def push(self, value):
        # self.validate_if_string(value)
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __repr__(self):
        return f"[{', '.join(reversed(self.data))}]"


# inheritance_exercise zero
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


if __name__ == '__main__':
    unittest.main()

# stack = Stack()
# stack.push('apple')
# print(stack.__str__())
# stack.push('carrot')
# print(stack.__str__())
