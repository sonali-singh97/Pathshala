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

  document.addEventListener('DOMContentLoaded', function() {
    console.log("hello from js file!")
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
  });