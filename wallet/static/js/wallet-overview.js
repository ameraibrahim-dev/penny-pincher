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
        readCategories();
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
        readCategories();
        filterDate();
        filterCategory();
        filterNote();
        computeTotal();
        display();
    }

    function filterDate() {
        let value = $(DATE_RANGE_FIELD_LOCATOR).val();
        start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
        end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));
        transactions = transactions.filter(value => {
            let transact_date = new Date(value.date);
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
    }


}