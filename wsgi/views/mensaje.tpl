% include('header.tpl')
   <body>
   <section>
   <table>
  <tr>
  <div id='aside'>
  
   %for d in doc['users']:
	    <td> <p><a href=https://www.twitter.com/{{d['screen_name']}} >{{d['name']}} , @{{d['screen_name']}} </a> </p></td>
	%end
   </div>
   </section>
   <tr>
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
  </tr>
  </table>
  </body>
% include('footer.tpl')
