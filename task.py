import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    # Завдання 1: Знайти найбільше значення в дереві
    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    @staticmethod
    def _find_max(node):
        current = node
        while current.right:
            current = current.right
        return current.value

    # Завдання 2: Знайти найменше значення в дереві
    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    @staticmethod
    def _find_min(node):
        current = node
        while current.left:
            current = current.left
        return current.value

    # Завдання 3: Знайти суму всіх значень в дереві
    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.value + self._sum_values(node.left) + self._sum_values(node.right)


tree = BinarySearchTree()
for _ in range(10):
    val = random.randint(1, 100)
    print(f"Додано значення: {val}")
    tree.insert(val)

print("Максимальне значення:", tree.find_max())
print("Мінімальне значення:", tree.find_min())
print("Сума всіх значень:", tree.sum_values())
