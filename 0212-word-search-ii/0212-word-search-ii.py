class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.word = word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        trie = Trie()

        for word in words:
            trie.insert(word)

        row = len(board)
        col = len(board[0])

        ans = []

        def dfs(r, c, node):

            ch = board[r][c]

            if ch not in node.children:
                return

            node = node.children[ch]

            if node.word is not None:
                ans.append(node.word)
                node.word = None

            board[r][c] = '#'

            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, node)

            if r + 1 < row and board[r + 1][c] != '#':
                dfs(r + 1, c, node)

            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, node)

            if c + 1 < col and board[r][c + 1] != '#':
                dfs(r, c + 1, node)

            board[r][c] = ch

        for r in range(row):
            for c in range(col):
                dfs(r, c, trie.root)

        return ans