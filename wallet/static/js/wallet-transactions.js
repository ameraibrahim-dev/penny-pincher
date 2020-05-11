const WALLET_TRANSACTIONS_API_URL = "/api/v1/user/wallet/transactions/list/";
const WALLET_PK = $("#walletID").val();
const TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR = "#total-period-expenses";
const TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR = "#total-period-earnings";

let transactions = [];
let totalPeriodExpenses = 0;
let totalPeriodEarnings = 0;

$(document).ready(function () {
    getALLTransactionsByWalletID();
    generateCategoriesHtml();
    computeTotal();
    // set date range
    if (transactions) {
        $('input[id="DateRangeFilter"]').daterangepicker({
         //   startDate: new Date(transactions[0].date),
           // endDate: new Date(transactions.slice(-1)[0].date),
            endDate: new Date(transactions[0].date),
            startDate: new Date(transactions.slice(-1)[0].date),
        })
    } else {
        $('input[id="DateRangeFilter"]').daterangepicker({})
    }

});

function getALLTransactionsByWalletID() {
    $.ajax({
        dataType: "json",
        url: WALLET_TRANSACTIONS_API_URL,
        data: {'wallet': WALLET_PK},
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
    // display these total number
    $(TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR).text(totalPeriodExpenses);
    $(TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR).text(totalPeriodEarnings);

}

function generateCategoriesHtml() {
    let checkboxes = document.getElementById('checkboxes');
    // get categories
    let categories = new Map();
    transactions.forEach(transact => {
        if (categories.has(transact.category.id) == false) {
            let key = transact.category.id;
            let value = transact.category;
            categories.set(key, value);
        }
    });

    //sort by is_expense
    categories = new Map([...categories.entries()].sort((a, b) => {
            return a[1].is_expense - b[1].is_expense
        }
    ).reverse());
    // generate category options
    //todo display categories
    categories.forEach((value, key) => {
        let label = document.createElement("label");
        let input = document.createElement("input");
        let span = document.createElement("span");

        input.type="checkbox";
        input.id=value.name;

        span.innerHTML=value.name;

        label.htmlFor=value.name;
        label.appendChild(input);
        label.appendChild(span);





        checkboxes.appendChild(label);
    })
}