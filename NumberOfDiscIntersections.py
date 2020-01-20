from collections import defaultdict


def solution(A):

    if not A:
        return 0

    starts = []
    stops = []

    for center in range(len(A)):
        starts.append(center - A[center])
        stops.append(center + A[center])

    x0 = min(starts)
    x1 = max(starts)

    start_counts = defaultdict(int)
    stop_counts = defaultdict(int)

    for start in starts:
        start_counts[start] += 1

    for stop in stops:
        stop_counts[stop] += 1

    result = 0
    opened = 0
    for idx in range(x0, x1 + 1):
        if start_counts[idx] > 0:
            if opened > 0:
                for _ in range(start_counts[idx]):
                    result += opened
                    opened += 1
            else:
                result += start_counts[idx] - 1
                opened += start_counts[idx]

            if result > 10_000_000:
                return -1

        opened -= stop_counts[idx]

    return result


if __name__ == "__main__":
    print(solution([1, 5, 2, 1, 4, 0]))

