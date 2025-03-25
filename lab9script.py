import tkinter as tk
from tkinter import ttk, messagebox
from poke_api import get_pokemon_info

# Define the function to handle the "Get Info" button click event.
# This function will fetch the Pokemon information from the PokeAPI and update the GUI elements accordingly.
def handle_btn_get_info():
    poke_name = ent_name.get()
    poke_info = get_pokemon_info(poke_name)
    
    # Check if the information was fetched successfully
    # If the information was fetched successfully, update the GUI elements with the fetched information.
    if poke_info:
        # Update Info
        lbl_height_val['text'] = f"{poke_info['height']} dm"
        lbl_weight_val['text'] = f"{poke_info['weight']} hg"
        lbl_type_val['text'] = ', '.join([t['type']['name'] for t in poke_info['types']])
        
        # Update Stats
        bar_hp['value'] = poke_info['stats'][0]['base_stat']
        bar_attack['value'] = poke_info['stats'][1]['base_stat']
        bar_defense['value'] = poke_info['stats'][2]['base_stat']
        bar_sp_atk['value'] = poke_info['stats'][3]['base_stat']
        bar_sp_def['value'] = poke_info['stats'][4]['base_stat']
        bar_speed['value'] = poke_info['stats'][5]['base_stat']
    else:
        messagebox.showerror("Error", f"Unable to fetch information for {poke_name} from the PokeAPI.")

# Define the main function to create the GUI elements.
# This function creates the main window, input frame, info frame, and stats frame.
def main():
    global ent_name, lbl_height_val, lbl_weight_val, lbl_type_val
    global bar_hp, bar_attack, bar_defense, bar_sp_atk, bar_sp_def, bar_speed

    # Create the main window
    root = tk.Tk()
    root.title("Pokémon Information Viewer")
    
    # Input Frame
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2, pady=(20, 10))
    
    lbl_name = ttk.Label(frm_input, text="Pokémon Name:")
    lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)
    
    ent_name = ttk.Entry(frm_input)
    ent_name.grid(row=0, column=1)
    
    btn_get_info = ttk.Button(frm_input, text="Get Info", command=handle_btn_get_info)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10, sticky="W")
    
    # Info Frame
    lblfrm_info = ttk.LabelFrame(root, text="Info")
    lblfrm_info.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="N")
    
    lbl_height = ttk.Label(lblfrm_info, text="Height:")
    lbl_height.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="E")
    lbl_height_val = ttk.Label(lblfrm_info, width=20)
    lbl_height_val.grid(row=0, column=1, padx=(0, 10), pady=(10, 5), sticky="W")
    
    lbl_weight = ttk.Label(lblfrm_info, text="Weight:")
    lbl_weight.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="E")
    lbl_weight_val = ttk.Label(lblfrm_info)
    lbl_weight_val.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="W")
    
    lbl_type = ttk.Label(lblfrm_info, text="Type:")
    lbl_type.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="E")
    lbl_type_val = ttk.Label(lblfrm_info)
    lbl_type_val.grid(row=2, column=1, padx=(0, 10), pady=5, sticky="W")
    
    # Stats Frame
    lblfrm_stats = ttk.LabelFrame(root, text="Stats")
    lblfrm_stats.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky="N")
    
    stats_labels = ["HP:", "Attack:", "Defense:", "Special Attack:", "Special Defense:", "Speed:"]
    stats_bars = []
    for i, label in enumerate(stats_labels):
        lbl_stat = ttk.Label(lblfrm_stats, text=label)
        lbl_stat.grid(row=i, column=0, padx=(10, 5), pady=5, sticky="E")
        bar_stat = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
        bar_stat.grid(row=i, column=1, padx=(0, 10), pady=5)
        stats_bars.append(bar_stat)
    
    bar_hp, bar_attack, bar_defense, bar_sp_atk, bar_sp_def, bar_speed = stats_bars
    
    root.mainloop()

main()