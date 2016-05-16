<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

<title>Simple Responsive Template</title>
<meta name="description" content="Simple Responsive Template is a template for responsive web design. Mobile first, responsive grid layout, toggle menu, navigation bar with unlimited drop downs, responsive slideshow">
<meta name="keywords" content="">

<!-- Mobile viewport -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">

<link rel="shortcut icon" href="images/favicon.ico"  type="image/x-icon">

<!-- CSS-->
<!-- Google web fonts. You can get your own bundle at http://www.google.com/fonts. Don't forget to update the CSS accordingly!-->
<link href='http://fonts.googleapis.com/css?family=Droid+Serif|Ubuntu' rel='stylesheet' type='text/css'>

<link rel="stylesheet" href="static/css/normalize.css">
<link rel="stylesheet" href="js/flexslider/flexslider.css">
<link rel="stylesheet" href="static/css/basic-style.css">

<!-- end CSS-->
    
<!-- JS-->
<script src="js/libs/modernizr-2.6.2.min.js"></script>
<!-- end JS-->



</style>
</head>

<body id="home">
  
<!-- header area -->
    <header class="wrapper clearfix">
		       
        <div id="banner">        
        	<div id="logo"><a href="basic.html"><img src="images/basic-logo.svg" alt="logo"></a></div> 
        </div>
        
        <!-- main navigation -->
        <nav id="topnav" role="navigation">
          <div class="menu-toggle">Menu</div>  
          <ul class="srt-menu" id="menu-main-navigation">
              <li class="current"><a href="basic.html">Home page</a></li>
             
              <li><a href="#">Acciones</a>
                  <ul>
                      <li class="current">
                          <a href="#">tweets</a>
                          <ul>
                              <li><a href="/twiter">Publicar un tweet</a></li>
                              <li><a href="#">Ver tweets</a></li>
                                                          
                          </ul>
                      </li>
                      <li class="current">
                          <a href="#">Mensajes directos</a>
                          <ul>
                              
                              <li><a href="#">Mensajería directa</a></li>
                              <li><a href="#">Historial de mensajes</a></li>
                          </ul>
                      </li>
		       <li class="current">
                          <a href="#">Estadísticas</a>
                          <ul>
                              
                              <li><a href="#">Seguidores</a></li>
                              
                          </ul>
                      </li>
		      
                      
                  </ul>
              </li>
              <li>
                  <a href="#">[info de la página]</a>
                 
              </li>
             
          </ul>     
		</nav><!-- end main navigation -->
  
    </header><!-- end header -->
 
 
<!-- hero area (the grey one with a slider -->
    <section id="hero" class="clearfix">    
    <!-- responsive FlexSlider image slideshow -->
    <div class="wrapper">
       <div class="row"> 
        <div class="grid_5">
            <h1>Simple Responsive Template</h1>
            <p>...is a template for responsive web design. A small set of tools and best practices that allows web designers to build responsive websites faster. Websites built with Simple Responsive Template will be optimized for screen widths between 320px and anything. Resize your browser to check it out.
            </p>
            <p><a href="#" class="buttonlink">CALL TO ACTION</a> <a href="#" class="buttonlink">ONE MORE</a></p>
        </div>
        <div class="grid_7 rightfloat">
              <div class="flexslider">
                  <ul class="slides">
                      <li>
                          <img src="images/basic-pic1.jpg" />
                          <p class="flex-caption">Love Brazil !!! Sea view from Rio de Janeiro fort.</p>
                      </li>
                      <li>
                          <a href="http://www.prowebdesign.ro"><img src="images/basic-pic2.jpg" /></a>
                          <p class="flex-caption">El Arco Cabo Mexico. This image is wrapped in a link.</p>
                      </li>
                      <li>
                          <img src="images/basic-pic3.jpg" />
                          <p class="flex-caption">Arches National Park, Utah, Usa.</p>
                      </li>
                      <li>
                          <img src="images/basic-pic4.jpg" />
                          <p class="flex-caption">Morocco desert.</p>
                      </li>
                  </ul>
                </div><!-- FlexSlider -->
              </div><!-- end grid_7 -->
        </div><!-- end row -->
       </div><!-- end wrapper -->
    </section><!-- end hero area -->





<!-- main content area -->   
<div id="main" class="wrapper">
    
    
<!-- content area -->    
	<section id="content" class="wide-content">
      <div class="row">	
        <div class="grid_4">
        	<h1 class="first-header">Introducción</h1>
            <img src="images/basic-pic1.jpg" />
            <p>[Aquí tengo que poner la intoducción]</p>
        </div>
     

	  </div><!-- end row -->
	</section><!-- end content area -->   
      
            
  </div><!-- #end div #main .wrapper -->


<!-- footer area -->    
<footer>
	<div id="colophon" class="wrapper clearfix">
    	footer stuff
    </div>
    
<!--You can NOT remove this attribution statement from any page, unless you get the permission from prowebdesign.ro--><div id="attribution" class="wrapper clearfix" style="color:#666; font-size:11px;">Site built with <a href="http://www.prowebdesign.ro/simple-responsive-template/" target="_blank" title="Simple Responsive Template is a free software by www.prowebdesign.ro" style="color:#777;">Simple Responsive Template</a></div><!--end attribution-->
    
</footer><!-- #end footer area --> 


<!-- jQuery -->
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="js/libs/jquery-1.9.0.min.js">\x3C/script>')</script>

<script defer src="js/flexslider/jquery.flexslider-min.js"></script>

<!-- fire ups - read this file!  -->   
<script src="js/main.js"></script>

</body>
</html>
