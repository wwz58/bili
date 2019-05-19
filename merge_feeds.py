import pandas as pd
from glob import glob

feeds_path = './feeds'
for dir in glob(feeds_path + '/[!f]*'):
    print dir
    files = sorted(glob(dir + '/*'))
    print files
    if len(files) > 1:
        left_f, right_f = files[-2], files[-1]
        left, right = pd.read_csv(left_f), pd.read_csv(right_f)
        right_keys = set(right['md_id'].tolist())
        for index, row in left.iterrows():
            if row['md_id'] not in right_keys:
                right = right.append(row,ignore_index=True)
        right.to_csv(right_f, index=False)
    else:
        print 'do nothing'
