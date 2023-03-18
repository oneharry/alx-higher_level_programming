#!/usr/bin/node
let count = 0;
exports.logMe = function (x) { console.log(`${count++}: ${x}`); };
