# Analysis

### Task 0 
**Big-oh : O(1)**
- we just access to lists (calls,texts) to read some info.

### Task 1
**Big-oh : O(n^2)**
- in method unique(texts ,calls)--> O(n^2).

### Task 2
**Big-oh : O(n^2)**
- in method longest_time(calls).

### Task 3
**Big-oh : O(n^2)**
- we have many lists in this task but all of them have time-complexity **O(n)**.
- we use the sort method it takes time-complexity **O(nlogn)**.
- in method find_code(calls) **O(n^2)**.
why **O(n^2)**? Because python not like other languages.

**In python :**			  	         	     
  if i[1][:4] not in F_code:     	
     F_code.append(i[1][:4])     				
				 	
**Big-oh :  O(n)** but it seems to be **O(1)**.

**In java :**

for (int j = 0; j< F_code.length;j++){
	 if (F_code[j]!= i[1][:4])
		F_code.append(i[1][:4]);
	}
	
**Big-oh : O(n)** 	

### Task4 : 
**Big-oh : O(n^3)**
- we have one loop Depends on the number of calls.
- we have second loop Depends on the number of telemarketers.
- we use the sort method it takes time-complexity **O(nlogn)**.
- in method find_all_telemarketers (calls,texts) **O(n^3)**.
