from datetime import date
d1 = date(2008,8,15)
d2 = date(2008,9,15)
    delta = end - start         # timedelta
    for i in range(delta.days + 1):
        d=str(start + timedelta(days=i))
