const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      console.log(`Number of students: ${students.length}`);

      const fields = {};

      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        const number = fields[field].length;
        const list = fields[field].join(', ');
        const message = `Number of students in ${field}: ${number}. List: ${list}`;

        console.log(message);
      });

      resolve();
    });
  });
}

module.exports = countStudents;
