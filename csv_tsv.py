import csv
tmp=csv.reader(open("./data/test_data.csv",'r',encoding='utf-8'),delimiter=',')
csv.writer(open('./data/test_data.tsv', 'w',encoding='utf-8',newline=''), delimiter='\t').writerows(tmp)
