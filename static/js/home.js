document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});

    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {fullWidth : true});

    console.log("inside js")
  });
  // Initialize collapsible (uncomment the lines below if you use the dropdown variation)
 // var collapsibleElem = document.querySelector('.collapsible');
 // var collapsibleInstance = M.Collapsible.init(collapsibleElem, options);

 