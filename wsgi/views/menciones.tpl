% include('estadisticas.tpl') 

 <form action="menciones" method="post">
      <textarea name="numero" id="textbox" rows="3" cols="5"></textarea>
 </form>



	   %for d in doc:
	   	<p>"Mencionado por :" {{d['in_reply_to_screen_name']}} "En la fecha:" {{d['created_at']}}</p>
		<p>"Mencionados:"</p>
		%for i in {{d['entities']['user_mentions']}}:
		   {{i['name']}}
		%end
	   	<p>{{d['text']}}</p>
	   %end
	






<!-- main content area -->   
<div id="main" class="wrapper">
    
    


% include('footer.tpl')
