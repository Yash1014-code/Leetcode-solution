class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        prefix = [0] * n
        max_left = 0 
        for i in range(n):
            max_left = max(max_left, height[i])
            prefix[i] = max_left
        suffix = [0] * n
        max_right = 0
        for i in range(n-1,-1,-1):
            max_right = max(max_right, height[i])
            suffix[i] = max_right
        
        # Step 3: Calculate trapped water
        water = 0
        for k in range(n):
            water += min(prefix[k], suffix[k]) - height[k]
        
        return water
