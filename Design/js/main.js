$('document').ready(function(){

    $('.col-sm-4.col-xs-4.story ').hover(function(){
    	$(this).css('opacity', '1')
    	console.log('kkkkkk');
    })


    $("img#gallrey-img").click(function(){

       var $src = $(this).attr("src");

       $("#image-box-popup img").attr("src", $src);

       $("div#image-box-popup ").css('display', 'block')

      $("#image-box-popup").click(function () {
        $("div#image-box-popup ").css('display', 'none')
    });       
 
    })

   
   $(".our_team_number_box1").hover(function(){
   	   $("div#our_team_number_des1").fadeIn('slow');
      },
      function(){
        $('div#our_team_number_des1').fadeOut('slow');
      }
   )

   $(".our_team_number_box2").hover(function(){
   	   $("div#our_team_number_des2").fadeIn('slow');
      },
      function(){
        $('div#our_team_number_des2').fadeOut('slow');
      }
   )

   $(".our_team_number_box3").hover(function(){
   	   $("div#our_team_number_des3").fadeIn('slow');
      },
      function(){
        $('div#our_team_number_des3').fadeOut('slow');
      }
   )
  

})