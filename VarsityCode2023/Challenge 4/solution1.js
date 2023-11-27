'use strict';

module.exports = {
  reverseWords
};

function reverseWords(sentence) {
    // Your code goes here
    return sentence.split(' ').reverse().join(' ')
}
