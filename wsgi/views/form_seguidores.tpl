

   <section>
   %for d in doc['users']:
	    <td> <p><a href="/mensaje/{{d['screen_name']}}" >{{d['name']}} , @{{d['screen_name']}} </a> </p></td>
	%end
   </div>
   </section>
    <form action="/seguidores" method="post">
      <p>@<input name="name" id="texbox" rows="1" cols="50" type="text" /> </p>
    </form>
    <a href="/menu">Cancelar</a>
  </body>

