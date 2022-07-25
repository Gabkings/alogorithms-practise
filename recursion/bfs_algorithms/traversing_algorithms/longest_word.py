import json
class Trie:
    def __init__(self):
        self.nodes = {}
    
    def add(self, word):
        nodes = self.nodes
        for i, ch in enumerate(word):
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
        nodes["#"] = {}
        
    def matches(self, word):
        nodes = self.nodes
        valid = True
        for i, ch in enumerate(word):
            if ch not in nodes or "#" not in nodes[ch]:
                valid = False
                break
            else:
                nodes = nodes[ch]
        return valid
    '''
    For debugging
    '''
    def printTrie(self):
        print(json.dumps(self.nodes, indent=4, sort_keys=True))
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        
        for word in words:
            t.add(word)
        
        m, w = float("-inf"), ""
        for word in words:
            if t.matches(word):
                l = len(word)
                if l > m:
                    w = word
                    m = l
                elif l == m:
                    if w and w > word:
                        w = word
        return w
