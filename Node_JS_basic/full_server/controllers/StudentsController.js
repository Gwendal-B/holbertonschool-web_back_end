import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const database = process.argv[2];

    readDatabase(database)
      .then((fields) => {
        const output = ['This is the list of our students'];

        Object.keys(fields)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
          .forEach((field) => {
            const number = fields[field].length;
            const list = fields[field].join(', ');
            const message = `Number of students in ${field}: ${number}. List: ${list}`;

            output.push(message);
          });

        response.status(200).send(output.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const database = process.argv[2];
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((fields) => {
        const list = fields[major].join(', ');

        response.status(200).send(`List: ${list}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
