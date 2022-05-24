import pandas as pd
import sys
import os
import statistics
import shutil
from datetime import datetime



source_dir = '/home/ubuntu/anbox/logs'
target_dir = '/home/ubuntu/anbox/archives'
means = []
stddevs = []


def fpsReading(f):
    with open('/home/ubuntu/anbox/logs/' + f, '+r') as myfile:
        df_fps = pd.read_json(myfile)
        mean_fps=df_fps.loc['frames_per_second']['video']['mean']
        std_fps=df_fps.loc['frames_per_second']['video']['stddev']
        means.append(mean_fps)
        stddevs.append(std_fps)
    return means, stddevs

def moveFiles(filenames):
    now = datetime.now()

    for afile in filenames:
        new_file = afile + str(now.strftime("-%d-%m-%Y-%H-%M-%S")) 
        shutil.move(os.path.join(source_dir, afile), target_dir)
        os.rename(target_dir + '/' + afile, target_dir + '/' + new_file)


def main():
    entries = os.listdir('/home/ubuntu/anbox/logs/')
    print('Number of running containers: ', len(entries))
    for i in entries:
        means, stddevs = fpsReading(i)
    print('list of ave. fps: ', means)
    print('list of stddev: ', stddevs)
    print('means:   ', statistics.mean(means))
    print('stddevs: ', statistics.mean(stddevs))
    moveFiles(entries)

if __name__ == '__main__':
    main()


