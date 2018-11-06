from collections import defaultdict

d = defaultdict(lambda: 'Sunday')

d['one']
d['two'] = 'Monday'
d['three'] = 'Tuesday'

for day in d:
    print d