
$(document).ready(function () {
    $("#exp").click(function () {
        $.ajax({
            url: '/getexpenses',
            data: $('form').serialize(),
            type: 'POST',  
            success: function (response) {
                $("p span").text(response["data"][0].amount_spent);
            }
        });
    });
   
    $("#saved_query").click(function () {
        $.ajax({
            url: '/savedquery',
            data: $('form').serialize(),
            type: 'POST',  
            success: function (response) {
                console.log(response);
            }
        });
    });

});