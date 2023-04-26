class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()

class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler

class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        return [part for part in path.split("/") if part]

# Test Cases
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'
