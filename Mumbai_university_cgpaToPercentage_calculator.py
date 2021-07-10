sem3 = float(input('enter your pointer of sem3:'))
sem4 = float(input('enter your pointer of sem4:'))
sem5 = float(input('enter your pointer of sem5:'))
sem6 = float(input('enter your pointer of sem6:'))
sem7 = float(input('enter your pointer of sem7:'))
sem8 = float(input('enter your pointer of sem8:'))


cgpa_avg = (sem3+sem4+sem5+sem6+sem7+sem8)/(6.0)
print('your avg cgpa is:',cgpa_avg)
if cgpa_avg < 6.75:
  print('you are not eligible for placements.') 
    #have some fun here :p
    print("\U0001F923"*4)

elif cgpa_avg > 7.0:
  print('multiply avg_cgpa * 7.4 + 12\n',cgpa_avg*7.4 + 12)
elif cgpa_avg < 7.0:
  print('multiply avg_cgpa* 7.2 +12\n', cgpa_avg*7.2 + 12)
