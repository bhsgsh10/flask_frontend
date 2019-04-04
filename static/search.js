var searchForFruit = function() {
    var searchedFruits = []
    var searchString = $("#search_str").val()
    for (i = 0; i < fruits.length; i++) {
        //iterate over each field in each fruit
        var fruit = fruits[i]
        var keys = Object.keys(fruit)
        for (j = 0; j < keys.length; j++){
            key = keys[j]
            if (key == "Id") {
                continue;
            } else {
                var value = fruit[key]
                console.log("Value is "+value+" Key is "+key)
                console.log(value.toLowerCase())
                if ((value.toLowerCase()).indexOf(searchString.toLowerCase()) >= 0){
                    console.log("Match!")
                    searchedFruits.push(fruit)
                    break
                } 
            }
            
        }
    }
    console.log(searchedFruits)
    //now create divs using searchedFruits
    showSearchResults(searchedFruits)
}

var showSearchResults = function(searchedFruits) {
    $.each(searchedFruits, function(index, fruit){
        //build the HTML for each of the search results
        console.log(fruit['Id'])
        var container_div = "<div class='container'>"
        var row_div = "<div class='row'>"
        var result_div = "<div class='result'>"
        var info_div1 = "<div class='col-md-12 name'>"+ fruit['Name'] +"</div>"
        var info_div2 = "<div class='col-md-12'>"+ fruit['Description'] +"</div>"
        var link_div = "<div class='col-md-12'><a href='/item/"+fruit['Id']+"' id='know_more'>Know more</a></div>"
        var whole_html = container_div + row_div + result_div + info_div1 + info_div2 + link_div + "</div></div></div>"
        $("#search_bar_btn").append(whole_html)
    })
}

$(document).ready(function() {
    console.log("Ready called")
    $("form.search_bar button").click(function(){
        searchForFruit()
    })

    $("#read_more").click(function(){
        openFruitPage()
    })
})