let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

for (let x of input.slice(1)) {
    let seq = x.split(" ").map(Number);
    console.log((((seq[2] - 1) % seq[0]) + 1) * 100 + Math.floor((seq[2]-1)/(seq[0]) + 1));
}