import re

def isValidISBN(isbn):

    isbn = re.sub('[^0-9X]', '', isbn)
    # print(isbn)
    # check for length
    if len(isbn) != 10:
        return False

    # Computing weighted sum
    # of first 9 digits
    _sum = 0
    for i in range(9):
        if 0 <= int(isbn[i]) <= 9:
            _sum += int(isbn[i]) * (10 - i)
        else:
            return False

    # Checking last digit
    if(isbn[9] != 'X' and
       0 <= int(isbn[9]) <= 9):
        return False

    # If last digit is 'X', add
    # 10 to sum, else add its value.
    _sum += 10 if isbn[9] == 'X' else int(isbn[9])

    # Return true if weighted sum of
    # digits is divisible by 11
    return (_sum % 11 == 0)


def is_isbn13(n):
    n = re.sub('[^0-9X]', '', n)
    # print(n)
    if len(n) != 13:
        return False
    product = (sum(int(ch) for ch in n[::2])
               + sum(int(ch) * 3 for ch in n[1::2]))
    return product % 10 == 0

if __name__ == '__main__':
    tests = '''
978-1734314502
978-1734314509
978-1788399081
978-1788399083'''.strip().split()
    for t in tests:
        print(f"ISBN13 {t} validates {is_isbn13(t)}")
# Driver Code
arrISBN = ['978-90-209-7557-4','978-2-87386-537-5','0-596-00048-0','0 9579218 4 3','90-430-0508-8','90-430-0779-X','978-90-209-7455-3','048629868X','0_140009_930','978-0552139823','978-0-596-51774-8','978-1-59059-908-2']

for el in arrISBN:
    if isValidISBN(el):
        print(True)
    else:
        if is_isbn13(el):
            print(True)
        else:
            print(False)
