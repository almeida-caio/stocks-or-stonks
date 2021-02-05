let counter = 0;
let countMax = 10;

let user_answered = true;
let score = 0;

document.addEventListener('DOMContentLoaded', function() {
	document.getElementById("forward_button").innerHTML = "<button class='keyButton button2' onclick='changeImage()'> NEW GAME </button>";
}, false);

function changeImage() {
	if (counter < countMax && user_answered) {
		document.getElementById("response_string").innerHTML = "";
		document.getElementById("forward_button").innerHTML = "";
		document.getElementById("generateButtons").innerHTML = "<button class='button button1' onclick='answerStock()'>STOCKS</button> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <button class='button button1' onclick='answerRandom()'>RANDOM</button>";
		user_answered = false;
		counter++;
		console.log(counter);

		first_coin = Math.round(Math.random())
		second_coin = Math.floor(1000 * Math.random())

		plot_name = first_coin.toString() + "-" + second_coin.toString() + ".png";
		
		if (first_coin == 1) {
			stock_ticker = metadata_variable[0][plot_name].ticker;
			start_date = metadata_variable[0][plot_name].start;
			end_date = metadata_variable[0][plot_name].end;
		}

		document.getElementById("file_name").innerHTML = "<img src=" + "'image-bank/" + plot_name + "'>";
	} else if (counter == countMax) {
		document.getElementById("response_string").innerHTML = "";
		document.getElementById("score_string").innerHTML = "Score: " + score.toString() + " out of " + countMax.toString();
		document.getElementById("forward_button").innerHTML = "";
		document.getElementById("file_name").innerHTML = "";
		document.getElementById("newer_game_button").innerHTML = "<button class='keyButton buttonReset' onclick='newGame()'> AGAIN? </button>";
	}
}

function answerStock() {
	if (!user_answered) {

		if (plot_name[0] == 0) {
			// console.log('wrong, this was randomly generated');
			document.getElementById("response_string").innerHTML = "wrong, this was randomly generated";
			document.getElementById("generateButtons").innerHTML = "";
			document.getElementById("forward_button").innerHTML = "<button class='keyButton button2' onclick='changeImage()'> NEXT IMAGE </button>"
		} else {
			score++;
			// console.log('right, that was the price of ' + stock_ticker + ' stocks, from ' + start_date + ' to ' + end_date);
			document.getElementById("response_string").innerHTML = 'right, that was the price of ' + stock_ticker + ' stocks, from ' + start_date + ' to ' + end_date;
			document.getElementById("generateButtons").innerHTML = "";
			document.getElementById("forward_button").innerHTML = "<button class='keyButton button2' onclick='changeImage()'> NEXT IMAGE </button>"
		}

		user_answered = true;
		if (counter == countMax) {
			gameEnded();
		}
	}
}

function answerRandom() {
	if (!user_answered) {

		if (plot_name[0] == 0) {
			score++;
			// console.log('right, this is a random walk');
			document.getElementById("response_string").innerHTML = 'right, this is a random walk';
			document.getElementById("generateButtons").innerHTML = "";
			document.getElementById("forward_button").innerHTML = "<button class='keyButton button2' onclick='changeImage()'> NEXT IMAGE </button>"
		} else {
			// console.log('wrong, that was the price of ' + stock_ticker + ' stocks, from ' + start_date + ' to ' + end_date);
			document.getElementById("response_string").innerHTML = 'wrong, that was the price of ' + stock_ticker + ' stocks, from ' + start_date + ' to ' + end_date;
			document.getElementById("generateButtons").innerHTML = "";
			document.getElementById("forward_button").innerHTML = "<button class='keyButton button2' onclick='changeImage()'> NEXT IMAGE </button>"
		}

		user_answered = true;
		if (counter == countMax) {
			gameEnded();
		}
	}
}

function gameEnded() {
	document.getElementById("forward_button").innerHTML = "<button class='keyButton button2' onclick='changeImage()'> SHOW ME THE RESULTS </button>"
}

function newGame() {
	counter = 0;
	user_answered = true;
	score = 0;
	document.getElementById("score_string").innerHTML = "";
	document.getElementById("newer_game_button").innerHTML = "";
	changeImage();
}