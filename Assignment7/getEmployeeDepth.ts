export interface Employee {
  id: number;
  name: string;
  position: string;
  salary: number;
  supervisor_id: number | null;
}

export interface EmployeeData {
  employees: Employee[];
}

export function getEmployeeDepth(employees: Employee[], employeeId: number): number {
  const employeeMap = new Map<number, Employee>();
  employees.forEach(emp => employeeMap.set(emp.id, emp));

  const visited = new Set<number>();

  function findDepth(id: number, depth: number): number {
    const employee = employeeMap.get(id);
    if (!employee) return -1; 

    if (visited.has(id)) return -1; 
    visited.add(id);

    if (employee.supervisor_id === null) {
      return 0; 
    }

    const supervisorDepth = findDepth(employee.supervisor_id, depth + 1);
    if (supervisorDepth === -1) return -1; 

    return supervisorDepth + 1;
  }

  return findDepth(employeeId, 0);
}
