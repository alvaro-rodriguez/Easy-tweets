% include('estadisticas.tpl') 

 <form action="menciones" method="post">
      <textarea name="numero" id="textbox" rows="3" cols="5"></textarea>
 </form>

    <section id="hero" class="clearfix">    
    <!-- responsive FlexSlider image slideshow -->
    <div class="wrapper">
       <div class="row"> 
        <div class="grid_5">


	   %for d in doc:
	   	<p>"Mencionado por :" {{d['in_reply_to_screen_name']}} "En la fecha:" {{d['created_at']}}</p>
	
	   	<p>{{d['text']}}</p>
	   %end
	</div>
       </div>
       </div>






<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
