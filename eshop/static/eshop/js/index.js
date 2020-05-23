const productListContainerElm = document.querySelector(".product-list");

function init() {
  getProductById();
}

function getProductById() {
  fetch("http://localhost:8000/eshop/api/v1/", {
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
      showAllProducts(data);
    })
    .catch(function (ex) {
      console.log("parsing failed", ex);
    });
}

function showAllProducts(data) {
  data.forEach((item) => {
    let clone = document
      .querySelector(".eshop-item-template")
      .content.cloneNode(true);
    let a = clone.querySelector(".product-detail-link");
    a.href = "http://localhost:8000/eshop/product-detail?id=" + item.id;
    clone.querySelector(".title").textContent = item.title;
    clone.querySelector(".description").textContent = item.description;
    clone.querySelector(".price").textContent = item.price;
    productListContainerElm.appendChild(clone);
  });
}

init();
