opacities = {
    "Sonne": 0.0,
    "Schnee": 0.5,
    "Nieselregen": 0.7,
    "Regen": 0.8,
    "Nebel": 1.0
}

for (const i of [1, 2, 3, 4]) {
    $("#slider" + i).slider().on('change', function (event) {
        const qs = new URLSearchParams({
            precipitation: document.getElementById("slider1").value,
            max_temp: document.getElementById("slider2").value,
            min_temp: document.getElementById("slider3").value,
            wind: document.getElementById("slider4").value
        })

        result = fetch(`http://127.0.0.1:5000/`, {
            method: "POST",
            body: qs
        })
        .then((response) => response.json())
        .then(data => {
            document.getElementById("result").innerHTML = data["result"]

            document.getElementById("light").style.opacity = opacities[data["result"]]
        })
    })
}
