from stack_implementation_using_linked_list import Stack


def infix_to_postfix(expression):
    st = Stack()
    postfix = ""
    for symbol in expression:
        if symbol == " " or symbol == "\t":
            continue
        elif symbol == "(":
            st.push(symbol)
        elif symbol == ")":
            next = st.pop()
            while next != "(":
                postfix = postfix + next
                next = st.pop()
        elif symbol in "%^*-+/":
            while not st.is_empty() and precedence(st.peek()) >= precedence(symbol):
                postfix = postfix + st.pop()
            st.push(symbol)
        else:
            postfix = postfix + symbol

    while not st.is_empty():
        postfix = postfix + st.pop()
    return postfix


def precedence( symbol):
    if symbol == "(":
        return 0
    if symbol in "*/":
        return 2
    if symbol in "+-":
        return 1
    if symbol == "^":
        return 3
    else:
        return 0


def evaluate_postfix( postfix):
    st = Stack()

    for symbol in postfix:
        if symbol.isdigit():
            st.push(int(symbol))
        else:
            x = st.pop()
            y = st.pop()

            if symbol == "+":
                st.push(y+x)
            elif symbol == "-":
                st.push(y-x)
            elif symbol == "*":
                st.push(y*x)
            elif symbol == "/":
                st.push(y/x)
            elif symbol == "^":
                st.push(y**x)
            elif symbol == "%":
                st.push(y%x)

    return st.pop()

##################################################


while True:

    expression = input("Enter the expression : ")
    if expression == "q":
        break
    postfix = infix_to_postfix(expression)
    print("Postfix expression is : ", postfix)
    print("Value of expression is : ", evaluate_postfix(postfix))







