class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        n1 = len(s1)
        n2 = len(s2)

        l=0
        s1_dict = {}


        for i in range(n1):

            if s1[i] in s1_dict:
                s1_dict[s1[i]] += 1
            else:
                s1_dict[s1[i]] = 1
        
        
        for i in range(n1):

            if s2[i] in s1_dict:
                s1_dict[s2[i]] -= 1
            else:
                s1_dict[s2[i]] = -1

        flag = True
        for key in s1_dict:
            if s1_dict[key] != 0:
                flag = False
        
        if flag:
            return True

        
        for i in range(n1,n2):

            if s2[i] in s1_dict:
                s1_dict[s2[i]] -= 1
            else:
                s1_dict[s2[i]] = -1


            if s2[i-n1] in s1_dict:
                s1_dict[s2[i-n1]] += 1
            else:
                s1_dict[s2[i-n1]] = 1


            flag = True
            for key in s1_dict:
                if s1_dict[key] != 0:
                    flag = False
            
            if flag:
                return True

        return False

        