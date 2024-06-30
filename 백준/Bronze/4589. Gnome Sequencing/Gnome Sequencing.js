let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");


console.log("Gnomes:")
input.slice(1).forEach(x => {
    let lis = x.split(" ").map(Number);
if (lis[0] <= lis[1] && lis[1] <= lis[2] || lis[0] >= lis[1] && lis[1] >= lis[2]) {
    console.log("Ordered");
} else {
    console.log("Unordered");
    }
});