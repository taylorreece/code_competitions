#!/usr/bin/env python3

file_out = open('output.txt', 'w')

def output(line):
    print(line)
    file_out.write(f"{line}\n")

def solve(n, ins, outs):
    my_map = []
    for i in range(n):
        my_map.append(["-"] * i + ["Y"] + ["-"] * (n-i-1))
    for i in range(n):
        if ins[i] == "N":
            for j in range(i):
                for k in range(i+1, n):
                    my_map[j][k] = "N"
            for j in range(i+1, n):
                for k in range(i):
                    my_map[j][k] = "N"
            for j in range(n):
                if i != j:
                    my_map[j][i] = "N"
        if outs[i] == "N":
            for j in range(i):
                for k in range(i+1, n):
                    my_map[k][j] = "N"
            for j in range(i+1, n):
                for k in range(i):
                    my_map[k][j] = "N"
            for j in range(n):
                if i != j:
                    my_map[i][j] = "N"
    for i in range(n):
        output("".join(my_map[i]).replace("-", "Y"))

with open('input.txt', 'r') as f:
    for i in range(int(f.readline())):
        
        output(f"Case #{i+1}:")
        solve(
            int(f.readline()),
            f.readline().strip(),
            f.readline().strip()
        )