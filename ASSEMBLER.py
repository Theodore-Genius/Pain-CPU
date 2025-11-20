def parse_register(reg_str):

    return int(reg_str.strip().upper().replace('X', ''))

def assemble_line(line):
 
    line = line.split('//')[0].strip()
    if not line:
        return None

    parts = line.replace(',', ' ').split()

    
    instr = parts[0].upper()
 

    opcodes = {
        'ADD': 0x1C,
        'LDR': 0x1D,
        'SUB': 0x3C,
        'STR': 0x0A
    }
    
    if instr not in opcodes:
        raise ValueError(f"Unknown instruction {instr}")
        
    opcode = opcodes[instr]

    if instr == 'STR':
    
        Rm = parse_register(parts[1])
        Rn = parse_register(parts[2])
        imm = int(parts[3])

        second_byte = (Rm << 2) + Rn
    else:
 
        Rd = parse_register(parts[1])
        Rn = parse_register(parts[2])
        imm = int(parts[3])
 
        second_byte = (Rd << 6) + Rn
    
    if imm < 0 or imm > 255:
        raise ValueError("Immediate out of range (0-255)")


    third_byte = imm & 0xFF
    

    instruction_word = (opcode << 16) | (second_byte << 8) | third_byte
    
 
    return f"{instruction_word:06x}"

def assemble_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            machine_code = assemble_line(line)
            if machine_code:
                outfile.write(machine_code + '\n')

if __name__ == "__main__":

    
    input_file = "assemblyExample.txt"
    output_file = "testCode.txt"
    assemble_file(input_file, output_file)
    print(f"Assembly from {input_file} has been translated to {output_file}.")