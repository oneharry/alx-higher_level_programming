#!/usr/bin/node
const fs = require('fs');
const arg = process.argv;
if (arg.length > 1) {
  const file = arg[2];
  const content = arg[3];
  fs.writeFile(file, content, (err, data) => {
    if (err) {
      console.log(err);
    }
  });
}
