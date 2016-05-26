% include('estadisticas.tpl') 

 
	%for d in doc['users']:
	     <p><a href=# >{{d['name']}} , @{{d['screen_name']}} </a> De {{d['location']}}</p>
	     <p>{{d['description']}}
	     <img {{d['profile_image_url']}}/>
	%end


<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
