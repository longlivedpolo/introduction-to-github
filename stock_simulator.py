# -*- coding: utf-8 -*-
# 二级市场股票买卖模拟器 - 简单版
# 买方 vs 卖方 概念练习

import random
import time

class StockSimulator:
    def __init__(self):
        self.cash = 100000.0          # 初始资金 10万
        self.portfolio = {}           # 持仓 {股票代码: 股数}
        self.current_price = {"AAPL": 150.0, "TSLA": 250.0, "BABA": 80.0}
        self.history = []

    def show_status(self):
        print("\n=== 当前持仓 & 资金 ===")
        print(f"现金: ¥{self.cash:,.2f}")
        total_value = self.cash
        for stock, shares in self.portfolio.items():
            value = shares * self.current_price.get(stock, 0)
            total_value += value
            print(f"{stock}: {shares}股 × ¥{self.current_price.get(stock,0):.2f} = ¥{value:,.2f}")
        print(f"总资产: ¥{total_value:,.2f}\n")

    def update_price(self):
        for stock in self.current_price:
            change = random.uniform(-5, 5)   # 随机涨跌
            self.current_price[stock] *= (1 + change/100)
            self.current_price[stock] = round(self.current_price[stock], 2)

    def buy(self, stock, shares):
        if stock not in self.current_price:
            print("不支持的股票")
            return
        cost = shares * self.current_price[stock]
        if cost > self.cash:
            print("资金不足！")
            return
        self.cash -= cost
        self.portfolio[stock] = self.portfolio.get(stock, 0) + shares
        print(f"✅ 买入 {shares}股 {stock} @ ¥{self.current_price[stock]:.2f}")

    def sell(self, stock, shares):
        if stock not in self.portfolio or self.portfolio[stock] < shares:
            print("持仓不足！")
            return
        revenue = shares * self.current_price[stock]
        self.cash += revenue
        self.portfolio[stock] -= shares
        if self.portfolio[stock] == 0:
            del self.portfolio[stock]
        print(f"✅ 卖出 {shares}股 {stock} @ ¥{self.current_price[stock]:.2f}")

# ==================== 主程序 ====================
if __name__ == "__main__":
    sim = StockSimulator()
    print("欢迎来到二级市场模拟交易！（买方/卖方练习）")
    print("初始资金：¥100,000")

    while True:
        sim.update_price()
        sim.show_status()
        print("操作： [b]买入  [s]卖出  [q]退出")
        action = input("请输入操作: ").strip().lower()

        if action == 'q':
            print("模拟结束。感谢练习！")
            break
        elif action == 'b':
            stock = input("股票代码 (AAPL/TSLA/BABA): ").upper()
            try:
                shares = int(input("买入股数: "))
                sim.buy(stock, shares)
            except:
                print("输入错误")
        elif action == 's':
            stock = input("股票代码 (AAPL/TSLA/BABA): ").upper()
            try:
                shares = int(input("卖出股数: "))
                sim.sell(stock, shares)
            except:
                print("输入错误")
        else:
            print("无效操作")

        time.sleep(0.5)