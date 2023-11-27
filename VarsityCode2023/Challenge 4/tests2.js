'use strict';

const QUnit = require('qunitjs');
const s = require('./solution2.js');

QUnit.test("SolutionTests", function(assert) {

    
    assert.deepEqual(s.balancePoint([ 2, 7, 4, 5, -3, 8, 9, -1 ]), 3);


});