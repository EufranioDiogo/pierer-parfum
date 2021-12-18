const quoters = [
  {
    quoterName: 'Ólivia Diogo',
    quoterImage: '../assets/images/quoters/pexels-andrea-piacquadio-774909.jpg',
    quoterQuote: 'Usar Pierer Parfum foi a melhor escolha que podia ter feito para o meu aroma!'
  },
  {
    quoterName: 'Jonathan Louransse',
    quoterImage: '../assets/images/quoters/pexels-justin-shaifer-1222271.jpg',
    quoterQuote: 'Pierer Parfum sem dúvidas é a melhor, melhor, melhor, marca de perfume que eu escolhi!'
  },
  {
    quoterName: 'Lucas Diogo',
    quoterImage: '../assets/images/quoters/pexels-stefan-stefancik-91227.jpg',
    quoterQuote: 'A primeira vez que utilizei Pierer foi com muita dúvida emando, mas desde a primeira vez Pierer tem sido a minha escolha.'
  },
  {
    quoterName: 'Luana Domingos',
    quoterImage: '../assets/images/quoters/pexels-motional-studio-1081685.jpg',
    quoterQuote: 'Uma perfumária, super, super, super!'
  },
]

const quoterName = document.querySelector('.testimonial-person-name')
const quoterImage = document.querySelector('.testimonial-container--element-img')
const quoterQuote = document.querySelector('.testimonial-person-desc')
let quoterIndex = 0
const quotesControllerList = document.querySelectorAll('.testimonial-container--controller--element')



const startSlide = () => {
  return setInterval(() => {
    if (quoterIndex - 1 < 0) {
      quotesControllerList[quoters.length - 1].classList.remove('testimonial-container--controller--element-active')
    } else {
      quotesControllerList[quoterIndex - 1].classList.remove('testimonial-container--controller--element-active')
    }

    quotesControllerList[quoterIndex].classList.add('testimonial-container--controller--element-active')
    quoterName.textContent = quoters[quoterIndex].quoterName
    quoterImage.src = quoters[quoterIndex].quoterImage
    quoterQuote.textContent = quoters[quoterIndex].quoterQuote

    quoterIndex++
    if (quoterIndex >= quoters.length) {
      quoterIndex = 0
    }
  }, 2000)
}

let slideStart = startSlide()

const changeQuoterIndex = (index) => {
  quotesControllerList[quoterIndex].classList.remove('testimonial-container--controller--element-active')
  
  quoterIndex = index
  quotesControllerList[index].classList.add('testimonial-container--controller--element-active')

  quoterName.textContent = quoters[quoterIndex].quoterName
  quoterImage.src = quoters[quoterIndex].quoterImage
  quoterQuote.textContent = quoters[quoterIndex].quoterQuote

  clearInterval(slideStart)
  slideStart = startSlide()
}



