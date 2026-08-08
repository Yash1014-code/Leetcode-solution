class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap={}
        for num in arr:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        hashset=set()
        flag=True
        for count in hashmap.values():
            if count in hashset:
                flag= False
            else:
                hashset.add(count)
        return flag 
