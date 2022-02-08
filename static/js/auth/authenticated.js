const API = "http://localhost:5000";
const AUTHENTICITY_END_POINT = `/account/authenticity`;

const accountAuthenticity = () => {
  const token = localStorage.getItem("pierer_parfum_token");
  console.log("okku");
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

      console.log(data);
      if (data.status === "success") {
        renderAuthenticatedComponents();
        changeLoginToLogout();
        alert("Success");
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
  document.querySelector("#login-button").textContent = "Logout";
  document.querySelector("#login-button").addEventListener("click", () => {
    localStorage.removeItem("pierer_parfum_token");
  });
};


const changeLogoutToLogin = () => {
  document.querySelector("#login-button").textContent = "Login";
  document.querySelector("#login-button").addEventListener("click", () => {
  });
};
