
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems, {});
});
  
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

  function toggleDrawer(){
    document.getElementById('side-drawer').classList.toggle("d-none");
    console.log("Drawer toggle")
  }

