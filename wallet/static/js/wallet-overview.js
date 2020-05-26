{
    const WALLET_TRANSACTIONS_API_URL = "/api/v1/user/wallet/transactions/list/";
    const WALLET_LIST_API_URL = "/api/v1/user/wallet/list/";
    const NOTE_FIELD_LOCATOR = "#filterByNoteTextField";
    const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
    const TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR = "#total-period-expenses";
    const TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR = "#total-period-earnings";

    const WALLET_PK = $("#walletID").val();
    let categories = [];
    let transactions = [];
    let totalPeriodExpenses = 0;
    let totalPeriodEarnings = 0;
    let walletInfo = null;
    let walletBalanceCurveCtx = document.getElementById('walletBalanceCurve').getContext('2d');
    let savingsExpensesContrastCtx = document.getElementById('savingsExpensesContrast').getContext('2d');
    let savingsExpensesContrastChart = null;
    let walletBalanceCurveChart = null;

    $(document).ready(function () {
        getALLTransactionsByWalletID();
        getWalletInfoWalletID();
        readCategories();
        computeTotal();
        initCharts();
    });
    $(NOTE_FIELD_LOCATOR).keyup(function () {
        filter();
    });
    $(DATE_RANGE_FIELD_LOCATOR).change(function () {
        filter();
    });

    $(document).on("click", "input[type='checkbox']", function () {
        if (categories.includes($(this).attr('id'))) {

            let index = categories.indexOf($(this).attr('id'));
            categories.splice(index, 1);

        }
        filter();
    });

    function readCategories() {
        $.each($("input[type='checkbox']:checked"), function () {
            if (categories.includes($(this).attr('id'))) {

            } else {
                if ($(this).attr('id') == undefined) {

                } else {
                    categories.push($(this).attr('id'));
                }
            }


        });
    }

    function getALLTransactionsByWalletID() {
        $.ajax({
            dataType: "json",
            url: WALLET_TRANSACTIONS_API_URL,
            data: {'wallet': WALLET_PK},
            async: false,
            success: function (result) {
                transactions = eval(result);
                // sort by date from most recent
                transactions.sort((a, b) => {
                    return new Date(a.date) - new Date(b.date);
                }).reverse();
            }
        });
    }

    function getWalletInfoWalletID() {
        $.ajax({
            dataType: "json",
            url: WALLET_LIST_API_URL,
            data: {'id': WALLET_PK},
            async: false,
            success: function (result) {
                walletInfo = eval(result)[0];
            }
        });
    }

    function filter() {
        getALLTransactionsByWalletID();
        readCategories();
        filterDate();
        filterCategory();
        filterNote();
        computeTotal();
        display();
    }

    function filterDate() {
        let value = $(DATE_RANGE_FIELD_LOCATOR).val();
        let start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
        let end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));
        //display filter range
        let displayText = moment(start_date).format("MMM") + " " + start_date.getDate() + " - " + moment(end_date).format("MMM") + " " + end_date.getDate();
        $(".chart-date-range").text(displayText);
        //filter
        transactions = transactions.filter(value => {
            let transact_date = new Date(value.date);
            transact_date.setHours(0, 0, 0, 0)
            return (transact_date >= start_date && transact_date <= end_date);
        });
    }

    function filterCategory() {
        transactions = transactions.filter(value => {
            return categories.includes(value.category.name)
        });
    }

    function filterNote() {
        let val = $(NOTE_FIELD_LOCATOR).val();
        if (val.trim() != '') {
            transactions = transactions.filter(value => {
                return value.note.toUpperCase() === val.toUpperCase();
            });
        }

    }

    function computeTotal() {
        totalPeriodExpenses = 0;
        totalPeriodEarnings = 0;

        transactions.forEach(transact => {
            if (transact.category.is_expense) {
                totalPeriodExpenses -= transact.amount.amount;
            } else {
                totalPeriodEarnings += transact.amount.amount;
            }
        });
    }

    function display() {
        // display these total number
        $(TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR).text(Number(totalPeriodExpenses).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));
        $(TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR).text(Number(totalPeriodEarnings).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));
        updateSavingsExpensesContrastChart();
        updateWalletBalanceCurveCtxChart();
    }

//charts.js
    function initCharts() {
        savingsExpensesContrastChart = new Chart(savingsExpensesContrastCtx, {
            type: 'doughnut',
            data: {
                labels: ['Earnings', 'Expenses',],
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
            options: pieOptions,
        });


        walletBalanceCurveChart = new Chart(walletBalanceCurveCtx, {
            type: 'line',
            data: {
                datasets: [{
                    label: "Account Balance",
                    strokeColor: "#0fbe09",
                    fill: "#0fbe09",
                    borderColor: "#0fbe09",
                    backgroundColor: "#0fbe09",
                    data: [32, 22],

                }],
                labels: ['label1', 'label2']
            },
            options: lineChartOptions,

        });
        updateWalletBalanceCurveCtxChart();
        updateSavingsExpensesContrastChart();
    }

    function updateWalletBalanceCurveCtxChart() {
        let accountBalanceInfo = new Map();
        let expenses = new Map();
        let earnings = new Map();
        let walletBalance = walletInfo.balance.amount;
        // reverse transactions to get original balance
        transactions.forEach(value => {
            if (value.is_expense) {
                walletBalance += value.amount.amount;
            } else {
                walletBalance -= value.amount.amount;
            }
        });
        //add created date,balance at that time
        let created_date = new Date(walletInfo.created).toISOString().substring(0, 10);
        accountBalanceInfo.set(created_date, walletBalance);

//create data
        transactions.reverse().forEach(value => {
            if (value.is_expense) {
                walletBalance -= value.amount.amount;
                if (expenses.has(value.date)) {
                    expenses.set(value.date, expenses.get(value.date) + value.amount.amount);
                } else {
                    expenses.set(value.date, value.amount.amount);
                }

            } else {
                walletBalance += value.amount.amount;
                if (earnings.has(value.date)) {
                    earnings.set(value.date, earnings.get(value.date) + value.amount.amount);
                } else {
                    earnings.set(value.date, value.amount.amount);
                }
            }
            accountBalanceInfo.set(value.date, walletBalance)
        });
        //generate values for all the labels
        let earnings_data = [];
        let expense_data = [];
        let labels = [...accountBalanceInfo.keys()];
        labels.forEach(value => {
            if (earnings.has(value)) {
                earnings_data.push(earnings.get(value))
            } else {
                earnings_data.push(0);
            }
            if (expenses.has(value)) {
                expense_data.push(expenses.get(value))
            } else {
                expense_data.push(0);
            }
        });
        //set data,labels and update
        walletBalanceCurveChart.data.datasets[0].data = [...accountBalanceInfo.values()];
        walletBalanceCurveChart.data.datasets[1] = {
            label: "Expenses",
            strokeColor: "#EE8572",
            fill: "#EE8572",
            borderColor: "#EE8572",
            backgroundColor: "#EE8572",
            data: expense_data,

        };
        walletBalanceCurveChart.data.datasets[2] = {
            label: "Earnings",
            strokeColor: "#49BEB7",
            fill: "#49BEB7",
            borderColor: "#49BEB7",
            backgroundColor: "#49BEB7",
            data: earnings_data,

        };
        walletBalanceCurveChart.data.labels = labels;
        walletBalanceCurveChart.update();
    }

    function updateSavingsExpensesContrastChart() {
        savingsExpensesContrastChart.data.datasets[0].data = [totalPeriodEarnings, totalPeriodExpenses];
        savingsExpensesContrastChart.update();
    }
}