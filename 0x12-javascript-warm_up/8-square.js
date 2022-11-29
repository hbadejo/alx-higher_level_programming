#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let rw = 0; rw < size; rw++) {
    let row = '';
    for (let co = 0; co < size; co++) {
      row += 'X';
    }
    console.log(row);
  }
}
