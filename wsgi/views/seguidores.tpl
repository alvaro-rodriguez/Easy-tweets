% include('estadisticas.tpl') 

 
	%for d in doc['users']:
	  <div class="flexslider" width="100%" >
	     <ul class="slides" width="100%" >
	     <p><a href=# >{{d['name']}} , @{{d['screen_name']}} </a> De {{d['location']}}</p>
	     <p>{{d['description']}}
	     <img {{d['profile_image_url']}}/>
	     </ul>
	  </div><!-- FlexSlider -->
	%end


<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
