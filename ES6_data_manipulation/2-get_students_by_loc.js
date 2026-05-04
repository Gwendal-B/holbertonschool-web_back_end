export default function getStudentsByLocation(student, city) {
  return student.filter((student) => student.location === city);
}
