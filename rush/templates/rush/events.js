function checkform() {
	// get all the inputs within the submitted form
	var inputs = document.getElementById("rushForm").getElementsByTagName('input');
	for (var i = 0; i < inputs.length; i++) {
		// only validate the inputs that have the required attribute
		if(inputs[i].value == ""){
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

var Rushes = {
};
function replaceAll(str, find, replace) {
    return str.replace(new RegExp(find, 'g'), replace);
}

var rushInfo;
{% for rush in rushes %}
	rushInfo = {
		'FirstName': "{{rush.first_name}}",
		'LastName': "{{rush.last_name}}",
		'Email': "{{rush.email|lower}}",
		'Phone': "{{rush.phone_number}}",
		'Majors': "{{rush.majors}}",
		'Minors': "{{rush.minors}}",
		'MajorSchools': eval(replaceAll("{{rush.major_schools}}","&#39;", "'")),
		'Grade': "{{rush.grade}}"
	};
	Rushes["{{rush.email|lower}}@bu.edu"] = rushInfo;
{% endfor %}


var lastChar = -1;

$('input#rushEmail').on('keyup', function(e) {
	lastChar = e.which;
	if (lastChar == 50) {
		var email = $(this).val() + "bu.edu";
		
		$(this).val(email);
		
		console.log($(this).val().toLowerCase() in Rushes)
		if ($(this).val().toLowerCase() in Rushes) {

			var rushesInfo = Rushes[email];
			$("input#rushFirstName").val(rushesInfo['FirstName']).parent().addClass("is-dirty");
			$("input#rushLastName").val(rushesInfo['LastName']).parent().addClass("is-dirty");
			$("input#rushPhone").val(rushesInfo['Phone']).parent().addClass("is-dirty");
			$("input#rushMajors").val(rushesInfo['Majors']).parent().addClass("is-dirty");
			$("input#rushMinors").val(rushesInfo['Minors']).parent().addClass("is-dirty");
			$("input#rushGrade").val(rushesInfo['Grade']).parent().addClass("is-dirty");

			$(".rush_grade .mdl-js-radio input[value='" + rushesInfo['Grade'] + "']").parent()[0].MaterialRadio.check();

			var schools = rushesInfo['MajorSchools'];
			for (var i = 0; i < schools.length; i++) {
				console.log($(".rush_schools input[value='" + schools[i] + "']"));
				$(".rush_schools .mdl-js-checkbox input[value='" + schools[i] + "']").parent()[0].MaterialCheckbox.check();
			}
		} else {
			$("input#rushFirstName").focus();
		}

	}
	
	
});