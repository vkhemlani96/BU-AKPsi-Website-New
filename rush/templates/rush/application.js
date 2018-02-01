var appIndex = 0;
var totalTime = 10 * 60;
var timeLeft = totalTime;
var interval = null;
function moveToNextPart() {
	if (!checkBasicDetails()) {
		if( document.getElementById("rushPic").files.length == 0 ){
			alert("Please include a picture of yourself with your application.");
			return;
		}
		if( document.getElementById("rushResume").files.length == 0 ){
			alert("Please include your resume with your application.");
			return;
		}
		alert("Please fill all required fields/fix invalid fields.");
		return;

		if ($("#rushEmail").val().trim().indexOf("@bu.edu", this.length - "@bu.edu".length) == -1 || $("#rushEmail").val().length > 15) {
			alert("Please use your BU email");
		}
		return;
	}
		
	if (!checkTextareas()) {
		alert("Please answer all required questions.");
		return
	}
	
	if (confirm("Are you sure you want to submit your application?")) {
		$("#rushForm").submit();
	}
}

function checkBasicDetails() {
	// get all the inputs within the submitted form
	var inputs = document.getElementById("rushForm").getElementsByTagName('input');
	for (var i = 0; i < inputs.length; i++) {
		// only validate the inputs that have the required attribute
		if(inputs[i].name.indexOf("rush") > -1 && inputs[i].name != "rushMinors" && (inputs[i].value == "" || !inputs[i].validity.valid)){
			console.log(inputs[i].name)
			// found an empty field that is required
			return false;
		}
	}
	return true;
}

function checkTextareas() {
	var inputs = document.getElementById("rushForm").getElementsByTagName('textarea');
	for (var i = 0; i < inputs.length; i++) {
		// only validate the inputs that have the required attribute
		if(inputs[i].className != "notRequired" && inputs[i].value == ""){
			// found an empty field that is required
			return false;
		}
	}
	return true
}

var Rushes = {};
function replaceAll(str, find, replace) {
    return str.replace(new RegExp(find, 'g'), replace);
}

var rushInfo;
{% for rush in rushes %}
	rushInfo = {
		'ApplicationStarted': "{{rush.application_started}}",
		'FirstName': "{{rush.first_name}}",
		'LastName': "{{rush.last_name}}",
		'Email': "{{rush.email|lower}}",
		'Phone': "{{rush.phone_number}}",
		'Majors': "{{rush.majors}}",
		'Minors': "{{rush.minors}}",
		'MajorSchools': eval(replaceAll("{{rush.major_schools}}","u?&#39;", "'")),
		'Grade': "{{rush.grade}}"
	};
	Rushes["{{rush.email|lower}}@bu.edu"] = rushInfo;
{% endfor %}

$('input#rushEmail').on('keyup', function(e) {
	lastChar = e.which;
	if (lastChar == 50) {
		var email = $(this).val() + "bu.edu";

		$(this).val(email);

		if ($(this).val().toLowerCase() in Rushes) {

			var rushesInfo = Rushes[email];
			$("input#rushFirstName").val(rushesInfo['FirstName']).parent().addClass("is-dirty");
			$("input#rushLastName").val(rushesInfo['LastName']).parent().addClass("is-dirty");
			$("input#rushPhone").val(rushesInfo['Phone']).parent().addClass("is-dirty");
			$("input#rushMajors").val(rushesInfo['Majors']).parent().addClass("is-dirty");
			$("input#rushMinors").val(rushesInfo['Minors']).parent().addClass("is-dirty");
			$("input#rushSchool").val(rushesInfo['MajorSchools']).parent().addClass("is-dirty");
			$("input#rushGrade").val(rushesInfo['Grade']).parent().addClass("is-dirty");
			$(".rush_grade .mdl-js-radio input[value='" + rushesInfo['Grade'] + "']").parent()[0].MaterialRadio.check();

			var schools = rushesInfo['MajorSchools'];
			for (var i = 0; i < schools.length; i++) {
				console.log($(".rush_schools input[value='" + schools[i] + "']"));
				$(".rush_schools .mdl-js-checkbox input[value='" + schools[i] + "']").parent()[0].MaterialCheckbox.check();
			}
			
			if (rushesInfo['AppSubmitted'] === "1") {
				setTimeout(function() {
					alert("Our records indicate that you've already submitted your application. If you need to make changes or believe there is an error, please email akpsi.nu.recruitment@gmail.com.")
					$("#beginApp").prop("disabled",true);
					return;
				}, 200)
			} else if (rushesInfo['StartedLogic'] === "1") {
				setTimeout(function() {
					alert("Our records indicate that you've already started this application once. If you need to make changes or believe there is an error, please email akpsi.nu.recruitment@gmail.com.")
					$("#beginApp").prop("disabled",true);
					return;
				}, 200)
			}
			
			$("input#rushAddress").focus();
		} else {
			$("input#rushFirstName").focus();
		}

		//					if ($(this).val().indexOf("@bu.edu") > 0) {
		//						$(this).val($(this).val().substring(0,$(this).val().indexOf("@bu.edu")+7));
		//					}
	}
});

$("textarea").focus(function() {
	$( this ).prev().css( "color", "#000033" );
});
$("#rushPic").focus(function() {
	$( this ).prev().css( "color", "#000033" );
});