from datetime import datetime 

def get_days_from_today(date):
   
    try:

        input_date = datetime.strptime(date, '%Y-%m-%d').date()

        today = datetime.today().date()

        delta = input_date - today

        return delta.days 
    
    except ValueError:

        print ('Ви ввели неправильний формати дати. Введіть в форматі \'YYYY-MM-DD\'')

        return None
    
print (get_days_from_today('2025-12-10'))