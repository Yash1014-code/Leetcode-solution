class Solution:
    def ladderLength(self, beginword: str, endword: str, wordset: List[str]) -> int:
        wordset=set(wordset)
        if endword not in wordset:
            return 0
        queue= deque()
        queue.append((beginword,1))
        while len(queue)!=0:
            curr_word,level=queue.popleft()
            if curr_word==endword : return level
            for i in range(0,len(curr_word)):
                for ch in "qwertyuiopasdfghjklzxcvbnm":
                    if ch == curr_word[i]:
                        continue
                    new_word=curr_word[:i]+ch+curr_word[i+1:]
                    if new_word in wordset:
                        queue.append((new_word,level+1))
                        wordset.remove(new_word)
        return 0                    
        
