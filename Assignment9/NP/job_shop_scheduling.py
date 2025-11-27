import itertools

# (Machine sequence, Time)
jobs = {
    'J1': [('M1', 3), ('M2', 2), ('M3', 2)],
    'J2': [('M2', 2), ('M1', 1), ('M3', 4)],
    'J3': [('M3', 4), ('M2', 3), ('M1', 2)],
    'J4': [('M1', 2), ('M3', 1), ('M2', 3)]
}

machines = ['M1', 'M2', 'M3']

def schedule(sequence):
    machine_time = {m:0 for m in machines}
    job_time = {j:0 for j in jobs}
    
    for job in sequence:
        for m, t in jobs[job]:
            start = max(machine_time[m], job_time[job])
            end = start + t
            machine_time[m] = end
            job_time[job] = end
    makespan = max(machine_time.values())
    return makespan

best_seq = None
min_makespan = float('inf')
for seq in itertools.permutations(jobs.keys()):
    ms = schedule(seq)
    if ms < min_makespan:
        min_makespan = ms
        best_seq = seq

print("Optimal Job Sequence:", best_seq)
print("Minimum Makespan:", min_makespan)
