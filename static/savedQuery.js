$(document).ready(function () {

    $.ajax({
        url: '/saved_query',
        type: 'POST',
        success: function (response) {
            var tableData = response["data"];
            $("#count").text(tableData.length);
            console.log(tableData);
            $("#saved_query_table").empty();
            var detail = '';
            detail += '<table style="width:100%"><tr><th>Query Name</th><th>Date Created</th></tr>';
            for (var i = 0; i < tableData.length; i++) {
                console.log(tableData[i])
                detail += '<tr><td>' + tableData[i][0] + '</td><td>' + tableData[i][2] + '</td></tr>';       
            }
            detail += '</table>'
            $("#saved_query_table").append(detail);
            
        }
    });
});
