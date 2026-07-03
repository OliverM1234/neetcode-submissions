class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        l=0
        str_dict = {".":0}

        for r in range(len(s)):
            
            if s[r] in str_dict:
                str_dict[s[r]]+=1
            else:
                str_dict[s[r]] = 1

            while (r-l+1) > (max(str_dict.values()) + k):
                
                str_dict[s[l]] -= 1
                l += 1
                

            res = max(res, r-l+1)

            print(l,r,res,str_dict)

        return res
                    
                
                
            

            