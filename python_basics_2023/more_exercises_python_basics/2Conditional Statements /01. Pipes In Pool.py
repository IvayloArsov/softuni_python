volume =  int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())
flow2 = pipe2*hours
flow1 = pipe1*hours
flow = flow1+flow2

if flow <= volume:
    print(f"The pool is {flow/volume*100:.2f}% full. Pipe 1: {flow1/flow*100:.2f}%. Pipe 2: {flow2/flow*100:.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {flow-volume:.2f} liters.")