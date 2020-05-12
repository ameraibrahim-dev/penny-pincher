{
    const NOTE_FIELD_LOCATOR = "#filterByNoteTextField";
    const DATE_RANGE_FIELD_LOCATOR = "#DateRangeFilter";
    const TOTAL_PERIOD_EXPENSES_TEXT_LOCATOR = "#total-period-expenses";
    const TOTAL_PERIOD_EARNINGS_TEXT_LOCATOR = "#total-period-earnings";
    let categories = [];
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

}