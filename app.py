# app.py
# =======================================
# Linear Regression Demo with Streamlit
# Built under CRISP-DM framework
# =======================================

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -----------------------------------------------------------
# 1️⃣ Business Understanding
# -----------------------------------------------------------
st.title("🔍 Linear Regression Demo (CRISP-DM Framework)")
st.write("""
本應用示範如何依據 **CRISP-DM** 流程建立一個互動式的線性回歸範例：
1. 生成合成資料 (Data Generation)
2. 建立線性回歸模型 (Modeling)
3. 識別離群點 (Outlier Detection)
4. 互動式調整與視覺化 (Deployment)
""")

# -----------------------------------------------------------
# 2️⃣ Data Understanding - User Inputs
# -----------------------------------------------------------
st.sidebar.header("📊 參數設定")

# 使用者可控制的參數
n = st.sidebar.slider("樣本數量 n", min_value=100, max_value=1000, value=300, step=50)
a_true = st.sidebar.slider("真實斜率 a", min_value=-10.0, max_value=10.0, value=3.0, step=0.5)
b_true = st.sidebar.number_input("截距 b", value=5.0)
var = st.sidebar.slider("雜訊變異數 var", min_value=0.0, max_value=1000.0, value=50.0, step=10.0)

st.sidebar.info("可調整參數以觀察資料分布與模型變化")

# -----------------------------------------------------------
# 3️⃣ Data Preparation - Data Generation
# -----------------------------------------------------------
np.random.seed(42)  # 固定亂數以利重現結果
x = np.random.uniform(-10, 10, n)
noise = np.random.normal(0, np.sqrt(var), n)
y = a_true * x + b_true + noise

data = pd.DataFrame({"x": x, "y": y})

st.subheader("📈 生成資料範例 (前10筆)")
st.dataframe(data.head(10))

# -----------------------------------------------------------
# 4️⃣ Modeling - Linear Regression
# -----------------------------------------------------------
model = LinearRegression()
X = x.reshape(-1, 1)
model.fit(X, y)

a_hat = model.coef_[0]
b_hat = model.intercept_
y_pred = model.predict(X)
r2 = model.score(X, y)

st.markdown(f"""
**模型結果：**
- 估計斜率 â = {a_hat:.3f}  
- 截距 b̂ = {b_hat:.3f}  
- R² = {r2:.4f}
""")

# -----------------------------------------------------------
# 5️⃣ Evaluation - Outlier Detection
# -----------------------------------------------------------
# 計算殘差並找出離群點
data["y_pred"] = y_pred
data["residual"] = abs(data["y"] - data["y_pred"])

# 按殘差大小排序，取前5筆離群點
outliers = data.nlargest(5, "residual")

st.subheader("🚨 Top 5 離群點")
st.dataframe(outliers)

# -----------------------------------------------------------
# 6️⃣ Deployment - Visualization (Scatter + Regression line)
# -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(data["x"], data["y"], label="資料點", alpha=0.6)
ax.plot(data["x"], data["y_pred"], color="red", label="回歸線", linewidth=2)

# 標註離群點
ax.scatter(outliers["x"], outliers["y"], color="orange", s=80, label="離群點")
for i, row in outliers.iterrows():
    ax.text(row["x"], row["y"], f"({row['x']:.1f}, {row['y']:.1f})", fontsize=8, color="darkred")

ax.set_title("線性回歸與離群點視覺化")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# -----------------------------------------------------------
# ✅ Summary
# -----------------------------------------------------------
st.markdown("""
---
### 🧭 結論 (CRISP-DM Summary)
- **Business Understanding：** 建立可互動觀察線性回歸與離群點的教學工具  
- **Data Understanding：** 生成符合指定參數的模擬資料  
- **Data Preparation：** 將資料整理為可供迴歸使用的格式  
- **Modeling：** 使用 LinearRegression 擬合資料  
- **Evaluation：** 識別離群點並評估模型擬合度  
- **Deployment：** 以 Streamlit 建立互動式應用  
---
""")
