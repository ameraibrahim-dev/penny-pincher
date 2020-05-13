{
    const WALLET_TRANSACTIONS_API_URL = "/api/v1/user/wallet/transactions/list/";
    const WALLET_LIST_API_URL = "/api/v1/user/wallet/list/";
    const NOTE_FIELD_LOCATOR = "#filterByNoteTextField";
    const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
    const TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR = "#total-period-expenses";
    const TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR = "#total-period-earnings";

    let categories = [];
    let transactions = [];
    let totalPeriodExpenses = 0;
    let totalPeriodEarnings = 0;
    let walletList = [];
    let walletBalanceCurveCtx = document.getElementById('walletBalanceCurve').getContext('2d');
    let savingsExpensesContrastCtx = document.getElementById('savingsExpensesContrast').getContext('2d');
    let savingsExpensesContrastChart = null;
    let walletBalanceCurveChart = null;

    $(document).ready(function () {
        getALLTransactions();
        getAllWallets();
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

    function getALLTransactions() {
        $.ajax({
            dataType: "json",
            url: WALLET_TRANSACTIONS_API_URL,
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

    function getAllWallets() {
        $.ajax({
            dataType: "json",
            url: WALLET_LIST_API_URL,
            async: false,
            success: function (result) {
                walletList = eval(result);
            }
        });
    }

    function filter() {
        getALLTransactions();
        getAllWallets();
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
        let displayText = moment(start_date).format("MMM") + " " + start_date.getDate() + " - " + end_date.getDate();
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
                labels: ['Savings', 'Expenses',],
                datasets: [{
                    label: '# of Votes',
                    data: [10, 30],
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
                    label: "Account Balance in PHP",
                    strokeColor: "#49BEB7",
                    fill: "#49BEB7",
                    borderColor: "#49BEB7",
                    backgroundColor: "#49BEB7",
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
        console.log("Wallet List:", walletList);
        console.log("Transactions:", transactions);
        // get date range
        let date_range = getDateRange();
        console.log("Date Range:", date_range);
        getWalletInitialBalance();
        let balance_info = getAccountBalanceInfo(date_range);
        console.log("Balance Info:", balance_info);
        let expense = getExpenses(date_range);
        let earnings = getEarnings(date_range);

    }

    function updateSavingsExpensesContrastChart() {
        savingsExpensesContrastChart.data.datasets[0].data = [totalPeriodEarnings, totalPeriodExpenses];
        savingsExpensesContrastChart.update();
    }

    function getExpenses(date_range = []) {
        let expenses = [];
        date_range.forEach(value => {
            let expense_transacts=transactions.filter(t => {
                t.date=value && t.category.is_expense==true;
            })
            console.log(expense_transacts)
        })

    }

    function getEarnings(date_range = []) {
        let earnings = [];
        date_range.forEach(value => {

        })
    }

    function getAccountBalanceInfo(date_range) {
        // create data
        let accountBalanceInfo = new Map();
        date_range.forEach(value => {
            // get all trasactions on that date
            let transactionOnThatDate = transactions.filter(t => t.date == value);
            transactionOnThatDate.forEach(singleTransact => {
                //find the target wallet
                let wallet = walletList.find(w => w.id == singleTransact.wallet);
                // transact
                if (singleTransact.is_expense) {
                    wallet.initial = wallet.initial - singleTransact.amount.amount;
                } else {
                    wallet.initial += singleTransact.amount.amount;
                }
            });
            accountBalanceInfo.set(value, getTotalInitialFromAllWallet());

        });
        return accountBalanceInfo;
    }

    function getTotalInitialFromAllWallet() {
        let sum = 0;
        walletList.forEach(value => {
            sum += value.initial;
        });
        return sum;
    }

    function getWalletInitialBalance() {
        transactions.forEach(value => {
            let wallet = walletList.find(w => w.id == value.wallet);
            if (wallet.initial == null) {
                wallet.initial = wallet.balance.amount;
            }
            if (value.is_expense) {
                wallet.initial += value.amount.amount;
            } else {
                wallet.initial -= value.amount.amount;
            }
        });
        walletList.forEach(value => {
            if (value.initial == null) {
                value.initial = value.balance.amount;
            }
        })
        console.log(walletList);
    }

    function getDateRange() {
        let date_range = [];
        transactions.forEach(value => {
            if (!date_range.includes(value.date)) {
                date_range.push(value.date)
            }
        });
        walletList.forEach(value => {
            date_range.push(value.created.substring(0, 10));
        });
        date_range.sort((a, b) => new Date(a) - new Date(b));
        return date_range;
    }
}

