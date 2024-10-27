#def format_name(f_name, l_name):
#     title_f_name=f_name.title()
#     title_l_name=l_name.title()
#     return title_f_name +" "+title_l_name
# print(format_name("EWELINA", "kOlEBuk"))

def is_leap_year(year):
    """Check if the year is leap"""
    # Write your code here.
    # Don't change the function name.
    if year%4==0:
        if year%100==0 and not year%400==0:
           return False
        return True
    else:
        return False

print(is_leap_year(100))

# Angela's solution
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False