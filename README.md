# Pain CPU User Manual
Michael Lamaze & Leonard Weber

**Pain** is a 22-bit CPU. It has four general purpose registers, supports both addition and subtraction, and includes load/store instructions with immediate offsets. The CPU is implemented in Logisim, with a Python assembler used to convert assembly instructions into machine code.

## Usage

Download or clone the **pain CPU package**, and ensure the following files are present in the same directory:

- `pain.circ` (your Logisim CPU)
- Your assembler Python script (e.g., `assembler.py`)
- Your assembly input file (e.g., `program.txt`)

### Running the Assembler

1. Ensure **Python** is installed on your system.
2. Save the assembler script with a `.py` extension.
3. Create a text file containing your assembly instructions and save it as a `.txt` file in the same directory.
4. Open a terminal in your IDE (or system console) and navigate to the directory containing both files.
5. Run your assembler script:

This will generate an output file named **testCode.txt** containing the machine code.

### Loading Instructions into Logisim

1. Open `pain.circ` in Logisim.
2. Navigate to the memory module (inside the **Address** circuit).
3. Right-click on the RAM and select **Load Image**.
4. Choose the generated `testCode.txt` file.
5. In the load dialog, change the format from **Binary** to **v3.0 Hex**, then click **OK**.
6. You should now see the hexadecimal encoding of your instructions loaded into memory.

To run the program:
- Use **Simulate → Tick** to step manually, or
- Enable **Auto-Tick** to run continuously.

Use **Simulate → Reset Simulation** (or **Ctrl+R**) to restart.

## CPU Architecture Overview

The **pain** CPU contains:

- **4 general-purpose registers**: `Rd`, `Rn`, `Rm`, `Rt`
- **An ALU** supporting:
- Addition (ADD)
- Subtraction (SUB)
- **RAM** for data storage
- **Load/Store instructions** using an 8-bit immediate offset
- A simple single-cycle datapath that executes one instruction per tick

Registers are referenced symbolically in the assembly code (Rd, Rn, Rm, Rt) but encoded as 2-bit values in machine code.
