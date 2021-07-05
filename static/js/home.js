
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

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var sidenavInstance = M.Sidenav.init(elems);

    var carousel = document.querySelectorAll('.carousel');
    var instance = M.Carousel.init(carousel, { 
      fullWidth: true,
      indicators: true});

     autoplay()
  
   var materialBox = document.querySelectorAll('.materialboxed');
   var materialBoxInstance = M.Materialbox.init(materialBox, {});

   var dropdown = document.querySelectorAll('.dropdown-trigger');
   var dropdownInstance = M.Dropdown.init(dropdown, {});

  });


  $(document).ready(function() {
    $('#example').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            'copy'
        ]
    } );
} );

  $(document).ready(function(){
    $(".dropdown-trigger").dropdown();    

    let owl = $('.owl-carousel')
     owl.owlCarousel({
      nav: true,
      slideSpeed : 100,
      paginationSpeed : 200,
      items:1
   })

  });

  // Initialize collapsible (uncomment the lines below if you use the dropdown variation)
 // var collapsibleElem = document.querySelector('.collapsible');
 // var collapsibleInstance = M.Collapsible.init(collapsibleElem, options);

 