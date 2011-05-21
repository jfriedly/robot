import sys
import re

notes = []

length_dict = {
        "FN": 16,
        "HN": 8,
        "QND": 6,
        "QN": 4,
        "END": 3,
        "EN": 2,
        "SN": 1,
}

with open(sys.argv[1]) as f:
    for line in f:
        res = re.search(r"""ENCODE_NOTE\s*\(\s*([A-GR])\s*,\s*([-0-9]+)\s*,\s*([-0-9]+)\s*,\s*([A-Z]+)\s*\)""", line)
        if res is not None:
            note = ord(res.group(1)) - ord('A')
            if note==17:
                note = 7
            octave = int(res.group(2))
            accidental = int(res.group(3))
            length = length_dict[res.group(4)]

            notes.append(note | (octave << 3) | ((accidental+1)<<7) | (length << 8))

    print 'int champions[] = {'
    for n in notes:
        print '  %d,' % n
    print '};'

