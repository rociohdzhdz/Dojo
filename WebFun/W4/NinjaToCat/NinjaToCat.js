
$("img").click(function () {
    $(this).hide();
    var im0 = $(this).attr("data-alt-src");
    $(this).attr("src", im0);
    $(this).show();
});
