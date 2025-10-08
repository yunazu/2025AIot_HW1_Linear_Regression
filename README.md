# 🔍 Linear Regression Demo (CRISP-DM Framework)

這是一個以 **CRISP-DM** 流程為基礎的互動式線性回歸範例，透過 **Streamlit** 介面讓使用者可以：
- 自訂資料生成參數（樣本數、斜率、雜訊變異數）
- 視覺化線性回歸結果
- 自動偵測與標示前五大離群點

本專案可作為資料科學、機器學習入門者理解 **CRISP-DM 實務應用流程** 的教學示例。

---

## 🧭 CRISP-DM 專案流程對應

| CRISP-DM 階段 | 對應實作內容 |
|----------------|---------------|
| **1. Business Understanding** | 建立一個互動式線性回歸展示工具 |
| **2. Data Understanding** | 產生模擬資料 `(x, y)` 並分析分布特性 |
| **3. Data Preparation** | 將資料整理為適用於回歸分析的格式 |
| **4. Modeling** | 使用 `scikit-learn` 的 `LinearRegression` 建模 |
| **5. Evaluation** | 計算 R²、找出前 5 名離群點 |
| **6. Deployment** | 使用 Streamlit 建立可視化互動式應用 |

---

## ⚙️ 功能特色

✅ 動態資料生成  
✅ 自動線性回歸擬合與結果顯示  
✅ 離群點偵測與標註  
✅ 互動式 UI（透過 Streamlit Slider 控制）  
✅ 自動重新繪製回歸圖與離群點標籤  

---

## 🧩 專案結構

linear_regression_crispdm/
├── app.py # 主程式 (Streamlit 應用)
├── README.md # 專案說明文件
└── requirements.txt (可選) # 套件需求


---

## 🧰 環境需求

請先安裝 Python 3.9 以上版本，並確保安裝以下套件：

```bash
pip install streamlit scikit-learn numpy pandas matplotlib
（你也可以在專案目錄中建立 requirements.txt 並使用
pip install -r requirements.txt 一次安裝所有依賴）
```

## 🚀 執行方式
下載或複製此專案至本機

在專案根目錄執行：


``` streamlit run app.py ```

Streamlit 啟動後，瀏覽器會自動開啟本地網址
例如：http://localhost:8501

## 🎮 使用說明
在左側側邊欄可調整以下參數：

參數	說明	範圍
n	資料點數量	100 ~ 1000
a	真實斜率	-10 ~ 10
b	截距	任意實數
var	雜訊變異數	0 ~ 1000

每次變更參數後，系統會自動重新生成資料並更新視覺化圖表。

畫面會顯示：

藍色點：模擬資料

紅色線：迴歸模型預測線

橘色點：Top 5 離群點

下方還會列出模型估計值（â、b̂、R²）與離群點明細表。

## 📊 範例畫面

+------------------------------------------+
| 📈 Linear Regression Demo (CRISP-DM)     |
|------------------------------------------|
| 🔹 散點圖 + 回歸線 + 離群點標示          |
| 🔹 R²、斜率、截距顯示                   |
| 🔹 Top 5 離群點資料表                   |
+------------------------------------------+
## 🧠 教學重點
了解 CRISP-DM 流程 在資料分析專案中的應用

理解 線性回歸 (Linear Regression) 基礎概念

實作 離群點偵測 (Outlier Detection)

使用 Streamlit 建立互動式資料分析工具

## 🏁 結論
本專案展示了從資料生成、建模、評估到部署的完整流程，
是學習資料分析專案規劃與線性回歸建模的理想入門範例。

## 📜 授權條款
此專案以 MIT License 授權釋出，可自由使用與修改。