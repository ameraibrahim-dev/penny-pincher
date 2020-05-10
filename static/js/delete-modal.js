target_class('.transaction-delete');
target_class('.delete-wallet-link');
target_class('.category-delete');


$('#modal-cancel').on('click', function () {

    $('#delete-modal').removeClass('-active');
    $('#modal-overlay').removeClass('-apply-overlay');

});

function target_class(trgt_class) {
    $(trgt_class).on('click', function () {
        $('#delete-modal').toggleClass('-active');
        $('#modal-overlay').toggleClass('-apply-overlay');
    });
}

function delete_modal(link, msg) {
    $('#modal-message').text(msg);
    $('#modal-delete').attr("href", link)
}