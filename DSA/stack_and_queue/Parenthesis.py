from stack_implementation_using_linked_list import Stack


def is_valid(expression):
    st = Stack()
    for ch in expression:
        if ch in "({[":
            st.push(ch)
        if ch in ")}]":
            if st.is_empty():
                print("Right parenthesis are more than left parenthesis")
                return False
            char = st.pop()
            if not match_expression(char, ch):
                print("Mismatched parenthesis are ", char , " and ", ch )
                return False

    if st.is_empty():
        print("Balanced Parenthesis")
        return True
    else:
        print("Left parenthesis are more than right parenthesis")
        return False


def match_expression(char, ch):

    if char == "(" and ch == ")":
        return True
    if char == "{" and ch == "}":
        return True
    if char == "[" and ch == "]":
        return True
    return False


if __name__ == "__main__":
    while True:
        expression = input("Enter the expression (q for quit) : ")
        if expression == "q":
            break

        if is_valid(expression):
            print("valid expression")
        else:
            print("invalid expression")






