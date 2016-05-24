% include('header.tpl')
   <body>
    <p>Mensaje directo:</p>
    <br />
    <form action="/mensaje" method="post">
      <p>Destino:</p>
      <p><input name="destino" id="texbox" rows="1" cols="50" type="text" /> </p>
      <p>Mensaje</p>
      <p><textarea name="mensaje" id="textbox" rows="3" cols="50"></textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
    </form>
    <a href="/menu">Cancelar</a>
  </body>
% include('footer.tpl')
