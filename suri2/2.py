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

# 貪欲法の初期解
print("貪欲法の結果")
print("組み合わせ:", combination)
print("合計価格: ", max_price)
print("合計サイズ: ", max_weight)

# 部分的に総当たり法を組み合わせて改良。残った容量で残ったアイテムを総当たりで最適化
remaining_capacity = capacity - max_weight
remaining_items = [i for i in range(n) if combination[i] == 0]

best_additional_price = 0
best_additional_combination = []

# 残ったアイテムの総当たり
for i in range(2 ** len(remaining_items)):
    tmp_weight = 0
    tmp_price = 0
    tmp_combination = [0] * n
    for j in range(len(remaining_items)):
        if i >> j & 1:
            tmp_weight += weight[remaining_items[j]]
            tmp_price += price[remaining_items[j]]
            tmp_combination[remaining_items[j]] = 1
        if tmp_weight > remaining_capacity:
            break
    if tmp_weight <= remaining_capacity and tmp_price > best_additional_price:
        best_additional_price = tmp_price
        best_additional_combination = tmp_combination

# 最終結果を統合
if best_additional_price == 0:
    print("残った容量に追加できるアイテムはありませんでした。")
else:
    final_combination = [max(a, b) for a, b in zip(combination, best_additional_combination)]
    final_price = max_price + best_additional_price
    final_weight = max_weight + sum(weight[i] for i in range(n) if best_additional_combination[i])

    print("改良された結果")
    print("組み合わせ:", final_combination)
    print("合計価格: ", final_price)
    print("合計サイズ: ", final_weight)

# 実行時間計測終了
end_time = time.time()
execution_time = end_time - start_time
print("計算時間: {:.6f}秒".format(execution_time))

