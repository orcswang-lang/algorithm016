class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)
        return list(dic.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [sorted(members) for _, members in groups]

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
