"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***

def sumRows(filename, header=False):
    import csv
    dict = {}
    with open(str(filename)) as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            total = 0
            for i in range(1, len(row)):
                try:
                    int(row[i])
                    total += int(row[i])
                except:
                    total += 0
            dict[row[0]] = total
        if header == True:
            var = list(dict.keys())
            dict.pop(var[0])
        return dict

def sumColumns(filename):
    import csv
    dict = {}
    with open(str(filename)) as csvfile:
        rdr = csv.reader(csvfile)
        for row in rdr:
            counter = 0
            for item in row:
                print(item)
            print(dict)

print(sumColumns("columns.csv"))
