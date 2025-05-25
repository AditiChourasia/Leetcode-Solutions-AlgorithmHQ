# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from bisect import bisect_left
from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse=True)
        n, m = len(tasks), len(workers)

        def canAssign(mid: int) -> bool:
            pills_used = 0
            available_workers = sorted(workers[:mid])  # Get the strongest `mid` workers

            for i in range(mid - 1, -1, -1):  # Assign the hardest tasks first
                required = tasks[i]

                if available_workers[-1] >= required:
                    available_workers.pop()
                elif pills_used < pills:
                    idx = bisect_left(available_workers, required - strength)
                    if idx == len(available_workers):
                        return False  # No worker can be boosted enough
                    available_workers.pop(idx)
                    pills_used += 1
                else:
                    return False  # No pills left and no strong enough worker
            return True

        low, high = 0, min(n, m)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if canAssign(mid):
                ans = mid
                low = mid + 1  # Try to assign more tasks
            else:
                high = mid - 1  # Try fewer tasks

        return ans
