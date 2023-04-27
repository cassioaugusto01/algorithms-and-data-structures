class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        suffixes = []
        for char, child_node in self.children.items():
            if child_node.is_word:
                suffixes.append(suffix + char)
            suffixes += child_node.suffixes(suffix=suffix + char)
        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# Test
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


# Test cases
f('ant')  # Should print: hology, agonist, onym
f('f')     # Should print: un, unction, actory
f('tri')   # Should print: e, gger, gonometry, pod

# Edge cases
# Test Case 1: Empty input
f('')  # Should print: empty line
# Test Case 2: Non-existent prefix
f('xyz')  # Should print: xyz not found
# Test Case 3: Single character words
MyTrie.insert("a")
f("a")  # Should print: empty line (as "a" is a word itself)
# Test Case 4: Large input
large_word = "a" * 1000
MyTrie.insert(large_word)
f("a" * 999)  # Should print: a (as it's the suffix of the large input)
