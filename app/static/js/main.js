$("div#answer").hide();
$("button#restart").hide();
$("p#middlebar").hide();
$("input#adress").focus();

var charUsed = 0;
var int = 0;

$("button#send").on("click", function (event) {

    $.ajax({
        // données reçu
        data: {
            question: $("#question").val()
        },
        type: "POST",
        url: "/process"
    })
        .done(function (data) {
            if (data.error === 1) {
                // gestion erreur
            } else {
                $("p#middlebar").show();
                $("p#result").text(data.summary);
                var map = L.map("mapid").setView([data.lat, data.longi], 15);
                L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
                    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                    maxZoom: 18,
                    id: "mapbox.streets",
                    accessToken: "pk.eyJ1Ijoic3NnbWFzdGVyIiwiYSI6ImNqeGF5dGFpajA2YmgzbnBud253ZmMwYm8ifQ.RFvKLrjywTTEEou9gRHG4A"
                }).addTo(map);
                L.marker([data.lat, data.longi]).addTo(map).bindPopup(data.formatted_adress).openPopup();
                clearInterval(intervalId);
            }
        });
});
event.preventDefault();