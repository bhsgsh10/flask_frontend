var submitItem = function(){
    
    var name = ($("#fruit_name").val() === undefined ? "" : $("#fruit_name").val())
    var season = ($("#season").val() === undefined ? "" : $("#season").val())
    var price = $("#price").val()
    console.log("price is " + price)
    var vitaminA = "Available"
    if ($("vit_a").val() === undefined || $("vit_a").val() === "off") {
        vitaminA = "Not available"
    }
    
    var vitmainC = "Available"
    if ($("#vit_c").val() === undefined || $("#vit_c").val() === "off") {
        vitmainC = "Not available"
    }
    var imageUrl = ($("#image_url").val() === undefined ? "" : $("#image_url").val())
    var description = ($("#fruit_description").val() === undefined ? "" : $("#fruit_description").val())

    if (name == "") {
        alert("Name cannot be empty")
        $("#fruit_name").val("")
        $("#fruit_name").focus()
    } else if (season == "") {
        alert("Season cannot be empty")
        $("#season").val("")
        $("#season").focus()
    } else if (price == "") {
        alert("Price cannot be empty or non-numeric")
        $("#price").val("")
        $("#price").focus()
    } else if (imageUrl == "") {
        alert("Image URL cannot be empty")
        $("#image_url").val("")
        $("#image_url").focus()
    } else if (description == "") {
        alert("Description cannot be empty")
        $("#fruit_description").val("")
        $("#fruit_description").focus()
    } else if (!$.isNumeric(price)) {
        alert("Price has to be a number")
        $("#price").val("")
        $("#price").focus()
    } else {
        var newItem = {
            "Name": name,
            "Season": season,
            "Price_$": price.toString(),
            "Vitamin_A": vitaminA,
            "Vitamin_C": vitmainC,
            "ImageUrl": imageUrl,
            "Description": description
        }
        $.ajax({
            type: "POST",
            url: "save_item",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(newItem),
            success: function(result){
                var item_id = result["new_id"]
                if (window.confirm("The fruit has been added successfully. Do you want to view the item?")) { 
                    //load_item(fruit_id)
                    url = "http://localhost:5000/item/" + item_id
                    window.open(url, "Thanks for Visiting!");
                }
            },
            error: function(request, status, error){
                alert("Failed to add fruit. Try again")
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        })

        
    }

}

var load_item = function(item_id) {
    $.ajax({
        type: "POST",
        url: "/item/"+item_id,
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(item_id),
        success: function(result) {

        }
    })
}


$(document).ready(function() {
    console.log("Hello World")
    $("#submit_item").click(function(){
        submitItem()
    })
})