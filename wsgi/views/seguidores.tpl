% include('estadisticas.tpl') 

 <!-- hero area (the grey one with a slider -->
    <section id="hero" class="clearfix">    
    <!-- responsive FlexSlider image slideshow -->
    <div class="wrapper">
       <div class="row"> 
        <div class="grid_5">
	    </div>

	%for d in doc['users']:
	  <div class="flexslider" width="100%" >
	     <ul class="slides" width="100%" >
	     <p><a href=https://www.twitter.com/{{d['screen_name']}} >{{d['name']}} , @{{d['screen_name']}} </a> De {{d['location']}}</p>
	     <p>{{d['description']}}
	     <img {{d['profile_image_url']}}/>
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
