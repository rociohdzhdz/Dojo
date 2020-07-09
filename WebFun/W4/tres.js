$("#square1").hide(300).show(1000).hide(300).show(1000).hide(300).show(1000);
$("#square2").slideUp(1000).delay(1000).slideDown(1000);
$(".square").fadeToggle(1000).fadeToggle(1000);
$("#square4").toggle(1000).toggle(1000);
$(function(){
$("#square5").css("background-color","yellow");
});

$(function() {
    $(".square").on("click", function(){
        $("#square6").toggle();
    });

});

$(function() {
    $("#square2").on("click", function(){
        $("#square6").slideToggle(200);
    });

});

$(function() {
    $("#square1").on("click", function(){
        $("#square5").fadeToggle(200);
    });

});

$(function() {
    $("#square4").on("mouseover", function(){
        $("#square7").fadeToggle(200);
    });

});

$(function() {
    $("#square5").on("click", function(){
        $("#square6").html("My new content");
    });

});

$(function() {
    $("#square8").on("click", function(){
        var panelId=$(this).attr("data-panelid");
        alert(panelId)
    });

});