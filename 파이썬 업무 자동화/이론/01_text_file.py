import os

with open("excel.txt", "w", encoding="utf-8") as f:
  for i in range(1, 11):
    f.write(f"{i}번째\n")

# file_folder = "text"

# for i in range(1, 10):
#   f = open(f"{file_folder}/0{i}.txt", "w", encoding="utf-8")
#   f.write(f"{i}번째 텍스트 파일 첫번째 줄입니다.\n")
#   f.write(f"{i}번째 텍스트 파일 두번째 줄입니다.\n")
#   f.write(f"{i}번째 텍스트 파일 세번째 줄입니다.")

# #   f.close()


# for i in range(1, 10):
#   f = open(f"{file_folder}/00{i}.txt", "w", encoding="utf-8")
#   data = [f"{i}번째 텍스트 파일 첫번째 줄입니다.\n", f"{i}번째 텍스트 파일 두번째 줄입니다.\n", f"{i}번째 텍스트 파일 세번째 줄입니다."]
#   f.writelines(data)

#   f.close()

# print("파일 쓰기를 완료했습니다.")

# file_list = os.listdir(file_folder)

# for text_file in file_list:
#   f = open(f"{file_folder}/{text_file}", "r", encoding="utf-8")
#   txt = f.readlines()
#   f.close()

#   print(txt)