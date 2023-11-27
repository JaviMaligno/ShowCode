'use strict';

module.exports = {
  balancePoint
};

function balancePoint(input) {
    // Your code goes here
    let leftSum = 0;
    let rightSum = input.reduce((a,b) => a+b, 0);
    
    for (let i = 0; i < input.length; i++) {
        rightSum -= input[i];
        if (leftSum === rightSum){
            return i;
        }
        leftSum += input[i];
    }
    return -1
}
