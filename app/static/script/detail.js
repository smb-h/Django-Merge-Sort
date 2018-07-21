$(document).ready(function () {
    
    // Tree Config
    var tree_structure = {
        chart: {
            container: "#Tree",
            levelSeparation: 25,
            siblingSeparation: 70,
            subTeeSeparation: 70,
            nodeAlign: "BOTTOM",
            scrollbar: "fancy",
            padding: 35,
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
        nodeStructure : {
            text: { name: "1,3,6,2,4,8,9,5" },
            children: [
                {
                    text: { name: "1,3,6,2" },
                    children: [
                        {
                            text: { name: "1,3" },
                            children: [
                                {
                                    text: { name: "1" }
                                },
                                {
                                    text: { name: "3" }
                                }
                            ]
                        },
                        {
                            text: { name: "6,2" },
                            children: [
                                {
                                    text: { name: "6" }
                                },
                                {
                                    text: { name: "2" }
                                }
                            ]
                        }
                    ]
                },
                {
                    text: { name: "4,8,9,5" },
                    children: [
                        {
                            text: { name: "4,8" },
                            children: [
                                {
                                    text: { name: "4" }
                                },
                                {
                                    text: { name: "8" }
                                }
                            ]
                        },
                        {
                            text: { name: "9,5" },
                            children: [
                                {
                                    text: { name: "9" }
                                },
                                {
                                    text: { name: "5" }
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    };



    // var tree = new Treant(tree_structure, function() { alert( 'Tree Loaded' ) }, $ );
    var tree = new Treant(tree_structure, $);


});