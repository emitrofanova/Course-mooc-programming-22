# Write your solution here
def run(program):
    answ = []
    variables_dct = {}
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        variables_dct[ch] = 0
    def_prog = program
    dct_loops = {}
    i = 0
    for line in program:
        i += 1
        line = line.split()
        if len(line) == 1 and line[0] != "END":
            dct_loops[line[0][:-1]] = i
    new_p = run2(program, variables_dct, def_prog, answ, dct_loops)
    while True:
        if new_p == None:
            break
        new_p = run2(new_p[0],new_p[1],new_p[2],new_p[3],new_p[4])
    return answ

def run2(program, variables_dct, def_prog, answ, dct_loops):
    for line in program:
        line_save = line
        line = line.split()
        if line[0] == "JUMP":
            sub_program = def_prog[dct_loops[line[1]]:]
            return [sub_program, variables_dct, def_prog, answ, dct_loops]
        elif line[0] == "IF":
            flag = False
            
            if line[2] == "==":
                if line[3].isnumeric():
                    if variables_dct[line[1]] == int(line[3]):
                        flag = True
                else:
                    if variables_dct[line[1]] == variables_dct[line[3]]:
                        flag = True
                if flag:
                    sub_program = def_prog[dct_loops[line[5]]:]
                    return [sub_program, variables_dct, def_prog, answ, dct_loops]

            elif line[2] == "!=":
                if line[3].isnumeric():
                    if variables_dct[line[1]] != int(line[3]):
                        flag = True
                else:
                    if variables_dct[line[1]] != variables_dct[line[3]]:
                        flag = True
                if flag:
                    sub_program = def_prog[dct_loops[line[5]]:]
                    return [sub_program, variables_dct, def_prog, answ, dct_loops]

            elif line[2] == "<":
                if line[3].isnumeric():
                    if variables_dct[line[1]] < int(line[3]):
                        flag = True
                else:
                    if variables_dct[line[1]] < variables_dct[line[3]]:
                        flag = True
                if flag:
                    sub_program = def_prog[dct_loops[line[5]]:]
                    return [sub_program, variables_dct, def_prog, answ, dct_loops]

            elif line[2] == "<=":
                if line[3].isnumeric():
                    if variables_dct[line[1]] <= int(line[3]):
                        flag = True
                else:
                    if variables_dct[line[1]] <= variables_dct[line[3]]:
                        flag = True
                if flag:
                    sub_program = def_prog[dct_loops[line[5]]:]
                    return [sub_program, variables_dct, def_prog, answ, dct_loops]

            elif line[2] == ">":
                if line[3].isnumeric():
                    if variables_dct[line[1]] > int(line[3]):
                        flag = True
                else:
                    if variables_dct[line[1]] > variables_dct[line[3]]:
                        flag = True
                if flag:
                    sub_program = def_prog[dct_loops[line[5]]:]
                    return [sub_program, variables_dct, def_prog, answ, dct_loops]
            
            elif line[2] == ">=":
                if line[3].isnumeric():
                    if variables_dct[line[1]] >= int(line[3]):
                        flag = True
                else:
                    if variables_dct[line[1]] >= variables_dct[line[3]]:
                        flag = True
                if flag:
                    sub_program = def_prog[dct_loops[line[5]]:]
                    return [sub_program, variables_dct, def_prog, answ, dct_loops]
        else:
            logic(line_save, variables_dct, answ)

def logic(command, variables_dct, answ):
    command = command.split()
    if command[0] == "MOV":
        if command[2].isnumeric():
            variables_dct[command[1]] = int(command[2])
        else:
            variables_dct[command[1]] = variables_dct[command[2]]
    elif command[0] == "PRINT":
        if command[1].isnumeric():
            answ.append(int(command[1]))
        else:
            answ.append(variables_dct[command[1]])
    elif command[0] == "ADD":
        if command[2].isnumeric():
            variables_dct[command[1]] += int(command[2])
        else:
            variables_dct[command[1]] += variables_dct[command[2]]
    elif command[0] == "SUB":
        if command[2].isnumeric():
            variables_dct[command[1]] -= int(command[2])
        else:
            variables_dct[command[1]] -= variables_dct[command[2]]
    elif command[0] == "MUL":
        if command[2].isnumeric():
            variables_dct[command[1]] *= int(command[2])
        else:
            variables_dct[command[1]] *= variables_dct[command[2]]
    elif command[0] == "END":
        return answ
    
if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 100")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
