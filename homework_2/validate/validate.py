def validate(pushed, popped):
    stack = []
    pop_index = 0

    for num in pushed:
        stack.append(num)

        while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1

    return len(stack) == 0
