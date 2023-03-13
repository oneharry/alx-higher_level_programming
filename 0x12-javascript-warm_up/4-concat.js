#!/usr/bin/node
/* prints the first 2 argument passed */
const args = process.argv;
const myArg = args[2] + ' is ' + args[3];
console.log(myArg);
