#!/usr/bin/nodejs
const ar1 = require('./100-data').list;
const ar2 = [];
let num = 0;
ar1.map((curr, index) => {
  num = curr * index;
  ar2.push(num);
  return ar2;
});
console.log(ar1);
console.log(ar2);
