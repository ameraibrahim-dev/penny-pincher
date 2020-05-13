
$(document).ready(function () {

    getDateToday();


});

function getDateToday(){
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"
    ];
    let today = new Date();
    let date = monthNames[today.getMonth()]+" "+today.getFullYear();
    let targetNode = document.getElementById('start-date');

    targetNode.innerText = date;

}