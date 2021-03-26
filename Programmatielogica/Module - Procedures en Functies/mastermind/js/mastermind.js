// Initialisation
const colors = ['white', 'red', 'green', 'blue', 'brown', 'black', 'yellow', 'cyan', 'orange'];
let currentBoxes = ['white', 'white', 'white', 'white'];
let count = 0;
let result = createResult();

// Boxes
const boxArr = ["box1", "box2", "box3", "box4"];
const prevArr = ["prev1", "prev2", "prev3", "prev4"];
const resultArr = ["result1", "result2", "result3", "result4"];

// Event listeners
for (let i = 0; i < currentBoxes.length; i++) {
    document.getElementById(boxArr[i]).addEventListener('click', function() {nextColor(i);});
}

document.getElementById("validateButton").addEventListener('click', function() {setPrevBoxes(); validate();});
document.getElementById("resetButton").addEventListener('click', reset);

// Functions
function nextColor(ind) {
    // Sets color of button to next in sequence (white -> red -> green -> blue)
    let nextInd;
    if (currentBoxes[ind] == colors[-1]) {
        nextInd = 0;
    }
    else {
        nextInd = colors.indexOf(currentBoxes[ind]) + 1;
    }
    document.getElementById(boxArr[ind]).style.backgroundColor = colors[nextInd];
    currentBoxes[ind] = colors[nextInd];
}


function validate() {
    // Updates the counter and checks the answer and gives the feedback
    count++;
    updateCounter();
    let check = true;
    for (let i = 0; i < currentBoxes.length; i++) {
        if (currentBoxes[i] == result[i]) {
            document.getElementById(resultArr[i]).style.backgroundColor = 'green';
        }
        else {
            check = false;
            document.getElementById(resultArr[i]).style.backgroundColor = 'red';
        }
    }
    if (check) {
        alert(`You got it in ${count} attempts!`);
    }
}


function setPrevBoxes() {
    // Sets the boxes on validation
    for (let i = 0; i < currentBoxes.length; i++) {
        document.getElementById(prevArr[i]).style.backgroundColor = currentBoxes[i];
    }
}


function reset() {
    // Resets the game
    for (let i = 0; i < currentBoxes.length; i++) {
        document.getElementById(resultArr[i]).style.backgroundColor = colors[0];
        document.getElementById(prevArr[i]).style.backgroundColor = colors[0];
        document.getElementById(boxArr[i]).style.backgroundColor = colors[0];
        currentBoxes[i] = colors[0];
    }
    result = createResult();
    count = 0;
    updateCounter();
}


function createResult() {
    // Creates a randomized result
    let res = [];
    for (let i = 0; i < currentBoxes.length; i++) {
        res.push(colors[Math.floor(Math.random() * colors.length)]);
    }
    console.log(res);
    return res;
}


function updateCounter() {
    // Updates the guess counter
    document.getElementById("counter").innerHTML = `Guess Counter: ${count}`;
}
