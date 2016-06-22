$(document).ready(function() {
	$('.col-sm-1').mouseenter(function() {
		$(this).fadeTo("fast", 1);
	});
});
$(document).ready(function() {
	$('.col-sm-1').mouseleave(function() {
		$(this).fadeTo("fast", 0.5);
	});
});


