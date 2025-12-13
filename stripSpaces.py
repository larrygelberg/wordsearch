# strip_every_other_keep_newlines.py

def strip_every_other_char(infile, outfile):
    with open(infile, 'r', encoding='utf-8') as f:
        data = f.read()

    result = []
    keep = True
    for c in data:
        if c == '\n':
            result.append(c)
            continue
        if keep:
            result.append(c)
        keep = not keep

    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(''.join(result))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python strip_every_other_keep_newlines.py input.txt output.txt")
    else:
        strip_every_other_char(sys.argv[1], sys.argv[2])
