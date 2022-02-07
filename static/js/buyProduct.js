const productId = window.location.toString().split("=")[1];
const API_BASE_URL = "http://localhost:5000";
const PRODUCT_BY_ID = `/products/${productId}`;
const BUY_PRODUCT_END_POINT = `/products/${productId}/buy`;
const productPreviewContainer = document.querySelector(".product-preview");
let productObject = {};

const renderProductInfo = (product) => {
  const previewContainer = document.querySelector(".product-preview");
  productObject = { ...product };

  previewContainer.innerHTML = `
  <div class="product-preview--top-container">
  <div class="top-container--product-container">
    <img src="${product.productPhoto}" class="product-container--image">
    <h2 class="product-container--perfume-name">
      Pierer ${product.productName}
    </h2>
  </div>

  <div class="top-container--controller-panel">
    <button class="buy-button">
      Comprar
    </button>
    <h3 class="product-price">
      ${product.productPrice} AOA
    </h3>
  </div>
</div>

<div class="product-preview--bottom-container">
  <ul class="desc-container--more-perfume-details">
    <li class="more-perfume-details">
      <h4 class="more-perfume-details--label normal-text under-line">Origem</h4>
      <h4 class="more-perfume-details--value normal-text">${
        product.productOrigem
      }</h4>
    </li>

    <li class="more-perfume-details">
      <h4 class="more-perfume-details--label normal-text under-line">Frangância</h4>

      <div class="fragancy-container">
        <div class="fragancy-container--inner-container">
          <div class="fragancy-container--element"></div>
          <div class="fragancy-container--element"></div>
          <div class="fragancy-container--element"></div>
          <div class="fragancy-container--element"></div>
          <div class="fragancy-container--element fragancy-container--element-inactive"></div>
        </div>
        <h4 class="more-perfume-details--value normal-text">Forte</h4>
      </div>
    </li>

    <li class="more-perfume-details">
      <h4 class="more-perfume-details--label normal-text under-line">Familia</h4>
      <h4 class="more-perfume-details--value normal-text">${
        product.productFamily
      }</h4>
    </li>

    <li class="more-perfume-details">
      <h4 class="more-perfume-details--label normal-text under-line">Genêro</h4>
      <h4 class="more-perfume-details--value normal-text">${
        product.productGender === "m" ? "Masculino" : "Femenino"
      }</h4>
    </li>
  </ul>
</div>
  `;

  document.querySelector(".buy-button").addEventListener("click", buyProduct);
};

const getPerfumeData = (productId) => {
  fetch(API_BASE_URL + PRODUCT_BY_ID, {
    method: "GET",
  })
    .then((res) => res.json())
    .then((data) => {
      const [
        id,
        productName,
        productOrigem,
        productFamily,
        productRate,
        productGender,
        productPrice,
        productPhoto,
      ] = data.data.product;

      renderProductInfo({
        id,
        productName,
        productOrigem,
        productFamily,
        productRate,
        productGender,
        productPrice,
        productPhoto,
      });
    })
    .catch((error) => {
      console.log(error);
    });
};

const buyProduct = (e) => {
  const accountId = localStorage.getItem('pierer_parfum_account_id')
  const quant_products = 1


  fetch(API_BASE_URL + BUY_PRODUCT_END_POINT, {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Allow-Headers": "*",
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({
      product_fk: productObject.id,
      account_fk: accountId,
      quant_product: quant_products,
      price_per_product: productObject.productPrice,
      total_price: productObject.productPrice * quant_products,
      date: (new Date()).getUTCDate()
    }),
  })
  .then(async response => {
    const data = await response.json();
    Swal.fire(
      "Compra Efectuada com Sucesso!",
      "Clique para verificar!",
      "success"
    );
  })
  .catch(error => {
    Swal.fire(
      "Compra Não Efectuada com Sucesso!",
      "Tente mais tarde novamente",
      "error"
    );
  })
};

getPerfumeData(productId);
