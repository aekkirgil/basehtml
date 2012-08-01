$(function(){
    $("#slides").slides({
    	next: 'next',
    	prev: 'prev',
    	play: 5000,
    	pause: 2500,
    	
    });
    
});

$(document).ready(function(){
	$('.tarife-ui').click(function(){
		$('.sip-tar').fadeOut('fast');	
		$('.tar-main').fadeIn('fast');
	});
	$('.siparis-ui').click(function(){
		$('.tar-main').fadeOut('fast');	
		$('.sip-tar').fadeIn('fast');
	});
});

$(document).ready(function(){
	if($('.sip-window').length) {
		var maxHeight = 0;
		$('.sip-window').each(function(){
			currentHeight=$(this).height();
			//console.log(currentHeight);
			if (currentHeight > maxHeight){
				maxHeight = currentHeight;
			}
		});
		$('.sip-window').height(maxHeight);
	}
});

YUI().use('transition', 'node', 'slider', function (Y) {
    
	Y.all(".menu-item").on("click", function(e) {
		e.halt();
		var node = e.target.get("tagName") == "A" ? e.target.get("parentNode") : e.target;
		this.each(function(item) {
			item.one("a").setStyle("color", "#000");
		});
		Y.one(".bg-orange").transition({
			duration: 0.40,
			left: node.getStyle("left")
		});
		node.one("a").transition({
			color: '#fff'
		});
	});
	
	
});


	$(function() {
		$( "#slider-range-min" ).slider({
			range: "min",
			value: 100,
			min: 100,
			max: 700,
			slide: function( event, ui ) {
				$( "#amount" ).val( "$" + ui.value );
			}
		});
		$( "#amount" ).val( "$" + $( "#slider-range-min" ).slider( "value" ) );
	});

