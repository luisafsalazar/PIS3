import os

def is_file_empty(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) == 0

def verify_nifti_files(root):
    empty_files = []
    
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(('.nii', '.nii.gz')):  # Puedes agregar más extensiones si es necesario
                file_path = os.path.join(dirpath, filename)
                if is_file_empty(file_path):
                    empty_files.append(file_path)
                    print(f"Archivo vacío encontrado: {file_path}")
    
    if not empty_files:
        print("No se encontraron archivos vacíos.")
    else:
        print(f"\nSe encontraron {len(empty_files)} archivos vacíos.")

if __name__ == "__main__":
    # Cambia esta ruta a la carpeta que deseas verificar
    root_directory = "C:/Users/user/Desktop/Lu_novia_linda/images_filtradas"
    verify_nifti_files(root_directory)
