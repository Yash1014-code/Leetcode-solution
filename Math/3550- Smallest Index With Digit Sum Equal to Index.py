lass Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx,num in enumerate(nums):
            c_sum=0
            while num!=0:
                c_sum += (num%10)
                num//=10
            if idx == c_sum:
                return idx
        return -1
