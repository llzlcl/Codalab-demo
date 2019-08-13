import csv
import sys
import os
from os.path import join
if len(sys.argv) == 1:
    # default local
    ROOT_DIR = os.getcwd()
    DIRS = {
        'reference': join(ROOT_DIR, 'reference'),
        'prediction': join(ROOT_DIR, 'output'),
        'score': join(ROOT_DIR, 'score'),
    }
elif len(sys.argv) == 3:
    # run in codalab
    DIRS = {
        'reference': join(sys.argv[1], 'ref'),
        'prediction': join(sys.argv[1], 'res'),
        'score': sys.argv[2],
    }
else:
    raise ValueError("Wrong number of arguments")
os.makedirs(DIRS['score'], exist_ok=True)
temp=['task1', 'task2']
result_path=sorted([join(DIRS['prediction'],path) for path in temp])
temp=['task1.csv', 'task2.csv']
reference_path=sorted([join(DIRS['reference'],path) for path in temp])


def get_auc(ref,res):
    count=0
    for i in range(len(ref)):
        if ref[i]==res[i]:
            count=count+1
    return count/len(ref)

def write_score(score_file):
    for i in range(len(result_path)):
        result_file=open(result_path[i],'r')
        result_reader=csv.reader(result_file)
        reference_file=open(reference_path[i],'r')
        reference_reader=csv.reader(reference_file)
        for j in range(i+1):
            result=result_reader.__next__()
            reference=reference_reader.__next__()
            auc=get_auc(reference,result)
            score_file.write('task'+str(i)+'_'+str(j)+': '+str(auc)+'\n')

def main():
    with open(join(DIRS['score'],'score.txt'),'w') as score_file:
        write_score(score_file)

if __name__ == '__main__':
    main()

