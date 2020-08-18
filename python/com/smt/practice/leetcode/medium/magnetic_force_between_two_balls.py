"""
1552. Magnetic Force Between Two Balls
User Accepted:1408
User Tried:2639
Total Accepted:1478
Total Submissions:5118
Difficulty:Medium
In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

------------
Runtime: 1040 ms, faster than 99.23% of Python3 online submissions for Magnetic Force Between Two Balls.
Memory Usage: 27 MB, less than 81.58% of Python3 online submissions for Magnetic Force Between Two Balls.

"""
from typing import List


class Solution:
    map = {}

    def maxDistance(self, position: List[int], m: int) -> int:
        self.map = {}
        position.sort()
        min_pos = position[0]
        max_pos = position[-1]
        # print("max: ", max_pos, ", min: ", min_pos)
        span = max_pos - min_pos + 1
        # print("span: ", span)
        max_interval = ((span - m) // (m - 1)) + 1
        # print("max_interval: ", max_interval)
        '''
        while max_interval >= 1:
            if self.balls_with_min_dist(position, max_interval) >= m:
                return max_interval
            max_interval -= 1
        '''
        l, r = 1, max_interval
        while l <= r:
            # print("L: ", l, ", R: ", r)
            if l == r:
                if self.balls_with_min_dist(position, l) >= m:
                    max_interval = l
                else:
                    max_interval = l - 1
                break
            mid = (l + r) // 2
            if self.balls_with_min_dist(position, mid) >= m:
                l = mid + 1
                max_interval = mid
            else:
                r = mid
        return max_interval

    def balls_with_min_dist(self, position: List[int], min_dist: int):
        if min_dist in self.map:
            return self.map[min_dist]
        # print("counting balls at min diatance: ", min_dist)
        cnt = 1
        prev_pos = position[0]
        for i in range(1, len(position)):
            if position[i] - prev_pos >= min_dist:
                # print(position[i], " - ", prev_pos, " >= ", min_dist)
                cnt += 1
                prev_pos = position[i]
            else:
                # print("skipping: ", position[i])
                pass
        self.map[min_dist] = cnt
        return cnt


