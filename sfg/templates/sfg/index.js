//Counter to go throw array containing image links
var imgCellIndex = 1;
//Array of arrays that contain imgs to display in each cell
var imgCell = [ [
"citigroup",
"kbcm",
],[
"ubs",
"citigroup",
],[
"santander",
"kbcm",
]];

function changeImgCell(index) {
	$(".imgCell" + index).fadeOut(function() {
		$(this).attr("src", "/static/sfg/img/placements/" + imgCell[index][imgCellIndex] + "_cropped.png");
	}).fadeIn();
	if (index == 0) {
		imgCellIndex = (imgCellIndex + 1) % 2;	
	}
}

setInterval(function() {
	//Changes Middle Cell
	changeImgCell(1);
	setTimeout(function() {
		//Changes Right Cell after delay
		changeImgCell(2)
	}, 1000);
	setTimeout(function() {
		//Changes Left Cell after delay
		changeImgCell(0)
	}, 2000);
}, 3000);

setTimeout(function() {
	$(".dropdown").each(function(index){
		$(this).css("left", "0");

		var parent = $(this).parent();
		var parentLeft = parent.offset().left;
		var parentRight = parentLeft + parent.outerWidth();
		var parentCenter = (parentLeft + parentRight)/2;
		var newOffset = $(this).offset();

		newOffset.top = 0;
		newOffset.left = parentCenter - $(this).outerWidth()/2;
		$(this).offset(newOffset);
		//		$(this).left("1000px");
	});
}, 100);