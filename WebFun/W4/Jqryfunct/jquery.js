$("#cl").click(function(){
    alert("Handles for .click() called")
});

$(function() {
    $("#bhide").on("click", function(){
        $("#hd").hide();
    });
});

$(function() {
    $("#bshow").on("click", function(){
        $("#hd").show();
    });
});

$(function() {
    $("#btoggle").on("click", function(){
        $("#tg").toggle(1000);
    });
});


$(function() {
    $("#bsdown").on("click", function(){
        $("#sq1").slideDown();
    });
});

$(function(){ 
    $("#bsup").on("click", function(){
        $("#sq2").slideUp().delay(500).slideDown();
    });
});

$(function(){ 
    $("#bstog").on("click", function(){
        $("#sq3").slideToggle();
    });
});



$(function(){ 
    $("#bfout").on("click", function(){
        $("#sq5").fadeOut().delay(1000).fadeIn();
    });
});

$(function(){ 
    $("#bbef").on("click", function(){
        $("#pbef").before("<p>Hello World</p>");
    });
});

$(function(){ 
    $("#baft").on("click", function(){
        $("#paft").after("<p>This is the After Function</p>");
    });
});

$(function(){ 
    $("#bapd").on("click", function(){
        $("#papd").append("<p>Hello Super World this is append</p>");
    });
});

$(function(){ 
    $("#bhtm").on("click", function(){
        $("#phtm").html("This a new html content");
    });
});


$(function(){ 
    $("#bat").on("click", function(){
        var title=$("em").attr("title");
        $("#pat").text(title);
    });
});

$(function(){ 
    $("#btxt").on("click", function(){
        $("#ptxt").text("<b> this is a new text</b>");
    });
});