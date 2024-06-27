let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split(" ");

let [A, B] = input.map(x=> Number(x.replaceAll("6","5")));
let [C, D] = input.map(x=> Number(x.replaceAll("5","6")));

console.log(A+B, C+D)
