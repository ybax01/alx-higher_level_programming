#!/usr/bin/node

const filePath = process.argv[2];
const content = process.argv[3];
const fs = require('fs');
fs.writeFile(filePath, 'utf8', content, function (err) {
  if (err) {
    console.log(err);
  } else {
  }
});
