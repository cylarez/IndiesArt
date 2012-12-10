<?php
// If a sidebar.php file exists in the WP root directory we
// use that, otherwise use this default wp-sidebar.php file.
if ( file_exists(ABSPATH . '/sidebar.php') ) :
	include_once(ABSPATH . '/sidebar.php');
else :
?>

<div id="sidebar" style="width:280px;">
	<div id="nav">

				
		<form id="searchform" method="get" action="<?php echo $PHP_SELF; ?>">

			<label for="s"><?php _e('Search:'); ?></label>	
			<input type="text" name="s" id="s" accesskey="4" />
			<input type="submit" name="submit" value="<?php _e('Search'); ?>" />

		</form>

				
		<div id="cats">
			<h2 id="nav-head"><?php _e('Navigate'); ?></h2>
			<ul>
				<?php wp_list_cats(); ?>
			</ul>
		</div>
		 
		<h2>Archives</h2>
		<ul>
		<?php wp_get_archives('type=monthly'); ?>
		</ul>
		
		<?php include ('./../templates/ads.html') ?>
		
		<h2>Links</h2>

		<?php wp_list_bookmarks('title_after=&title_before='); ?>


		<div id="meta">
			<h2 id="nav-other"><?php _e('Other'); ?></h2>
			<ul>
				<?php wp_register(); ?>
				<li><?php wp_loginout(); ?></li>
				<li><a href="<?php bloginfo('atom_url'); ?>" title="<?php _e('Syndicate this site using Atom'); ?>"><?php _e('Atom feed'); ?></a></li>
				<li><a href="<?php bloginfo('rss2_url'); ?>" title="<?php _e('Syndicate this site using RSS'); ?>"><?php _e('<abbr title="Really Simple Syndication">RSS</abbr> feed'); ?></a></li>
				<li><a href="<?php bloginfo('comments_rss2_url'); ?>" title="<?php _e('The latest comments to all posts in RSS'); ?>"><?php _e('Comments <abbr title="Really Simple Syndication">RSS</abbr> feed'); ?></a></li>
				<?php wp_meta(); ?>
			</ul>
		</div>
		
		<br /><br />
		
		<!-- BuySellAds.com Zone Code -->
		<div id="bsap_1256998" class="bsarocks bsap_fb81e1d174a96c1de689e094a6997158"></div>
		<!-- End BuySellAds.com Zone Code -->
		 <div class="clear"></div>
		
		<div>
			
			<h2>Facebook Network</h2>

			<iframe src="http://www.facebook.com/plugins/likebox.php?profile_id=113879095324838&amp;width=250&amp;colorscheme=light&amp;connections=12&amp;stream=false&amp;header=true&amp;height=360" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:292px; height:360px;" allowTransparency="true"></iframe>
			<br /><br />
			
			<iframe src="http://www.facebook.com/plugins/recommendations.php?site=blog.indiesart.com&amp;width=250&amp;height=500&amp;header=true&amp;colorscheme=light&amp;border_color=%23E0E0E0" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:250px; height:500px;" allowTransparency="true"></iframe>
			
			<form action="https://www.paypal.com/cgi-bin/webscr" method="post" style="text-align:center;margin: 20px;">
				<input type="hidden" name="cmd" value="_s-xclick">
				<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----">
				<input type="image" src="<?php echo INDIE_URL ?>assets/style/images/beer.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
				<img alt="" border="0" src="https://www.paypal.com/fr_FR/i/scr/pixel.gif" width="1" height="1">
			</form>
			
			<script>
			new TWTR.Widget({
			  version: 2,
			  type: 'search',
			  search: 'indiesart',
			  interval: 3000,
			  subject: 'Twitter',
			  width: 'auto',
			  height: 300,
			  theme: {
			    shell: {
			      background: '#E0E0E0',
			      color: '#000000'
			    },
			    tweets: {
			      background: '#ffffff',
			      color: 'grey',
			      links: 'black'
			    }
			  },
			  features: {
			    scrollbar: false,
			    loop: true,
			    live: true,
			    hashtags: true,
			    timestamp: true,
			    avatars: true,
			    toptweets: true,
			    behavior: 'default'
			  }
			}).render().start();
			</script>

			
		</div>
	</div>
	
</div>

<div class="clear"></div>
<?php endif; ?>