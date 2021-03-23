#!/usr/bin/nodejs
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let n = 0;
  while (n < num) {
    console.log('C is fun');
    n++;
  }
}
