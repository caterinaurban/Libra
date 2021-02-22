import os

def order(logfile):
    D = dict()
    D['boxes'] = 0
    D['symbolic'] = 10
    D['deeppoly'] = 20
    D['neurify'] = 30
    D['boxes_deeppoly'] = 40
    D['boxes_neurify'] = 50
    D['deeppoly_symbolic'] = 60
    D['neurify_symbolic'] = 70
    D['deeppoly_neurify'] = 80
    D['boxes_deeppoly_neurify'] = 90
    D['deeppoly_neurify_symbolic'] = 100
    C = dict()
    C['4'] = 0
    C['8'] = 200
    C['16'] = 400
    C['32'] = 600
    C['64'] = 800
    name = logfile.split('-')       # ['japanese', '20', 'boxes', '4cpu.log']
    return D[name[2]] + C[name[3].replace('cpu.log', '')]

# current directory
directory = os.fsencode('.').decode('utf-8')

header = ['File Name', 'L', 'U', 'Input', '|C|', '|F|p', '|F|f', 'Time']
print('\t '.join(header))

logs = [logfile for logfile in os.listdir(directory) if logfile.endswith('.log')]

# for each logfile in the current directory
for logfile in sorted(logs, key=order):
    # for each line of the current logfile
    with open(logfile, 'r', encoding='latin-1') as filename:
        tuned = None
        found = None
        compressed = None
        pre = None
        result = None
        total = None
        for line in filename:
            if line.startswith('Autotuned to: '):   # Autotuned to: L = 0.03125, U = 5
                tuned = line.split()
            if line.startswith('Found: '):
                found = line.split()
            if line.startswith('Compressed'):
                compressed = line.split()
            if line.startswith('Pre-Analysis Result: '):
                pre = line.split()
            if line.startswith('Result: '):
                result = line.split()
            if line.startswith('Total'):
                total = line.split()

        lower = tuned[4].strip(',')
        upper = tuned[7]

        patterns = found[1]
        zipped = compressed[2] if compressed else ''
        rest = found[4].split('[')
        feasible = rest[0]
        completed = rest[1].strip(']')

        _space = float(pre[4].strip('()').strip('%'))
        space = '{0:.2f}%'.format(_space)

        if total != None:
            seconds = float(total[-2].strip('s'))
            hours = seconds // 3600
            hours_str = str(hours)
            minutes = (seconds % 3600) // 60
            total_minutes = str(seconds // 60).split(".")[0]
            seconds = seconds % 60
            time =  '|{}h |{}m |{}s'.format(int(hours), int(minutes), int(seconds)).replace('|0h ', '').replace('|0m ', '').replace('|', '')
        else:
            total_minutes = "NN"
            time = "still running"

        if compressed:
            fetched = [logfile, lower, upper, space, completed, zipped, feasible, hours_str, time]
        else:
            fetched = [logfile, lower, upper, space, completed, patterns, feasible, hours_str, time]
        print('\t '.join(fetched))
