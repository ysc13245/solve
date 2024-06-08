var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(" ");

console.log(Math.floor(Math.min(input[0],input[1])/2));