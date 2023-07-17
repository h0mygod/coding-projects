class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = []
        counts = []
        for x in range(len(strs)):
            counts.append({})
            word = strs[x]
            for i in range(len(word)):
                counts[x][word[i]] = 1 + counts[x].get(word[i], 0)
        length = len(counts)
        print(counts)
        for m in range(length):
            anagrams.append([])
            selected = counts[m]
            for n in range(length):
                if selected == counts[n]:
                    anagrams[m].append(strs[n])

        new_anagrams = []
        for elem in anagrams:
            if elem not in new_anagrams:
                new_anagrams.append(elem)
        return new_anagrams
