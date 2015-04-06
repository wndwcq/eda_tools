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


    
    /* ---- 知识库的搜素下拉菜单处理 ----*/
    $('.kb_serch_button').click(function(){
        $('#kb_serch').attr("value",$(this).attr("data-type"))                
        //alert($(this).attr("data-type") + "0000" + $(this).attr("data-name"))
        $('#kb_serch').html("<span>" + $(this).attr("data-name") + "</span>")
    });
    
    $('#kb_serch').click(function(){
        alert("test!!" + $(this).attr("value") + "   " + $(this).attr("name"))
    });  

     
    $('.make_a_thumb').click(function(){
        // -- 使用Ajax技术，在后台对点赞结果加1
        $.post('/kb_make_thumb',
            'kbid=' + $(this).parent().parent().parent().attr("id"),
            function(data,status){
                if (status == "success"){
                    switch(data.msg)
                    {
                    case "OK":
                        alert("success");                        
                        var time = $(this).attr("data-time");
                        $(this).attr("data-time",++time);
                        $(this).html("<span class=\"glyphicon glyphicon-heart-empty\" class=\"badge\"> </span>   " + $(this).attr("data-time")); 
                        break;
                    case "NO_YOUSELF":
                        alert(" : )    给自己点赞，是不厚道的行为。");
                       /*  $(this).html("<span class=\"glyphicon glyphicon-heart-empty\" class=\"badge\" data-toggle=\"popover\" data-trigger=\"focus\" title=\"不能给自己点赞\"  多发动群众吧，大家的眼光是雪亮的\"> </span>")
                        $(this).children("span").popover(data-animation="true") */
                        break;
                    case "ERROR":   
                        alert(" have error ");
                        break;
                    };                    
                };
            });
    });

    
}); // end ready



    
