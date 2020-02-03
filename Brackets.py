def solution(S):

    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for symbol in S:
        if symbol in pairs:
            stack.append(pairs[symbol])
        else:
            if not stack:
                return 0
            if stack.pop() != symbol:
                return 0

    return 1


def isValidPair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True 
    if left == '{' and right == '}':
        return True   
    return False
 

def solution_100(S):
    stack = []
     
    for symbol in S:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return 0
            last = stack.pop()
            if not isValidPair(last, symbol):
                return 0
     
    if len(stack) != 0:
        return 0
             
    return 1


if __name__ == "__main__":
    print(solution("[([)()]])"))  # 0
    print(solution("{[()()]}"))  # 1

