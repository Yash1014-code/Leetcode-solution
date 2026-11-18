import heapq
class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = []
        ans = []
        n = len(nums1)
        m = len(nums2)

        for i in range(min(n,k)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))

        while heap and len(ans)<k :
            s, i, j = heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])

            if j+1<m:
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
        return ans        
