def solution(A):

    if not A:
        return 0

    starts = []
    stops = []

    for center in range(len(A)):
        starts.append(center - A[center])
        stops.append(center + A[center])

    starts.sort()
    stops.sort()

    num_open = 0
    result = 0
    c_idx = 0

    for o_idx in range(len(starts)):

        if starts[o_idx] > stops[c_idx]:
            while stops[c_idx] < starts[o_idx]:
                num_open -= 1
                c_idx += 1

        result += num_open
        if result > 10_000_000:
            return -1

        num_open += 1

    return result


if __name__ == "__main__":
    print(solution([1, 5, 2, 1, 4, 0]))

