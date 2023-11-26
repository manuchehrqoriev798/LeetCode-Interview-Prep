class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        result = []
        for i, a in enumerate(s_nums):
            if i > 0 and a == s_nums[i-1]:                          # for skiping dublicate
                continue

            l, r = i + 1, len(s_nums)-1
            while l < r:
                threeSum = a + s_nums[l] + s_nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, s_nums[l], s_nums[r]])         # adds solution to result
                    l += 1                                           # changes l pointer in order to continue
                    while s_nums[l]==s_nums[l-1] and l < r:          # checks if there are two neighbors so it will just skip them by incrementing l
                        l += 1
        return result



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):

            l, r = i + 1, len(nums) - 1
            while l < r:

                potentialSum = nums[i] + nums[l] + nums[r] 
                if potentialSum > 0:
                    r -= 1
                elif potentialSum < 0:
                    l += 1
                else:
                    triplets.add((nums[i] , nums[l] ,nums[r]))
                    l += 1

        return triplets






class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        negatives, positives, zeros = [], [], []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeros.append(num)

        # for checking in 0(1) time
        negatives_set, positives_set = set(negatives), set(positives)

        if zeros:
            for num in positives_set:
                if -1 * num in negatives_set:
                    res.add(tuple([-1*num, 0, num]))
        
        if len(zeros) >= 3:
            res.add(tuple([0, 0, 0]))
        
        # 5. For all pairs of negative numbers (-3, -1), check to see if their complement (4) exists in the positive number set
        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                target = -1 * (negatives[i] + negatives[j])
                if target in positives_set:
                    res.add(tuple(sorted([negatives[i], negatives[j], target])))
        

        # 5. For all pairs of negative numbers (-3, -1), check to see if their complement (4) exists in the positive number set
        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                target = -1 * (positives[i] + positives[j])
                if target in negatives_set:
                    res.add(tuple(sorted([positives[i], positives[j], target])))


        return res

             