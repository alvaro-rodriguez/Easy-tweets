% include('estadisticas.tpl') 

 
	%for d in doc['users']:
	     <p>{{d['name']}}</p> 
	%end


<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
