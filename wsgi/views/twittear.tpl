% include('header.tpl')
   <body>
    <p>Buen momento para un tweet:</p>
    <br />
    <form action="/twittear" method="post">
      <p><textarea name="tweet" id="textbox" rows="3" cols="50"></textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
    </form>
    <a href="/twitter_logout">Desconectar</a>
  </body>
% include('footer.tpl')
