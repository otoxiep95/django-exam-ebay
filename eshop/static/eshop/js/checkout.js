const orderConfirmationScreen = document.querySelector(
  ".checkout-confirmation"
);
const checkoutAdressScreen = document.querySelector(".checkout-adress");
const checkoutPaymentScreen = document.querySelector(".checkout-payment");
const orderItemsListElm = document.querySelector(".checkout-products-list");
const toOrderListButton = document.querySelector(".to-confirmation-button");
const toAdressButton = document.querySelectorAll(".to-adress-button");
const toPaymentButton = document.querySelectorAll(".to-payment-button");
const finalizeOrder = document.querySelector(".finalize-shop-button");
const shoppingCartId = document.querySelector("input[name='shopping_cart_id']")
  .value;
const userId = document.querySelector("input[name='user_id']").value;
console.log(shoppingCartId);

const idArray = [];
function init() {
  getShoppingOrderProducts();
  toOrderListButton.addEventListener("click", showOrderConfirmationScreen);
  toAdressButton.forEach((elementButton) => {
    elementButton.addEventListener("click", showCheckoutAdressScreen);
  });
  toPaymentButton.forEach((elementButton) => {
    elementButton.addEventListener("click", showcheckoutPaymentScreen);
  });
  finalizeOrder.addEventListener("click", completeShoppingCart);
}

function showOrderConfirmationScreen() {
  orderConfirmationScreen.style.display = "grid";
  checkoutAdressScreen.style.display = "none";
  checkoutPaymentScreen.style.display = "none";
}
function showCheckoutAdressScreen() {
  console.log(checkoutAdressScreen);
  orderConfirmationScreen.style.display = "none";
  checkoutAdressScreen.style.display = "grid";
  checkoutPaymentScreen.style.display = "none";
}
function showcheckoutPaymentScreen() {
  orderConfirmationScreen.style.display = "none";
  checkoutAdressScreen.style.display = "none";
  checkoutPaymentScreen.style.display = "grid";
}

function getShoppingOrderProducts() {
  fetch(
    "http://localhost:8000/eshop/api/v1/order_product?shopping_cart_id=" +
      shoppingCartId,
    {
      credentials: "include",
      headers: {
        "X-CSRFToken": csrftoken,
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    }
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log("Data is ok", data);
      getOrderItemsDetail(data);
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

function getOrderItemsDetail(data) {
  data.forEach((item) => {
    fetch("http://localhost:8000/eshop/api/v1/" + item.product + "/", {
      credentials: "include",
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
        idArray.push(data.id);
        showOrderItem(data);
      })
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  });
}

function showOrderItem(data) {
  let clone = document
    .querySelector(".order-item-template")
    .content.cloneNode(true);
  //   let a = clone.querySelector(".product-detail-link");
  //   a.href = "http://localhost:8000/eshop/product-detail?id=" + item.id;
  clone.querySelector(".title").textContent = data.title;
  clone.querySelector(".description").textContent = data.description;
  clone.querySelector(".price").textContent = data.price;
  orderItemsListElm.appendChild(clone);
}

function completeShoppingCart() {
  fetch(
    "http://localhost:8000/eshop/api/v1/shopping_cart/" + shoppingCartId + "/",
    {
      method: "PATCH",
      credentials: "include",
      headers: {
        "X-CSRFToken": csrftoken,
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ completed: true }), //ordered_date: Date.now()
    }
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log("Data is ok", data);
      deleteProducts();
      createNewShoppingCart();
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

function deleteProducts() {
  idArray.forEach((id) => {
    console.log(id);
    fetch("http://localhost:8000/eshop/api/v1/" + id + "/", {
      method: "PATCH",
      credentials: "include",
      headers: {
        "X-CSRFToken": csrftoken,
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ available: false }),
    })
      .then(function (response) {
        console.log(response);
        return response.json();
      })
      .then(function (data) {})
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  });
}

function createNewShoppingCart() {
  fetch("http://localhost:8000/eshop/api/v1/shopping_cart/", {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": csrftoken,
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ ordered_date: Date.now(), buyer: userId }),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log("Data is ok", data);
      window.location.href = "http://localhost:8000/eshop/";
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

init();
