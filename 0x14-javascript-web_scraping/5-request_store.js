#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const arg = process.argv;
if (arg.length > 2) {
  const url = arg[2];
  const filename = arg[3];
  request(url, (err, res, body) => {
    if (err) {
      return;
    }
    fs.writeFile(filename, res.body, (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  });
}
