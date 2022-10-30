/////////////////////
///////Java script for post page
/////////////////////

$(function(){
    //exceuted when js menu cicked
    $('.js-menu-icon').click(function() {
        //$(this) : self elemnt, namely div.js-menu-icon
        //next() : Next to div.js-menu-icon, namely div.menu
        // toggle() : switch show and hide
        $(this).next().toggle();
    })
})
