let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");


let origin = input[0].substring(0, 5);
let sum = 0;
input.slice(2).forEach(x => sum += x.substring(0, 5) === origin ? 1 : 0);

console.log(sum);

