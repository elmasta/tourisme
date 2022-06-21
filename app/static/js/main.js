$("div#list").hide();
$("div#mapContainer").hide();
$("div#recherche").show();

$("#submit").on("click", function (event) {

    $.ajax({
        // données reçu

        data: {
            chooseYourFarm: $("#chooseYourFarm").val(),
            sinon: $("#sinon").val()
        },
        type: "POST",
        url: "/process"
    })
        .done(function (sinon) {
            if (sinon[0].error === "error") {
                console.log("ici")
            } else {
                $("div#list").show();
                $("div#mapContainer").show();
                $("div#recherche").hide();

                var map = L.map('map').setView([49.443232, 1.099971], 8);
                var dataMap = [];
                for (i in sinon) {

                    // table construction
                    $("tbody").append("<tr><td>" + sinon[i].name +
                        "</td><td>" + sinon[i].cat +
                        "</td><td>" + sinon[i].addr +
                        "</td><td>" + sinon[i].contact +
                        "</td></tr>");

                    // map marker
                    dataMap.push({ lat: sinon[i].lat, lon: sinon[i].lon, name: sinon[i].addr });
                }

                // const dataMap = [
                //     { lon: 49.513703, lat: -1.521295, name: "blabla1" },
                //     { lon: 48.511333, lat: -0.561925, name: "blabla2" },
                //     { lon: 49.707181, lat: 1.671823, name: "blabla3" },
                // ]

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(map);

                // icon personalisé (pas implémenté)
                var myIcon = L.icon({
                    iconUrl: 'my-icon.png',
                    iconSize: [38, 95],
                    iconAnchor: [22, 94],
                    popupAnchor: [-3, -76],
                });

                for (let index = 0; index < dataMap.length; index++) {
                    L.marker([dataMap[index].lat, dataMap[index].lon]).addTo(map).bindPopup(dataMap[0].name)
                }
            }
        })
    event.preventDefault();
});