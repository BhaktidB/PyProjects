# def get_length(dna):
#     """ (str) -> int

#     Return the length of the DNA sequence dna.

#     >>> get_length('ATCGAT')
#     6
#     >>> get_length('ATCG')
#     4
#     """
#     return len(dna)

# def is_longer(dna1, dna2):
#     """ (str, str) -> bool

#     Return True if and only if DNA sequence dna1 is longer than DNA sequence
#     dna2.

#     >>> is_longer('ATCG', 'AT')
#     True
#     >>> is_longer('ATCG', 'ATCGGA')
#     False
#     """
#     return len(dna1) > len(dna2)


# def count_nucleotides(dna, nucleotide):
#     """ (str, str) -> int

#     Return the number of occurrences of nucleotide in the DNA sequence dna.

#     >>> count_nucleotides('ATCGGC', 'G')
#     2
#     >>> count_nucleotides('ATCTA', 'G')
#     0
#     """
#     nuc = ''
#     for ch in dna:
#         if ch in nucleotide:
#             nuc = nuc + ch

#     return len(nuc)

# def contains_sequence(dna1, dna2):
#     """ (str, str) -> bool

#     Return True if and only if DNA sequence dna2 occurs in the DNA sequence
#     dna1.

#     >>> contains_sequence('ATCGGC', 'GG')
#     True
#     >>> contains_sequence('ATCGGC', 'GT')
#     False

#     """
#     if dna2 in dna1:
#         return True
#     else:
#         return False

# def is_valid_sequence(dna):
#     '''
#     (str) -> bool
#     Return True if and only if the return value is valid(that is it should not contain values other than 'A' 'G' 'T' 'C')

#     >>>is_invalid_sequence("ATCG")
#     True
#     >>>is_invalid_sequence("DFGHJK")
#     False

#     '''

#     for ch in dna:
#         if ch in ('ATCG'):
#             return True
#         else:
#             return False

# def insert_sequence(dna1, dna2, index):
#     '''
#     (str, str, int) -> str
#     Return the DNA sequence obtained by inserting the second DNA sequence into
#     the first DNA sequence at the given index.

#     >>>insert_sequence('CCGG', 'AA', 2)
#     CCAAGG
#     >>>insert_sequence('ATKT', 'TT', 1)
#     ATTTKT
#     '''
#     return dna1[:index] + dna2 + dna1[index:]

# def get_complement(nucleotide):
#     '''

#     (str) -> str
#     Return the nucleotide's complement.

#     >>>get_complement('A')
#     T
#     >>>get_complement('C')
#     G
#     '''
#     if nucleotide == 'A':
#         return 'T'
#     elif nucleotide == 'T':
#          return 'A'

#     if nucleotide == 'C':
#         return 'G'
#     elif nucleotide == 'G':
#             return 'C'

# def get_complementary_sequence(dna):
#     '''
#     (str) -> str

#     Return the complement of a given DNA sequence.

#     >>> get_complementary_sequence('ATCGGACT')
#     TAGCCTGA
#     >>> get_complementary_sequence('GCACTCC')
#     CGTGAGG
#     '''
#     c = ''
#     for ch in dna:
#         c = c + get_complement(ch)
#     return c



import tkinter as tk
from tkinter import messagebox

# DNA functions (same as before)
def get_length(dna):
    return len(dna)

def is_valid_sequence(dna):
    for ch in dna:
        if ch not in ('A', 'T', 'C', 'G'):
            return False
    return True

def get_complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return ''

def get_complementary_sequence(dna):
    return ''.join(get_complement(ch) for ch in dna)


# --- GUI setup ---
def on_get_length():
    dna = entry_dna.get().upper()
    if not is_valid_sequence(dna):
        messagebox.showerror("Invalid DNA", "DNA sequence contains invalid characters!")
        return
    result = get_length(dna)
    label_result.config(text=f"Length: {result}")

def on_is_valid():
    dna = entry_dna.get().upper()
    result = is_valid_sequence(dna)
    label_result.config(text=f"Valid DNA? {'✅ Yes' if result else '❌ No'}")

def on_get_complementary():
    dna = entry_dna.get().upper()
    if not is_valid_sequence(dna):
        messagebox.showerror("Invalid DNA", "DNA sequence contains invalid characters!")
        return
    result = get_complementary_sequence(dna)
    label_result.config(text=f"Complementary Sequence: {result}")

def on_count_nucleotide():
    dna = entry_dna.get().upper()
    nucleotide = entry_nucleotide.get().upper()
    if not is_valid_sequence(dna):
        messagebox.showerror("Invalid DNA", "DNA sequence contains invalid characters!")
        return
    if nucleotide not in ('A','T','C','G') or len(nucleotide) != 1:
        messagebox.showerror("Invalid Nucleotide", "Please enter a single nucleotide (A, T, C, or G)")
        return
    count = dna.count(nucleotide)
    label_result.config(text=f"Count of {nucleotide}: {count}")

# Main window
root = tk.Tk()
root.title("🧬 DNA Toolkit")
root.geometry("700x400")
root.resizable(False, False)
root.configure(bg="#2C3E50")  # dark blue background

# Fonts and colors
font_header = ("Helvetica", 16, "bold")
font_label = ("Helvetica", 12)
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 11, "bold")
font_result = ("Helvetica", 13, "italic")

fg_color = "#ECF0F1"  # light text
btn_color = "#3498DB"  # blue buttons
btn_hover_color = "#2980B9"

# Header label
header = tk.Label(root, text="DNA Sequence Analyzer", font=font_header, fg=fg_color, bg=root['bg'])
header.pack(pady=(15, 10))

# Frame for inputs
frame_inputs = tk.Frame(root, bg=root['bg'])
frame_inputs.pack(pady=5)

# DNA input
label_dna = tk.Label(frame_inputs, text="DNA Sequence:", font=font_label, fg=fg_color, bg=root['bg'])
label_dna.grid(row=0, column=0, sticky="e", padx=5, pady=8)

entry_dna = tk.Entry(frame_inputs, font=font_entry, width=30)
entry_dna.grid(row=0, column=1, padx=5, pady=8)

# Nucleotide input for counting
label_nuc = tk.Label(frame_inputs, text="Nucleotide (A/T/C/G):", font=font_label, fg=fg_color, bg=root['bg'])
label_nuc.grid(row=1, column=0, sticky="e", padx=5, pady=8)

entry_nucleotide = tk.Entry(frame_inputs, font=font_entry, width=5)
entry_nucleotide.grid(row=1, column=1, sticky="w", padx=5, pady=8)

# Frame for buttons
frame_buttons = tk.Frame(root, bg=root['bg'])
frame_buttons.pack(pady=15)

def on_enter(e):
    e.widget['background'] = btn_hover_color

def on_leave(e):
    e.widget['background'] = btn_color

# Helper to create styled buttons
def create_button(text, cmd, col):
    btn = tk.Button(frame_buttons, text=text, font=font_button, bg=btn_color, fg=fg_color,
                    activebackground=btn_hover_color, activeforeground=fg_color,
                    padx=15, pady=7, relief="flat", command=cmd, cursor="hand2")
    btn.grid(row=0, column=col, padx=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

btn_length = create_button("Get Length", on_get_length, 0)
btn_valid = create_button("Is Valid?", on_is_valid, 1)
btn_complement = create_button("Get Complement", on_get_complementary, 2)
btn_count = create_button("Count Nucleotide", on_count_nucleotide, 3)

# Result label
label_result = tk.Label(root, text="Result will be shown here", font=font_result, fg="#F39C12", bg=root['bg'])
label_result.pack(pady=10)

root.mainloop()
