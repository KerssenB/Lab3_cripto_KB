def modify_string(string):
    if not string:
        return "0"
    
    # Cambiar la primera letra por Mayúscula y Agregar 0 al final.
    new_string = string[0].upper() + string[1:]
    new_string += '0'
    
    return new_string

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='latin-1') as infile:
        lines = infile.readlines()
        
    formatted_lines = []
    for line in lines:
        stripped_line = line.strip()
            
        # Omitir las líneas que están vacías o comienzan con un nùmero.
        if not stripped_line or stripped_line[0].isdigit():
            continue 
            
        formatted_lines.append(modify_string(stripped_line))
        lines_count = len(formatted_lines)
        
    with open(output_file, 'w', encoding='latin-1') as outfile:
        for line in formatted_lines:    
            outfile.write(line + '\n')
        
    print(f"Se ha combiado el .dic correctamente. Cantidad de contraseñas: " + str(lines_count) + ".")
    
    
input_file = "rockyou.dic"
output_file = "rockyou_mod.dic"
    
process_file(input_file, output_file)
