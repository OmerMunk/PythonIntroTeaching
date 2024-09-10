nums = [1, 2, 3]
assets = [
    {1, 2, 3},
    {2, 3, 4},
    {3, 4, 5},
    {3, 4, 5},
    {3, 4, 5},
]

print(nums)
print(*nums) # ==== print(1, 2, 3)
# all_sets = set.union(assets[0], assets[1], assets[2])
all_sets = set.union(*assets)

def u_and_i_sets(sets):
    return set.union(*sets), set.intersection(*sets)