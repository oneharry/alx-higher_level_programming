#!/usr/bin/node
const fs = require('fs');
const arg = process.argv;
if (arg.length > 1) {
  const file = arg[2];
  fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
}
