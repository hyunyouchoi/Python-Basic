def f(w,h):
    return w*h
w = eval(input("Hourly Wage: "))
h = eval(input("Hours Worked: "))
p = f(w,h)
if w<0 and h <0:
   print("Invalid Value")
if w > 0 and h <= 40 and f(w,h) <= 400:
   p= f(w,h)*0.8
   print("Home pay amount is:",p)
if w > 0 and h > 40 and f(w,h) <= 400:
   p= (f(w,40)+f(w,h-40)*1.5)*0.8
   print("Home pay amount is:",p)
if w > 0 and h > 40 and f(w,h) > 400:
   p= (f(w,40)+f(w,h-40)*1.5)*0.72
   print("Home pay amount is:",p)
if w > 0 and h <= 40 and f(w,h) > 400:
   p= f(w,h)*0.72
   print("Home pay amount is:",p)
