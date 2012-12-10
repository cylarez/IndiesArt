<?php
// If a header.php file exists in the WP root directory we
// use that, otherwise use this default wp-header.php file.
if ( file_exists(ABSPATH . '/header.php') ) :
	include_once(ABSPATH . '/header.php');
else :
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns:fb="http://www.facebook.com/2008/fbml">

<head profile="http://gmpg.org/xfn/11">
	<title><?php bloginfo('name'); ?><?php wp_title(); ?></title>
	<meta http-equiv="Content-Type" content="text/html; charset=<?php bloginfo('charset'); ?>" />
	<meta name="generator" content="WordPress <?php bloginfo('version'); ?>" /> <!-- leave this for stats please -->
	<link href="<?php echo INDIE_URL ?>assets/style/images/favicon.png" rel="shortcut icon"/>
	<meta name="google-site-verification" content="exJMMKZzfAIGT88wiStwFXBJseUCLvq4RW_lDkWs-Y4" />
	
	<script type="text/javascript" src="<?php echo INDIE_FILES_URL ?>js/jquery-1.4.4.min.js"></script>
	<script type="text/javascript" src="<?php echo INDIE_FILES_URL ?>js/jQuery.easing.js"></script>
	<script type="text/javascript" src="<?php echo INDIE_FILES_URL ?>js/jQuery.fancybox.js"></script>
	<script type="text/javascript" src="<?php echo INDIE_FILES_URL ?>js/indiesart.js?v=5"></script>
	<script src="http://widgets.twimg.com/j/2/widget.js"></script>
	
	<style type="text/css" media="screen">
		@import url( <?php bloginfo('stylesheet_url'); ?> );
	</style>
	
	<link media="screen" href="<?php echo INDIE_FILES_URL ?>style/style.css" type="text/css" rel="stylesheet"/>
	<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="http://feeds.feedburner.com/IndiesartBlog" />
	<link rel="alternate" type="text/xml" title="RSS .92" href="<?php bloginfo('rss_url'); ?>" />
	<link rel="alternate" type="application/atom+xml" title="Atom 0.3" href="<?php bloginfo('atom_url'); ?>" />
	
	<link rel="pingback" href="<?php bloginfo('pingback_url'); ?>" />
    <?php wp_get_archives('type=monthly&format=link'); ?>
	<?php //comments_popup_script(); // off by default ?>
	<?php wp_head(); ?>
	
	<!-- BuySellAds.com Ad Code -->
	<script type="text/javascript">
	(function(){
	  var bsa = document.createElement('script');
	     bsa.type = 'text/javascript';
	     bsa.async = true;
	     bsa.src = '//s3.buysellads.com/ac/bsa.js';
	  (document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);
	})();
	</script>
	<!-- End BuySellAds.com Ad Code -->
</head>

<body>
	<div id="wrapper">	
		<div id="main" class="content">
			<div id="header">
				
				<h1><a href="<?php echo INDIE_URL ?>">Indies<span class="colored">art</span><span style="font-size:.7em"> .com</span></a></h1>
				
				<div id="top">
					<div class="desc">Daily illustrations and graphic stuff for alternative art lovers</div>
					<div class="social-media">
						<a target="_blank" href="http://feeds.feedburner.com/IndiesartBlog"><img src="<?php echo INDIE_URL ?>assets/style/images/rss-logo.png" alt="rss"/></a>
						<a target="_blank" href="http://twitter.com/indiesart"><img src="<?php echo INDIE_URL ?>assets/style/images/twitter-logo-2.png" alt="twitter"/></a>
						<a title="Facebook" target="_blank" href="http://www.facebook.com/pages/Indiesart/113879095324838"><img src="<?php echo INDIE_URL ?>assets/style/images/facebook.png" alt="facebook"/></a>
					</div>
				</div>
				<div class="clear"></div>
			</div>
			
			<ul id="menu">
				<li><a href="<?php echo INDIE_URL ?>" title="Home">Home</a></li>
				<li><a class="current" href="<?php bloginfo('url'); ?>">Blog</a></li>
				<li><a href="<?php echo INDIE_URL ?>search">Artists</a></li>
				<li><a id="submission" href="<?php echo INDIE_URL ?>account/submission/list">Submissions!</a></li>
				<li><a href="<?php echo INDIE_URL ?>random">Discover</a></li>
				<li><a href="<?php echo INDIE_URL ?>iphone">iPhone App</a></li>
				<li><a href="mailto:info@indiesart.com">Contact</a></li>	
			</ul>
			
			<div id="content" class="panel-left" style="width:664px">
<?php endif; ?>