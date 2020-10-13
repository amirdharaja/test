
def post(X, Y):
    temp, outputs, output_length, output_total = [], [], len(X), 0
    for d in X:
        if d >= Y:
            temp = []
            temp.append(d)
            return {'Sub Array': temp}
        else:
            temp.append(int(d))
            output_total += d
            if output_total >= Y and len(temp) < output_length:
                output_length = len(temp)
                outputs = temp.copy()
                temp = []
                output_total = 0

    if not outputs:
        return {'Sub Array': 'NOT AVAILABLE'}

    return {'Sub Array': outputs }


test_list = list(map(int, input('LIST ELEMETS').split()))
key = int(input('KEY: '))
print(post(test_list, key))
