from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from experiments import run_all, run_one

if __name__ == '__main__':
    experiment_name = sys.argv[1] if len(sys.argv) > 1 else ''

    if not experiment_name or experiment_name == 'ALL':
        run_all()
    else:
        run_one(experiment_name)
