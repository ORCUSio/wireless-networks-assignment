// Q13. Delete the rollno property from an object. Print before and after.

let student = {
  name: "David Rayy",
  sclass: "V1",
  rollno: 12,
};

console.log("Before deletion:", student);

delete student["rollno"];

console.log("After deletion:", student);
