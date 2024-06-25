let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

let ans = 0;
for (let i = input.length-1; i >= 0; i--) {
    if (!isNaN(input[i])) {
        ans = Number(input[i])+(3-i);
        if (ans % 3 == 0) {
            if (ans % 5 == 0) {
                console.log("FizzBuzz");
                break;
            } else {
                console.log("Fizz");
                break;
            }
        } else if (ans % 5 == 0) {
            console.log("Buzz");
            break;
        } else {
            console.log(ans);
            break;
        }
    }
}