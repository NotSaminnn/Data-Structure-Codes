def evalMathExpression(expr):
    # -----------------------------------------
    # Helper functions
    # -----------------------------------------

    def isOpening(c):
        return c == '(' or c == '[' or c == '{'

    def isClosing(c):
        return c == ')' or c == ']' or c == '}'

    def matching(a, b):
        if a == '(' and b == ')': return True
        if a == '[' and b == ']': return True
        if a == '{' and b == '}': return True
        return False

    def isOperator(c):
        return c=='+' or c=='-' or c=='*' or c=='/' or c=='^'

    def precedence(op):
        if op == '+' or op == '-': return 1
        if op == '*' or op == '/': return 2
        if op == '^': return 3
        return 0

    # ----------------------------------------------------------
    # STEP 1: CHECK BALANCED PARENTHESES
    # ----------------------------------------------------------
    temp = Stack()
    i = 0
    while i < len(expr):
        ch = expr[i]

        if isOpening(ch):
            temp.push(ch)

        elif isClosing(ch):
            if temp.isEmpty():
                print("Invalid Expression")
                return
            top = temp.pop()
            if not matching(top, ch):
                print("Invalid Expression")
                return

        i += 1

    if not temp.isEmpty():
        print("Invalid Expression")
        return

    # ----------------------------------------------------------
    # STEP 2: INFIX → POSTFIX (Push into QUEUE)
    # ----------------------------------------------------------
    stack = Stack()             # operator stack
    queue = LinkedListQueue()   # postfix queue

    number = ""    # to collect multi-digit numbers
    i = 0

    while i < len(expr):
        ch = expr[i]

        # ---- BUILD NUMBER ----
        if ch >= '0' and ch <= '9':
            number += ch

        else:
            # when number ends, push to queue
            if number != "":
                queue.enqueue(number)
                number = ""

            # handle operators
            if isOperator(ch):
                while (not stack.isEmpty()
                       and precedence(stack.peek()) >= precedence(ch)
                       and stack.peek() != '('):
                    queue.enqueue(stack.pop())
                stack.push(ch)

            # handle parentheses (convert all types to round internally)
            elif isOpening(ch):
                stack.push('(')

            elif isClosing(ch):
                while stack.peek() != '(':
                    queue.enqueue(stack.pop())
                stack.pop()  # remove '('

        i += 1

    # last number if exists
    if number != "":
        queue.enqueue(number)

    # empty remaining operators
    while not stack.isEmpty():
        queue.enqueue(stack.pop())

    # ----------------------------------------------------------
    # STEP 3: PRINT POSTFIX
    # ----------------------------------------------------------
    print("Postfix:", end=" ")
    cur = queue.front
    while cur is not None:
        print(cur.elem, end=" ")
        cur = cur.next
    print()

    # ----------------------------------------------------------
    # STEP 4: EVALUATE POSTFIX
    # ----------------------------------------------------------
    evalStack = Stack()
    cur = queue.front

    while cur is not None:
        token = cur.elem

        if token[0] >= '0' and token[0] <= '9':  # operand
            val = 0
            for d in token:
                val = val*10 + (ord(d) - ord('0'))
            evalStack.push(val)

        else:  # operator
            b = evalStack.pop()
            a = evalStack.pop()

            if token == '+': evalStack.push(a + b)
            elif token == '-': evalStack.push(a - b)
            elif token == '*': evalStack.push(a * b)
            elif token == '/': evalStack.push(a // b)
            elif token == '^':
                # simple power (no built-in)
                res = 1
                for _ in range(b):
                    res *= a
                evalStack.push(res)

        cur = cur.next

    print("Result:", evalStack.pop())
