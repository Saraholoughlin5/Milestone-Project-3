$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.fixed-action-btn').floatingActionButton({direction: "left", hoverEnabled: false});
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('input#input_text, textarea#textarea2').characterCounter();
  });
 
