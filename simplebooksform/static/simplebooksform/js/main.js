$(document).ready(function() {
    var TAB_KEY = 9;
    var ENTER_KEY = 13;
    var legend = $('form#books legend');
    
    $('#books li:not(:first)').hide();
    $('#books li:first input').focus();
    
    $('#books input').keydown(function(event) {
        var keyHit = event.which;
        if ((!event.shiftKey && keyHit == TAB_KEY) || keyHit == ENTER_KEY) {
             event.preventDefault();
             
             if($(this).attr('name') == 'submit') {
                 legend.text("Please make sure the data is correct and then click Submit");
                 return false;
             }

             $(this).parent().next('li').slideDown(300, function() {
                 var forminput = $(this).find('input');
                 var name = forminput.attr('name');
                 var title = "Type in " + name + " and press Enter";
                 
                 if(name == 'submit') {
                     title = "You are done, now you can save"
                 }
                 forminput.focus();
                 legend.text(title);
             });
         }
    }); 
});