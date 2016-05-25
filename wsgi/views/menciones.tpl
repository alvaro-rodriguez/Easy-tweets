% include('estadisticas.tpl') 

 <form action="menciones" method="post">
      <textarea name="numero" id="textbox" rows="3" cols="5"></textarea>
 </form>

      %for d in doc:
      	   <p>{{d['text']}} </p>
	   <p>menciones:</p>
	   %for m in {{d['user_mention']}}:
	   	{{m['name']}}
	   %end
      %end




<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
