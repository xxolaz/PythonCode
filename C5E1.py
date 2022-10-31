input_numbers = []

print('After entering your numbers please type tcmm or tca, or type help')
while True:
    n = input("Enter a number:")        #asks user to input numbers
    try:
        if str(n) == 'tcmm': #tcmm (total,count,max,min) lets user choose max/min or average
            total = sum(input_numbers)
            count = len(input_numbers)
            largest = max(input_numbers)
            smallest = min(input_numbers)
            print('Total:' , total)
            print('Count:' , count)
            print('Maximum:' , largest)
            print('Minimum:' , smallest)
            break

        elif str(n) == 'tca':     #tca (total,count,average)
            total = sum(input_numbers)
            count = len(input_numbers)
            average = sum(input_numbers) / len(input_numbers)
            print('Total:' , total)
            print('Count:' , count)
            print('Average:' , average)
            break

        elif str(n) == 'help':  #lets user understand what they need to enter and understand what tca/tcmm mean
            print('tca = Total, Count, Average\ntcmm = Total, Count, Max, Min')

        elif int(n) >= 0:       #adds numbers to the list
            input_numbers.append (int(n))

        else:
            pass


    except:
        print('Invaild Input')
