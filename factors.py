import math

def solution(N):
    result = 0
    sq_root = math.ceil(math.sqrt(N))
    for i in range(1, sq_root):
        if int(N / i) * i == N:
            result += 2

    if sq_root * sq_root == N:
        result += 1

    return result

def main():
    print(solution(24))


if __name__ == '__main__':
    main()
