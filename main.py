import numpy as np
import sub1
import sub2
import sub3

a = np.array([25, 46, 81, 30, 22])
ave = sub1.ave(a)
print("ave = ", ave)
sum = sub2.sum(a)
mult = sub2.mult(a)
print("sum = ", sum)
print("mult = ", mult)
diff = sub3.diff(a)
print("diff = ", diff)
