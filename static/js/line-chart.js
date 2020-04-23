var ctx = document.getElementById('homeLineChart');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        
        labels: ['March 03,2020', 'March 12,2020', 'March 21,2020', 'March 31,2020'],
        datasets: [{
            label: "Account Balance in PHP",
            strokeColor: "#49BEB7",
            fill:"#49BEB7",
            borderColor:"#49BEB7",
            backgroundColor:"#49BEB7",
            data: [1000, 5000, 30000,20000]

        }],
        
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            xAxes: [{
                gridLines: {
                    color: "rgba(0, 0, 0, 0)",
                },
                
                
            }],
            yAxes: [{
                
                
            }]
        },

        tooltips: {
            callbacks: {
              label: function(tooltipItem, data) {
                //get the concerned dataset
                var dataset = data.datasets[tooltipItem.datasetIndex];
                //calculate the total of this data set
                var total = dataset.data.reduce(function(previousValue, currentValue, currentIndex, array) {
                  return previousValue + currentValue;
                });
                //get the current items value
                var currentValue = dataset.data[tooltipItem.index];
                //calculate the precentage based on the total and current item, also this does a rough rounding to give a whole number
                var percentage = Math.floor(((currentValue/total) * 100)+0.5);
          
                return percentage + "%";
              }
            }
          } 
    }

    
});