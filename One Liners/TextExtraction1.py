# Data
text = '''
Call me Ishamel. Some years ago - never mind how long precisaely - having little or no money in my purse,
and nothing particular to intereset me on shore, I thought I would sail about a little and see the water part
of the world. It is a way of driving off the spleen, and regulating the circulation. - Moby Dick'''

# One Liner
w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]

# Result
print(w)
