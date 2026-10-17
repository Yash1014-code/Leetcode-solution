class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitSum(num):
            total = 0
            while num :
                total += num%10
                num //= 10
            return total

        n = len(nums)
        order = sorted(range(n), key= lambda x: (digitSum(nums[x]),nums[x]))
        visited = [False]*n
        swap = 0

        for i in range(n):
            if visited[i]:
                continue
            cycle = 0
            j = i
            while not visited[j]:
                visited[j]=True
                j = order[j]
                cycle+=1
            swap += cycle-1
        return swap   



        
