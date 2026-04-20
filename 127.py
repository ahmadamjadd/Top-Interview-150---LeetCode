from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char == word[i]:
                        continue
                        
                    neighbor = word[:i] + char + word[i+1:]
                    
                    if neighbor in wordSet:
                        wordSet.remove(neighbor)
                        queue.append((neighbor, level + 1))
                        
        return 0
