import os
import sys

arg = sys.argv

files = arg[1:] if len(arg) >= 2 else [i for i in os.listdir() if i.endswith('.txt')]
_r = lambda x: open(x).read()

for i in files:
    f_content = _r(i)
    f_content = f_content.strip()
    f_content = [j.strip().split("\n") for j in f_content.split("\n\n")]
    validate = set([len(k) for k in f_content]) == {3}
    if(validate):
        # Validated now write tsv file
        f_clean = [z[0].strip('[]').split('-')+z[1:] for z in f_content]
        f_clean = [[int(z[0]), int(z[1])] + z[2:] for z in f_clean]
        outf = i.replace(".txt", ".tsv")
        with open(outf, "w") as fp:
            for y in f_clean:
                fp.write("\t".join([str(m) for m in y]) + "\n")
    else:
        # File corrupted Correct the file
        print(i, [l for l in f_content if len(l) != 3])
