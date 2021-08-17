import os

basic_name = "core_phase"

for i in range(20):
    count = i + 1
    if count < 10:
        nr = "0" + str(count)
    else:
        nr = str(count)
    with open(basic_name + nr + ".py", 'w') as fp:
        pass