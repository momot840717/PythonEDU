import numpy as np

class AndPerceptron:
    def __init__(self, input_length=2, weights=None, bias=-1):
        if weights is None:
            self.weights = np.ones(input_length) * 1  # 預設權重為1
        else:
            self.weights = weights
        self.bias = bias

    @staticmethod
    def activation_function(x):
        if x > 0:
            return 1
        return 0

    def __call__(self, input_data):
        weighted_input = self.weights * input_data
        weighted_sum = weighted_input.sum() + self.bias
        return AndPerceptron.activation_function(weighted_sum)




# 設置權重和偏置
weights = np.array([1, 1])
bias = -1

# 創建 AND 邏輯感知機
AND_Gate = AndPerceptron(2, weights, bias)

# 定義輸入數據
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# 測試 AND 邏輯感知機
for x in input_data:
    out = AND_Gate(np.array(x))
    print(f"{x} -> {out}")
