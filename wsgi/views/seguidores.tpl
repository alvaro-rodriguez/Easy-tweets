% include('estadisticas.tpl') 

 
	%for d in {{doc['users']}}:
	     {{d['name']}} 
	%end


<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
