'use strict';

module.exports = {
  rotThirteen
};


function rotThirteen(str) {
    return str.replace(/[a-zA-Z]/g, function(chr) {
        var start = chr <= 'Z' ? 65 : 97;
        return String.fromCharCode(start + (chr.charCodeAt(0) - start + 13) % 26);
    });
}
