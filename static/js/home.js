const autoplay = () => {

  let indicatorItems = document.querySelectorAll('.carousel .indicator-item'),
    slideTime = 3000,
    activeClass = "active";
  setInterval(() => {
    indicatorItems.forEach(el => {
      if (el.classList.contains(activeClass)) {
        sib = el.nextElementSibling;
        if (sib == null) {
          indicatorItems[0].click();
        } else {
          sib.click()
        }
      }
    });
  }, slideTime);
}



function openNav() {
  document.getElementsByClassName("mobile-sidenav")[0].style.visibility = "visible";
  document.getElementsByClassName("mobile-sidenav-overlay")[0].style.visibility = "visible";
}

function closeNav() {
  document.getElementsByClassName("mobile-sidenav")[0].style.visibility = "hidden";
  document.getElementsByClassName("mobile-sidenav-overlay")[0].style.visibility = "hidden";
}

document.addEventListener('DOMContentLoaded', function () {
  // var elems = document.querySelectorAll('.sidenav');
  // console.log(elems)
  // var sidenavInstance = M.Sidenav.init(elems);

  // document.getElementsByClassName(".sidenav-trigger")[0].addEventListener("click", function(){
  //   // console.log("sidenav")
  //   sidenavInstance.open()
  // });

  var carousel = document.querySelectorAll('.carousel');
  var instance = M.Carousel.init(carousel, {
    fullWidth: true,
    indicators: true
  });

  autoplay()

  var materialBox = document.querySelectorAll('.materialboxed');
  var materialBoxInstance = M.Materialbox.init(materialBox, {});

  var dropdown = document.querySelectorAll('.dropdown-trigger');
  var dropdownInstance = M.Dropdown.init(dropdown, {});
});


$(document).ready(function () {
  $('#example').DataTable({
    dom: 'Bfrtip',
    buttons: [
      'copy'
    ]
  });
});

$(document).ready(function () {


  let owl = $('.owl-carousel')
  owl.owlCarousel({
    nav: true,
    slideSpeed: 100,
    paginationSpeed: 200,
    items: 1
  })

  $('.home-carousel').owlCarousel({
    loop:true,
    nav:true,
    navigationText: ["<div class='nav-button owl-prev'><i class='fas fa-arrow-left'></i></div>","<div class='nav-button owl-prev'><i class='fas fa-arrow-right'></i></div>"],
    animateOut: 'slideOutDown',
    animateIn: 'flipInX',
    items: 1,
    smartSpeed: 450
  });

  $(".dropdown-trigger").dropdown();

});