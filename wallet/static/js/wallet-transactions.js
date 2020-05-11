const WALLET_TRANSACTIONS_API_URL = "/api/v1/user/wallet/transactions/list/";
const WALLET_PK = $("#walletID").val();

let transactions = [];
let totalPeriodExpenses = 0;
let totalPeriodEarnings = 0;

$(document).ready(function () {
    getALLTransactionsByWalletID();
    generateCategoriesHtml();
    computeTotal();
    alert(totalPeriodExpenses);
    alert(totalPeriodEarnings);
});

function getALLTransactionsByWalletID() {
    $.ajax({
        dataType: "json",
        url: WALLET_TRANSACTIONS_API_URL,
        data: {'wallet': WALLET_PK},
        async: false,
        success: function (result) {
            transactions = result;
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
    })
    //todo display these total number

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
    // generate category options
    categories = new Map([...categories.entries()].reverse(a => {
        a.is_expense
    }));
    categories.forEach((value, key) => {
        console.log(value, key);
    })
}