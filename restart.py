def main():
    with open('last_prime.txt', 'r+') as f:
        f.seek(0)
        f.truncate()
        f.write('2')

if __name__ == '__main__':
    main()