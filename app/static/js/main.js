$("input#submit").on("click", function (event) {

    $.ajax({
        // données reçu
        data: {
            chooseYourFarm: $("#chooseYourFarm").val(),
            manual: $("#sinon").val()
        },
        type: "POST",
        url: "/process"
    })
        .done(function (data) {})

})

var map = L.map('map').setView([49.443232, 1.099971], 8);
const dataMap = [
    { lon: 49.513703, lat: -1.521295, name: "blabla1" },
    { lon: 48.511333, lat: -0.561925, name: "blabla2" },
    { lon: 49.707181, lat: 1.671823, name: "blabla3" },

]

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var myIcon = L.icon({
    iconUrl: 'my-icon.png',
    iconSize: [38, 95],
    iconAnchor: [22, 94],
    popupAnchor: [-3, -76],
});

for (let index = 0; index < dataMap.length; index++) {
    L.marker([dataMap[index].lon, dataMap[index].lat]).addTo(map).bindPopup(dataMap[index].name)
}
//         });
// });