class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_length = len(s)
        wordDict = sorted(wordDict, key=lambda x : len(x))

        word_length = [0] * len(wordDict)
        for i, word in enumerate(wordDict):
            word_length[i] = len(word)

        dp = [False] * s_length
        dp[0] = True

        for i in range(s_length):
            if dp[i]:
                for j, word in enumerate(wordDict):
                    reach = i + word_length[j]
                    if reach > s_length:
                        break

                    if s.startswith(word, i):
                        reach = i + word_length[j]
                        if reach == s_length:
                            return True
                        dp[reach] = True

        return False