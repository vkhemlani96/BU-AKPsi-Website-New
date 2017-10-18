$(".brother_img").hover(function(event) {
	$(this).children("div").animate({
		top: 0
	},300);
	$(this).find(".gold_seperator").css({
		display: "block"	
	});
}, function(event) {
	$(this).children("div").animate({
		top: "204px"
	},300);
	$(this).find(".gold_seperator").css({
		display: "non"	
	});
});

$(function() {
	$("img.lazy").lazyload({
		effect : "fadeIn"
	});
});