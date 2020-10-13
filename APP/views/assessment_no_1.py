
def post(X, Y):
    temp, outputs, output_length, output_total = [], [], len(X), 0
    for d in X:
        if d >= Y:
            outputs = []
            outputs.append(d)
            return {'Sub Array >= ': outputs}
        else:
            temp.append(int(d))
            output_total += d
            if output_total >= Y and len(temp) <= output_length:
                output_length = len(temp)
                outputs = temp.copy()
                temp = []
                output_total = 0

    if not outputs:
        return {'Sub Array': 'NOT AVAILABLE'}

    output_total = sum(outputs)
    differ = output_total - Y

    if differ > 0:
        if outputs[-1] <= differ:
            del outputs[-1]
        elif outputs[0] <= differ:
            del outputs[0]
        
    return {'Sub Array >= ': outputs }


while True:
    try:
        test_list = list(map(int, input('LIST ELEMETS SEPERATED BY "SPACE": ').split()))
        flag = True
        for d in test_list:
            if d <= 0:
                flag = False
                break
        if flag:
            pass
        else:
            print("\t-----------------------------------------------------------")
            print("\t\tALL LIST ELEMENTS ONLY GRETER THAN 0", test_list)
            print("\t-----------------------------------------------------------")
            exit()
        key = int(input('KEY: '))
        print("\t---------------------------------------------------")
        print('\t\t',post(test_list, key))
        print("\t---------------------------------------------------")

    except:
        print('INVALID INPUT')
