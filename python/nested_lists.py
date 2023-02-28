records = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
    
all_marks = list(set([x[1] for x in records]))
sorted_marks = sorted(all_marks)

if len(sorted_marks) > 1:
    second_highest = sorted_marks[1]

    names = []
    for name, marks in filter(lambda x: x[1] == second_highest, records):
        names.append(name)
        
    for i in sorted(names):
        print(i)
