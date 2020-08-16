"""
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.
You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.

https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/
"""


class Solution:
    map = dict()

    def minDays(self, n: int) -> int:

        if n in self.map:
            return self.map[n]

        self.map[n] = 1 if n == 1 else 2 if n == 2 or n == 3 else 1 + min(((n % 2) + self.minDays(n // 2)),
                                                                          ((n % 3) + self.minDays(n // 3)))

        return self.map[n]


if __name__ == "__main__":
    sol = Solution()
    answer = sol.minDays(10)
    print(answer) # 4
