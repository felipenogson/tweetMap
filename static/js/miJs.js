// Map Init
var map = L.map('mapid').setView([30, -101], 3);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox/streets-v11',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: 'pk.eyJ1IjoiZmVsaXBvbiIsImEiOiJjazgzeTc3c2IxaWFyM2twYXo1dnh3dXlsIn0.6Nt3yDdsPUkQi9FPycXSxg'
}).addTo(map);
// Map marker classes
var blueIcon = new L.Icon({
  iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});
var greenIcon = new L.Icon({
  iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

// Socket Init
const socket = io();
socket.on('connect', function () {
  socket.emit('my event', {
    data: 'Hola estoy listo'
  });
});

socket.on('tweets', function (tweets) {
  window.tweets = tweets;

  tweets.forEach((tweet, index) => {
    tweets[index] = L.marker([tweet.geometry.coordinates[1], tweet.geometry.coordinates[0]])
      .addTo(map)
      .bindPopup(
        `<a href=${tweet.properties.url} target="New_tab">${tweet.properties.text}</a> <b>${tweet.properties.user}`
        )
  });

});
socket.on('addMarker', tweet => {
  // L.marker([tweet.geometry.coordinates[1],tweet.geometry.coordinates[0]]).addTo(map).bindPopup(`<a href=${tweet.properties.url} target="New_tab">${tweet.properties.text}</a> <b>${tweet.properties.user}` )
  delTweet = tweets.pop();
  map.removeLayer(delTweet);
  tweets.forEach( (t) => t.setIcon(blueIcon))
  tweets.unshift(
    L.marker([tweet.geometry.coordinates[1], tweet.geometry.coordinates[0]])
    .addTo(map).bindPopup(
      `<a href=${tweet.properties.url} target="New_tab">${tweet.properties.text}</a> <b>${tweet.properties.user}`
      )
    .setIcon(greenIcon)
  );

  document.querySelector('#lastTweet').innerHTML =
    `<p>${tweet.properties.text}</p>
              <p><b>${tweet.properties.user}</b></p>
              <p><i>${tweet.properties.created_at}</i></p>`;
});

// News feed generator or receiver
socket.on('addArticle', article => {
 article = JSON.parse(article);
 var articleData = document.querySelector('#articleData');
 articleData.innerHTML = `
                <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                  <h6 class="m-0 font-weight-bold text-primary">News and information</h6>
                </div>
                <img src="${article.thumbnail }" alt="article thumbnail" class="card-img-top rounded p-2" id="article-thumbnail">
                <div class="card-body" id="article">
                  <h5 id="article-title">${article.title}</h5>
                  <a href="${article.url}" id="article-url">${ article.url }</a>
                </div>
                `
});