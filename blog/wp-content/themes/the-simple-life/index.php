<?php 
/* Don't remove this line. */


require('./wp-blog-header.php');
include('header.php');
?>

<?php if (have_posts()) : while (have_posts()) : the_post(); ?>

<div class="post">

	<div class="left number colored">.<?php the_ID(); ?> |</div>
	
	<div class="left head-title">
		<h2 class="title" id="post-<?php the_ID(); ?>"><a href="<?php the_permalink() ?>" rel="bookmark"><?php the_title(); ?></a></h2>
		<div class="meta"><p>posted on <?php the_date()?> in <?php the_category(',') ?> <?php edit_post_link(__('Edit This')); ?></p></div>	
	</div>
	
	<div class="clear storycontent">
	
		<div style="float:left;padding-left:10px;height:150px;width:75px;">
			
			<div style="padding-bottom:10px">
				<?php if (function_exists('tweetmeme')) echo tweetmeme(); ?>
			</div>
			
			<div style="padding-bottom:10px">
				<?php 
				//if (function_exists('fbmeme')) echo fbmeme(); 
				if (function_exists('facebook_sharecount')) echo facebook_sharecount();
				// if (function_exists('fbshare_manual')) echo fbshare_manual();
				?>
			</div>
			
		</div>
			
		<?php the_content(__('(more...)')); ?>
		
		<br />
	</div>
	
	
	<p class="postmetadata"><?php the_tags('Tags: ', ', ', '<br />'); ?></p>
	<div class="feedback">
            <?php wp_link_pages(); ?>
            <p><?php comments_popup_link(__('Comments (0)'), __('Comments (1)'), __('Comments (%)'), '', ''); ?></p>
	</div>
	
	<!--
	<?php trackback_rdf(); ?>
	-->

</div>

<?php comments_template(); // Get wp-comments.php template ?>

<?php endwhile; else: ?>
<p><?php _e('Sorry, no posts matched your criteria.'); ?></p>
<?php endif; ?>

<?php posts_nav_link(' — ', __('&laquo; Previous'), __('Next &raquo;')); ?>

<?php include('footer.php'); ?>