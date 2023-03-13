#!/usr/bin/node
/* prints C is Fun x number of times */
const num = Number(process.argv[2]);
let i;
if (!num) {
  console.log('Missing number of occurrences');
} else if (num > 0) {
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
