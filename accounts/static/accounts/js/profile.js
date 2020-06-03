const ownedProductList = document.querySelector(
  ".owned-product-list-container"
);
const ordersList = document.querySelector(".order-list");

const userId = document.querySelector("input[name='user_id']").value;
const userGroup = document.querySelector("input[name='user_group']").value;

function init() {
  getUserPastOrders();
  if (userGroup === "seller") {
    getSellerProducts();
  }
}

function getUserPastOrders() {
  fetch("http://localhost:8000/eshop/api/v1/shopping_cart?user_id=" + userId, {
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

      getShoppingProducts(data);
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

function getShoppingProducts(data) {
  data.forEach((item) => {
    let orderClone = document
      .querySelector(".order-template")
      .content.cloneNode(true);
    orderClone.querySelector(".order-date").textContent = item.ordered_date;
    pastOrderProductList = orderClone.querySelector(".products");
    pastOrderProductList.id = item.id;
    ordersList.appendChild(orderClone);
    fetch(
      "http://localhost:8000/eshop/api/v1/order_product?shopping_cart_id=" +
        item.id,
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
        console.log(item.id);
        console.log("Data is ok", data);
        getOrderItemsDetail(data, item.id);
      })
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  });
}

function getOrderItemsDetail(data, containerId) {
  const productContainer = document.getElementById(containerId);
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
        let clone = document
          .querySelector(".order-item-template")
          .content.cloneNode(true);
        //   let a = clone.querySelector(".product-detail-link");
        //   a.href = "http://localhost:8000/eshop/product-detail?id=" + item.id;
        clone.querySelector(".title").textContent = data.title;
        clone.querySelector(".description").textContent = data.description;
        clone.querySelector(".price").textContent = data.price;
        productContainer.appendChild(clone);
      })
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  });
}

function getSellerProducts() {
  fetch("http://localhost:8000/eshop/api/v1?user_id=" + userId, {
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
      showSellerProducts(data);
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

function showSellerProducts(data) {
  data.forEach((item) => {
    let clone = document
      .querySelector(".product-template")
      .content.cloneNode(true);
    clone.querySelector(".title").textContent = item.title;
    clone.querySelector(".description").textContent = item.description;
    clone.querySelector(".price").textContent = item.price;
    clone.querySelector(".delete-btn").id = item.id;
    clone.querySelector(".delete-btn").addEventListener("click", (e) => {
      deleteProduct(e.target.id);
    });
    ownedProductList.appendChild(clone);
  });
}

function deleteProduct(id) {
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
      return response.json();
    })
    .then(function (data) {})
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

init();
