"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q),
such that 0 ≤ P ≤ Q < N, is called a slice of array A.
The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
"""

def solution(A):
    # On the every step we are searching for max sum for the array which ends on the current element.
    # This sum is the best of the current element and the maximum sum for previous element plus the current element.
    # The approach doesn't work for the case when all elements are below the zero.
    # For that case the max sum is equal to the max (negative) element.
    max_ending = result = 0
    all_negative = True
    max_negative = A[0]
    for a in A:
        max_ending = max(a, max_ending + a)
        result = max(result, max_ending)
        if a < 0:
            max_negative = max(max_negative, a)
        else:
            all_negative = False

    if all_negative:
        return max_negative

    return result


def main():
    a = [3, 2, -6, 4, 0]
    print("solution is", solution(a))

    a = [-3, -2, -6, -4, -10]
    print("solution is", solution(a))


if __name__ == '__main__':
    main()
