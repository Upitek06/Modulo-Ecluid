# gcd(1071, 462)
class Euclid:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
        self.temp_a = []
        self.temp_b = []
        self.res_r = []
        self.hasil = 0

    def euclid(self):
        while self.a % self.b != 0:
            c = self.a % self.b
            self.res_r.append(c)
            self.a = self.b
            self.temp_a.append(self.a)
            self.b = c
            self.temp_b.append(self.b)
        self.hasil = self.b

class EuclidDiperluas:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.hasil = 0
        self.res_r = []
        self.res_s = []
        self.res_t = []
        self.res_q = []

    def euclid_diperluas(self):
        self.res_r.append(self.a)
        self.res_q.append(0)
        self.res_s.append(1)
        self.res_t.append(0)

        self.res_r.append(self.b)
        self.res_q.append(self.a // self.b)
        self.res_s.append(0)
        self.res_t.append(1)
        i = 2
        while self.res_r[i-1] > 0:
            self.res_r.append(self.res_r[i-2] - (self.res_r[i-1] * self.res_q[i-1]))
            if self.res_r[i] == 0:
                self.res_r.pop()
                break
            self.res_q.append(self.res_r[i-1] // self.res_r[i])
            self.res_s.append(self.res_s[i-2] - (self.res_s[i-1] * self.res_q[i-1]))
            self.res_t.append(self.res_t[i-2] - (self.res_t[i-1] * self.res_q[i-1]))
            i += 1
        self.hasil = self.a * self.res_s[i-1] + self.b * self.res_t[i-1]

class ModularInvers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.hasil = 0
        self.res_r = []
        self.res_s = []
        self.res_t = []
        self.res_q = []

    def modular_invers(self):
        self.res_r.append(self.a)
        self.res_q.append(0)
        self.res_s.append(1)
        self.res_t.append(0)

        self.res_r.append(self.b)
        self.res_q.append(self.a // self.b)
        self.res_s.append(0)
        self.res_t.append(1)
        i = 2
        while self.res_r[i-1] > 0:
            self.res_r.append(self.res_r[i-2] - (self.res_r[i-1] * self.res_q[i-1]))
            if self.res_r[i] != 0:
                self.res_q.append(self.res_r[i-1] // self.res_r[i])
                self.res_s.append(self.res_s[i-2] - (self.res_s[i-1] * self.res_q[i-1]))
                self.res_t.append(self.res_t[i-2] - (self.res_t[i-1] * self.res_q[i-1]))
            else:
                break
            i += 1
        self.hasil = self.a * self.res_s[-1] + self.b * self.res_t[-1]
        if self.hasil != 1:
            return 0
        else:
            self.hasil = self.res_t[-1]
            if self.hasil < 0:
                self.hasil += self.a