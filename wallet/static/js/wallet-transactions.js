const WALLET_TRANSACTIONS_API_URL = "/api/v1/user/wallet/transactions/list/";
const WALLET_PK = $("#walletID").val();
let transactions = null;


$(document).ready(function () {
    getALLTransactionsByWalletID();
    generateCategoriesHtml();
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

function generateCategoriesHtml() {
    // get categories
    let categories = new Map();
    transactions.forEach(function (transact) {
        if (categories.has(transact.category.id) == false) {
            let key = transact.category.id;
            let value = transact.category;
            categories.set(key, value);
        }
    });
    // generate category options
    categories = new Map([...categories.entries()].reverse(a => {a.is_expense}));
    categories.forEach((value, key) => {
        console.log(value, key);
    })


}