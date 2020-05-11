const WALLET_TRANSACTIONS_API_URL = "/api/v1/user/wallet/transactions/list/";
const WALLET_PK = $("#walletID").val();
const TOTAL_PERIOD_EXPENSES_LOCATOR = "#total-period-expenses";
const TOTAL_PERIOD_EARNINGS_LOCATOR = "#total-period-earnings";

let transactions = [];
let totalPeriodExpenses = 0;
let totalPeriodEarnings = 0;

$(document).ready(function () {
    getALLTransactionsByWalletID();
    generateCategoriesHtml();
    computeTotal();
    $('input[id="DateRangeFilter"]').daterangepicker(

    );
});

function getALLTransactionsByWalletID() {
    $.ajax({
        dataType: "json",
        url: WALLET_TRANSACTIONS_API_URL,
        data: {'wallet': WALLET_PK},
        async: false,
        success: function (result) {
            transactions = result;
            // sort by date
            transactions.sort((a, b) => {
                return new Date(a.date) - new Date(b.date);
            });
        }
    });
}

function computeTotal() {
    totalPeriodExpenses = 0;
    totalPeriodEarnings = 0;

    transactions.forEach(transact => {
        if (transact.category.is_expense) {
            totalPeriodExpenses += transact.amount.amount;
        } else {
            totalPeriodEarnings += transact.amount.amount;
        }
    });
    // display these total number
    $(TOTAL_PERIOD_EXPENSES_LOCATOR).text(totalPeriodExpenses);
    $(TOTAL_PERIOD_EARNINGS_LOCATOR).text(totalPeriodEarnings);

}

function generateCategoriesHtml() {
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
    categories.forEach((value, key) => {
        console.log(value, key);

    })
}