import math

def get_area_of_rectangle(l, w):
	area = int(math.sqrt(int(math.pow(l[2] - l[0], 2)) + int(math.pow(l[3] - l[1], 2))) * math.sqrt(int(math.pow(w[2] - w[0], 2)) + int(math.pow(w[3] - w[1], 2))))
	return area
rect = input()
def get_coords_of_rec(l,coords):
	return {'bottomLeft': (l[0], l[1]), 'bottomRight': (coords[2], coords[0]), 'topLeft': (l[2], l[3]), 'topRight': (coords[2], coords[3])}

def is_rec_intersect(r1, r2):
	print r1['topLeft']
	if ((r1['topLeft'][0] < r2['bottomRight'][0]) and (r1['bottomRight'][0] > r2['topLeft'][0])
		and (r1['topLeft'][1] < r2['bottomRight'][1]) and (r1['bottomRight'][1] > r2['topLeft'][1])):
		print 'True',
		return True
	else:
		return False
recs = []
areas = []
area = 0
for rec in range(rect):
	l = []
	w = []
	coords = [int(coord) for coord in raw_input().split()]
	print coords
	l.extend((coords[0], coords[1], coords[0], coords[3]))
	w.extend((l[2], l[3], coords[2], coords[3]))
	recs.append(get_coords_of_rec(l, coords))
	print l, recs
	area = area + get_area_of_rectangle(l, w)
	areas.append(area)
	print area
print areas
for rec in range(1, len(recs)):
	print rec
	print is_rec_intersect(recs[rec-1], recs[rec])