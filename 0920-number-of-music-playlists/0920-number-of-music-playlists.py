class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        Q = 10 ** 9 + 7

        ans = 1
        for i in range(n, n - k, -1):
            ans = ans * i % Q

        tmp = ans
        ans *= (n - k) ** (goal - k) % Q

        sign = 1
        for i in range(1, n - k):
            ans = (ans - sign * tmp * comb(n - k, i) * (n - k - i) ** (goal - k)) % Q
            sign = -sign

        return ans