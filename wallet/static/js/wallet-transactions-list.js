const NOTE_FIELD_LOCATOR = "#filterByNoteTextField";
let options = {
    valueNames: ['name', 'note', 'amount'],
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
    console.log("on change");
    transaction_list.search($(NOTE_FIELD_LOCATOR).val(), ['note']);
});