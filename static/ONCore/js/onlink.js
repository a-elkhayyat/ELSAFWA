$(".confirm-delete").on("click", function(e) {
    var link = this;

    e.preventDefault();

    $("<div>هل انت متأكد من حذف هذا العنصر؟</div>").dialog({
        buttons: {
            "Ok": function() {
                window.location = link.href;
            },
            "Cancel": function() {
                $(this).dialog("close");
            }
        }
    });
});