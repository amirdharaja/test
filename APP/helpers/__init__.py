def validate(list_data, key):
        if not list_data or not key:
            return {'status': False, 'detail': 'LIST AND KEY CANNOT BE EMPTY', }

        if not key.isdigit() or int(key) <= 0:
            return {'status': False, 'detail': 'KEY(Y) VALUE MUST BE GREATER THAN EQUAL TO 1', 'given key(Y)': key }

        for d in list_data:
            if not str(d).isdigit() or int(d) <= 0:
                return {'status': False, 'detail': 'LIST(X) CAN CONTAIN NON_NEGATIVE NUMBERS (greater than 1 and above) ONLY', 'given list(X)': list_data }

        return {'status': True}
