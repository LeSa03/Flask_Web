// validiranje input polja za br indeksa

function validacija() {
  let brIndeksa = document.querySelector("#broj-indeksa").value;

  let regIzraz = /^\d{4}\/\d{6}$/;

  let rezultat = regIzraz.test(brIndeksa);
  if (!rezultat) {
    alert("Neispravno unet broj indeksa!");
  }
  return rezultat;
}
