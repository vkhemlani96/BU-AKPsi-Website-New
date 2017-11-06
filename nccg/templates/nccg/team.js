$(".brother_img > div").each(function(index) {
	$(this).css({
		top: "204px"
	});
});

$(".brother_img").hover(function(event) {
	$(this).children("div").animate({
		top: 0
	},300);
}, function(event) {
	$(this).children("div").animate({
		top: "204px"
	},300);
});

$(function() {
	$("img.lazy").lazyload({
		effect : "fadeIn"
	});
});