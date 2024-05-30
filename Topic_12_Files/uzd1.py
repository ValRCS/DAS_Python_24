def file_line_len(fpath, encoding="utf-8", errors="ignore"):
    # some files have ff fe in the beginning which can cause problems decoding
    with open(fpath, encoding=encoding, errors=errors) as file:
        lines = file.readlines()
        return len(lines)
    
print(file_line_len("Topic_12_Files/frost.txt"))

src = r"C:\Users\val-wd\OneDrive\github\RBS_PBM773_Introduction_to_AI\requirements.txt"
# print(file_line_len(src, encoding="ascii"))
print(file_line_len(src))

