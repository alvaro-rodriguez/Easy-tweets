% include('estadisticas.tpl') 
<p><a href="#" class="buttonlink">CALL TO ACTION</a> <a href="#" class="buttonlink">ONE MORE</a></p>

      %for d in dic:
      	   <p>{{d['text']}} </p>
	   <p>menciones:</p>
	   %for m in {{d['user_mention']}}:
	   	{{m['name']}}
	   %end
      %end




<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
