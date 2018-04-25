def make_readable(seconds):
    res = []
    if seconds > 3599:
        hour = seconds / 3600
        seconds = seconds % 3600
        res.append('%02d:' % hour)
    else:
        res.append('00:')
        
    if seconds > 59:
        min = seconds / 60
        seconds = seconds % 60
        res.append('%02d:' % min)
    else:
        res.append('00:')
        
    if seconds > 0:
        res.append('%02d' % seconds)
    else:
        res.append('00')
    # Do something
    return ''.join(res)
