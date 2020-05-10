$('#delete-btn').on('click', function(){

    $('#delete-modal').toggleClass('-active');
    $('#modal-overlay').toggleClass('-apply-overlay');

});

$('#modal-cancel').on('click', function(){

    $('#delete-modal').removeClass('-active');
    $('#modal-overlay').removeClass('-apply-overlay');

});

function delete_modal(link,msg){
    $('#modal-message').text(msg);
    $('#modal-delete').attr("href",link);
}