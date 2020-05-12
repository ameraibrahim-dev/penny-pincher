const NOTE_FIELD_LOCATOR = "#filterByNoteTextField";
const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
let categories = [];
let options = {
    valueNames: ['name', 'note', 'amount', 'date', {name: 'isExpense', attr: 'value'}],
    page: 10,
    pagination: [{
        name: "pagination",
        paginationClass: "pagination",
        outerWindow: 2,
        innerWindow: 2,

    }],
};

let transaction_list = new List('transactions-list', options);
$(NOTE_FIELD_LOCATOR).keyup(function () {
    let val = $(NOTE_FIELD_LOCATOR).val();
    if (val.length == '') {
        transaction_list.search();
    } else {
        transaction_list.search($(NOTE_FIELD_LOCATOR).val(), ['note']);
    }
    //update total
    updateTotal(transaction_list.visibleItems);


});
$(DATE_RANGE_FIELD_LOCATOR).change(function () {
    filterFunction();
    //update total
    updateTotal(transaction_list.visibleItems);

});

function isCheckboxChecked() {


    $("input[type='checkbox']").click(function () {
        if (categories.includes($(this).attr('id'))) {

            let index = categories.indexOf($(this).attr('id'));
            categories.splice(index, 1);

        } else {


        }
        //Adds each checked checkbox to array.
        $.each($("input[type='checkbox']:checked"), function () {
            if (categories.includes($(this).attr('id'))) {

            } else {
                if ($(this).attr('id') == undefined) {

                } else {
                    categories.push($(this).attr('id'));
                }
            }


        });
        filterFunction();
        updateTotal(transaction_list.visibleItems);
    });


    return categories;
}

function filterFunction() {
    let value = $(DATE_RANGE_FIELD_LOCATOR).val();
    start_date = new Date(value.split("-")[0].replace(/\s+/g, ''));
    end_date = new Date(value.split("-")[1].replace(/\s+/g, ''));
    transaction_list.filter(function (item) {
        let transact_date = new Date(Date.parse(item.values().date));
        if ((transact_date >= start_date && transact_date <= end_date) && (categories.includes(item.values().name))) {
            return true;
        } else {
            return false;
        }
    });

}

function updateTotal(items) {
    let totalPeriodExpenses = 0;
    let totalPeriodEarnings = 0;
    items.forEach(value => {
        if (value.values().isExpense == 'True') {
            totalPeriodExpenses -= parseFloat(value.values().amount.replace(",",""));
        } else {
            totalPeriodEarnings += parseFloat(value.values().amount.replace(",",""));
        }
    });
    if (totalPeriodExpenses == 'NaN') {
        totalPeriodExpenses = 0;
    }
    if (totalPeriodEarnings == 'NaN') {
        totalPeriodEarnings = 0;
    }
    // display these total number
    $(TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR).text(Number(totalPeriodExpenses).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));
    $(TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR).text(Number(totalPeriodEarnings).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ","));

}