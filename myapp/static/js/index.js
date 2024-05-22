$(document).ready(function() {
    $('.message a').click(function(){
        $('.form form').animate({height: "toggle", opacity: "toggle"}, "slow");
    });

    $(".quantity").each(function(id, val){
        $(val).change(function(){
            $(val).parent().siblings().eq(4).text(parseInt($(val).parent().siblings().eq(3).text())*$(val).val());
        });
    })

    $("#update").click(function(){
        let table = $('tbody');
        $(table).children().each(function(id, val){
            $.ajax({
                type: 'get',
                url: '/myapp/update/',
                data: {'id': $(val).attr("id"), quantity: $(val).children().eq(3).children().val()},
                success: function(){
                    $(".modal .modal-body").text("Successful update");
                    $(".modal").modal('show');
                    setTimeout(function () {
                        $('.modal').modal('hide');
                    }, 2000);
                }
            });
        })
    })

    $("#pay").click(function(){
        $('tbody').empty();
        $.ajax({
            type: 'get',
            url: '/myapp/bill/',
            success: function(){
                $(".modal .modal-body").text("Successful payment");
                $(".modal").modal('show');
                setTimeout(function () {
                    $('.modal').modal('hide');
                }, 2000);
            }
        });
    });
})

function add(id){
    $.ajax({
        type: 'get',
        url: '/myapp/add/',
        data: {'id': id}
    }).done( function(){
        $("#number_product").text(parseInt($("#number_product").text()) + 1);
    });
}

function del(id){
    $.ajax({
        type: 'get',
        url: '/myapp/del/',
        data: {'id': id},
        success: function(data){
            console.log(id);
            $(("#"+id)).remove()
        }
    });
}
