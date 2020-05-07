let categories = [];
const TYPE_FIELD_LOCATOR = "#id_is_expense";
const CATEGORY_FIELD_LOCATOR = "#id_category";
const EARNING_CATEGORIES_API_URL = "/api/v1/user/earnings/categories/";
const EXPENSE_CATEGOREIS_API_URL = "/api/v1/user/expenses/categories/";
// on type change
$(TYPE_FIELD_LOCATOR).change(
    function () {
        let type = $(TYPE_FIELD_LOCATOR + " option:selected").text();
        getCategories(type);
        generateCategoryOptions();
    }
);

function getCategories(type) {
    let url = null;
    //determine ajax url
    switch (type.toLowerCase()) {
        case "earning":
            url = EARNING_CATEGORIES_API_URL;
            break;
        case "expense":
            url = EXPENSE_CATEGOREIS_API_URL;
            break;
        default:
            categories = [];
            break;
    }
    // ajax call to get categories
    if (url != null) {
        $.ajax({
            url: url,
            type: 'GET',
            datatype: 'json',
            async: false,
            success: function (result) {
                categories = eval(result);
            },
            error: function (error) {
                alert(error);
            }
        });
    }
}

// generate html and update category options
function generateCategoryOptions() {
    let categoryOptions = "<option value=''  selected>---------</option>";
    categories.forEach(function (category) {
        categoryOptions += "<option value='" + category.name + "'  selected>" + category.name + "</option>"
    });
    $(CATEGORY_FIELD_LOCATOR).html(categoryOptions);
}
