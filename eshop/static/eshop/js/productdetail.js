let urlParams = new URLSearchParams(window.location.search);
let id = urlParams.get("id");
console.log(id);
function init() {
  getProductById();
}

function getProductById() {
  fetch("http://localhost:8000/eshop/api/v1/" + id, {
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": csrftoken,
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log("Data is ok", data);
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

init();
