def compare_files(file_path1, file_path2):
    """Compare two files and return True if they are the same, False otherwise."""
    try:
        with open(file_path1, 'rb') as f1, open(file_path2, 'rb') as f2:
            # Read and compare the files in chunks
            while True:
                chunk1 = f1.read(4096)  # Read 4KB at a time
                chunk2 = f2.read(4096)
                
                if chunk1 != chunk2:
                    return False  # Files are different
                
                if not chunk1:  # End of file reached
                    break
        
        return True  # Files are the same
    except FileNotFoundError:
        print(f"One of the files was not found: {file_path1}, {file_path2}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    # file1 = 'fileCompare/adminRoleWorkspace.json'         
    # file2 = 'fileCompare/adminRoleWorkspace2.json'        
    # file1 = 'fileCompare/India (Copy).xlsx' 
    # file2 = 'fileCompare/India (Copy)2.xlsx'   
    # file1 = 'fileCompare/loaclUser' 
    # file2 = 'fileCompare/loaclUser2'
    file1 = 'fileCompare/India.xlsx'
    file2 = 'fileCompare/India2.xlsx'


    if compare_files(file1, file2):
        print("The files are the same.")
    else:
        print("The files are different.")