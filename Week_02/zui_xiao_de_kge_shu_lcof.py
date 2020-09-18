class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        import heapq
        return heapq.nsmallest(k, arr)