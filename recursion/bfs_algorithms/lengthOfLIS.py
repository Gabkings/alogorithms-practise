def arrayChallenge(arr):
    if not arr:
        return 0

    # dp[i] := LIS ending at nums[i]
    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# arr = [9,9,4,2]
arr = [10,22,9,33,21,50,41,60,22,68,90]

print(arrayChallenge(arr))