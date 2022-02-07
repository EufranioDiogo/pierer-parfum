const API_BASE_URL = "http://localhost:5000";
const SIGNUP_END_POINT = `/account`;

const signupUser = (accountData) => {
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
      console.log('Res: ', response)

      const data = await response.json();

      console.log('Data: ', data)

      localStorage.setItem('pierer_parfum_token', JSON.stringify(data.data.token))

      Swal.fire(
        "Usuário Criado!",
        "Clique para continuar!",
        "success"
      );
    })
    .catch((error) => {
      Swal.fire(
        "Usuário não criado!",
        "Tente mais tarde novamente",
        "error"
      );
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

    signupUser(accountData);
  });

console.log('dmsimdsi')