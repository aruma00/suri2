import numpy as np
import time

# 物の個数
n = 8
# 要領
capacity = 25
# 物の重さ、価値
weight = [3, 6, 5, 4, 8, 5, 3, 4]
price = [7, 12, 9, 7, 13, 8, 4, 5]

# 各アイテムの価値/重さの比を計算
value_per_weight = [p / w for p, w in zip(price, weight)]

# アイテムを価値/重さの比が高い順にソート
items = sorted(zip(value_per_weight, weight, price, range(n)), reverse=True)

# 最高の重さと価格と最適な組み合わせを記録する
max_weight = 0
max_price = 0
combination = [0] * n

# 実行時間計測開始
start_time = time.time()

# 容量が許す限りアイテムを追加
for vpw, w, p, index in items:
    if max_weight + w <= capacity:
        max_weight += w
        max_price += p
        combination[index] = 1

# 実行時間計測終了
end_time = time.time()

print("合計が最大になる組み合わせ")
print(combination)
print("合計価格: ", max_price)
print("合計サイズ: ", max_weight)

# 計算時間
execution_time = end_time - start_time
print("計算時間: {:.6f}秒".format(execution_time))
