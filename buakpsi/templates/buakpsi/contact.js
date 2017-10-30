function validateForm() {
	if (confirm("Are you sure you want to send this message?")) {
		return true;
	} else {
		return false;	
	}
}