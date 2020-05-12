var expanded = false;

$(document).ready(function () {
  let categories
  categories = isCheckboxChecked();
  showCheckboxes();

});

function showCheckboxes() {
  let checkboxes = document.getElementById("checkboxes");

  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

function isCheckboxChecked(){

  let categories = [];

  $("input[type='checkbox']").click(function () {
      if(categories.includes($("input[type='checkbox']").attr('id'))){
         let index = categories.indexOf($(this).attr('id'));
          categories.splice(index,1);
      }else {

        //Adds each checked checkbox to array.
        $.each($("input[type='checkbox']:checked"), function () {
          if ($(this).attr('id') == undefined) {
          } else {
            categories.push($(this).attr('id'));
          }
        });
      }
    console.log(categories);
  });

  return categories;
}