$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    var character = $("#character").val();
    var strength = $("#strength").val();
    var speed = $("#speed").val();
    var intelligence = $("#intelligence").val();
    var specialAbilities = $("#specialAbilities").val();
    var weaknesses = $("#weaknesses").val();
  
    // check if inputs are valid

    // create the payload
    var payload = {
        "character": character,
        "strength": strength,
        "speed": speed,
        "intelligence": intelligence,
        "specialAbilities": specialAbilities,
        "weaknesses": weaknesses,
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            var prob = parseFloat(returnedData["prediction"]).toFixed(3);

            if (prob > 0.5) {
                $("#output").text(`You might win the battle with a probability of ${prob}!`);
            } else {
                $("#output").text(`You did not win the battle with probability of ${prob}, try getting stronger and try again. :(`);
            }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
