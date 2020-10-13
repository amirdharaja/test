PROBLEM STATEMENT:
    1. Given an array X and a number y,find the contiguous subarray of smallest length whose sum is greater than y.
    (Note: Array X contains only positive numbers)
        Ex 1: 
            X=[8,17,40,92],
            Y=22
            output subarray can be either [40] or [92]

        Ex 2: 
            X=[8,19,3,4,6] ,
            Y=22
            output subarray is [8,19]
---------------------------------------------------------------------------------------------

ENDPOINTS:
    GET & POST: your-host/test/   <!--#Ex: http://127.0.0.1:8000/test/ -->

---------------------------------------------------------------------------------------------
SAMPLE INPUT 1:
    {
        "list": [8,17,40,92], <!-- X value -->
        "key": "22" <!-- Y value -->
    }

SAMPLE OUTPUT 1:
    {
        "status": true,
        "Sub Array": [
            40
        ]
    }


SAMPLE INPUT 2:
    {
        "list": [8,19,3,4,6], <!-- X value -->
        "key": "22" <!-- Y value -->
    }

SAMPLE OUTPUT 2:
    {
        "status": true,
        "Sub Array": [
            8,
            19
        ]
    }



    2. Create a Django project with single field model and write a GET and POST Rest API using Serializer.
   Give the model name as Test and field name as testdata(type=Textfield), where testdata takes the input in the form of nested dictionary in POST method and 
   returns the same nested dictionary in  GET method.

----------------------------------------- END -------------------------------------------