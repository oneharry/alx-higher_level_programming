#!/usr/bin/node
/* prints the second biggest integer */
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let i; const arr = [];
  for (i = 2; i < args.length; i++) {
    arr.push(args[i]);
  }
  console.log(arr.sort((a, b) => a - b)[arr.length - 2]);
}
