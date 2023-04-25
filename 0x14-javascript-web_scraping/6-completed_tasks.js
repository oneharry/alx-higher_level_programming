#!/usr/bin/node
const request = require('request');

const arg = process.argv;
if (arg.length > 2) {
  const url = arg[2];
  request(url, (err, res, body) => {
    if (err) {
      return;
    }
    const tasks = JSON.parse(body);
    const completedTasks = tasks.filter(task => task.completed === true);

    const dic = {};

    completedTasks.forEach(task => {
      if (dic[task.userId]) {
        dic[task.userId] += 1;
      } else {
        dic[task.userId] = 1;
      }
    });
    console.log(dic);
  });
}
