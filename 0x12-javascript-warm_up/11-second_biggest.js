#!/usr/bin/nodejs
if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let count = 2;
  const ar = [];
  while (count < process.argv.length) {
    ar.push(process.argv[count]);
    count++;
  }
  ar.sort(function (a, b) {
    return a - b;
  });
  console.log(ar[ar.length - 2]);
}
