sx, sy, gx, gy = map(int, input().split())
gy *= -1

print(-((gx - sx) / (gy - sy) * sy) + sx)