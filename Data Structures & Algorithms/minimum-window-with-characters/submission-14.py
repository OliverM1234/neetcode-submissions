class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sol = s+"."

        if len(t) > len(s):
            return ""

        t_dict = {}

        for l in t:
            if l in t_dict:
                t_dict[l] += 1
            else:
                t_dict[l] = 1

        l = 0

        for r in range(len(s)):

            if s[r] in t_dict:
                t_dict[s[r]] -= 1

            flag = True
            for key in t_dict:
                if t_dict[key] > 0:
                    flag = False

            while flag:
                print(l,r, t_dict)


                if s[l] not in t_dict:
                    l += 1
                    continue


                if t_dict[s[l]] < 0:
                    t_dict[s[l]] += 1
                    l +=1

                elif t_dict[s[l]] == 0:


                    run = True
                    for key in t_dict:
                        if  t_dict[key] > 0:
                            flag = False
                            run = False

                    if run:
                        if (r-l+1) < len(sol):
                            sol = s[l:(r+1)]
                        
                    flag = False

                    
                else:

                    flag = False

                            
                        



        if sol == (s+"."):
            return ""

        return sol


        