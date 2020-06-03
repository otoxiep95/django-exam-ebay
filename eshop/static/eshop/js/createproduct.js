const createProductButton = document.querySelector(".create-product-button");

function init() {
  createProductButton.addEventListener("click", createProduct);
}

function createProduct() {
  const form = document.querySelector("form");
  const title = form.querySelector("input[name='title']").value;
  const description = form.querySelector("input[name='description']").value;
  const price = Number(form.querySelector("input[name='price']").value);
  const image = form.querySelector("input[name='product_image']").files[0];
  const seller = form.querySelector("input[name='user_id']").value;
  let formData = new FormData();
  //formData.append("image", image);
  formData.append("title", title);
  formData.append("description", description);
  formData.append("price", price);
  formData.append("seller", seller);
  console.log(image);
  fetch("http://localhost:8000/eshop/api/v1/", {
    method: "POST",
    credentials: "include",
    headers: {
      "X-CSRFToken": csrftoken,
      //"Content-Type": "multipart/form-data",
    },
    body: formData, //JSON.stringify({ title, description, price, seller, image }),
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
