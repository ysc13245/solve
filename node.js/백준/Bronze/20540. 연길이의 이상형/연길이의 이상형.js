var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim();


let ans = ""
const mbti = {
    'I': 'E',
    'E': 'I',
    'S': 'N',
    'N': 'S',
    'T': 'F',
    'F': 'T',
    'P': 'J',
    'J': 'P'
}

for (const c of input) {
    ans += mbti[c];
}
console.log(ans);
