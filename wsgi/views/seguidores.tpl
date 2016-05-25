% include('estadisticas.tpl') 

 
	%for d in {{doc['user']}}:
	     {{d['name']}}  {{d['screen_name']}}  <img src={{d['profile_image_url']}}/>
	%end


<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
