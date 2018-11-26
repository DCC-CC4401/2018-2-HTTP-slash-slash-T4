jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});
jQuery(document).ready(function($) {
    $(".clickable-rowPendiente").click(function() {
        window.location = $(this).data("href");
    });
});