const API = "http://localhost:5000";
const AUTHENTICITY_END_POINT = `/account/authenticity`;

const accountAuthenticity = () => {
  const token = localStorage.getItem("pierer_parfum_token");

  fetch(API + AUTHENTICITY_END_POINT, {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Allow-Headers": "*",
      "Content-Type": "application/json",
      Authorization: token,
    },
    method: "POST",
  })
    .then(async (response) => {
      const data = await response.json();

      if (data.status === "success") {
        renderAuthenticatedComponents();
        changeLoginToLogout();
      } else {
        changeLogoutToLogin();
      }
    })
    .catch((error) => {
      console.log(error);
    });
};

accountAuthenticity();

const renderAuthenticatedComponents = () => {};
const changeLoginToLogout = () => {
  console.log('Txe meu nengue')
  document.querySelector("#login-button").textContent = "Logout";

  document.querySelector("#buy-orders-button").style = "display: inline-block";
  document.querySelector("#login-button").addEventListener("click", () => {
    localStorage.removeItem("pierer_parfum_token");
  });
};

const changeLogoutToLogin = () => {
  document.querySelector("#login-button").textContent = "Login";
  document.querySelector("#buy-orders-button-item").style = "display: none";

  document.querySelector("#login-button").addEventListener("click", () => {});
};
