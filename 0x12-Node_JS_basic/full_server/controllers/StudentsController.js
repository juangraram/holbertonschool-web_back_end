import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const table = await readDatabase(process.argv[2]);
      const fields = ['This is the list of our students'];
      let field = '';

      for (const key of Object.keys(table)) {
        if (key) {
          field = `Number of students in ${key}: ${
            table[key].length
          }. List: ${table[key].join(', ')}`;
          fields.push(field);
        }
      }
      res.status(200).send(`${fields.join('\n')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    if (!['CS', 'SWE'].includes(req.params.major)) {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const table = await readDatabase(process.argv[2]);
      res.status(200).send(`List: ${table[req.params.major].join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}
