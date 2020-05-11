let categories = [];
const TYPE_FIELD_LOCATOR = "#id_is_expense";
const CATEGORY_FIELD_LOCATOR = "#id_category";
const SELECTED_CATEGORY_TYPE_LOCATOR = "#selected_category_isExpense";
const SELECTED_CATEGORY_NAME_LOCATOR = "#selected_category_name";
const EARNING_CATEGORIES_API_URL = "/api/v1/user/earnings/categories/";
const EXPENSE_CATEGORIES_API_URL = "/api/v1/user/expenses/categories/";
const SELECTED_CATEGORY_IS_EXPENSE = $(SELECTED_CATEGORY_TYPE_LOCATOR).val();
const SELECTED_CATEGORY_NAME = $(SELECTED_CATEGORY_NAME_LOCATOR).val();

// on type change
$(TYPE_FIELD_LOCATOR).change(
    function () {
        let type = $(TYPE_FIELD_LOCATOR + " option:selected").text();
        getCategories(type);
        generateCategoryOptions(type);
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
            url = EXPENSE_CATEGORIES_API_URL;
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
function generateCategoryOptions(type) {
    let selectedCatType = null;
    if (SELECTED_CATEGORY_IS_EXPENSE == "False") {
        selectedCatType = "Earning";
    } else if (SELECTED_CATEGORY_IS_EXPENSE == "True") {
        selectedCatType = "Expense";
    }
    let categoryOptions = "";
    if (selectedCatType.toLowerCase() == type.toLowerCase()) {
        categoryOptions = "<option value='" + SELECTED_CATEGORY_NAME + "'  selected>" + SELECTED_CATEGORY_NAME + "</option>";
    } else {
        categoryOptions = "<option value=''  selected>---------</option>";
    }

    categories.forEach(function (category) {
        if (SELECTED_CATEGORY_NAME != category.name) {
            categoryOptions += "<option value='" + category.name + "'>" + category.name + "</option>"
        }

    });
    $(CATEGORY_FIELD_LOCATOR).html(categoryOptions);
}

$(document).ready(function () {
    if (SELECTED_CATEGORY_NAME != null) {
        let type = $(TYPE_FIELD_LOCATOR + " option:selected").text();
        getCategories(type);
        let categoryOptions = "<option value='" + SELECTED_CATEGORY_NAME + "'  selected>" + SELECTED_CATEGORY_NAME + "</option>";
        categories.forEach(function (category) {
            if (SELECTED_CATEGORY_NAME != category.name) {
                categoryOptions += "<option value='" + category.name + "'>" + category.name + "</option>"
            }

        });
        $(CATEGORY_FIELD_LOCATOR).html(categoryOptions);
    }
});