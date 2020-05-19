var ctx = document.getElementById('homePieChart');
let pieOptions= {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    display: false,
                    gridLines: {
                        color: "rgba(0, 0, 0, 0)",
                    },
                    ticks: {
                        display: false //this will remove only the label
                    }
                }],
                yAxes: [{
                    display: false,
                    gridLines: {
                        color: "rgba(0, 0, 0, 0)",
                    },
                    ticks: {
                        display: false //this will remove only the label
                    }
                }]
            }
        }
;