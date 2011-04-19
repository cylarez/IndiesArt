<?php
/*
Plugin Name: Sharecount for Facebook
Plugin URI: http://widgets.fbshare.me/plugins/wordpress/sharecount
Description: The Sharecount plugin for Facebook shows the number of shares on Facebook your posts get and allows users to share it themselves. This plugin is based on the <a href="http://www.backtype.com/plugins/tweetcount">Backtype Tweetcount</a> plugin.
Version: 0.9.2
Author: FBShare.Me
Author URI: http://www.fbshare.me/
*/

/*  Copyright 2009  Snowball Factory, Inc  (email : info@snowballfactory.com)

	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 2 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/


if (is_admin()) {
	add_action('admin_menu', 'fbsc_options');
	add_action('admin_init', 'fbsc_init');
	register_activation_hook(__FILE__, 'fbsc_activate');
}

add_filter('the_content', 'fbsc_update');
add_filter('get_the_excerpt', 'fbsc_remove_filter', 9);

function fbsc_options() {
	add_options_page('FB Sharecount Settings', 'Sharecount for Facebook', 8, 'facebook-sharecount', 'fbsc_options_page');
}

// Register these variables (WP 2.7 & newer)
function fbsc_init() {
	if (function_exists('register_setting')) {
		register_setting('fbsc-options', 'fbsc_size');
		register_setting('fbsc-options', 'fbsc_location');
		register_setting('fbsc-options', 'fbsc_style');
		register_setting('fbsc-options', 'fbsc_api_key');
		register_setting('fbsc-options', 'fbsc_google_analytics');
		register_setting('fbsc-options', 'fbsc_badge_text');
		register_setting('fbsc-options', 'fbsc_badge_color');
		register_setting('fbsc-options', 'fbsc_pages');
	}
}

// default options
function fbsc_activate() {
	add_option('fbsc_size', 'large');
	add_option('fbsc_location', 'top');
	add_option('fbsc_style', 'float:left;margin-right:10px;');
	add_option('fbsc_api_key', '');
	add_option('fbsc_google_analytics', '');
	add_option('fbsc_badge_text', '');
	add_option('fbsc_badge_color', '');
	add_option('fbsc_pages', 'true');
}

function fbsc_update($content) {
	global $post;
	
	if (get_option('fbsc_location') == 'manual') {
		return $content;
	}
	
	if (is_feed()) {
		return $content;
	}
	
	if (is_page() and (get_option('fbsc_pages') != 'true')) {
		return $content;
	}
	
	if (get_post_meta($post->ID, 'fbsc', true) == '') {
		$button = facebook_sharecount();
		switch (get_option('fbsc_location')) {
			case 'topbottom':
				return $button . $content . $button;
			break;
			case 'top':
				return $button . $content;
			break;
			case 'bottom':
				return $content . $button;
			break;
			default:
				return $button . $content;
			break;
		}
	} else {
		return $content;
	}
}

function fbsc_remove_filter($content) {
	remove_action('the_content', 'fbsc_update');
	return $content;
}

function fbsc_options_page() {
	echo '<div class="wrap">';
	if (function_exists('screen_icon')) { screen_icon(); }
	echo'<h2>Sharecount for Facebook</h2>';
	echo '<form method="post" action="options.php">';
	wp_nonce_field('update-options');
	echo '<table class="form-table">';
	echo '<tr valign="top"><th scope="row">Size</th><td><select name="fbsc_size"><option value="">large</option><option value="small"' . ((get_option('fbsc_size')=='small')?' selected':'') . '>small</option></select></td></tr>';
	echo '<tr valign="top"><th scope="row">Location</th><td><select name="fbsc_location"><option value="top">top</option><option value="bottom"' . ((get_option('fbsc_location')=='bottom')?' selected':'') . '>bottom</option><option value="topbottom"' . ((get_option('fbsc_location')=='topbottom')?' selected':'') . '>top &amp; bottom</option><option value="manual"' . ((get_option('fbsc_location')=='manual')?' selected':'') . '>manual</option></select> <span class="setting-description">For manual positioning, echo facebook_sharecount(); where you would like the button to appear</span></td></tr>';
	echo '<tr valign="top"><th scope="row">Wrapper Style</th><td><input type="text" name="fbsc_style" value="' . get_option('fbsc_style') . '" /> <span class="setting-description">CSS for positioning, margins, etc</span></td></tr>';
	echo '<tr valign="top"><th scope="row">Badge Color</th><td><input type="text" name="fbsc_badge_color" value="' . get_option('fbsc_badge_color') . '" /> <span class="setting-description">Color of the badge background in large button (use <a href="http://www.w3schools.com/CSS/css_colors.asp">standard CSS RGB hex codes</a>, *do not* include a leading #)</span></td></tr>';
	echo '<tr valign="top"><th scope="row">Badge Text</th><td><input type="text" name="fbsc_badge_text" value="' . get_option('fbsc_badge_text') . '" /> <span class="setting-description">Color of the badge text in large button (use <a href="http://www.w3schools.com/CSS/css_colors.asp">standard CSS RGB hex codes</a>, *do not* include a leading #)</span></td></tr>';
	echo '<tr valign="top"><th scope="row">Show Button on Pages</th><td><input type="checkbox" value="true" name="fbsc_pages"' . ((get_option('fbsc_pages')=='true')?' checked':'true') . ' /> <span class="setting-description">Show the button on Pages as well as Posts</span></td></tr>';
	echo '</table><p>The button will generate fbshare.me links by default unless you have an <a href="http://awe.sm">awe.sm</a> account</p><table class="form-table">';
	echo '<tr valign="top"><th scope="row">awe.sm API Key</th><td><input type="text" name="fbsc_api_key" value="' . get_option('fbsc_api_key') . '" /> <span class="setting-description">Optional: will use your <a href="http://awe.sm">awe.sm</a> account settings if specified</span></td></tr>';
	echo '<tr valign="top"><th scope="row">Google Analytics Parameters</th><td><input type="checkbox" value="true" name="fbsc_google_analytics"' . ((get_option('fbsc_google_analytics')=='true')?' checked':'true') . ' /> <span class="setting-description">Adds <a href="http://www.google.com/support/googleanalytics/bin/answer.py?answer=55518" target="_blank">Google Analytics parameters</a> to fbshare.me links (if no awe.sm API Key specified)</span></td></tr>';
	echo '</table>';
	echo '<input type="hidden" name="action" value="update" /><input type="hidden" name="page_options" value="fbsc_size,fbsc_location,fbsc_style,fbsc_api_key,fbsc_google_analytics,fbsc_badge_color,fbsc_badge_text,fbsc_pages" /><p class="submit"><input type="submit" class="button-primary" value="Save Changes" /></p></form></div>';
}

function facebook_sharecount($size=null, $style=null, $api_key=null, $google_analytics=null, $badge_color=null, $badge_text=null) {
	global $post;
	$url = '';
	$cnt = null;
	
	// let users override these vars when calling manually
	$size = ($size === null) ? get_option('fbsc_size') : $size;
	$style = ($style === null) ? get_option('fbsc_style') : $style;
	$api_key = ($api_key === null) ? get_option('fbsc_api_key') : $api_key;
	$google_analytics = ($google_analytics === null) ? get_option('fbsc_google_analytics') : $google_analytics;
	$badge_color = ($badge_color === null) ? get_option('fbsc_badge_color') : $badge_color;
	$badge_text = ($badge_text === null) ? get_option('fbsc_badge_text') : $badge_text;
	
	if (get_post_status($post->ID) == 'publish') {
		$url = get_permalink();
		$title = $post->post_title;
		
		if ((function_exists('curl_init') || function_exists('file_get_contents')) && function_exists('unserialize')) {
			$meta = get_post_meta($post->ID, 'fbsc_cache', true);
			if ($meta != '') {
				$pieces = explode(':', $meta);
				$timestamp = (int)$pieces[0];
				$cnt = (int)$pieces[1];
			}
			

		}
	}


	if ($style !== '') {
		$button = '<div style="' . $style . '">';
	} else {
		$button = '';
	}

	if ($size == 'small') {
		$button .= 	'<iframe height="18" width="81" src="http://widgets.fbshare.me/files/fbshare.php?';
	} else {
		$button .= 	'<iframe height="69" width="53" src="http://widgets.fbshare.me/files/fbshare.php?';	
	}
	
	$button .= 'url=' . $url . '&title=' . wp_specialchars($title, '1');
	 			
	if ($size !== '') {
		$button .= '&size=' . wp_specialchars($size, '1');
	} else {
		$button .= '&size=large';
	}
	if ($google_analytics !== '') {
		$button .= '&google_analytics=' . wp_specialchars($google_analytics, '1');
	}
	if ($api_key !== '') {
		$button .= '&awesm_api_key=' . wp_specialchars($api_key, '1');
	}
	if ($badge_color !== '') {
		$button .= '&badge_color=' . wp_specialchars($badge_color, '1');
	}
	if ($badge_text !== '') {
		$button .= '&badge_text=' . wp_specialchars($badge_text, '1');
	}
	$button .= '" frameborder="0" scrolling="no" allowtransparency="true"></iframe>';

	
	if ($style !== '') {
		$button .= '</div>';
	}
			 
	return $button;
}



function fbsc_urlopen($url) {
	if (function_exists('curl_init')) {
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt ($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_HEADER, false);
		$result = curl_exec($ch);
		curl_close($ch);
		return $result;
	} else {
		return file_get_contents($url);
	}
}

?>
