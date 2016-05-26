% include('estadisticas.tpl') 

 
<!-- hero area (the grey one with a slider -->
    <section id="hero" class="clearfix">    
    <!-- responsive FlexSlider image slideshow -->
    <div class="wrapper">
       <div class="row"> 
        <div class="grid_5">
	    </div>

	   %for d in doc:

              <div class="flexslider" width="100%" >
	      <ul class="slides" width="100%" >
		<p>Conversación con: {{d['senders_screen_name']}}</p>
	   	<p>{{d['text']}}</p>
		 </ul>
                </div><!-- FlexSlider -->

	   %end

         
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
