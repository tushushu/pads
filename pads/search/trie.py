# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-09 11:50:14
@Last Modified by:   tushushu
@Last Modified time: 2018-11-09 11:50:14
"""
from itertools import chain


class Trie(object):
    """Trie class to match one or many strings.

    Properties:
        tree {dict} -- Multi-level dict. Set the common prefix as key,
        end with "|". e.g. words → tree
        words: ["hi", "how", "high"]
        tree: {"h": {"i": {"|": None, "g": {"h": {"|": None}}},
        "o": {"w": {"|": None}}}}
    """

    def __init__(self, words):
        self.tree = self._build_tree(words)

    def __str__(self):
        return str(self.tree)

    def _build_tree(self, words):
        """Build a dict tree by input words.

        Arguments:
            words {list} -- 1d list with string. e.g. ["hi", "how", "high"]

        Returns:
            dict
        """

        head = {}
        for word in words:
            node = head
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            else:
                node["|"] = None
        return head

    def match_one(self, s):
        """Match and return only one word between s and tree.

        Arguments:
            s {str} -- Target string. Should not contain "@" or "|".

        Returns:
            str
        """

        node = self.tree
        ret = []
        iterator = chain(s, "@")
        for c in iterator:
            if "|" in node:
                return ''.join(ret)
            if c in node:
                ret.append(c)
                node = node[c]
            else:
                node = self.tree
                ret = []
        return None

    def match_many(self, s):
        """Match and return all the words between s and tree.

        Arguments:
            s {str} -- Target string. Should not contain "@" or "|".

        Returns:
            list
        """

        node = self.tree
        rets = []
        ret = []
        iterator = chain(s, "@")
        for c in iterator:
            if "|" in node:
                rets.append(''.join(ret))
            if c in node:
                ret.append(c)
                node = node[c]
            else:
                node = self.tree
                ret = []
                if c in node:
                    ret.append(c)
                    node = node[c]
        return rets


def test():
    words = ["hi", "high", "good", "go", "how", "great", "nice"]
    tree = Trie(words)
    test_cases = [
        ["hi", "hi", ["hi"]],
        ["high", "hi", ["hi", "high"]],
        ["", None, []],
        ["like", None, []],
        ["nohighgood", "hi", ["hi", "high", "go", "good"]]
    ]
    for test_case in test_cases:
        s, one, many = test_case
        assert tree.match_one(s) == one
        assert all(a == b for a, b in zip(tree.match_many(s), many))
    print("All the tests passed!")


if __name__ == "__main__":
    test()
