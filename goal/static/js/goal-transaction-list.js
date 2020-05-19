{
    const GOAL_TRANSACTIONS_API_URL = "/api/v1/user/goal/transactions/list/";
    const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
    const SEARCH_FIELD_LOCATOR = "#searchField";
    const GOAL_PK = $("#goaltID").val();
    let transactions = [];

    let options = {
        valueNames: ['name', 'note', 'amount', 'date'],
        page: 10,
        pagination: [{
            name: "pagination",
            paginationClass: "pagination",
            outerWindow: 2,
            innerWindow: 2,
        }],
    };


    function getALLTransactionsByGoalID() {
        $.ajax({
            dataType: "json",
            url: GOAL_TRANSACTIONS_API_URL,
            data: {'goal': GOAL_PK},
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

    $(document).ready(function () {
        getALLTransactionsByGoalID();
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
    let goalTransactionsList = new List('transactions-list', options);
    $(DATE_RANGE_FIELD_LOCATOR).change(function () {
        filterFunction();
    });
    $(SEARCH_FIELD_LOCATOR).keyup(function () {
        let val = $(SEARCH_FIELD_LOCATOR).val();
        if (val.length == '') {
            goalTransactionsList.search();
        } else {
            goalTransactionsList.search($(SEARCH_FIELD_LOCATOR).val(), ['note', 'amount']);
        }
    });

    function filterFunction() {
        let value = $(DATE_RANGE_FIELD_LOCATOR).val();
        start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
        end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));

        goalTransactionsList.filter(function (item) {
            let transact_date = new Date(Date.parse(item.values().date));
            transact_date.setHours(0, 0, 0, 0);
            if (transact_date >= start_date && transact_date <= end_date) {
                return true;
            } else {
                return false;
            }
        });

    }

}


