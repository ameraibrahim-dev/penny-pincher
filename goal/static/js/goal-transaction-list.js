{
    const GOAL_TRANSACTIONS_API_URL = "/api/v1/user/goal/transactions/list/";
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
        console.log(transactions)
        if (transactions) {
            $('input[id="DateRangeFilter"]').daterangepicker({
                endDate: new Date(transactions[0].date),
                startDate: new Date(transactions.slice(-1)[0].date),
            })
        } else {
            $('input[id="DateRangeFilter"]').daterangepicker({})
        }
        let goalList = new List('transactions-list', options);
    });

}


