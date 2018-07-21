from .models import Node, Tree

# import json
import simplejson as json



def NodeGenerator(tree, DH, parent):
    
    RestJs = open('RestJs.json', 'a+')
    

    # Node.nodeData = DH
    NodeData = DH

    LChild = []
    RChild = []

    # Set Parent
    if DH is parent:
        NodeParent = None
    else :
        NodeParent = parent
    
    if len(DH) <= 1:
        LChild = None
        RChild = None
    else :
        middle = int(len(DH) / 2)
        LChild = DH[:middle]
        RChild = DH[middle:]

    # Save for process tree
    # JsonStr = json.dumps({
        #     'TreeRoot': tree.root, 
        #     'parent': NodeParent, 
        #     'nodeData': NodeData, 
        #     'lchild': LChild, 
        #     'rchild': RChild,
        # }, indent=4,
        # )
    JsonStr = json.JSONEncoder().encode({
            'TreeRoot': tree.root, 
            'parent': NodeParent, 
            'nodeData': NodeData, 
            'lchild': LChild, 
            'rchild': RChild,
        }
        )
        
    RestJs.write(JsonStr + ',\n')

    # Save for API
    node = Node.objects.create(
        TreeRoot = tree,
        parent = NodeParent,
        nodeData = NodeData,
        # children = children,
        lchild = LChild,
        rchild = RChild,
    )
    # End Condition
    if len(DH) <= 1:
        return
    # Manipulating DH for next state
    mid = int(len(DH) / 2)
    LeftDH = DH[:mid]
    RightDH = DH[mid:]
    NodeParent = DH
    NodeGenerator(tree, LeftDH, NodeParent)
    NodeGenerator(tree, RightDH, NodeParent)


    RestJs.close()

