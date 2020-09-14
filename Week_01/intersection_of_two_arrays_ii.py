class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return num.elements()

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1, num2 = map(collections.Counter, (nums1, nums2))
        return (num1 & num2).elements()

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        哈希计数
        :param nums1:
        :param nums2:
        :return:
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection

    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 对两个数组分别排序
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        # 设置两个指针，分别指向两个数组的首部
        index1 = index2 = 0
        # 当两个数组指针其中任意一个超出列表长度,则终止循环
        while index1 < length1 and index2 < length2:
            # 当值nums1指针值小于nums2指针值时，则nums1指针向右移动一位
            if nums1[index1] < nums2[index2]:
                index1 += 1
            # 当值nums1指针值大于nums2指针值时，则nums2指针向右移动一位
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                # 当值nums1指针值等于nums2指针值时，则将结果存起来,并且两个指针分别向右移动一位
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection