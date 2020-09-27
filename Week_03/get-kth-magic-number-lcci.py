class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        numList = [1]
        p3 = p5 = p7 = 0
        for _ in range(k):
            minNum = min(numList[p3] * 3, numList[p5] * 5, numList[p7] * 7)
            numList.append(minNum)

            if minNum == numList[p3] *3: p3 +=1
            if minNum == numList[p5] *5: p5 +=1
            if minNum == numList[p7] *7: p7 +=1

        return numList[k-1]

    def getKthMagicNumber1(self, k: int) -> int:
        nums = [3, 5, 7]
        heap = [1]
        dedu = set([1])

        for _ in range(k):
            res = heapq.heappop(heap)
            for num in nums:
                cur = res * num
                if cur not in dedu:  # 用集合set去重
                    dedu.add(cur)
                    heapq.heappush(heap, cur)
        return res

    def getKthMagicNumber2(self, k: int) -> int:
        nums = [3, 5, 7]
        heap = [1]

        for _ in range(k):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:  # 在堆顶去重
                res = heapq.heappop(heap)
            for num in nums:
                heapq.heappush(heap, res * num)
        return res

    def getKthMagicNumber3(self, k: int) -> int:
        nums = [3, 5, 7]
        heap = [(1, 1)]

        for _ in range(k):
            res, flag = heapq.heappop(heap)
            for num in nums:
                if flag <= num:  # 利用flag直接去重
                    heapq.heappush(heap, (res * num, num))
        return res