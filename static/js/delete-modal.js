target_class('.transaction-delete');
target_class('.delete-wallet-link');
target_class('.category-delete');

target_form('#create-wallet-form','Successfully created Wallet.');
target_form('#update-wallet-form','Successfully updated Wallet.');
target_form('#add-goal-form','Successfully created Goal.');
target_form('#update-goal-form','Successfully updated Goal.');



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

function delete_modal(link,msg,confirm_msg) {
     $('#modal-message').text(msg);
     $('#confirm-message').text(confirm_msg);
     $('#modal-confirm-btn').attr("href", link);
}

function display_confirmation(){
    $('#modal-card').removeClass('-active');
    $('#modal-confirm').toggleClass('-active');
}

function create_modal(trgt_form, confirm_msg){
        $('#delete-modal').toggleClass('-active');
        $('#modal-overlay').toggleClass('-apply-overlay');
        $('#modal-card').removeClass('-active');
        $('#modal-confirm').toggleClass('-active');
        $('#confirm-control').toggleClass('-hidden');
        $('#redirect-msg').toggleClass('-active');
        $('#confirm-message').text(confirm_msg);
}

function target_form(trgt_form,confirm_msg) {

  $(trgt_form).on("submit", function(e) {
      let form =this;
     create_modal(trgt_form,confirm_msg);

     e.preventDefault();

     setTimeout( function () {
        form.submit();
    }, 800);


     //
     // if($('#element').data('clicked')) {
     //
     //    $(trgt_form).submit();
     //
     // }else{
     //     e.preventDefault();
     // }

  });

  // $('#modal-confirm-btn').on('click',function(){
  //     $(trgt_form).submit();
  // });

}