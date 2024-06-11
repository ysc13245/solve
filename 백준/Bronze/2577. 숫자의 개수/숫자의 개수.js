var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split("\n");


let s = input[0]*input[1]*input[2]+"";

let sum = 0;
for (let i = 0; i < 10; i++) {
    sum = 0;
    s.split('').forEach(x=> x==i?sum+=1:0);
    console.log(sum);
    
}

