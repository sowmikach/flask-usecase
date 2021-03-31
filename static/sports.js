$(document).ready(function () {
    $("input[name='search']").click(function () {
        var test = $(this).val();
        $("div.search").hide();
        $("#" + test).show();
    });
    $("#sports_data").click(function () {
        var sp = $("#sport").val();
        var year = $("#year").val();
        if(sp == '' || year == ''){alert("cannot be empty"); }
        if(sp != '' && year != ''){
        $.ajax({
            url: '/getsports',
            data: $('#sports_form').serialize(),
            type: 'POST',
            success: function (response) {
                var sportsData = response["data"];
                $("#details_table").empty();
                var details = '';
                details += '<table style="width:100%"><tr><th>Firstname</th><th>Lastname</th></tr>';
                for (var i = 0; i < sportsData.length; i++) {
                    details += '<tr><td>' + sportsData[i].first_name + '</td><td>' + sportsData[i].last_name + '</td></tr>';
                }
                details += '</table>'
                $("#details_table").append(details);
            }
        });
    }
    });

    $("#saved_query_sports").click(function () {
        $.ajax({
            url: '/savedquerysports',
            data: $('form').serialize(),
            type: 'POST',  
            success: function (response) {
                console.log(response);
            }
        });
    });

    $("#salary_data").click(function () {
        var salary_low = $("#salary_low").val();
        var salary_high = $("#salary_high").val();
        if (salary_low == '') { alert("cannot be empty"); }
        if (salary_high == '') { alert("cannot be empty"); }
        if (salary_low >= salary_high){ alert("salary low cannot be higher than salary high"); }
        if (salary_low != '' && salary_high != '' && salary_low < salary_high) {
            $.ajax({
                url: '/getsalary',
                data: $('#salary_form').serialize(),
                type: 'POST',
                success: function (response) {
                    var salaryData = response["data"];
                    $("#details_table_sal").empty();
                    var detail = '';
                    detail += '<table style="width:100%"><tr><th>Firstname</th><th>Lastname</th></tr>';
                    for (var i = 0; i < salaryData.length; i++) {
                        if (salaryData[i].salary >= salary_low && salaryData[i].salary <= salary_high) {
                            detail += '<tr><td>' + salaryData[i].first_name + '</td><td>' + salaryData[i].last_name + '</td></tr>';
                        }
                    }
                    detail += '</table>'
                    $("#details_table_sal").append(detail);

                }
            });
        }
    });

    $("#saved_query_salary").click(function () {
        $.ajax({
            url: '/savedquerysalary',
            data: $('form').serialize(),
            type: 'POST',  
            success: function (response) {
                console.log(response);
            }
        });
    });



});

