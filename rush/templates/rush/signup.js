function checkform() {
	// get all the inputs within the submitted form
	var inputs = document.getElementById("rushForm").getElementsByTagName('input');
	for (var i = 0; i < inputs.length; i++) {
		// only validate the inputs that have the required attribute
		console.log(inputs[i])
		if(inputs[i].value == "" && inputs[i].name != 'rushMinors'){
			// found an empty field that is required
			return false;
		}
	}
	return true;
}

$("#formSubmit").click(function() {

	if (checkform()) {

		if ($("#rushEmail").val().trim().indexOf("@bu.edu", this.length - "@bu.edu".length) == -1 || $("#rushEmail").val().length > 15) {
			alert("Please use your BU email");
			return;
		}

		$("#rushForm").submit();
	} else {
		alert("Please fill all required fields");
	}


});

$('input').on('keydown', function(e) {
	if (e.which == 13 || e.keyCode == 13) {
		$("#formSubmit").click();
	}
});