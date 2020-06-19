# https://www.youtube.com/watch?v=AHhAL001ScQ

from enum import Enum


class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Variable:
    def __init__(self, name):
        self.name = name
        self.domain = [Colors.RED, Colors.GREEN, Colors.BLUE]
        self.edges = []


WA = Variable("Western Australia")
NT = Variable("Northern Territories")
SA = Variable("South Australia")
Q = Variable("Queensland")
NSW = Variable("New South Wales")
V = Variable("Victoria")
T = Variable("Tasmania")

WA.edges = [NT, SA]
NT.edges = [WA, SA, Q]
SA.edges = [WA, NT, Q, NSW, V]
Q.edges = [NT, SA, NSW]
NSW.edges = [Q, SA, V]
V.edges = [SA, NSW, T]
T.edges = [V]


def domain_wipeout(color, node):
    for n in node.edges:
        try:
            n.domain.remove(color)
        except:
            pass


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


# Starting point is SA
search_tree = [SA, WA, NT, Q, NSW, V, T]
# Select starting color
c = Colors.RED
for node in search_tree:
    # print(node.name, node.domain)
    c = node.domain[0]
    # Eliminate color from edges
    domain_wipeout(c, node)
    # Remove other colors from current node for this branch
    for _c in node.domain:
        if _c != c:
            node.domain = remove_values_from_list(node.domain, _c)
    print(node.name, " -> ", node.domain[0])


# print(SA.name, SA.domain)
# print(WA.name, WA.domain)
# print(NT.name, NT.domain)
# print(Q.name, Q.domain)
# print(NSW.name, NSW.domain)
# print(V.name, V.domain)
# print(T.name, T.domain)
