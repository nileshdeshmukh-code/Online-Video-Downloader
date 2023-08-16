$(document).ready(function () {

    $("#errorToast").toast("show");
    $("#searchSpinner").hide();
    $(document).on('submit', "#frmSearch", function (event) {
       
        event.preventDefault();
        $("#result").html("");
        $("#searchSpinner").show();
        url = $("#url").val();
        search(url);
        $("#errorToast").toast("show");
        
    });

    $("#url").keyup(function (event) {
        // var form = document.querySelector('#frmSearch')
        // if(form.checkValidity())
        // {
        //     event.preventDefault();        
        //     $('#frmSearch').delay(200).submit();
        // }
       
       
    });
}
);

function hideerror() {
    $("#errorToast").removeClass("show");
};


function search(url) {
    $.ajax({
        type: 'POST',
        url: "/search",
        data: { url: url },
        dataType: "json",
        success: function (data) {

            $("#searchSpinner").hide();
            $("#result").html(data);
            $("#result").append(data.htmlresponse);

        },
        error: function (data) {
            alert("exception")
            $("#searchSpinner").hide();
            $("#result").html(data);
            $("#result").append(data.htmlresponse);


        }
    });
};



