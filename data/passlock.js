function unlock () {
    var pre_pass = ""
    if (document.cookie.includes("lock")) {
        pre_pass = document.cookie.split(";")[0]
    }
    var password = document.getElementById("password").value
    console.log(pre_pass, password)
    if (password.includes("Tuzicao") || pre_pass.includes("Tuzicao")) {
        document.getElementById("pass-require").style.display = "none"
        document.getElementById("unlock").style.display = ""
        document.cookie = "lock=" + "Tuzicao"
    }
}

document.getElementById("unlock").style.display = "none"
unlock()