import sys

if __name__ == '__main__':
    output = []
    while True:
        word = input()
        stack = []
        if word == '.':
            break
        else:
            for i in range(len(word)):
                if word[i] == '(':
                    stack.append('(')
                elif word[i] == '[':
                    stack.append('[')
                elif word[i] == ')':
                    if len(stack) == 0:
                        stack.append(')')
                    else:
                        if stack[len(stack)-1] == '(':
                            stack.pop()
                        else:
                            stack.append(')')
                elif word[i] == ']':
                    if len(stack) == 0:
                        stack.append(']')
                    else:
                        if stack[len(stack)-1] == '[':
                            stack.pop()
                        else:
                            stack.append(']')
            if len(stack) == 0:
                output.append('yes')
            else:
                output.append('no')
    for j in range(len(output)):
        print(output[j])
