def CheckGenap(n):
    '''
    fungsi untuk menceta angka genap dengan output bolean (benar/salah)
    '''
    if n % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    userInput = input('Masukan angka: ')
    userInputNum = int(userInput)
    print(CheckGenap(userInputNum))
