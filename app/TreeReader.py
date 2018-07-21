
# import json
import simplejson as json
import os


DicList = []

def TreeReader():
    assert (os.path.exists('RestJs.json'))

    RestJs = open('RestJs.json', 'r')

    # Pure String Reverse Order
    TreeJs = open('TreeJs.json', 'w')
    for line in reversed(RestJs.readlines()):
        TreeJs.write(line)
    # TreeJs.write(LoadedJson)
    TreeJs.close()
    RestJs.close()


    TREE = open('TreeJs.json', 'r')
    Conf = open('app/static/script/Generator.js', 'w')

    pure = TREE.readlines()
    
    global DicList
    DicList = []
    for part in pure:
        JsPart = part[:-2]
        DicList.append(json.loads(JsPart))

    # Generate Tree Strcture
    Gn = TreeStrcture(DicList)

    Conf.write(Gn)    
    Conf.close()

    TREE.close()




def NodeFinder(NodeVal):
    global DicList
    for node in DicList:
        if (node.get('nodeData') == NodeVal):
            return node


def NodeGenerator(TreeFormat, node):


    def TxtGn(node):
        string = ''
        string += 'text: { name: "'
        string += str(node.get('nodeData'))
        string += '" } '
        string += ', '
        return string

    def ChildGn(node):
        # if node.get('lchild') or node.get('rchild'):
        string = ''
        string += 'collapsed: true,'
        string += 'children: ['

        if node.get('lchild') and node.get('rchild'):

            string += '{'

            Left = NodeFinder(node.get('lchild'))
            Right = NodeFinder(node.get('rchild'))
            

            # ************
            string += TxtGn(Left)

            
            if Left.get('lchild'):
                # string += ChildGn(Left)
                string += ChildGn(Left) + '},{'
            else :
                string += '},{'


            string += TxtGn(Right)
            if Right.get('rchild'):
                string += ChildGn(Right)
            

            string += '}'
                
        else:
            if node.get('lchild'):
                string += '{'
                nd = NodeFinder(node.get('lchild'))
                # *********
                # string += '},{'
                string += TxtGn(nd)
                string += '},'
            elif node.get('rchild'):
                string += '{'
                nd = NodeFinder(node.get('rchild'))
                string += TxtGn(nd)
                # *********
                # string += '},{'
                string += '},'
   


        string += ']'
        # string += ' , '
        # print(string)
        return(string)


    # Root
    txt = TxtGn(node)
    
    TreeFormat += txt
    if node.get('lchild') or node.get('rchild'):
        chld = ChildGn(node)
        TreeFormat += chld
        

    # print(TreeFormat)
    return TreeFormat

def SortedNodeGenerator(TreeFormat, node):


    def TxtGn(node):
        string = ''
        string += 'text: { name: "'
        # Sort Part :D
        node.get('nodeData').sort()
        string += str(node.get('nodeData'))
        string += '" } '
        string += ', '
        return string

    def ChildGn(node):
        # if node.get('lchild') or node.get('rchild'):
        string = ''

        # Collapse South Root Node
        Root = node.get('TreeRoot')
        Root.sort()
        if node.get('nodeData') == Root:
            # print('This iS Root')
            string += 'collapsed: true,'

        string += 'children: ['

        if node.get('lchild') and node.get('rchild'):

            string += '{'

            Left = NodeFinder(node.get('lchild'))
            Right = NodeFinder(node.get('rchild'))
            

            # ************
            string += TxtGn(Left)

            
            if Left.get('lchild'):
                # string += ChildGn(Left)
                string += ChildGn(Left) + '},{'
            else :
                string += '},{'


            string += TxtGn(Right)
            if Right.get('rchild'):
                string += ChildGn(Right)
            

            string += '}'
                
        else:
            if node.get('lchild'):
                string += '{'
                nd = NodeFinder(node.get('lchild'))
                # *********
                # string += '},{'
                string += TxtGn(nd)
                string += '},'
            elif node.get('rchild'):
                string += '{'
                nd = NodeFinder(node.get('rchild'))
                string += TxtGn(nd)
                # *********
                # string += '},{'
                string += '},'
   


        string += ']'
        # string += ' , '
        # print(string)
        return(string)


    # Root
    txt = TxtGn(node)
    
    TreeFormat += txt
    if node.get('lchild') or node.get('rchild'):
        chld = ChildGn(node)
        TreeFormat += chld
        

    # print(TreeFormat)
    return TreeFormat


def TreeStrcture(DicList):

    Root = DicList[0]
    pure = NodeGenerator('', Root)
    Srtd = SortedNodeGenerator('', Root)

    # Set Tree Config
    TreeNorthConfig = '''
    $(document).ready(function () {

        $("#TraceScroll").mCustomScrollbar({
            
			theme:"dark-3",
			axis: "y",
			scrollButtons: {
				enable: true,
			}
            
            
        });



    // NTree Config
    var Ntree_structure = {
        chart: {
            container: "#NTree",
            rootOrientation: 'NORTH',
            levelSeparation: 25,
            siblingSeparation:  70,
            subTeeSeparation:   70,
            nodeAlign: "BOTTOM",
            scrollbar: "fancy",
            padding: 35,
            
            animateOnInit: true,
            animation: {
                nodeAnimation: "easeOutBounce",
                nodeSpeed: 700,
                connectorsAnimation: "bounce",
                connectorsSpeed: 700
            },
            node: { 
                HTMLclass: "evolution-tree",
                collapsable: true,
                 },
            
            connectors: {
                type: "bCurve",
                style: {
                    "stroke-width": 2,
                    "stroke-linecap": "round",
                    "stroke": "#ccc"
                }
            }
        },

        // Node Structure\n
        '''

    TreeNorthConfig += '\tnodeStructure : { ' + pure + '}' + '};'

    TreeSouthConfig = '''
    
    // STree Config
    var Stree_structure = {
        chart: {
            container: "#STree",
            rootOrientation: 'SOUTH',
            levelSeparation: 25,
            siblingSeparation:  70,
            subTeeSeparation:   70,
            nodeAlign: "BOTTOM",
            scrollbar: "fancy",
            padding: 35,
            
            //Start Up Animate
            //animateOnInit: true,
            animation: {
                nodeAnimation: "easeOutBounce",
                nodeSpeed: 700,
                connectorsAnimation: "bounce",
                connectorsSpeed: 700
            },
            node: { 
                HTMLclass: "evolution-tree",
                collapsable: true,
                 },
            
            connectors: {
                type: "bCurve",
                style: {
                    "stroke-width": 2,
                    "stroke-linecap": "round",
                    "stroke": "#ccc"
                }
            }
        },

        // Node Structure\n
        ''' 

    TreeSouthConfig += '\tnodeStructure : { ' + Srtd + '}' + '};'

    TreeObj = '''


    // var tree = new Treant(tree_structure, function() { alert( 'Tree Loaded' ) }, $ );\n
    var Ntree = new Treant(Ntree_structure, $);
    var Stree = new Treant(Stree_structure, $);


    // Modal
    $("#centralModalSuccess").on('show.bs.modal', function(){
        //alert("Hello World!");
    });                
                

    });
    '''

    FullFormat = TreeNorthConfig + TreeSouthConfig + TreeObj

    # print('Done Create Tree Config', DicList[0].get('nodeData'))
    return (FullFormat)