

$("#formSig").submit(function(e){
  
  var $form = $(this)
  var $error = $form.find(".error")
  var data = $form.serialize()
  console.log($form)
  
  console.log(data)
  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(response) {
      console.log(response)
      window.location.href = "/dashboard/";
    },
    error: function(response) {
      console.log(response)
      $error.text(response.responseJSON.error).removeClass("error--hidden")
    }

  });
  e.preventDefault();
});
$("#form_Login").submit(function(e){
  
  var $form = $(this)
  var $error = $form.find(".error")
  var data = $form.serialize()
  console.log($form)
  
  console.log(data)
  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(response) {
      console.log(response)
      window.location.href = "/dashboard/";
    },
    error: function(response) {
      console.log(response)
      $error.text(response.responseJSON.error).removeClass("error--hidden")
    }

  });
  e.preventDefault();
});


