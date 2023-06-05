# %%
"""
'''
write a python3 function that receives a list of doctors and labels that identify their field and other caracteristics, like this: 

[['name', 'labels'], ['Matt', 'board certified oncology'],['Jhoanna','oncology, board certified']], and the function returns all of the oncologist that are board cerified ordered alphabetically
'''
​
'''
doctors = [
    ['Matt', 'board certified, oncology'],
    ['Jhoanna', 'oncology, board certified'],
    ['Sam', 'neurology, board certified']
]
​
SearchParams >
excercise(doctors, ['board certified','oncology'])
​
output: Sam
"""

# %%
# lista de doctores
doctors = [
    ['Matt', 'board certified, oncology'],
    ['Jhoanna', 'oncology, board certified'],
    ['Sam', 'neurology, board certified']
]

# %%
# excercise(doctors, ['board certified','oncology'])

# %%
qualifications_lookup = ['board certified','oncology']

# %%
qualifications_list = [doc[1].split(', ') for doc in doctors]

# %%
qualifications_dict = dict(enumerate(qualifications_list))

# %%
idx_list = []

for idx_searched, qualifs_searched in qualifications_dict.items():
    if qualifs_searched[0] in qualifications_lookup and qualifs_searched[1] in qualifications_lookup:
            idx_list.append(idx_searched)
    else:
        pass

# %%
idx_list

# %%
[idx if  for idx, qualifs in qualifications_dict]

# %%
i = 0
for qualifs in qualifications_list:
    qualifs.split(', ')

# %%
def excercise(doctors_list, qualifications_lookup):
    """This function returns a listed names of the doctors
    given with the qualifications asked in the input"""

    qualifications_list = [doc[1].split(', ') for doc in doctors]

    qualifications_dict = dict(enumerate(qualifications_list))
    
    idx_list = []

    for idx_searched, qualifs_searched in qualifications_dict.items():
        if qualifs_searched[0] in qualifications_lookup and qualifs_searched[1] in qualifications_lookup:
                idx_list.append(idx_searched)
        else:
            pass

    
    new_doctors_list = [doctors_list[idx_got][0] for idx_got in idx_list]
    
    return new_doctors_list

# %%
excercise(doctors, ['board certified','oncology'])

# %%



