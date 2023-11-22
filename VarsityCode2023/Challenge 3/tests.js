'use strict';

const QUnit = require('qunitjs');
const s = require('./solution.js');

QUnit.test("SolutionTests", function(assert) {

    
    assert.deepEqual(s.rotThirteen("Hello world"), "Uryyb jbeyq");


    assert.deepEqual(s.rotThirteen("Goodbye world"), "Tbbqolr jbeyq");


});