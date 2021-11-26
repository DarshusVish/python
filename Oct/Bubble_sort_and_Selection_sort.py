
def bsort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

def ssort(list):
    for i in range(len(list)-1):
        m = i
        for j in range(i,len(list)):
            if list[j]< list[m]:
                m = j
        # print(list)
        temp = list[i]
        list[i] = list[m]
        list[m] = temp


ll = [2,4,1,9,5,3]
ssort(ll)

print(ll)