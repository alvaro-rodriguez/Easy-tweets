% include('header.tpl')
   <body>
    <p>tweet:</p>
    <br />
    <form action="twittear" method="post">
      <p><textarea name="twittear" id="textbox" rows="3" cols="50"></textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
    </form>
    <a href="/menu">Cancelar</a>
  </body>
% include('footer.tpl')
