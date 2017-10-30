function initMap() {

	var map;

	var info1Marker;
	var info2Marker;
	var event1Marker;
	var event2Marker;

	var infosession1 = new google.maps.LatLng(42.349172, -71.106589);
	var infosession2 = new google.maps.LatLng(42.350080, -71.103776);

	var info1Window = new google.maps.InfoWindow({
		content: "<div class='text-center'><strong>Information Session I, Professional Night</strong><br>PHO 206 (Photonics Center Auditorium)<br><strong>Fashion Night</strong><br>PHO 906 (Photonics Center Colloquium Room)</div>"
	});
	var info2Window = new google.maps.InfoWindow({
		content: "<div class='text-center'><strong>Infomation Session II</strong><br>STO B50 (Stone Science Auditorium)</div>",
	});

	map = new google.maps.Map(document.getElementById('map-canvas'), {
		zoom: 17,
		center: new google.maps.LatLng(42.349626, -71.1051818),
		scrollwheel: false,
	});

	info1Marker = new google.maps.Marker({
		position: infosession1,
		map: map,
		title: 'Information Session I, Professional Night, Fashion Night (PHO)'
	});
	info2Marker = new google.maps.Marker({
		position: infosession2,
		map: map,
		title: 'Information Session II, Professional Night (STO)'
	});
//			event1Marker = new google.maps.Marker({
//				position: event1,
//				map: map,
//				title: 'Fashion Night (COM)'
//			});
//			event2Marker = new google.maps.Marker({
//				position: event2,
//				map: map,
//				title: 'Community Service Event (GSU)'
//			});

	info1Window.open(map,info1Marker);
	info2Window.open(map,info2Marker);
//			event1Window.open(map,event1Marker);
//			event2Window.open(map,event2Marker);

//			map.fitBounds(bounds);

}
