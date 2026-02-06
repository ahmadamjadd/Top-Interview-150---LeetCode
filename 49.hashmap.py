class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in final_dict:
                final_dict[sorted_word] = [word]
            else:
                final_dict[sorted_word].append(word)
        ans = []
        for key,value in final_dict.items():
            ans.append(value)
        return ans
                            
            

        
