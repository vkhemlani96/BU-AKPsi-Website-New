var appIndex = 0;
var totalTime = 10 * 60;
var timeLeft = totalTime;
var interval = null;
function moveToNextPart() {
	if (appIndex == 0) {
		
		if (checkBasicDetails()) {

			if ($("#rushEmail").val().trim().indexOf("@bu.edu", this.length - "@bu.edu".length) == -1 || $("#rushEmail").val().length > 15) {
				alert("Please use your BU email");
				return;
			}
			
			appIndex = 1;
			$("#description").addClass("hidden")
			$("#application_start").addClass("hidden")
			$("#application_written").removeClass("hidden")
			window.scrollTo(0,0);
			
			if (!($("#rushEmail").val().toLowerCase() in Rushes)) {
				$.ajax({
					type: "POST",
					url: "signup.php",
					data: {
						rushFirstName: $("#rushFirstName").val(),
						rushLastName: $("#rushLastName").val(),
						rushEmail: $("#rushEmail").val(),
						rushPhone: $("#rushPhone").val(),
						rushMajors: $("#rushMajors").val(),
						rushMinors: $("#rushMinors").val(),
						rushSchool: $("#rushSchool").val(),
						rushGrade: $("#rushGrade").val(),
						rushChannel: 'Application' // various ways to store the ID, you can choose
					},
					success: function(data) {
					  // POST was successful - do something with the response
					},
					error: function(data) {
					  // Server error, e.g. 404, 500, error
					}
				});
			}

		} else {
			if( document.getElementById("rushPic").files.length == 0 ){
				alert("Please include a picture of yourself with your application.");
				return;
			}
			alert("Please fill all required fields/fix invalid fields.");
		}
		
	} else if (appIndex == 1) {
		
		if (!checkTextareas()) {
			alert("Please answer all required questions.");
			return
		}
		
		if (confirm("The following portion of the application has a 10 minute time limit and must be completed in one sitting. Press 'OK' to begin.")) {
			appIndex = 2;
			interval = setInterval(countdownTime, 1000)
			$("#application_written").addClass("hidden")
			$("#application_logic").removeClass("hidden")
			window.scrollTo(0,0);
			
			$.ajax({
					type: "POST",
					url: "startedLogic.php",
					data: {
						email: $("#rushEmail").val(),
					},
					success: function(data) {
					  // POST was successful - do something with the response
					},
					error: function(data) {
					  // Server error, e.g. 404, 500, error
					}
				});
		}
		
	} else if (appIndex == 2) {
		
		clearInterval(interval)
		
		if (confirm("Are you sure you want to submit your application?")) {
			$("input[name=time]").val((totalTime - timeLeft).toString())
			$("#rushForm").submit();
		} else {
			interval = setInterval(countdownTime, 1000)
		}
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
		if(inputs[i].className != "notRequired" && inputs[i].value == "" && inputs[i].name != "q9_second"){
			// found an empty field that is required
			console.log("textarea" + i);
			return false;
		}
	}
	return true
}

var textElement = $("#countdownClock > p")
function countdownTime() {
	timeLeft--;
	if (timeLeft % 60 < 10) {
		textElement.text("Time Left: " + Math.floor(timeLeft / 60) + ":0" + (timeLeft % 60))
	} else {
		textElement.text("Time Left: " + Math.floor(timeLeft / 60) + ":" + (timeLeft % 60))
	}
	if (timeLeft == 0) {
		clearInterval(interval)
		autoSubmit()
	}
}

function autoSubmit() {
	alert("Thank you for applying! Unfortunately time has run out for the logical portion of this test. Your application will now be submitted.")
	$("input[name=time]").val((totalTime - timeLeft).toString())
	$("#rushForm").submit();
}

var Rushes = {};
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
			$("input#rushMinors").val(rushesInfo['Majors']).parent().addClass("is-dirty");
			$("input#rushSchool").val(rushesInfo['MajorSchools']).parent().addClass("is-dirty");
			$("input#rushGrade").val(rushesInfo['Grade']).parent().addClass("is-dirty");
			console.log(rushesInfo['AppSubmitted'])
			
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