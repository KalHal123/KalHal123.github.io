let file;

function handleFiles(files) {
    file = files[0];
    document.querySelector("#drop-area p").textContent = file.name;
}

function uploadImage() {
    const numColors = document.getElementById("numColors").value;
    const formData = new FormData();
    formData.append("image", file);
    formData.append("numColors", numColors);

    fetch("/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        displayColors(data.colors);
    })
    .catch(error => console.error("Error:", error));
}

function displayColors(colors) {
    const colorsDiv = document.getElementById("colors");
    colorsDiv.innerHTML = "";
    colors.forEach(color => {
        const colorBox = document.createElement("div");
        colorBox.className = "color-box";
        colorBox.style.backgroundColor = color.hex;
        colorBox.innerHTML = `
            <p>${color.hex}</p>
            <p>${color.rgb}</p>
        `;
        colorsDiv.appendChild(colorBox);
    });
}
