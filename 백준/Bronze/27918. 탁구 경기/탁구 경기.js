let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");


let D = 0;
let P = 0;

input.slice(1).forEach(x=>{
    if (Math.abs(D-P)>1) return;
    if (x==='D') D++;
    else P++;
})
console.log(D+':'+P);