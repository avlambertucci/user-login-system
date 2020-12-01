
$(document).ready(function(){
 
  $("#formSig").submit(function(e){
    
    console.log('teste')
  

    let $form = $(this)
    let data = $form.serialize()
    console.log(form)
    console.log(data)
  
    fetch('/user/signup', { 
      type: 'POST',
      data: data,
      dataType: 'json',
      success: function(response) {
        console.log(response)
      },
      error: function(response) {
        console.log(response)
      }
  
    })
    e.preventDefault();
  
  })
});