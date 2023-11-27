'use strict';

const QUnit = require('qunitjs');
const s = require('./solution1.js');

QUnit.test("SolutionTests", function(assert) {

    
    assert.deepEqual(s.reverseWords("the quick brown fox"), "fox brown quick the");


});