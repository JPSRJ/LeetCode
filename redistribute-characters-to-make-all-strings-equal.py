class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}
        for i in words:
            for j in i:
                count[j] = count.get(j, 0) + 1

        for x in count.values():
            if x % len(words) != 0:
                return False
        return True
