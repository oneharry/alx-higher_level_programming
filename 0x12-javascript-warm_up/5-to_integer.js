#!/usr/bin/node
/* prints arguments that are numbers */
const args = process.argv;
const myArg = args[2];
if (!isNaN(Number(myArg)) && myArg) {
  console.log('My number:', Number(myArg));
} else {
  console.log('Not a number');
}
