user_info={'first_name':'имя','last_name':'фамилия'}
user_info['first_name']=input('Введите имя ')
user_info['last_name']=input('Введите фамилию ')
info=user_info.get('last_name')+' '+user_info.get('first_name')
print(info)