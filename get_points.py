import matplotlib.pyplot as plt

file_name = input("What is the name of the file:")

fig, ax = plt.subplots()
ax.axis('equal')
pts = plt.ginput(-1, 0)
n = len(pts)

file_path = 'points/'
with open(file_path + file_name, 'w+') as f:
    f.write('%d\n' % n)
    for (x, y) in pts:
        f.write('%f %f\n' % (x, y))