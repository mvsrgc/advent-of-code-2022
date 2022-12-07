from __future__ import annotations

import pytest


class TreeNode:
    def __init__(self, name: str, size: int | None = None) -> None:
        self.name = name
        self.size = size
        self.children: list[TreeNode] = []
        self.parent = None

    def add_child(self, child: TreeNode) -> None:
        child.parent = self
        if child not in self.children:
            self.children.append(child)

    def print_tree(self) -> None:
        spaces = " " * self.get_level() * 3
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

    def __repr__(self) -> str:
        return self.name


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")

    tree = TreeNode("/")
    last_dir = tree.search("/")
    for idx, line in enumerate(lines):
        if line.startswith("$ cd .."):
            if last_dir.parent is not None:
                last_dir = last_dir.parent
            else:
                last_dir = tree.search("/")
        if (
            line.startswith("$ cd")
            and not line.startswith("$ cd /")
            and not line.startswith("$ cd ..")
        ):
            # directory change
            folder_name = line.split(" ")[2]
            node = tree.search(folder_name)
            if node is not None:
                last_dir.add_child(node)
                last_dir = node
            else:
                if last_dir is not None:
                    last_dir.add_child(TreeNode(folder_name))

        if line.startswith("$ ls"):
            # list of files and folders
            count = 1
            if idx + count < len(lines) - 1:
                this_line = lines[idx + count]
            while not this_line.startswith("$"):
                if this_line.split(" ")[0] == "dir":
                    # it's a dir
                    node_name = this_line.split(" ")[1]
                    node = TreeNode(name=node_name)
                    if tree.search(node) == None:
                        last_dir.add_child(node)
                else:
                    # it's a file
                    node_name = this_line.split(" ")[1]
                    node_size = int(this_line.split(" ")[0])
                    node = TreeNode(name=node_name, size=node_size)
                    if tree.search(node) == None:
                        last_dir.add_child(node)

                count += 1
                this_line = lines[idx + count]

    tree.print_tree()


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
