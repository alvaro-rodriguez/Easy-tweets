% include('estadisticas.tpl') 

  
  <iframe width="90%" height="200px"  > 
	   %for d in doc:
	   	<p>"Mencionado por :" {{d['in_reply_to_screen_name']}} "En la fecha:" {{d['created_at']}}</p>
	
	   	<p>{{d['text']}}</p>
	   %end

  </iframe>




<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
