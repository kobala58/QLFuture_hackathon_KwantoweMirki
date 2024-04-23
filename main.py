from qiskit_optimization import QuadraticProgram

def main():
    DOCTORS = 10
    PATIENTS = 20
    qubo = QuadraticProgram()
    
    for x in range(DOCTORS):
        for y in range(PATIENTS)
        vars = [qubo.binary_var(f"w[{x},{y}]")

    qubo.maximize()

if __name__ == "__main__":
    main()
