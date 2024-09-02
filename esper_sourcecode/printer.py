import time
import os

def printing(sub):
    pre=0
    for i in range(len(sub)):
        try:
            time.sleep(sub[i][0]-pre)
            print(sub[i][1])
            time.sleep(sub[i+1][0]-sub[i][0])
            pre=sub[i+1][0]
            os.system('cls')
        except:
            pass

if __name__=="__main__":
    test = [
        [2,'Replicants are bioengineered humans, designed by Tyrell corporation for use off-world. \nTheir enhanced strength made them ideal slave labor.'],
        [7,''],
        [8,'After a series of violent rebellions, their manufacture became prohibited and Tyrell corp went bankrupt.'],
        [13,''],
        [14,'The collapse of ecosystems in the mid 2020s led to the rise of the industrialist Niander Wallace,\nwhose mastery of synthetic farming averted famine.'],
        [19,''],
        [20,'Wallace acquired the remains of Tyrell corp and created a new line of replicants who obey.'],
        [25,''],
        [26,'Many older model replicants - Nexus 8s with open-ended lifespans - survived.\nThey are hunted down and \'retired\'.'],
        [31,''],
        [32,'Those that hunt them still go by the name...'],
        [36,''],
        [36,'Those that hunt them still go by the name...\nBlade Runner'],
        [40,'']
        ]
    printing(test)