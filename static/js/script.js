/* Jquery Initialization - Materialize Features */

$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('.fixed-action-btn').floatingActionButton({
        direction: "top",
        hoverEnabled: false
    });
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.datepicker').datepicker({
        format: "dd mmm yyyy",
        yearRange: 2,
        showClearBtn: true,
        i18n: {
            done: "Select"
        },
    });
     $('.modal').modal();
});

