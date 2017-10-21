



var lowestYear = {{ "hello" }};
var highestYear = {{ total_alumni }};

console.log(lowestYear, highestYear);

$(".alumni_table h3").on("click",function() {
	var year = $(this).data("year");

	console.log(year);

	if (year == undefined) {
		return;	
	}


	var currentYear = $(".selected").data("year");
	console.log(currentYear);

	$(".hidden_left").each(function(index) {
		if (index >= year - lowestYear)
			$(this).animate({
				width: "68px"
			});
		else 
			$(this).animate({
				width: 0
			});
	});
	$(".hidden_right").each(function(index) {
		if (index < (year-lowestYear + 1))
			$(this).animate({
				width: "68px"
			});
		else
			$(this).animate({
				width: 0
			});
	});

	$(".selected").text(currentYear).removeClass("selected");
	$(this).addClass("selected").text("Class of " + year);

	if (year != currentYear) {
		var currentCell = $(".visible_cell");
		currentCell.removeClass("visible_cell").fadeOut();
		$("#year"+year).addClass("visible_cell").fadeIn();
	}
});

function commaSeparateNumber(val){
	while (/(\d+)(\d{3})/.test(val.toString())){
		val = val.toString().replace(/(\d+)(\d{3})/, '$1'+','+'$2');
	}
	return val;
}

var chapterAlumni = {{ total_alumni }};
var alumniWorldwide = 260000;
var alumniChapters = 43;
var duration = 1;

var options = {useEasing : true, useGrouping : true, separator : ',', decimal : '.', prefix : '', suffix : '' };
setTimeout(function() {
	new CountUp("chapterAlumni", 0, chapterAlumni, 0, duration, options).start();
	new CountUp("alumniWorldwide", 0, alumniWorldwide, 0, duration, options).start();
	new CountUp("alumniChapters", 0, alumniChapters, 0, duration, options).start();
}, 250);

(function scroll(){
	$(".alumni_scroll").animate({
		left: "-4229px"
	}, 25000, "linear", function() {
		$(".alumni_scroll").css("left","100%");
		scroll();
	});
})();