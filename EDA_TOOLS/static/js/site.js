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
        window.location.href="/update_a_kb_record/?Row=" + $(this).attr("id")
    }); 

    $('.make_a_thumb').click(function(){
       // $.get('/kb_make_thumb','kbid = ' + $(this).attr("id"))
       //$(this).text("  3   ");
       alert("this is a test" + $(this).value());
    });
     
}); // end ready




    
