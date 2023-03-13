#!/usr/bin/node
/* prints a square */
const num = Number(process.argv[2]);
let i, j;
if (!num || isNaN(num)) {
  console.log('Missing size');
} else if (num > 0) {
  for (i = 0; i < num; i++) {
    let space = '';
    for (j = 0; j < num; j++) {
      space += 'X';
    }
    console.log(space);
  }
}
