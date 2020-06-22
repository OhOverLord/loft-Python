class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def chek_parentheses(s):
    sch = 0
    st = Stack()
    brackets = {')': '(', ']': '[', '}': '{'}
    for i, symbol in enumerate(s, 1):
        if symbol in brackets.values():
            st.push(symbol)
            if sch == 0:
                sch = i
        elif symbol in brackets:
            if st.isEmpty() or brackets[symbol] != st.pop():
                return i
            if st.isEmpty():
                sch = 0
    if not st.isEmpty():
        return sch
    else:
        return "Success"


def main():
    s = input()
    print(chek_parentheses(s))


if __name__ == '__main__':
    main()
