var currentKeymap = keymaps[0];
var currentLongText = longtexts[0];

window.onload = function() {
   // 実行したい処理
	var psText = document.querySelector("#dropdownMenuButton1");
	var psItems = document.querySelectorAll("#presetselect #ul1 li a");
 	psItems.forEach((element, index) => {
		console.log(element);
		element.addEventListener("click", () => {
			psText.textContent = element.innerText;
			currentKeymap = keymaps[index];
		});
	});
	var fileYatsu = document.getElementById("formFileSm");
	fileYatsu.addEventListener( "change", (e) => {
		var result = e.target.files[0];
		var reader = new FileReader();
		reader.readAsText(result);
		reader.addEventListener( "load", () => {
			currentKeymap = JSON.parse(reader.result);
		});
	});

	var presetTxt = document.querySelector("#dropdownMenuButton2");
	var textArea = document.getElementById("floatingTextarea2");
	var presetItems = document.querySelectorAll("#presetselect #ul2 li a");
 	presetItems.forEach((element, index) => {
		console.log(element);
		element.addEventListener("click", () => {
			presetTxt.textContent = element.innerText;
			textArea.value = longtexts[index];
			currentLongText = longtexts[index];
		});
	});
	textArea.value = longtexts[0];

	textArea.addEventListener("input", () => {
		//console.log(textArea.value);
		currentLongText = textArea.value;
	});
}


