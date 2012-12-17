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

			<iframe src="http://www.facebook.com/plugins/likebox.php?profile_id=113879095324838&amp;width=250&amp;colorscheme=light&amp;connections=12&amp;stream=false&amp;header=true&amp;height=360" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:270px; height:360px;" allowTransparency="true"></iframe>
			<br /><br />
			
			<iframe src="http://www.facebook.com/plugins/recommendations.php?site=blog.indiesart.com&amp;width=250&amp;height=500&amp;header=true&amp;colorscheme=light&amp;border_color=%23E0E0E0" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:270px; height:500px;" allowTransparency="true"></iframe>

			<br/><br/>

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