const NOTE_FIELD_LOCATOR = "#filterByNoteTextField";
const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
let options = {
    valueNames: ['name', 'note', 'amount', 'date'],
    page: 5,
    pagination: [{
        name: "pagination",
        paginationClass: "pagination",
        outerWindow: 2,
        innerWindow: 2,

    }],
};

let transaction_list = new List('transactions-list', options);
$(NOTE_FIELD_LOCATOR).keydown(function () {
    let val = $(NOTE_FIELD_LOCATOR).val();
    if (val.length == '') {
        transaction_list.search();
    } else {
        transaction_list.search($(NOTE_FIELD_LOCATOR).val(), ['note']);
    }


});
$(DATE_RANGE_FIELD_LOCATOR).change(function () {
    let value = $(DATE_RANGE_FIELD_LOCATOR).val();
    start_date = value.split("-")[0].replace(/\s+/g, '');
    end_date = value.split("-")[1].replace(/\s+/g, '');
    transaction_list.filter(function (item) {
        console.log(item)
        return true;
        //todo filter
        if (item.values().date > 1) {
            return true;
        } else {
            return false;
        }
    });
});