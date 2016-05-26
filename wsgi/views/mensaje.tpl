% include('header.tpl')
   <body>
  <div class='aside'>
   %for d in doc['users']:
	  <div class="flexslider" width="100%" >
	     <ul class="slides" width="100%" >
	     <p><a href=https://www.twitter.com/{{d['screen_name']}} >{{d['name']}} , @{{d['screen_name']}} </a> De {{d['location']}}</p>
	     <p>{{d['description']}}
	     <img {{d['profile_image_url']}}/>
	     </ul>
	  </div><!-- FlexSlider -->
	%end
   </div>

    <p>Mensaje directo:</p>
    <br />
    <form action="/mensaje" method="post">
      <p>Destino:</p>
      <p>@<input name="destino" id="texbox" rows="1" cols="50" type="text" /> </p>
      <p>Mensaje</p>
      <p><textarea name="mensaje" id="textbox" rows="3" cols="50"></textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
    </form>
    <a href="/menu">Cancelar</a>

  </body>
% include('footer.tpl')
