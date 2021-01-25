import os
import shutil

origin = os.getcwd()
count = 0
target = 'node_modules'
last_target = ''


def seekAndDestroy():
    global count
    global last_target
    current = os.getcwd()

    repertory = os.listdir()
    print(repertory)
    if target in repertory:
        filepath = os.path.join(current, target)
        last_target = filepath
        shutil.rmtree(filepath, ignore_errors=True)
        count += 1
    for file in repertory:
        nextpath = os.path.join(current, file)
        if os.path.isdir(nextpath):
            os.chdir(nextpath)
            seekAndDestroy()
    return


seekAndDestroy()

print(last_target)
if count == 1:
    print(str(count) + " targets deleted!")
elif count == 1:
    print(str(count) + 'target deleted!')
else:
    print('No target found.')

# top = os.getcwd()
# count = 0
# for root, dirs, files in os.walk(top, topdown=False):
#     for name in dirs:
#         if name == 'node_modules':
#             print(name)
#             count += 1
#             # filename = os.path.join(root, name)
#             # shutil.rmtree(filename, ignore_errors=True)
# print(count + " modules eliminated!")
