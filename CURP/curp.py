import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape, transitions, start_state, accept_states):
        self.tape = list(tape)
        self.head = 0
        self.state = start_state
        self.transitions = transitions
        self.accept_states = accept_states

    def step(self):
        current_symbol = self.tape[self.head]
        if (self.state, current_symbol) in self.transitions:
            new_state, write_symbol, direction = self.transitions[(self.state, current_symbol)]
            self.tape[self.head] = write_symbol
            self.state = new_state
            if direction == 'R':
                self.head += 1
            elif direction == 'L':
                self.head -= 1
        else:
            raise ValueError(f"No transition defined for state {self.state} and symbol {current_symbol}")

    def run(self):
        try:
            while self.state not in self.accept_states:
                self.step()
        except ValueError:
            return False
        return self.state in self.accept_states

def validate_curp():
    curp = entry_curp.get()
    tm = TuringMachine(curp, transitions, start_state, accept_states)
    is_valid = tm.run()

    if is_valid:
        messagebox.showinfo("Resultado", "CURP válida")
    else:
        messagebox.showerror("Resultado", "CURP inválida")

transitions = {
    ('q0', 'A'): ('q1', 'A', 'R'),
    ('q1', 'B'): ('q2', 'B', 'R'),
   
    ('q19', ' '): ('q20', ' ', 'R'), 
}


start_state = 'q0'
accept_states = {'q20'}


root = tk.Tk()
root.title("Validador de CURP - Máquina de Turing")


label = tk.Label(root, text="Ingresa la CURP:")
label.pack(pady=10)

entry_curp = tk.Entry(root, width=25)
entry_curp.pack(pady=5)


button_validate = tk.Button(root, text="Validar CURP", command=validate_curp)
button_validate.pack(pady=20)

root.mainloop()
