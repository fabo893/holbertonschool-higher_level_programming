#!/usr/bin/nodejs
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let x = 0;
  while (x < num) {
    let y = 0;
    while (y < num) {
      process.stdout.write('X');
      y++;
    }
    process.stdout.write('\n');
    x++;
  }
}
