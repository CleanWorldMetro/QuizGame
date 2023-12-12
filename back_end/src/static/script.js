"use strict";

const URL = "http://127.0.0.1:5000/worldmap/locations/";

const METRO = [60.224102435937006, 24.760262698335563];
const MINUTE = 60 * 1000;
// 60.224102435937006, 24.760262698335563

const map = L.map("map", { tap: false });
L.tileLayer("https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", {
  maxZoom: 20,
  subdomains: ["mt0", "mt1", "mt2", "mt3"],
}).addTo(map);
// map.setView([60, 24], 7);
map.setView([METRO[0], METRO[1]], 3);

const getDataFromAPI = async (url) => {
  const response = await fetch(`${url}`); //fetch response from request
  if (!response.ok) throw new Error("Invalid server input!");
  const jsonData = await response.json();
  return jsonData;
};
let cityList = [];

const updateLocalStorage = async (url) => {
  const fetchedData = await getDataFromAPI(url);
  const convertedJsonData = JSON.stringify(fetchedData);
  localStorage.setItem("cityList", convertedJsonData);
  cityList = JSON.parse(localStorage.getItem("cityList"));
  console.log("storage updated");
  console.log(cityList);
  return;
};

const settingUp = async () => {
  try {
    cityList = JSON.parse(localStorage.getItem("cityList"));
    if (
      cityList === null ||
      cityList === undefined ||
      cityList == [] ||
      cityList[0].value === ""
    ) {
      const jsonData = await getDataFromAPI(URL);
      const convertedJsonData = JSON.stringify(jsonData);
      console.log("get data from API");
      localStorage.setItem("cityList", convertedJsonData);
      cityList = JSON.parse(localStorage.getItem("cityList"));
    }
    console.log("updated storage");
    console.log(cityList);
    // return;
    // }
    // const data = await getDataFromAPI(URL);
    // console.log(data);
    // {
    //   "name": "Dammam",
    //   "value": {
    //     "location": "Dammam",
    //     "latitude": 26.4367824,
    //     "longitude": 50.1039991,
    //     "weather": "Clouds",
    //     "weather_description": "broken clouds",
    //     "temperature": 16.06,
    //     "feels_like": 16.18
    //   }
    // }

    //update local storage every minute with new data from API
    // setInterval(() => updateLocalStorage(URL), MINUTE);

    for (let location of cityList) {
      let latitude = location.value.latitude;
      let longitude = location.value.longitude;
      //   // content = "<"
      //   // location.value.latitude
      const marker = L.marker([latitude, longitude]).addTo(map);
      // marker.bindPopup(`<b>${location.name}</b>`).openPopup();
      const popUpContent = document.createElement("div");
      popUpContent.classList = "popup-container";
      const form = document.createElement("form");
      const input = document.createElement("input");
      const button = document.createElement("button");
      form.action = "#";
      form.method = "post";
      input.name = "location_name";
      input.type = "hidden";
      input.value = location.name;
      button.type = "submit";
      button.innerHTML = "Select";

      form.appendChild(input);
      form.appendChild(button);
      popUpContent.appendChild(form);
      marker.bindPopup(popUpContent).openPopup();
    }
    // console.log(`lon: ${location.value.longitute}`);
    return;
  } catch (error) {
    // handle error
    console.log(error.message);
  }
};
// const main = () => {
//   console.log("what we have here");
//   console.log(cityList);
// };

settingUp();
// main();
