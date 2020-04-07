# to update table fields for a teacher

from .models import cltt, tett

def func1(tidi):
    print(f"function request")
    tea = tett.objects.get(tid = tidi)
    cla = cltt.objects.all()
    for data in cla:
        print(f"Checking class" + " " + data.clno + " " + data.clse)
        if (data.clno == tea.cl1 and data.clse == tea.se1 and data.cltime == tea.ti1) or (data.clno == tea.cl2 and data.clse == tea.se2 and data.cltime == tea.ti2) or (data.clno == tea.cl3 and data.clse == tea.se3 and data.cltime == tea.ti3) or (data.clno == tea.cl4 and data.clse == tea.se4 and data.cltime == tea.ti4) or (data.clno == tea.cl5 and data.clse == tea.se5 and data.cltime == tea.ti5) or (data.clno == tea.cl6 and data.clse == tea.se6 and data.cltime == tea.ti6) or (data.clno == tea.cl7 and data.clse == tea.se7 and data.cltime == tea.ti7) or (tea.cl1 > 12 and data.cltime == tea.ti1):
            # start here
            print (f"found class" + " " + data.clno + " " + data.clse)

            # monday
            de = data.m0
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.m1
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.m2
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.m3
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.m4
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.m5
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.m6
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            if (data.cltime == "Summer"):
                de = data.m7
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

                de = data.m8
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

            # tuesday
            de = data.t0
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.t1
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.t2
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.t3
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.t4
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.t5
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.t6
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            if (data.cltime == "Summer"):
                de = data.t7
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

                de = data.t8
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

            # wednesday
            de = data.w0
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.w1
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.w2
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.w3
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.w4
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.w5
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.w6
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            if (data.cltime == "Summer"):
                de = data.w7
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

                de = data.w8
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

            # thursday
            de = data.h0
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.h1
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.h2
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.h3
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.h4
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.h5
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.h6
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            if (data.cltime == "Summer"):
                de = data.h7
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

                de = data.h8
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

            # friday
            de = data.f0
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.f1
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.f2
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.f3
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.f4
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.f5
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.f6
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            if (data.cltime == "Summer"):
                de = data.f7
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

                de = data.f8
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

            # saturday
            de = data.s0
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.s1
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.s2
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.s3
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.s4
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.s5
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.s6
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            if (data.cltime == "Summer"):
                de = data.s7
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

                de = data.s8
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

            # sunday
            de = data.u0
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.u1
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.u2
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.u3
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.u4
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.u5
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            de = data.u6
            if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                tea.m1 += str(data.clno) + " " + data.clse + "|"
                tea.save()

            if (data.cltime == "Summer"):
                de = data.u7
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()

                de = data.u8
                if (de.find(tea.sub1)) or (de.find(tea.sub2)):
                    tea.m1 += str(data.clno) + " " + data.clse + "|"
                    tea.save()