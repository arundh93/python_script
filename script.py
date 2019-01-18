from pathlib import Path
import os

PP_CD = "PP_CD"

p = Path('.')
pathlist = list(p.glob('**/*.txt'))

mappedList = list(map(lambda x: str(x), pathlist))
print(mappedList)

PP_LIST = ["PP1", "PP2", "PP3", "PP4"]

for our_pp in PP_LIST:
    for path in mappedList:
        f = open(path, 'r')
        content = f.read()
        new_content = content.replace(PP_CD, our_pp)
        new_file_path = path.replace(PP_CD, our_pp)
        if not os.path.exists(os.path.dirname(new_file_path)):
            os.makedirs(os.path.dirname(new_file_path))
        nf = open(new_file_path, 'w')
        nf.write(new_content)
