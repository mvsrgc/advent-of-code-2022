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
        self.children.append(child)

    def print_tree(self) -> None:
        spaces = " " * self.get_level() * 4
        if self.size is None:
            print(spaces + self.name)
        else:
            print(spaces + str(self.size) + "-" + self.name)

        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

    def search(self, name: str, size: int | None = None) -> TreeNode | None:
        if self.name == name and self.size == size:
            return self

        node = None
        for child in self.children:
            node = child.search(name, size)
            if node is not None:
                break

        return node

    def get_level(self) -> int:
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def get_size(self) -> int:
        size = 0

        if self.size:
            size += self.size

        for child in self.children:
            size += child.get_size()

        return size

    def get_at_most(self, most: int) -> int:
        size = 0

        if self.get_size() <= most:
            size += self.get_size()


        return size

    def __repr__(self) -> str:
        return f"{self.name} - {self.size}"


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")

    tree = TreeNode("/")
    last_dir = None
    for idx, line in enumerate(lines):
        if line.startswith("$ cd .."):
            if last_dir.parent is not None:
                last_dir = last_dir.parent
            else:
                last_dir = tree.search("/")

        if (
            line.startswith("$ cd")
            and not line.startswith("$ cd ..")
            and not line.startswith("$ cd /")
        ):
            dir_name = line.split(" ")[2]
            last_dir = tree.search(dir_name)

        if line.startswith("$ cd /"):
            last_dir = tree.search("/")

        if line.startswith("$ ls"):
            for i in range(9999):  # yeah...
                if idx + i + 1 > len(lines) - 1:
                    break

                ls_line = lines[idx + i + 1]

                if ls_line.startswith("$"):
                    break

                if ls_line.split(" ")[0] == "dir":
                    dir_name = ls_line.split(" ")[1]
                    searched = tree.search(dir_name)
                    if searched is not None:
                        continue
                    last_dir.add_child(TreeNode(dir_name))
                else:
                    size = int(ls_line.split(" ")[0])
                    file_name = ls_line.split(" ")[1]
                    searched = tree.search(file_name, size)
                    if searched is not None:
                        continue
                    last_dir.add_child(TreeNode(file_name, size))
    tree.print_tree()
    print(tree.get_at_most(100000))


def test_1():
    print()
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

    assert tree.search("folder_1") is not None
    assert tree.search("folder_2") is not None
    assert tree.search("folder_3") is None

    folder_3 = TreeNode("folder_3")
    tree.add_child(folder_3)
    assert tree.search("folder_3") is not None

    file_node = TreeNode("duplicate.txt", 12345)
    folder_3.add_child(file_node)

    searched = tree.search("duplicate.txt", 12345)
    assert searched.name == "duplicate.txt" and searched.size == 12345

    duplicate_file_node = TreeNode("duplicate.txt", 54321)
    folder_2.add_child(duplicate_file_node)

    searched = tree.search("duplicate.txt", 54321)
    assert searched.name == "duplicate.txt" and searched.size == 54321

    folder_3.add_child(TreeNode("folder_3", 12345))

    searched = tree.search("folder_3", 12345)
    assert searched.name == "folder_3" and searched.size == 12345


def test_2():
    tree = TreeNode("/")

    folder_a = TreeNode("a")
    tree.add_child(folder_a)

    folder_e = TreeNode("e")

    folder_a.add_child(folder_e)

    folder_e.add_child(TreeNode("i", 584))

    folder_a.add_child(TreeNode("f", 29116))
    folder_a.add_child(TreeNode("g", 2557))
    folder_a.add_child(TreeNode("h.lst", 62596))

    tree.add_child(TreeNode("b.txt", 14848514))
    tree.add_child(TreeNode("c.dat", 8504156))

    folder_d = TreeNode("d")
    tree.add_child(folder_d)
    folder_d.add_child(TreeNode("j", 4060174))
    folder_d.add_child(TreeNode("d.log", 8033020))
    folder_d.add_child(TreeNode("d.ext", 5626152))
    folder_d.add_child(TreeNode("k", 7214296))

    assert folder_e.get_size() == 584
    assert folder_a.get_size() == 94853
    assert folder_d.get_size() == 24933642
    assert tree.get_size() == 48381165

    assert tree.get_at_most(500) == 0
    assert tree.get_at_most(584) == 584
    assert tree.get_at_most(100000) == 95437

    tree.print_tree()