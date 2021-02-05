class BinaryNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, childData):
        if self.data:
            # If the new Node is lower then it must go to the left
            if childData < self.data:
                # If there is no left NOde then we create it
                if self.left is None:
                    self.left = BinaryNode(childData)
                # If there is a left Node then we insert a child Node to that Node
                else:
                    self.left.insert(childData)
            # If the data is larger then it must go to the right
            elif childData >= self.data:
                # If the right child node is empty then we create a Node on the right
                if self.right is None:
                    self.right = BinaryNode(childData)
                # If a node on the right exists then we insert a child node for that node
                else:
                    self.right.insert(childData)

    # We form a recursive printTree function
    def printTree(self):
        # If a left node exists then we traverse to the node and re-run the function
        if self.left:
            self.left.printTree()
        print(self.data)
        # After traversing the left we then also traverse the right
        if self.right:
            self.right.printTree()

    # InOrder traversal : Left --> Current --> Right
    def inOrderTraversal(self, currentNode):
        result = []
        if currentNode:
            # Once we are at the current node we then recursively do in order traversal down the left child node
            result = self.inOrderTraversal(currentNode.left)
            # Once we have traversed the left we append the current Node
            result.append(currentNode.data)
            # Now we have the left node and root node traversed
            # Now we have to traverse the right node in the same manner and add this to the result
            result = result + self.inOrderTraversal(currentNode.right)
        return result

    # PreOrder traversal: Current --> left --> right
    def preOrderTraversal(self, currentNode):
        result = []
        if currentNode:
            # When we are at the current node we first add the current node to the traversal
            result.append(currentNode)
            # We then recursively do the same process down the left child branch
            result = result + self.preOrderTraversal(currentNode.left)
            # Once the left branch is done we then traverse the right child in the same format
            result = result + self.preOrderTraversal(currentNode.right)
        return result

    # PostOrder traversal: Left --> Right --> Current
    def postOrderTraversal(self, currentNode):
        result = []
        if currentNode:
            result = self.preOrderTraversal(currentNode.left)
            result = result + self.preOrderTraversal(currentNode.right)
            result.append(currentNode)
        return result


root = BinaryNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inOrderTraversal(root))