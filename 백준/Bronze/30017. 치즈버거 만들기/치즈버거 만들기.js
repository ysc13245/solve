let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split(" ");

let A = Number(input[0]);
let B = Number(input[1]);

if (A > B) {
    A = B + 1;
} else {
    B = A -1;
}

console.log(A + B);
