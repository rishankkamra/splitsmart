print('Welcome To The SplitSmart App')
person = input('Enter Your Name: ')
print('Enter 1 if you want to view your Balance or Enter 2 if you want to Add Expense: ')
while True:
    rn = int(input('Enter 1 or 2: '))
    if rn == 1:
        print("You have chosen 'View Balance'.")
        with open(person, 'r') as t:
            d = t.readlines()
            i = 0
            no_user = len(d) / 2
            print(no_user)
            # print(d)
            all_user = []
            for user in range(int(no_user)):
                u = []
                u.sort
                for x in range(2):
                    u.append(d[i + x])
                i = +2

                all_user.append(u)
            print(all_user)

        break
    elif rn == 2:
        print("You have chosen 2 'Add Expenses'. ")
        print('Enter the space separated names of the members:')
        members_names = (input())
        print('Total amount paid:')
        amount_paid = int(input())
        z = members_names.split()
        d = z, amount_paid
        emp_list = []

        num_of_members = len(z)
        p = amount_paid / (num_of_members + 1)
        for i in range(len(z)):
            y = (emp_list.append(z[i]))
            for i in range(1):
                j = (emp_list.append(p))
        print(emp_list)
        with open(person, 'a') as filecope:
            for leadset in emp_list:
                filecope.write('%s\n' % leadset)

        g = open(person, 'r')
        cc = (g.readlines())
    g.close()
    break