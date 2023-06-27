class Stack():

    def __init__(self):
        self.stack = []
        self.flag = True

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':

    stack = Stack()
    buf = {'(': ')', '[': ']', '{': '}'}

    sequence = input('Введите последовательность скобок: ')
    for elem in sequence:
        if elem in '([{':
            stack.push(elem)

        elif elem in ')]}':
            if stack.is_empty():
                stack.flag = False
                break

            stack_elem = stack.pop()
            if stack_elem in '([{' and elem == buf[stack_elem]:
                continue

            stack.flag = False
            break

    if stack.is_empty() and stack.flag:
        print('Сбалансированно')
    else:
        print('Несбалансированно')



