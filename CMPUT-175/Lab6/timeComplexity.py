li = []
for j in range(10): # <--- 10
    for i in range(n) # <--- O(n)
        li.insert(0,i) # <--- O(n)
# O(n^2)

li = []
for j in range(n): # <--- O(n)
    for i in range(n): # <--- O(n)
        li.insert(0,i) # <--- O(n)
# O(n^3)
li = []
for j in range(n): # <--- O(n)
    for i in range(n): # <--- O(n)
        li.insert(0,i) # <--- O(n) }
        li.pop(0) # <--- O(n)      }2 O(n)
# O(n^2*2n) = O(2n^3) = O(n^3)