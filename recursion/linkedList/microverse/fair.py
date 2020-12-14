def solution(A, B):
    if len(A) <= 1:
        return 0
    for index in range(1, len(A)):
        A[index] = A[index - 1] + A[index]
        B[index] = B[index - 1] + B[index]
    indices = 0
    for index in range(0, len(A) - 1):
        prefix_a = A[index]
        prefix_b = B[index]
        suffix_b = B[-1] - prefix_b
        suffix_a = A[-1] - prefix_a
        sums = {prefix_a, prefix_b, suffix_b, suffix_a}

        if len(sums) == 1:
            indices += 1
    return indices
