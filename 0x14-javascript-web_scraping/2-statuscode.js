#!/usr/bin/node
const request = require('request');
const arg = process.argv;
if (arg.length > 1) {
  const url = arg[2];
  request(url, (err, res, body) => {
    if (err) {
      return;
    }
    console.log('code:', res.statusCode);
  });
}
