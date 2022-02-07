const API_BASE_URL = "http://localhost:5000";
const QUOTERS_ENDPOINT = "/quoters";
let quoters = [];

const getQuotes = () => {
  console.log("Entrou");
  fetch("http://127.0.0.1:5000/quoters", {
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
      const extractedQuoters = data?.data?.quoters?.map((quoter) => {
        const [id, quoterName, quoterQuote, quoterImage] = quoter;
        return { id, quoterName, quoterQuote, quoterImage };
      });

      quoters = extractedQuoters;
    })
    .catch((err) => {
      console.log(err);
    });
};

const quoterName = document.querySelector(".testimonial-person-name");
const quoterImage = document.querySelector(
  ".testimonial-container--element-img"
);
const quoterQuote = document.querySelector(".testimonial-person-desc");
let quoterIndex = 0;
const quotesControllerList = document.querySelectorAll(
  ".testimonial-container--controller--element"
);

const startSlide = () => {
  return setInterval(() => {
    if (quoterIndex - 1 < 0) {
      quotesControllerList[quoters.length - 1].classList.remove(
        "testimonial-container--controller--element-active"
      );
    } else {
      quotesControllerList[quoterIndex - 1].classList.remove(
        "testimonial-container--controller--element-active"
      );
    }

    quotesControllerList[quoterIndex].classList.add(
      "testimonial-container--controller--element-active"
    );
    quoterName.textContent = quoters[quoterIndex].quoterName;
    console.log("Image: ", quoters[quoterIndex].quoterImage);
    quoterImage.src =
      quoters[quoterIndex].quoterImage ||
      "../assets/images/quoters/pexels-andrea-piacquadio-774909.jpg";
    quoterQuote.textContent = quoters[quoterIndex].quoterQuote;

    quoterIndex++;
    if (quoterIndex >= quoters.length) {
      quoterIndex = 0;
    }
  }, 5000);
};

let slideStart = startSlide();

const changeQuoterIndex = (index) => {
  quotesControllerList[quoterIndex].classList.remove(
    "testimonial-container--controller--element-active"
  );

  quoterIndex = index;
  quotesControllerList[index].classList.add(
    "testimonial-container--controller--element-active"
  );

  quoterName.textContent = quoters[quoterIndex].quoterName;
  quoterImage.src = quoters[quoterIndex].quoterImage;
  quoterQuote.textContent = quoters[quoterIndex].quoterQuote;

  clearInterval(slideStart);
  slideStart = startSlide();
};

getQuotes();
