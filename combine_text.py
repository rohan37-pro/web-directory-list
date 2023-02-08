import os
from tqdm import tqdm


# altimate = "altimate_directory-list.txt"
# file_list = os.listdir("./")
# print(file_list)
# with open(altimate, 'r') as file:
# 	word_list = file.readlines()
# 	file.close()

# print(f"{len(word_list)} lines loaded from altimate_directory-list")
# for file_name in file_list:
# 	if file_name != "combine_text.py" and file_name != "altimate_directory-list.txt":
# 	    print(f"filename={file_name}")
# 	    temp_list = []
# 	    with open(f"./{file_name}",'r') as file:
# 	        temp_list = file.readlines()
	        
# 	        for i in tqdm(temp_list):
# 	            if i not in word_list:
# 	                word_list.append(i)
# 	        print(f"in {file_name} {len(temp_list)} entries found", end=" --> ")
# 	        print(f"{len(word_list)} new words added..")
# 	        file.close()

# with open(f"./{altimate}",'a') as file:
#     for i in word_list:
#         file.write(f"{i}")
#     file.close()


altimate = "altimate_directory-list.txt"
with open(altimate, 'r') as file:
	word_list = file.readlines()
	file.close()

print(f"{len(word_list)} words found")
print(f"first element is {word_list[0]}")
print(f"word {word_list[0]} also found on index {word_list.index(word_list[0], 1)}")
last_elem_index = word_list.index(word_list[0], 1) -1
print(f'the last element is {word_list[last_elem_index]}')
last_element = word_list[last_elem_index]
print(f"the last element is also found on index {word_list.index(last_element, last_elem_index +1)}")

final_word_list = word_list[:word_list.index(word_list[0], 1)] + word_list[word_list.index(last_element, last_elem_index +1) + 1 : ]

with open("altimate_directory-list2.txt", 'w') as file :
	for i in final_word_list:
		file.write(i)

print("file writing complete ")

# print(f"{len(word_list)} words found")
# print("sorting word list....")
# word_list.sort()
# print("sorting complete")

# temp = []
# for i in tqdm(range(len(word_list)-1)):
# 	if word_list[i] == word_list[i+1]:
# 		word_list.remove(word_list[i])

# print(f"after eleminating {len(word_list)} left")

# with open("altimate_directory-list2.txt", 'w') as file :
# 	for i in word_list:
# 		file.write(i)

# print("file writing complete ")
