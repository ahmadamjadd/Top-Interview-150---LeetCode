class Node:
    def __init__(self):
        self.children = {}
        self.isTerminal = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = Node()
            currNode = currNode.children[c]
        currNode.isTerminal = True

    def search(self, word: str) -> bool:
        def dfs(index: int, currNode: Node) -> bool:
            if index == len(word):
                return currNode.isTerminal

            c = word[index]

            if c == ".":
                for child in currNode.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            if c not in currNode.children:
                return False
            return dfs(index + 1, currNode.children[c])

        return dfs(0, self.root)
