const API_BASE_URL = "http://localhost:5000";
const SIGNUP_END_POINT = `/account/verify`;

const loginUser = (accountData) => {
  fetch(API_BASE_URL + SIGNUP_END_POINT, {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Allow-Headers": "*",
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(accountData),
  })
    .then(async (response) => {
      const data = await response.json();

      console.log(data)
      if (data.status == "success") {
        localStorage.setItem(
          "pierer_parfum_token",
          JSON.stringify(data.data.token)
        );

        setTimeout(() => {
          window.location.pathname = "/";
        }, 2500);
      } else {
        Swal.fire("Dados errados!", "Tente mais tarde novamente", "error");
      }
    })
    .catch((error) => {
      Swal.fire("Dados errados!", "Tente mais tarde novamente", "error");
    });
};

document
  .querySelector(".form-container--controller-submit-button")
  .addEventListener("click", (e) => {
    e.preventDefault();

    const form = new FormData(document.querySelector(".form-container"));
    let accountData = {};

    for (let formElement of form) {
      accountData[formElement[0]] = formElement[1];
    }

    loginUser(accountData);
  });
