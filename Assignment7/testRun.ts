import { getEmployeeDepth, Employee } from "./getEmployeeDepth.js";

const employees: Employee[] = [
  { id: 1, name: "Alice Johnson", position: "CEO", salary: 250000, supervisor_id: null },
  { id: 2, name: "Bob Smith", position: "CTO", salary: 180000, supervisor_id: 1 },
  { id: 7, name: "Grace Lee", position: "Senior Developer", salary: 120000, supervisor_id: 4 },
  { id: 4, name: "David Brown", position: "Engineering Manager", salary: 140000, supervisor_id: 2 },
  { id: 12, name: "Liam Garcia", position: "Intern Developer", salary: 50000, supervisor_id: 7 },
];

console.log(getEmployeeDepth(employees, 1));  // 0
console.log(getEmployeeDepth(employees, 2));  // 1
console.log(getEmployeeDepth(employees, 7));  // 3
console.log(getEmployeeDepth(employees, 12)); // 4
console.log(getEmployeeDepth(employees, 999)); // -1
