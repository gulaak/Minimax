import random
import numpy as np
class Node:
    def __init__(self,data=None,type=None):
        self.data = data
        self.type = type
        self.decision = None
        self.children = []
        self.min = []
        self.max = []

    def __str__(self):
        return f"Data: {self.data}, Type: {self.type}"


class GameTree:
    branchFactor = 3
    depth = 4

    def __init__(self):
        self.root = Node(0,'max')



    def decreaseLevel(self):
        self.level -=1

    def increaseLevel(self):
        self.level += 1
    def constructTree(self):
        self.level = self.depth
        for i in range(0,self.branchFactor):
            self.root.children.append(Node(0,'min'))
            self.decreaseLevel()
            self.construct_Tree(self.root.children[i])
            self.level = self.depth


    def construct_Tree(self,child):
        if(child.type == 'max' and self.level > 2):
            for i in range(0,self.branchFactor):
                child.children.append(Node(0,'min'))
                self.decreaseLevel()
                self.construct_Tree(child.children[i])
            self.increaseLevel()
        elif(child.type =='min' and  self.level > 2):
            for i in range(0,self.branchFactor):
                child.children.append(Node(0,'max'))
                self.decreaseLevel()
                self.construct_Tree(child.children[i])
            self.increaseLevel()
        else:
            for i in range(0,self.branchFactor):
                child.children.append(Node(random.randint(0,50),'utility'))
            self.increaseLevel()
            return

    def max_player(self,node):
        if node.type == 'utility':
            return node.data
        else:
            for i in node.children:
                node.max.append(self.min_player(i))
            node.decision = np.argmax(node.max)
            return max(node.max)

    def min_player(self,node):
        if node.type == 'utility':
            return node.data
        else:
            for i in node.children:
                node.min.append(self.max_player(i))
            node.decision = np.argmin(node.min)
            return min(node.min)

    def mini_max(self):
        if self.root.type == 'max':
            for i in self.root.children:
                self.root.max.append(self.min_player(i))
            self.root.decision = np.argmax(self.root.max)
        else:
            for i in self.root.children:
                self.root.min.append(self.max_player(i))
            self.root.decision= np.argmin(self.root.min)

    def createPath(self):
        print('Decision: %d' %(self.root.decision))
        self.create_Path(self.root.children[self.root.decision])

    def create_Path(self,node):
        while(node.type != 'utility'):
            print('Decision: %d' %(node.decision))
            self.create_Path(node.children[node.decision])
            return
    def bfs(self):
        for child in self.root.children:
            self.bfs_print(child)

    def bfs_print(self,node):
        if node.type =='utility':
            print('Utility: %d' %(node.data))
            return
        for child in node.children:
            self.bfs_print(child)










myTree = GameTree()
myTree.constructTree()

myTree.mini_max()
myTree.createPath()

myTree.bfs() #prints all utility nodes at bottom depth of tree.



