let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

let N = Number(input[0]);
let shirts = input[1].split(" ").map(Number);
let [t, p] = input[2].split(" ").map(Number);

let sum = 0;
shirts.forEach(x=> sum += Math.ceil(x/t));

console.log(sum);
console.log(Math.floor(N/p), N % p);

