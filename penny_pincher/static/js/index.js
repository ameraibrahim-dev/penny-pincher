{
    const ALL_TRANSACTIONS_API_URL = "/api/v1/user/wallet/transactions/list/";
    const ALL_USED_CATEGORIES_API_URL = "/api/v1/user/used/categories/";
    const ALL_Wallets_API_URL = "/api/v1/user/wallet/list/";
    const TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR = "#total-period-expenses";
    const TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR = "#total-period-earnings";
    const TOTAL_LOCATOR = "#total";

    let transactions = [];
    let categories = [];
    let wallets = [];
    let totalPeriodExpenses = 0;
    let totalPeriodEarnings = 0;
    let total = 0;


    $(document).ready(function () {

        getALLTransactions();
        getAllWallets();
        generateCategoriesHtml();
        computeTransactionTotal();
        computeTotal();
        // set date range
        if (transactions) {
            $('input[id="DateRangeFilter"]').daterangepicker({
                endDate: new Date(transactions[0].date),
                startDate: new Date(transactions.slice(-1)[0].date),
            })
        } else {
            $('input[id="DateRangeFilter"]').daterangepicker({})
        }

    });

    function getALLTransactions() {
        $.ajax({
            dataType: "json",
            url: ALL_TRANSACTIONS_API_URL,
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

    function getAllWallets() {
        $.ajax({
            dataType: "json",
            url: ALL_Wallets_API_URL,
            async: false,
            success: function (result) {
                wallets = result;
            }
        });
    }

    function computeTransactionTotal() {
        totalPeriodExpenses = 0;
        totalPeriodEarnings = 0;

        transactions.forEach(transact => {
            if (transact.category.is_expense) {
                totalPeriodExpenses -= transact.amount.amount;
            } else {
                totalPeriodEarnings += transact.amount.amount;
            }
        });
        // display these total number
        $(TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR).text(Number(totalPeriodExpenses).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));
        $(TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR).text(Number(totalPeriodEarnings).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));
    }

    function computeTotal() {
        total = 0;
        wallets.forEach(wallet => {
            total += (wallet.balance.amount);
        });
        $(TOTAL_LOCATOR).text(Number(total).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));

    }

    function generateCategoriesHtml() {
        let checkboxes = document.getElementById('checkboxes');
        // get categories
        $.ajax({
            dataType: "json",
            url: ALL_USED_CATEGORIES_API_URL,
            async: false,
            success: function (result) {
                categories = result;
            }
        });

        //sort by is_expense
        categories.sort((a, b) => {
            return a.is_expense - b.is_expense
        }).reverse();

        // generate category options
        //todo display categories
        categories.forEach(value => {
            let label = document.createElement("label");
            let input = document.createElement("input");
            let span = document.createElement("span");

            input.type = "checkbox";
            input.checked = true;
            input.id = value.name;

            span.innerHTML = value.name;

            label.htmlFor = value.name;
            label.className = 'category-select';
            label.appendChild(input);
            label.appendChild(span);


            checkboxes.appendChild(label);
        })
    }
}