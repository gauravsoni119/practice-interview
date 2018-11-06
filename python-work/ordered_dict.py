from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['0'] = 'Sunday'
ordered_dict['1'] = 'Monday'
ordered_dict['2'] = 'Tuesday'

unordered_dict = {}
unordered_dict['0'] = 'Sunday'
unordered_dict['1'] = 'Monday'
unordered_dict['2'] = 'Tuesday'

for key, val in ordered_dict.items():
    print val

for key, val in unordered_dict.items():
    print val