import os
from os.path import join
import sys



if len(sys.argv) == 1:
    # default local
    ROOT_DIR = os.getcwd()
    DIRS = {
        'train': join(ROOT_DIR, 'train'),
        'test': join(ROOT_DIR, 'test'),
        'para': join(ROOT_DIR, 'para'),
        'output': join(ROOT_DIR, 'output'),
        'submission': join(ROOT_DIR, 'code_submission')
    }
elif len(sys.argv) == 4:
    # run in codalab
    DIRS = {
        'train': join(sys.argv[1], 'train'),
        'test': join(sys.argv[1], 'test'),
        'para': join(sys.argv[1], 'para'),
        'output': sys.argv[2],
        'submission': sys.argv[3]
    }
else:
    raise ValueError("Wrong number of arguments")

sys.path.append(DIRS['submission'])
import model

def main():    
    temp=['task1', 'task2']
    train_path=sorted([join(DIRS['train'],path) for path in temp])
    para_path=sorted([join(DIRS['para'],path,'variable.ckpt') for path in temp])
    test_path=sorted([join(DIRS['test'],path) for path in temp])
    output_path=sorted([join(DIRS['output'],path) for path in temp])

    for path in [join(DIRS['para'],path) for path in temp]:
        os.makedirs(path, exist_ok=True)
    os.makedirs(DIRS['output'], exist_ok=True)

    model.Model(train_path,para_path,test_path,output_path)


if __name__ == '__main__':
    main()
