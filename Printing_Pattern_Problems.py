guest = ['rahul','pankaj','nitin']
for x in guest:
    print(x.title() + ' You are invoted for the dinner ...!')

print('Hey there , Nitin will not be able to make it.')
guest[2] = 'sushil'
print('Hello all ! we found a bigger table and inviting others at the dinner.')
guest.insert(0,'manoj')
guest.insert(2,'kuldeep')
guest.append('suresh')

for y in guest:
    print(y.title()  + ' ! You are invited for the dinner.')

