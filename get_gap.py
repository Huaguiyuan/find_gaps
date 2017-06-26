#! python script

import os
cwd = os.getcwd()

with open("band_extrema.dat") as f:
    bands = [ line.split() for line in f ]

remove_indices = {0, 2, 3, 5, 6}
for b in bands:
    b[:] = [ v for i, v in enumerate(b) if i not in remove_indices ]
    b[0] = int(b[0])
    b[1] = float(b[1])
    b[2] = float(b[2])

regions = [ bands[0][1:3] ]
bandnum = [ [ bands[0][0],bands[0][0] ] ]
save = regions[:]

for b in bands:
    regions.append(b[1:3])
    bandnum.append([b[0],b[0]])
    while True:
        l_regions = len(regions)
        done = False
        for j in sorted(xrange(1,l_regions),reverse=True):
            for i in sorted(range(j),reverse=True):
                if regions[j][0] <= regions[i][1] and regions[j][1] >= regions[i][1]:
                    regions[i][1] = regions[j][1]
                    bandnum[i][1] = bandnum[j][1]
                    if regions[j][0] < regions[i][0]:
                        regions[i][0] = regions[j][0]
                        bandnum[i][0] = bandnum[i][0]
                    del regions[j]
                    del bandnum[j]
                    done = True
                    break
                elif regions[j][0] <= regions[i][0] and regions[j][1] >= regions[i][0]:
                    regions[i][0] = regions[j][0]
                    bandnum[i][0] = bandnum[j][0]
                    if regions[j][1] > regions[i][1]:
                        regions[i][1] = regions[j][1]
                        bandnum[i][1] = bandnum[j][1]
                    del regions[j]
                    del bandnum[j]
                    done = True
                    break
            if done:
                break
        if regions==save:
            break
        else:
            save=regions[:]

ngap = len(regions)-1

fw = open( 'gap.dat', 'w+' )
fw.truncate()
fw.write('Total number of gaps: '+str(ngap)+'\n')
for k in range(ngap):
    fw.write('------------------------\n')
    fw.write('No.'+str(k+1)+':\n')
    fw.write('\t'+str(bandnum[k][1])+'\t'+str(regions[k][1])+'\n')
    fw.write('\t'+str(bandnum[k+1][0])+'\t'+str(regions[k+1][0])+'\n')

fw.close()



