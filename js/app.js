$(document).ready(function() {
    $("#content").load("./pages/inicio.html");

    $("#navbarSupportedContent a").click(function(event) {
        var item = event.target.id
        if(item.trim()!=""){
            var enlace = item.trim().split("-");
            $("#content").load("./pages/"+enlace[1]+".html", function(responseText, statusText, xhr){
                if (statusText == "error" ) {
                    $("#content").load("./pages/404.html");
                }
            })
        }
    });
});