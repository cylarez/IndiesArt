<?php 
/* Don't remove this line. */
require('./wp-blog-header.php');
include('header.php');

?>

<?php if (have_posts()) : while (have_posts()) : the_post(); ?>
<div class="post">
	 <h1 id="post-<?php the_ID(); ?>"><a href="<?php the_permalink() ?>" rel="bookmark"><?php the_title(); ?></a></h1>
	
	<div class="post-content">
		<?php the_content(__('(more...)')); ?>
	</div>
	
	<!--
	<?php trackback_rdf(); ?>
	-->

</div>
<?php endwhile; else: ?>
<p><?php _e('Sorry, no posts matched your criteria.'); ?></p>
<?php endif; ?>

<?php posts_nav_link(' &#8212; ', __('&laquo; Previous'), __('Next &raquo;')); ?>

<?php include('footer.php'); ?>