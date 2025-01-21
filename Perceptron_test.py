import numpy as np

class Perceptron:
    def __init__(self, weights=None, bias=-1 , input_length=2):
        if weights is None:
            self.weights = np.ones(input_length)  # 預設權重為 [1. 1.]
        else:
            self.weights = weights
        self.bias = bias

    @staticmethod
    def activation_function(x):
        if x > 0:
            return 1
        return 0

    def __call__(self, input_data):
        weighted_input = np.dot(self.weights, input_data)
        weighted_sum = weighted_input.sum() + self.bias
        return Perceptron.activation_function(weighted_sum)




# 設置權重和偏置
weights = np.array([1, 1])
bias = -1

# 創建 AND 感知器
AND_Gate = Perceptron(weights, bias)

# 定義輸入數據
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# 資料代入 AND 感知器
for x in input_data:
    out = AND_Gate(np.array(x))
    print(f"{x} -> {out}")


### 嘗試做出 or 感知器