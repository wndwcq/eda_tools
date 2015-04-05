$(document).ready(function() {
    /*教训呀，dajax的代码不要放在这里.否则执行不了*/
	$('#ajaxbutton').mouseover(function(){
        alert("this is a test");
    });
   
    $('#open').click(function() {
        $('#login form').slideToggle(300);
        $(this).toggleClass('close');
    });
        
  //  setInterval("myFunction()",10000);
    
    /*---------- my code is here------------------*/
    $('.record_detail').dblclick(function(){
        window.location.href="/update_a_kb_record/?Row=" + $(this).parent().attr("id")
        //alert("test->" + $(this).parent().attr("id"))
    }); 

    /* -----    点赞操作 ---------*/
    $('.make_a_thumb').click(function(){
        alert("test  test !!!")
        $(this).attr("disabled","true")
        // -- 使用Ajax技术，在后台对点赞结果加1
        $.get('/kb_make_thumb','kbid=' + $(this).parent().parent().parent().attr("id") )
        var time = $(this).attr("data-time");
        $(this).attr("data-time",++time);
        $(this).html("<span class=\"glyphicon glyphicon-heart-empty\" class=\"badge\"> </span>   " + $(this).attr("data-time")); 
    });
    
    /* ---- 知识库的搜素下拉菜单处理 ----*/
    $('.kb_serch_button').click(function(){
        $('#kb_serch').attr("value") = $(this).attr("data-type")
        alert($(this).attr("data-name"))
        $('#kb_serch').html($(this).attr("data-name"))
    });
    
    $('#kb_serch').click(function(){
        alert("test!!")
    })
     
}); // end ready




    
