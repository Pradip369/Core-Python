class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()

root = Node(1025)
l_node = Node(748)
r_node = Node(458)
root.left = l_node
root.right = r_node
root.show()

def sum(a,b):

    """Parse the list of expenses and return the list of triples (date, value, currency).
    Ignore lines starting with #.
    Parse the date using datetime.
    Example expenses_string:
        2016-01-02 -34.01 USD
        2016-01-03 2.59 DKK
        2016-01-03 -2.72 EUR
    """
