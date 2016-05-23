% include('header.tpl')
   <body>
    <p>Mensaje directo:</p>
    <br />
    <form action="/mensaje" method="post">
      <p><textarea name="tweet" id="textbox" rows="3" cols="50"></textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
    </form>
    <a href="/menu">Cancelar</a>
  </body>
% include('footer.tpl')
