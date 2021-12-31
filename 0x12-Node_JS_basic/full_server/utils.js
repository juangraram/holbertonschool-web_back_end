const fs = require('fs');

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    let data = '';
    const table = {};

    fs.readFile(path, 'utf8', (err, myDB) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      data = myDB
        .toString()
        .split('\n')
        .filter((item) => item)
        .map((data) => data.split(','));

      data = data.slice(1, data.length);
      data.forEach((student) => {
        if (!table[student[3]]) {
          table[student[3]] = [student[0]];
        } else {
          table[student[3]].push(student[0]);
        }
      });

      resolve(table);
    });
  });
}const fs = require('fs');

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    let data = '';
    const table = {};

    fs.readFile(path, 'utf8', (err, myDB) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      data = myDB
        .toString()
        .split('\n')
        .filter((item) => item)
        .map((data) => data.split(','));

      data = data.slice(1, data.length);
      data.forEach((student) => {
        if (!table[student[3]]) {
          table[student[3]] = [student[0]];
        } else {
          table[student[3]].push(student[0]);
        }
      });

      resolve(table);
    });
  });
}
