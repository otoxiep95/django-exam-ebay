let urlParams = new URLSearchParams(window.location.search);
let id = urlParams.get("id");

const productTitleElm = document.querySelector(".title");
const productDescriptionElm = document.querySelector(".description");
const productPriceElm = document.querySelector(".price");
// const productId = document.querySelector("input['product_id']").value;
const shoppingCartId = document.querySelector("input[name='shopping_cart_id']")
  .value;
const buyProductButton = document.querySelector(".buy-product-button");

buyProductButton.addEventListener("click", createOrderItem);

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
      showProductDetails(data);
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

function showProductDetails(data) {
  productTitleElm.textContent = data.title;
  productDescriptionElm.textContent = data.description;
  productPriceElm.textContent = data.price;
}

function createOrderItem() {
  console.log(id, shoppingCartId);
  fetch("http://localhost:8000/eshop/api/v1/order_product/", {
    method: "POST",
    credentials: "include",
    headers: {
      "X-CSRFToken": csrftoken,
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ product: id, shopping_cart: shoppingCartId }),
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
