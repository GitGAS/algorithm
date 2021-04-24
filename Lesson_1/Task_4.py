Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

#############################################################################################

def authorization_1(users_dict, user_name, password):
    """Функция проверяет существование пользователя, соответствие пароля и успешность прохождения авторизации.
    входные параметры:
    - словарь информации по учетным данным
    - имя пользователя
    - пароль
    Сложность: !!!. O(1) - константа.
    """
    if users_dict.get(user_name):                               # !!! O(1)
        if users_dict[user_name]['password'] == password:       # !!! O(1)
            if users_dict[user_name]['is_active'] == 'TRUE':    # !!! O(1)
                return 'access granted'                         # !!! O(1)
            else:
                return 'please activate your account'           # !!! O(1)
        else:
            return 'the password is incorrect'                  # !!! O(1)
    else:
        return 'the user does not exist'                        # !!! O(1)

#############################################################################################

def authorization_2(users_dict, user_name, password):
    """Функция проверяет существование пользователя, соответствие пароля и успешность прохождения авторизации.
    входные параметры:
    - словарь информации по учетным данным
    - имя пользователя
    - пароль
    Сложность: !!!. O(n) - линейная.
    """
    for key, value in users_dict.items():                   # !!! O(n)
        if key == user_name:                                # !!! O(1)
            if value['password'] == password:               # !!! O(1)
                if value['is_active'] == 'TRUE':            # !!! O(1)
                    return 'access granted'                 # !!! O(1)
                else:
                    return 'please activate your account'   # !!! O(1)
            else:
                return 'the password is incorrect'          # !!! O(1)
    else:
        return 'the user does not exist'                    # !!! O(1)

#############################################################################################
users_dict = {
    'kuznetsov': {'password':'qazwsx', 'is_active':'TRUE'},
    'sidorov': {'password':'werkwdkc', 'is_active':'TRUE'},
    'pupkin': {'password':';lbrtbuu', 'is_active':'TRUE'},
    'ivanov': {'password':'tttrrrqqq', 'is_active':'FALSE'},
    'petrov': {'password':'peace', 'is_active':'TRUE'},
    'noname': {'password':'', 'is_active':'FALSE'},
    'guest': {'password':'', 'is_active':'TRUE'}
}

print(authorization_1(users_dict,'kuznetsov','qazwsx'))
print(authorization_1(users_dict,'kuznetsov','qazwsx1'))
print(authorization_1(users_dict,'kuznetsov1','qazwsx1'))
print(authorization_1(users_dict,'ivanov','tttrrrqqq'))

print(authorization_2(users_dict,'kuznetsov','qazwsx'))
print(authorization_2(users_dict,'kuznetsov','qazwsx1'))
print(authorization_2(users_dict,'kuznetsov1','qazwsx1'))
print(authorization_2(users_dict,'ivanov','tttrrrqqq'))