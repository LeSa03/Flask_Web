function validacija(){
    let brojindeksa = document.querySelector("#broj-indeksa").ariaValueMax;

    let regIzraz = /^\d{4}\/\d{6}$/;

    let rezultat = regIzraz.test(brojindeksa);
    if (!rezultat) {
        window.alert("neispravno");
    }

    return rezultat;
}