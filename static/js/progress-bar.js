let elem = document.getElementById("progress-bar");
let width = 1;
let limit = parseInt(document.getElementById("progress-percent").textContent);
let id = setInterval(frame, 10);

function frame() {
    if (width > limit) {
        clearInterval(id);
        i = 0;
    } else {
        width++;
        elem.style.width = width + "%";
    }
}

