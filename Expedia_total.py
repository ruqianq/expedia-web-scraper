fname = raw_input("Enter file name: ")  #Ask user for input
input = open(fname,"r")
total_lst = list()
tax_lst = list()
for line in input:
   if "Total:	USD" in line :
    line = line.strip()
    word = line.split()
    total = [word[2]]
    for total_amt in total:
	    if total_amt not in total_lst:
	       total_lst.append(total_amt)
   if "Daily taxes	" in line : 
    line = line.strip()
    word = line.split()
    tax = [word[2]]
    for tax_amt in tax:
	    if tax_amt not in tax_lst:
	       tax_lst.append(tax_amt)
matrix = [tax_lst,total_lst]
for cols in zip(*matrix):
    print " ".join(cols) # it is the end
