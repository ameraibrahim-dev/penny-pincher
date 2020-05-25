{
    const GOAL_TRANSACTIONS_API_URL = "/api/v1/user/goal/transactions/list/";
    const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
    const SEARCH_FIELD_LOCATOR = "#searchField";
    const GOAL_PK = $("#goalID").val();
    let transactions = [];

    let options = {
        valueNames: ['name', 'note', 'amount', 'date'],
        page: 10,
        pagination: [{
            name: "pagination",
            paginationClass: "pagination",
            outerWindow: 2,
            innerWindow: 2,
        }],
    };
    var expenseEarningsChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Earnings', 'Expenses'],
            datasets: [{
                label: '# of Votes',
                data: [0, 0],
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
    });

    function getALLTransactionsByGoalID() {
        $.ajax({
            dataType: "json",
            url: GOAL_TRANSACTIONS_API_URL,
            data: {'goal': GOAL_PK},
            async: false,
            success: function (result) {
                transactions = result;
                // sort by date from most recent
                transactions.sort((a, b) => {
                    return new Date(a.date) - new Date(b.date);
                }).reverse();
            }
        });
    }

    $(document).ready(function () {
        getALLTransactionsByGoalID();
// set date range
        if (transactions.length>0) {
            $('input[id="DateRangeFilter"]').daterangepicker({
                endDate: new Date(transactions[0].date),
                startDate: new Date(transactions.slice(-1)[0].date),
            })
        } else {
            $('input[id="DateRangeFilter"]').daterangepicker({})
        }
        filterFunction();
        //event listener
        $(DATE_RANGE_FIELD_LOCATOR).change(function () {
            filterFunction();
        });
        $(SEARCH_FIELD_LOCATOR).keyup(function () {
            let val = $(SEARCH_FIELD_LOCATOR).val();
            if (val.length == '') {
                goalTransactionsList.search();
            } else {
                goalTransactionsList.search($(SEARCH_FIELD_LOCATOR).val(), ['note', 'amount', 'name', 'date']);
            }
            filterFunction();
        });
    });
    let goalTransactionsList = new List('transactions-list', options);

    function filterFunction() {
        let value = $(DATE_RANGE_FIELD_LOCATOR).val();
        start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
        end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));

        goalTransactionsList.filter(function (item) {
            let transact_date = new Date(Date.parse(item.values().date));
            transact_date.setHours(0, 0, 0, 0);
            if (transact_date >= start_date && transact_date <= end_date) {
                return true;
            } else {
                return false;
            }
        });
        expenseEarningsChart.data.datasets[0].data = [getSum(false), getSum(true)];
        expenseEarningsChart.update();

    }

    function getSum(isExpense) {
        let items = goalTransactionsList.visibleItems;
        let sum = 0;
        let value = null;
        let value_isExpense = false;
        items.forEach(value => {
            value = value.values();
            if (value.name == "Earning") {
                value_isExpense = false;
            } else {
                value_isExpense = true;
            }
            if (isExpense == value_isExpense) {
                sum += parseFloat(value.amount.replace(",", ""));
            }
        });
        return sum;

    }


}


