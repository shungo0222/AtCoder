import math

a, b, h, m = list(map(int,input().split()))

h_deg = (60*h + m) * (math.pi*2 / 720)
m_deg = m * (math.pi*2 / 60)

cos = math.cos(abs(h_deg - m_deg))

print(math.sqrt((a*a) + (b*b) - (2*a*b*cos)))