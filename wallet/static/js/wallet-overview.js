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
    $(document).ready(function () {
        getALLTransactionsByWalletID();
        getWalletInfoWalletID();
        console.log(transactions)
        console.log(walletInfo)
    });
    $(NOTE_FIELD_LOCATOR).keyup(function () {

    });
    $(DATE_RANGE_FIELD_LOCATOR).change(function () {

    });

    function isCheckboxChecked() {


        $("input[type='checkbox']").click(function () {
            if (categories.includes($(this).attr('id'))) {

                let index = categories.indexOf($(this).attr('id'));
                categories.splice(index, 1);

            } else {


            }
            //Adds each checked checkbox to array.
            readCategories();
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


}