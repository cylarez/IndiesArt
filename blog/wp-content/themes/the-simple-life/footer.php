<?php
// If a footer.php file exists in the WP root directory we
// use that, otherwise use this default wp-footer.php file.
if ( file_exists(ABSPATH . '/footer.php') ) :
	include_once(ABSPATH . '/footer.php');
else :
?>
</div>



<?php
// This code pulls in the sidebar:
include('sidebar.php');
?>
		<div id="sub-content">
			<div class="hr"></div>
			
			<div id="footer">
				<div style="float:left">
				<p>Daily illustration ressources for indies arts lovers.</p>
				<ul>
					<li><a href="<?php echo INDIE_URL ?>" title="Home">Home</a> -</li>
					<li><a href="/">Blog</a> -</li>
					<li><a class="current" href="<?php echo INDIE_URL ?>search">Artists</a></li>
				</ul>
				</div>
				<div class="social-links">
					<a href="http://twitter.com/indiesart">Follow Us on Twitter</a>
					<img src="<?php echo INDIE_URL ?>/assets/style/images/twitter-logo.jpg" alt="twitter" />
				</div>
				<div class="clear"></div>
				<p id="copyright">&copy; Copyright IndiesArt.com</p>
			</div>
		</div>
	</div>
	
	</div>
	
	<?php //do_action('wp_footer', ''); ?>

	<div id="fb-root"></div>
    <script type="text/javascript">
      window.fbAsyncInit = function() {
        FB.init({appId: '139707482707461', status: true, cookie: true,
                 xfbml: true});
      };
      (function() {
        var e = document.createElement('script');
        e.type = 'text/javascript';
        e.src = document.location.protocol +
          '//connect.facebook.net/en_US/all.js';
        e.async = true;
        document.getElementById('fb-root').appendChild(e);
      }());
    </script>
    
    <script type="text/javascript">
		var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
		document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
		</script>
		<script type="text/javascript">
		try {
		var pageTracker = _gat._getTracker("UA-11521531-1");
		pageTracker._setDomainName(".indiesart.com");
		pageTracker._trackPageview();
		} catch(err) {}
	</script>
	
</body>
</html>
<?php endif; ?>