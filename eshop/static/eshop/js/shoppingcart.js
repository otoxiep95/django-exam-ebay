const orderProductsListContainer = document.querySelector(
  ".order-products-list"
);
const shoppingCartId = document.querySelector("input[name='shopping_cart_id']")
  .value;

const checkOutButton = document.querySelector(".check-out-button");

function init() {
  getShoppingOrderProducts();
}

function getShoppingOrderProducts() {
  fetch(
    "http://localhost:8000/eshop/api/v1/order_product?shopping_cart_id=" +
      shoppingCartId,
    {
      credentials: "same-origin",
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
        showOrderItem(data, item.id);
      })
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  });
}

function showOrderItem(data, id) {
  console.log(id);
  let clone = document
    .querySelector(".order-item-template")
    .content.cloneNode(true);
  //   let a = clone.querySelector(".product-detail-link");
  //   a.href = "http://localhost:8000/eshop/product-detail?id=" + item.id;
  clone.querySelector(".title").textContent = data.title;
  clone.querySelector(".description").textContent = data.description;
  clone.querySelector(".price").textContent = data.price;
  const removeButton = clone.querySelector(".remove-btn");
  removeButton.id = id;
  removeButton.addEventListener("click", (e) => {
    console.log(e.target.id);
    removeFromBasket(e.target.id);
  });
  orderProductsListContainer.appendChild(clone);
}

function removeFromBasket(id) {
  fetch("http://localhost:8000/eshop/api/v1/order_product/" + id + "/", {
    method: "DELETE",
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": csrftoken,
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then(function (response) {
      return response;
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

init();
