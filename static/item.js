var fruit = function(item_id) {
    match_index = item_id - 1
    console.log(fruits)
    console.log("item id is" + item_id)
    $.each(fruits, function(index, fr) {
        
        if (index == match_index) {
            var chosen_fruit = fruits[index]

            var name_div = "<div class='col-md-12' id='fruit_name'><h1>"+ chosen_fruit['Name'] +"</h1></div>"
            $("#main_content").append(name_div)
            var image_div = "<div class='col-md-12' id='image_div'><img class='center-block' src="+chosen_fruit['ImageUrl']+" alt='Responsive image' id='main_image'></img></div>"
            $("#main_content").append(image_div)

            var nutritional_information_div = "<div class='col-md-12' id='nutri_info'><h4>Nutritional Information</h4></div>"
            $("#nutritional").append(nutritional_information_div)
            var vitaminA_info_div = "<div class='col-md-12 id='vit_a'><span class='header'>Vitamin A: </span>"+ chosen_fruit['Vitamin_A'] +"</div>"
            $("#nutritional").append(vitaminA_info_div)
            var vitaminC_info_div = "<div class='col-md-12 id='vit_a'><span class='header'>Vitamin C: </span>"+ chosen_fruit['Vitamin_C'] +"</div>"
            $("#nutritional").append(vitaminC_info_div)

            var fruit_description_div = "<div class='col-md-12' id='desc_info'><h4>Fruit description and more information</h4></div>"
            $("#fruit_description").append(fruit_description_div)
            var season_div = "<div class='col-md-12' id='season_div'><span class='header'>Season: </span>"+ chosen_fruit['Season'] +"</div>"
            $("#fruit_description").append(season_div)
            var description = "<div class='col-md-12' id='desc'><span class='header'>More about the fruit: </span>"+ chosen_fruit['Description'] +"</div"
            $("#fruit_description").append(description)

            var price_div = "<div class='col-md-12' id='fruit_price'><h4>Price (per oz): $"+ chosen_fruit['Price_$'] +"</h4></div>"
            $("#price").append(price_div)
        }
        
        // if (fr["id"] === item_id) {
        //     console.log("The world is good")
        // }
        // $.each(value, function(index2, value2){
        //     if (index2 == "id" && value2 == item_id) {
        //         return 0
        //     }
        // })
    })
}

$(document).ready(function() {
    // search for the fruit in fruits whose id is provided
    fruit(item_id)
})