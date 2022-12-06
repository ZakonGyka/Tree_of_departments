$(document).ready(function()
{
    $("button").click(function(){
        $("#div1").load("employees_list.txt");
    });
    // activate Nestable for list 1
    $('#nestable').nestable({
        group: 1
    })//.nestable('collapseAll');
    $('#nestable2').nestable({
        group: 1
    })
    .on('change', updateOutput);



    $('#nestable-menu').on('click', function(e)
    {
        var target = $(e.target),
            action = target.data('action');
        if (action === 'collapse-all') {
            $('.dd').nestable('collapseAll');
        }
        if (action === 'expand-all') {
            $('.dd').nestable('expandAll');
        }
    });
});


$('.dd').on('uploadchildren', function() {

});