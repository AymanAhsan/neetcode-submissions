class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            s_count = Counter(s)
            count_key = frozenset(s_count.items())

            res[count_key].append(s)
            
        return list(res.values())