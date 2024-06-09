var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString();


let score = 0;

let rool = {
    "P":1,
    "p":-1,
    "N":3,
    "n":-3,
    "B":3,
    "b":-3,
    "R":5,
    "r":-5,
    "Q":9,
    "q":-9
}

for (const c of input) {
    if (c in rool) {
        score += rool[c];
    }
}

console.log(score);

