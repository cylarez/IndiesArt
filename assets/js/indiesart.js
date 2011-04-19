$(document).ready(function() {
	fancyGroup();
	//launchMeebo();
	//Meebo("domReady");

	
	// Menu
	$('#menu a').each(function() {
		var href 	=	$(this).attr('href').substr(0, 14);
		var url		=	window.location.pathname.substr(0, 14);
		
		if (href == url) {
			$(this).addClass('current');
		}
	});
	
	var h = 170;

	$('.thumbs-medium').mouseleave(function() {
		$(this).find('.image-frame').animate({height:"-="+ h, bottom:"-="+ h})
	}).mouseenter(function() {
		$(this).find('.image-frame').animate({height:"+="+ h, bottom:"+="+ h})
	});
	
	$('.thumbs-medium .opener').click(function() {
		document.location = $(this).attr('id');
	});
	
/*
	$('.thumbs-classy').click(function() {
		console.log('test')
		$(this).find('.thumbs-href').click();
	});
*/

});

function fancyGroup() 
{
	completeBox	=	function(t, num)
	{
		FB.XFBML.parse();
	}
	
	$('.fancybox').fancybox({
		'zoomSpeedIn' : 600,
		'zoomSpeedOut' : 500,
		'transitionIn' : 'elastic',
		'transitionOut' : 'elastic',
		'hideOnContentClick': false,
		'onComplete':completeBox,
		'titlePosition': 'over'
		
	});
}

function launchMeebo()
{
	if (typeof Meebo == 'undefined') {
		Meebo=function(){(Meebo._=Meebo._||[]).push(arguments)};
		(function(q){
		var d=document,b=d.body;
		if(!b){var cb=arguments.callee;return setTimeout(function(){cb(q)},100);}
		var m=b.insertBefore(d.createElement('div'), b.firstChild), s=d.createElement('script');
		m.id='meebo'; m.style.display='none'; m.innerHTML='<iframe id="meebo-iframe" frameBorder="0" ></iframe>';
		s.src='http'+(q.https?'s':'')+'://'+(q.stage?'stage-':'')+'cim.meebo.com/cim/cim.php?network='+q.network;
		d.getElementsByTagName('head')[0].appendChild(s);
		})({network: 'indiesart_fu82nu', stage: false});
		Meebo('makeEverythingSharable', {minImageWidth:250});
	}
}

function log(s) 
{
	if (typeof console != "undefined" && typeof console.debug != "undefined") {
		console.log(s);
	}
}