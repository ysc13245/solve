var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

input.slice(1).forEach(function(x) {
    let seq = x.split(" ").map(Number);
    console.log((((seq[2]-1)%seq[0])+1)*100 + Math.floor((seq[2]-1)/(seq[0])+1));
})
