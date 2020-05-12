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
    let walletBalanceCurveCtxChart = null;

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

    function isCheckboxChecked() {


        $("input[type='checkbox']").click(function () {
            if (categories.includes($(this).attr('id'))) {

                let index = categories.indexOf($(this).attr('id'));
                categories.splice(index, 1);

            } else {


            }
            //Adds each checked checkbox to array.
            filter();
        });


        return categories;
    }

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
        console.log("before filter:", transactions)
        readCategories();
        filterDate();
        console.log("after filter date:", transactions)
        filterCategory();
        console.log("after filter category:", transactions)
        filterNote();
        console.log("after filter note:", transactions)
        computeTotal();
        console.log("after compute", transactions)
        display();
        console.log(transactions)
    }

    function filterDate() {
        let value = $(DATE_RANGE_FIELD_LOCATOR).val();
        start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
        end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));
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
            console.log(transact.category.is_expense)
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
    }

//charts.js
    function initCharts() {
        savingsExpensesContrastChart = new Chart(savingsExpensesContrastCtx, {
            type: 'doughnut',
            data: {
                labels: ['Savings', 'Expenses',],
                datasets: [{
                    label: '# of Votes',
                    data: [totalPeriodEarnings, totalPeriodExpenses],
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

        walletBalanceCurveCtxChart = new Chart(walletBalanceCurveCtx, {
            type: 'line',
            data: {
                labels: ['March 03,2020', 'March 12,2020', 'March 21,2020', 'March 31,2020'],
                datasets: [{
                    label: "Account Balance in PHP",
                    strokeColor: "#49BEB7",
                    fill: "#49BEB7",
                    borderColor: "#49BEB7",
                    backgroundColor: "#49BEB7",
                    data: [1000, 5000, 30000, 20000]

                }],

            },
            options: lineChartOptions,

        });

    }
}