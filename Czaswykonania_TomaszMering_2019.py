# Program 'Czas wykonania'
# Drukuje czas wykonania danej czynności liczony w godzinach i minutach
# Python 3.7.1

def czas_wykonania():
    t1 = input('Wprowadź czas rozpoczęcia czynności (t1) w formacie cyfr hhmm: ')
    if len(t1) == 4 and t1.isdigit(): # and (t1 < 0 or t1 > 1439):
        h1 = int(t1[0:2])
        m1 = int(t1[2:4])
        czas1 = h1*60 + m1
        #print czas1
    else:
        print ('Podałeś niewłaściwe dane!')
    t2 = input('Wprowadź czas zakończenia czynności (t2>t1) w formacie cyfr hhmm: ')
    if len(t2) == 4 and t2.isdigit(): # and (t2 < 0 or t2 > 1439):
        h2 = int(t2[0:2])
        m2 = int(t2[2:4])
        czas2 = h2*60 + m2
        #print czas2
    else:
        print ('Podałeś niewłaściwe dane!')
    t3 = czas2 - czas1
   #print t3
    print ('\n')
    print ('Czas wykonania czynności w godzinach wynosi: ', int(t3/60), 'godzin.')
    print ('Czas wykonania czynności w minutach wynosi: ', t3 % 60, 'minut(y).')
        
czas_wykonania()

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
