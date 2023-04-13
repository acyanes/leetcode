class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popindex = 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and popindex < len(popped) and popped[popindex]==stack[-1]:
                stack.pop()
                popindex+=1
        return len(stack) == 0