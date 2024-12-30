my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] #Стиль кода. Цикл While. 1.2
n = 0
while  n < len(my_list):
    number = my_list[n]
    if number > 0:
        print(number)
    elif number < 0:
        break
    n += 1

# if my_list[n] > 0:
 #       print(my_list[n])
  #      n = n + 1
   # else :
     #   n = n + 1
     #   continue