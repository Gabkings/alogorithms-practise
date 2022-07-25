class Solution:

    def getMedian(self, arr1, arr2):
        i, j = 0, 0
        m1, m2 = -1, -1

        n = len(arr1)

        count = 0
        while count < n + 1:
            count += 1

            # Below is to handle case where all
            # elements of ar1[] are smaller than
            # smallest(or first) element of ar2[]
            if i == n:
                m1 = m2
                m2 = ar2[0]
                break

            # Below is to handle case where all
            # elements of ar2[] are smaller than
            # smallest(or first) element of ar1[]
            elif j == n:
                m1 = m2
                m2 = ar1[0]
                break
            # equals sign because if two
            # arrays have some common elements
            if ar1[i] <= ar2[j]:
                m1 = m2  # Store the prev median
                m2 = ar1[i]
                i += 1
            else:
                m1 = m2  # Store the prev median
                m2 = ar2[j]
                j += 1
        return (m1 + m2)/2

    def findMedianSortedArrays(self, nums1, nums2):
        merged_arr = nums1 + nums2
        merged_arr.sort()
        n = len(merged_arr)
        if(n % 2 == 0):
            return (merged_arr[int(n/2) - 1] + merged_arr[int(n/2)])/2
        else:
            return merged_arr[int(n/2)]


sln = Solution()

ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]

print(sln.findMedianSortedArrays(ar1, ar2))
