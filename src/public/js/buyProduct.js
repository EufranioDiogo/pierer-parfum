const buyProduct = (e) => {
  Swal.fire("Compra Efectuada com Sucesso!", "Clique para verificar!", "success");
};

document.querySelector(".buy-button").addEventListener("click", buyProduct);
