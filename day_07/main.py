from __future__ import annotations

import pytest


class TreeNode:
    def __init__(self, name: str, data: str | None = None) -> None:
        self.name = name
        self.data = data
        self.children: list[TreeNode] = []
        self.parent = None

    def add_child(self, child: TreeNode) -> None:
        child.parent = self
        self.children.append(child)

    def print_tree(self) -> None:
        spaces = ' ' * self.get_level() * 3
        print(spaces + self.name)

        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

    def search(self, name: str) -> TreeNode | None:
        if self.name == name:
            return self

        if len(self.children) > 0:
            for child in self.children:
                return child.search(name)

        return None

    def get_level(self) -> int:
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level


def test_1():
    tree = TreeNode("/")
    assert tree.children == []

    folder_1 = TreeNode("folder_1")
    folder_2 = TreeNode("folder_2")
    folder_1.add_child(folder_2)
    tree.add_child(folder_1)
    assert tree.children == [folder_1]
    assert tree.children[0].parent == tree
    assert tree.children[0].children == [folder_2]
    assert tree.children[0].children[0].parent == folder_1
    assert tree.get_level() == 0
    assert tree.children[0].get_level() == 1
    assert tree.children[0].children[0].get_level() == 2

    folder_2_searched = tree.search("folder_2")
    assert folder_2_searched.name == "folder_2"
    assert tree.search("folder_3") == None

    tree.add_child(TreeNode("folder_3"))
    assert len(tree.children) == 2
    tree.print_tree()
