if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])
    records = sorted(sorted(records, key=lambda x: x[1])[1:3])

    for i in records:
        print(i[0], sep='\n')
