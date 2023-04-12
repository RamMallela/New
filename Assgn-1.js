const apartments = {
	building1: ["101", "102", "103" ,"104", "105", "106", "107", "108", "109", "110"],
	building2: ["201", "202", "203" ,"204", "205", "206", "207", "208", "209", "210"],
	building3: ["301", "302", "303" ,"304", "305", "306", "307", "308", "309", "310"],
	building4: ["401", "402", "403" ,"404", "405", "406", "407", "408", "409", "410"],
	building5: ["501", "502", "503" ,"504", "505", "506", "507", "508", "509", "510"],
};

function getApartments() {
	const buildingSelect = document.getElementById("buildings");
	const apartmentSelect = document.getElementById("apartments");
	const selectedBuilding = buildingSelect.value;

	apartmentSelect.innerHTML = '<option value="">--Select Apartment--</option>';

	if (selectedBuilding) {
		apartmentSelect.disabled = false;
		for (let i = 0; i < apartments[selectedBuilding].length; i++) {
			const option = document.createElement("option");
			option.text = apartments[selectedBuilding][i];
			apartmentSelect.add(option);
		}
	}
	else {
		apartmentSelect.disabled = true;
		apartmentSelect.innerHTML = '<option value="">--Select Apartment--</option>';
	}
}

function getApartmentDetails() {
	const apartmentSelect = document.getElementById("apartments");
	const selectedApartment = apartmentSelect.value;
	const apartmentDetailsDiv = document.getElementById("apartmentDetails");

	if (selectedApartment === building1) {
		 apartmentDetailsDiv.innerHTML = `Apartment ${selectedApartment} is a 2-bhk apartment and has a view of the park.`;
	}
	else if (selectedApartment === building2){
	     apartmentDetailsDiv.innerHTML = `Apartment ${selectedApartment} is a 3-bhk apartment with a balcony.`;
	}
	else if(selectedApartment === building3){
		 apartmentDetailsDiv.innerHTML = `Apartment ${selectedApartment} is a 2-bhk apartment with a balcony and a view of the park.`;
	}
	else if(selectedApartment === building4){
		 apartmentDetailsDiv.innerHTML = `Apartment ${selectedApartment} is a 3-bhk apartment with a balcony and a view of the park.`;
	}
	else if(selectedApartment === building5){
		 apartmentDetailsDiv.innerHTML = `Apartment ${selectedApartment} is a 4-bhk apartment with 2 balconies.`;
	}
	else(selectedApartment) =>
		apartmentDetailsDiv.innerHTML = "";
	
}
