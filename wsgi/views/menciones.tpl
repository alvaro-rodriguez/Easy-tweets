% include('estadisticas.tpl') 

 
<!-- hero area (the grey one with a slider -->
    <section id="hero" class="clearfix">    
    <!-- responsive FlexSlider image slideshow -->
    <div class="wrapper">
       <div class="row"> 
        <div class="grid_5">  

	   %for d in doc:
	   	<p>"Mencionado por :" {{d['in_reply_to_screen_name']}} "En la fecha:" {{d['created_at']}}</p>
	
	   	<p>{{d['text']}}</p>
	   %end
<p><a href="#" class="buttonlink">CALL TO ACTION</a> <a href="#" class="buttonlink">ONE MORE</a></p>
           </div>
        <div class="grid_7 rightfloat">
              <div class="flexslider">
                  <ul class="slides">
       
                  </ul>
                </div><!-- FlexSlider -->
              </div><!-- end grid_7 -->
        </div><!-- end row -->
       </div><!-- end wrapper -->
    </section><!-- end hero area -->






<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
