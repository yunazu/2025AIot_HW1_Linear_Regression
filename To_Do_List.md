*Prompt：我需要基於CRISP-DM框架，完成下列 Linear Regression 範例。先依照最終成果要求，說明執行步驟(To do list)。 最終成果要求如下：[...20250920_AutoDeployLR
/2_modified_project_plan.md內容...]*

---
# 🧭 CRISP-DM 專案執行步驟 (To-Do List)
## 1. Business Understanding（業務理解）

### 目標：

建立一個互動式的 Streamlit 應用程式，讓使用者可：

* 自訂資料生成參數 (n, a, var)

* 觀察線性回歸結果

* 識別離群點

### To-do:

* 明確定義應用目的（教育示範、資料科學概念練習）。

* 決定輸出內容（迴歸方程式、R²值、圖表、離群點資訊）。

2. Data Understanding（資料理解）

目標：
了解如何產生與分析模擬資料。

To-do:

* 生成合成資料 (x, y)，根據公式：

``` y=a⋅x+b+noise,noise∼N(0,var) ```

* 探索資料分布特性（均值、變異數、散佈狀況）。

* 可視化散點圖。

## 3. Data Preparation（資料準備）

### 目標：
整理並確保資料格式正確，適合進行回歸分析。

### To-do:

* 使用 NumPy 生成 x 和 y。

* 將資料整理為 pandas DataFrame（包含 x, y）。

* 若有需要，可加入標準化或過濾（此範例可略）。

## 4. Modeling（建模）

### 目標：
利用線性迴歸模型擬合資料，並繪出回歸線。

### To-do:

* 使用 scikit-learn 的 LinearRegression 擬合模型。

* 獲取係數 a_hat, 截距 b_hat。

* 計算預測值 y_pred。

* 計算模型評估指標（例如 R²）。

* 在散點圖上畫出紅色回歸線。

## 5. Evaluation（評估）

### 目標：
評估模型表現與識別異常點（離群點）。

### To-do:

* 計算每個點的殘差（residual = |y - y_pred|）。

* 找出前 5 個殘差最大的點（Top 5 outliers）。

* 在圖上標註離群點（用不同顏色或標籤）。

## 6. Deployment（部署）

### 目標：
使用 Streamlit 建立互動式 Web 介面。

### To-do:

* 使用 Streamlit 建立 UI：

    * st.slider：讓使用者調整 n, a, var

    * st.button 或 st.checkbox：重新生成資料

* 在主畫面顯示：

    * 生成的散點圖與紅色迴歸線

    * 模型方程式與 R²

    * Top 5 離群點的列表

* 確保每次使用者改變參數時，自動重新繪圖。

## ✅ 最終成果 (Deliverables)

Streamlit app 檔案（app.py）

### 功能：

* 可互動調整參數

* 顯示線性回歸結果與 R²

* 可視化散點圖 + 迴歸線

* 標示離群點

### 結果畫面包含：

1. 使用者控制區（參數調整）

2. 圖表區（散點＋回歸線＋離群點）

3. 模型摘要資訊