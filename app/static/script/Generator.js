
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

        // Node Structure

        	nodeStructure : { text: { name: "[123, 16, 875, 541, 54, 45, 8, 48]" } , collapsed: true,children: [{text: { name: "[123, 16, 875, 541]" } , collapsed: true,children: [{text: { name: "[123, 16]" } , collapsed: true,children: [{text: { name: "[123]" } , },{text: { name: "[16]" } , }]},{text: { name: "[875, 541]" } , collapsed: true,children: [{text: { name: "[875]" } , },{text: { name: "[541]" } , }]}]},{text: { name: "[54, 45, 8, 48]" } , collapsed: true,children: [{text: { name: "[54, 45]" } , collapsed: true,children: [{text: { name: "[54]" } , },{text: { name: "[45]" } , }]},{text: { name: "[8, 48]" } , collapsed: true,children: [{text: { name: "[8]" } , },{text: { name: "[48]" } , }]}]}]}};
    
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

        // Node Structure

        	nodeStructure : { text: { name: "[8, 16, 45, 48, 54, 123, 541, 875]" } , collapsed: true,children: [{text: { name: "[16, 123, 541, 875]" } , children: [{text: { name: "[16, 123]" } , children: [{text: { name: "[123]" } , },{text: { name: "[16]" } , }]},{text: { name: "[541, 875]" } , children: [{text: { name: "[875]" } , },{text: { name: "[541]" } , }]}]},{text: { name: "[8, 45, 48, 54]" } , children: [{text: { name: "[45, 54]" } , children: [{text: { name: "[54]" } , },{text: { name: "[45]" } , }]},{text: { name: "[8, 48]" } , children: [{text: { name: "[8]" } , },{text: { name: "[48]" } , }]}]}]}};


    // var tree = new Treant(tree_structure, function() { alert( 'Tree Loaded' ) }, $ );

    var Ntree = new Treant(Ntree_structure, $);
    var Stree = new Treant(Stree_structure, $);


    // Modal
    $("#centralModalSuccess").on('show.bs.modal', function(){
        //alert("Hello World!");
    });                
                

    });
    