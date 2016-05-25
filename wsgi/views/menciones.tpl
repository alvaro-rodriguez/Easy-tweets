% include('estadisticas.tpl') 

 <form action="menciones" method="post">
      <textarea name="numero" id="textbox" rows="3" cols="5"></textarea>
 </form>

      %for d in doc:
      	   <p>{{d['text']}}>
	
	   %end
      %end




<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
