# https://leetcode.com/problems/reformat-date/

def reformatDate(date):
    d_struct = date.split()
    try:
        d_struct[0] = int(d_struct[0][0] + d_struct[0][1])
    except:
        d_struct[0] = '0' + str(d_struct[0][0])
    # print(d_struct)
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_no = month_list.index(d_struct[1]) + 1
    if month_no < 10:
            month_no = '0' + str(month_no)
    ref_date = d_struct[2] + '-' + month_no + '-' + d_struct[0]
    return ref_date

date = "1st Mar 2052"
print(reformatDate(date))   

# 24ms; faster than 93%
# 14.3MB; less than 5%