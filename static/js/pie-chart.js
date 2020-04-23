var ctx = document.getElementById('homePieChart');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Savings', 'Expenses'],
        datasets: [{
            label: '# of Votes',
            data: [30000, 12000],
            backgroundColor: [
                '#49BEB7',
                '#EE8572',
                
            ],
            borderColor: [
                '#49BEB7',
                '#EE8572',
                
            ],
            borderWidth: 0
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                display:false,
                gridLines: {
                    color: "rgba(0, 0, 0, 0)",
                },
                ticks: {
                    display: false //this will remove only the label
                }
            }],
            yAxes: [{
                display:false,
                gridLines: {
                    color: "rgba(0, 0, 0, 0)",
                },
                ticks: {
                    display: false //this will remove only the label
                }
            }]
        }
    }
});