const API_BASE_URL = "http://localhost:5000";
const MEN_PERFUMES_ENDPOINT = "/products/male";
const perfumesContainer = document.querySelector("#perfume-container");

const getMenPerfumes = () => {
  console.log("Entrou");
  fetch(API_BASE_URL + MEN_PERFUMES_ENDPOINT, {
    method: "GET",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Allow-Headers": "*",
      "Content-Type": "application/json",
    },
  })
    .then((res) => res.json())
    .then((data) => {
      data?.data?.products?.map(async (perfume) => {
        const [
          id,
          productName,
          productProvinience,
          productFamily,
          productFraganceRate,
          productGender,
          productPhoto,
        ] = perfume;

        console.log(
          "Provinience: ",
          productProvinience,
          "Family: ",
          productFamily
        );
        renderPerfumeItem({
          id,
          productName,
          productProvinience,
          productFamily,
          productFraganceRate,
          productGender,
          productPhoto,
        });
      });

      console.log("Perfumes: ", data);
    })
    .catch((err) => {
      console.log(err);
    });
};

const renderPerfumeItem = (perfume) => {
  const div = `
  <div class="row-2--perfume-container">
        <div class="perfume-container--img-container">
          <img src="${
            perfume.productPhoto === null
              ? "../../assets/images/perfumes/kailey-sniffin-UPjXnyeGXuA-unsplash.jpg"
              : perfume.productPhoto
          }" 
          alt=""
            class="perfume-container--img-container--img">
        </div>
        <div class="perfume-container--desc-container">
          <h3 class="desc-container--perfume-name heading-3">Pierer <span class="main-color">${
            perfume.productName
          }</span></h3>

          <ul class="desc-container--more-perfume-details">
            <li class="more-perfume-details">
              <h4 class="more-perfume-details--label normal-text under-line">Origem</h4>
              <h4 class="more-perfume-details--value normal-text">${
                perfume.productProvinience
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
          </ul>

          <a href="#" class="btn-see-more-about-perfume heading-2">
            Ver mais
          </a>
        </div>
      </div>
  `;

  perfumesContainer.innerHTML += div;
};

getMenPerfumes();
