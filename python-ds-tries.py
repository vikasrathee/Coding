# class TrieNode:
#     def __init__(self) -> None:
#         self.children = {}
#         self.end = 0

# class Trie:
#     def __init__(self) -> None:
#         self.root = TrieNode()
    
#     def build(self,words):
#         for word in words:
#             self.put(word)
    
#     def put(self, word):
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 next = TrieNode()
#                 node.children[ch] = next
#                 node = next
#             else:
#                 node = node.children[ch]
#         node.end = 1

#     def dfs(self, node, prefix, suggest):
#         if node.children:
#             for char in node.children:
#                 suggest_word = prefix + char
#                 if node.children[char].end:
#                     suggest.append(suggest_word)                
#                 self.dfs(node.children[char], suggest_word,suggest)

#     def find(self, prefix):
#         node = self.root
        
#         for ch in prefix:
#             if ch in node.children:
#                 node = node.children[ch]
#             else:
#                 return []

#         # traverse to get all 
#         suggest = []
#         self.dfs(node, prefix, suggest)
#         return suggest

    

# if __name__=="__main__":
#     temp=Trie()
#     temp.build(["naveen","sethu","logan","nainika", "love", "limca"])
#     x=temp.find("l")
#     print(x)
#     pass






class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = 0

class Trie:
    
    def __init__(self) -> None:
        self.root = TrieNode()

    def build(self, words):
        for word in words:
            self.add(word)
    
    def add(self, word):
        node = self.root

        for _ in word:
            if _ not in node.children:
                next = TrieNode()
                node.children[_]  = next
                node = next
            else:
                node = node.children[_]
        
        node.end = 1


    def dfs(self, node, prefix, suggest):
            if node.children:
                for _ in node.children:
                    suggest_word = prefix + _
                    if node.children[_].end == 1:
                        print(suggest_word)
                        suggest.append(suggest_word)
                    self.dfs(node.children[_], suggest_word, suggest)

    def find(self, prefix):
        node = self.root

        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return []

        suggest = []
        self.dfs(node, prefix, suggest)

        return suggest


if __name__=="__main__":
    temp=Trie()
    temp.build(["n","sethu","logan","nainika", "love", "limca"])
    print(temp.root.children)
    x=temp.find("")
    print(x)
    pass



    

