class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        q, heap, freq = deque(), [], Counter(tasks)
        for k,v in freq.items():
            heapq.heappush(heap, -v)
        cnt = 0
        while heap or q:
            cnt += 1
            if heap:
                task = heapq.heappop(heap)
                if task+1 != 0:
                    q.append((task+1, n+cnt))
            if q and q[0][1] == cnt:
                newFreq, _ = q.popleft()
                heapq.heappush(heap, newFreq)
        return cnt