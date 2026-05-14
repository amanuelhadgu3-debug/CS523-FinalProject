from flask import Flask, render_template_string
import pandas as pd
import glob
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>

<head>

<title>E-Commerce Streaming Dashboard</title>

<meta http-equiv="refresh" content="2">

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:'Poppins',sans-serif;
    background:linear-gradient(135deg,#0f172a,#020617);
    color:white;
    padding:30px;
}

.header{
    margin-bottom:30px;
}

h1{
    font-size:48px;
    font-weight:700;
    color:#00ffcc;
    margin-bottom:10px;
}

.subtitle{
    color:#94a3b8;
    font-size:18px;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
    margin-bottom:30px;
}

.card{
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    padding:25px;
    box-shadow:0 10px 30px rgba(0,0,0,0.4);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
}

.card-title{
    color:#94a3b8;
    font-size:16px;
    margin-bottom:10px;
}

.card-value{
    font-size:36px;
    font-weight:700;
    color:#00ffcc;
}

.table-container{
    background:rgba(255,255,255,0.05);
    border-radius:20px;
    overflow:hidden;
    box-shadow:0 10px 30px rgba(0,0,0,0.4);
}

table{
    width:100%;
    border-collapse:collapse;
}

th{
    background:#111827;
    color:#00ffcc;
    padding:18px;
    font-size:15px;
    text-transform:uppercase;
    letter-spacing:1px;
}

td{
    padding:16px;
    text-align:center;
    border-bottom:1px solid rgba(255,255,255,0.05);
    color:#f8fafc;
}

tr:nth-child(even){
    background:rgba(255,255,255,0.02);
}

tr:hover{
    background:rgba(0,255,204,0.08);
}

.footer{
    margin-top:30px;
    text-align:center;
    color:#64748b;
    font-size:14px;
}

.badge{
    background:#00ffcc22;
    color:#00ffcc;
    padding:6px 12px;
    border-radius:999px;
    font-size:13px;
    display:inline-block;
    margin-top:10px;
}

</style>

</head>

<body>

<div class="header">
    <h1>🛒 Live E-Commerce Analytics</h1>

    <div class="subtitle">
        Real-Time Streaming Dashboard using Kafka + Spark + Flask
    </div>

    <div class="badge">
        LIVE STREAM ACTIVE
    </div>
</div>

<div class="cards">

    <div class="card">
        <div class="card-title">💰 Total Revenue</div>
        <div class="card-value">${{ revenue }}</div>
    </div>

    <div class="card">
        <div class="card-title">📦 Total Orders</div>
        <div class="card-value">{{ orders }}</div>
    </div>

</div>

<div class="table-container">
    {{ table | safe }}
</div>

<div class="footer">
    CS523 Big Data Streaming Project • Spark Structured Streaming
</div>

</body>
</html>
"""

@app.route("/")
def home():

    files = glob.glob("../hive_output/*.parquet")

    valid_files = [f for f in files if os.path.getsize(f) > 0]

    if not valid_files:
        return "No streaming data yet"

    latest_file = max(valid_files, key=os.path.getctime)

    df = pd.read_parquet(latest_file)

    revenue = round(df["total_amount"].sum(), 2)
    orders = len(df)

    table = df.tail(20).to_html(
        index=False,
        classes="table",
        border=0
    )

    return render_template_string(
        HTML,
        table=table,
        revenue=revenue,
        orders=orders
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)