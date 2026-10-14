class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        out = []
        num_dict = {}

        for n in nums:

            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1

        unique_nums = list(num_dict.keys())
        print(num_dict, unique_nums)

        def genCombs(i, cur):

            if i >= len(unique_nums):
                print(cur)
                out.append(cur.copy())
                return

            cur_num = unique_nums[i]

            print(f"cur_num: {cur_num},num_dict[cur_num]: {num_dict[cur_num]},i: {i},cur: {cur}")
            
            genCombs(i+1, cur)
            
            for _ in range(num_dict[cur_num]):
                cur.append(cur_num)
                genCombs(i+1, cur)

            for _ in range(num_dict[cur_num]):
                cur.pop()

                

        genCombs(0, [])

        return out