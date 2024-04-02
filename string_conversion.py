# Author:Yi Sun(Tim) 2024-1-31

def steps_to_convert(line1, line2):
    len1, len2 = len(line1), len(line2)
    # 创建一个二维数组 dp，用于存储子问题的最小操作数。数组的行数为 len1 + 1，列数为 len2 + 1。
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    # 初始化数组的第一行和第一列，即当另一个字符串为空时，将当前字符串的字符全部删除或插入的最小操作数。
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    # 开始填充数组，跳过第一行和第一列，因为它们已经在初始化时处理过了。
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # 如果当前字符相等，说明不需要额外操作，继承左上方的最小操作数。
            if line1[i - 1] == line2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 如果当前字符不相等，需要进行操作。在删除、插入、替换三个操作中选择最小的操作数，并加上1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],       # 删除
                                    dp[i][j - 1],      # 插入
                                    dp[i - 1][j - 1])  # 替换
    # 返回 dp 数组的右下角元素，即将 line1 转换为 line2 所需的最小操作数。
    return dp[len1][len2]

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert("line1", "line1") == 0, "eq"
    assert steps_to_convert("line1", "line2") == 1, "2"
    assert steps_to_convert("line", "line2") == 1, "none to 2"
    assert steps_to_convert("ine", "line2") == 2, "need two more"
    assert steps_to_convert("line1", "1enil") == 4, "everything is opposite"
    assert steps_to_convert("", "") == 0, "two empty"
    assert steps_to_convert("l", "") == 1, "one side"
    assert steps_to_convert("", "l") == 1, "another side"
    print("You are good to go!")


