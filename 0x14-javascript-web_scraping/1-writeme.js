#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[3];
fs.writeFile(process.argv[2], filePath, function (err, filePath) {
  if (err) {
    console.log(err);
  }
});
