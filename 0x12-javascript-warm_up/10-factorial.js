#!/usr/bin/node
/* prints an computes a factorial */
const args = process.argv;
function factorial (a) {
  if (a === 0 || isNaN(a)) { return 1; }
  return a * factorial(a - 1);
}
console.log(factorial(Number(args[2])));
