const createProductButton = document.querySelector(".create-product-button");

function init() {
  getLoggedUser();
  createProductButton.addEventListener("click", createProduct);
}

function createProduct() {
  const form = document.querySelector("form");
  const title = form.querySelector("input[name='title']").value;
  const description = form.querySelector("input[name='description']").value;
  const price = Number(form.querySelector("input[name='price']").value);
  const seller = form.querySelector("input[name='user_id']").value;
  fetch("http://localhost:8000/eshop/api/v1/", {
    method: "POST",
    credentials: "include",
    headers: {
      "X-CSRFToken": csrftoken,
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title, description, price, seller }),
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
