// document.addEventListener('DOMContentLoaded', function() { 
//     var elems = document.querySelectorAll('select');
//     var instances = M.FormSelect.init(elems, options);
//   });

  function toggleStudent() {
    document.getElementsByClassName("class-promotion-form")[0].style.display = "none";
    document.getElementsByClassName("stu-promotion-form")[0].style.display = "block";
    console.log("function-called")
  }

  function toggleClass() {
    document.getElementsByClassName("class-promotion-form")[0].style.display = "block";
    document.getElementsByClassName("stu-promotion-form")[0].style.display = "none";
    console.log("function-called student")
  }