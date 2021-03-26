// Initialisation
let resT = document.getElementById("res");
const dflt = resT.innerHTML;
let operation = "";
let firstNum = "";
let secondNum =  "";
const numArr = ["btn0", "btn1", "btn2", "btn3", "btn4", "btn5", "btn6", "btn7", "btn8", "btn9"];

// Event listeners
for (let i = 0; i < 10; i++) {
    document.getElementById(numArr[i]).addEventListener('click', function() {addNum(i.toString());});
}

document.getElementById("btnClr").addEventListener('click', clear);
document.getElementById("btnEql").addEventListener('click', getResult);

document.getElementById("btnSum").addEventListener('click', function() {addOperation('+')});
document.getElementById("btnSub").addEventListener('click', function() {addOperation('-')});
document.getElementById("btnMul").addEventListener('click', function() {addOperation('*')});
document.getElementById("btnDiv").addEventListener('click', function() {addOperation('/')});

// Functions
function addNum(num) {
    resT.innerHTML += num;
    if (!operation) {
        firstNum += num;
    }
    else {
        secondNum += num;
    }
}


function clear() {
    resT.innerHTML = dflt;
    operation = "";
    firstNum = "";
    secondNum = "";
}


function getResult() {
    let fn = parseInt(firstNum);
    let sn = parseInt(secondNum)
    switch(operation) {
        case "add":
            resT.innerHTML = fn + sn;
            break;
        case "subtract":
            resT.innerHTML = fn - sn;
            break;
        case "multiply":
            resT.innerHTML = fn * sn;
            break;
        case "divide":
            resT.innerHTML = fn / sn;
            break;
    }
    firstNum = resT.innerHTML;
    secondNum = "";
    operation = "";
}


function addOperation(op) {
    if (!operation) {
        switch(op) {
            case '+':
                resT.innerHTML += '+';
                operation = "add";
                break;
            case '-':
                resT.innerHTML += '-';
                operation = "subtract";
                break;
            case '*':
                resT.innerHTML += '*';
                operation = "multiply";
                break;
            case '/':
                resT.innerHTML += '/';
                operation = "divide";
                break;
        }
    }
    else {
        console.error("Error: Operator already selected.");
    }
}
