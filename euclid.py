# gcd(1071, 462)
class Euclid:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.res_r = []
        self.res_s = []
        self.res_t = []
        self.res_q = []

    def euclid(self):
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
            print(f"i = {i}")
            self.res_r.append(self.res_r[i-2] - (self.res_r[i-1] * self.res_q[i-1]))
            print(f"r = {self.res_r[i-2]} - ({self.res_r[i-1]} * {self.res_q[i-1]}) = {self.res_r[i-2] - (self.res_r[i-1] * self.res_q[i-1])}")
            print(f"r = {self.res_r}")
            print(f"r = {self.res_r[i]}")
            if self.res_r[i] == 0:
                break
            self.res_q.append(self.res_r[i-1] // self.res_r[i])
            print(f"q = {self.res_r[i-1]} // {self.res_r[i]} = {self.res_q[i]}")
            self.res_s.append(self.res_s[i-2] - (self.res_s[i-1] * self.res_q[i-1]))
            print(f"s = {self.res_s[i]}")
            self.res_t.append(self.res_t[i-2] - (self.res_t[i-1] * self.res_q[i-1]))
            print(f"t = {self.res_t[i]}\n")
            i += 1
        return self.a * self.res_s[i-1] + self.b * self.res_t[i-1]

tes = Euclid(1071, 462)
hasil = tes.euclid()
print(hasil)