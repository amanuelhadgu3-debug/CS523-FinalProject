# CS523 Big Data Technology – Final Project

# Real-Time E-Commerce Analytics and Distributed Monitoring Platform

This project is an enhanced and modernized version of the original CS523 final project.  
The system simulates real-time e-commerce order streams using Apache Kafka and processes the data using Apache Spark Structured Streaming for live analytics and dashboard visualization.

---

# Enhanced Features Added

## 1. Kafka Real-Time Data Ingestion
- Implemented real-time order event ingestion using Apache Kafka
- Simulated live e-commerce transactions with continuously generated order events
- Kafka topics used for distributed messaging and scalable event streaming

---

## 2. Spark Structured Streaming
- Implemented Apache Spark Structured Streaming for distributed stream processing
- Used DataFrame APIs and micro-batch processing
- Enabled scalable and fault-tolerant real-time analytics

---

## 3. Spark SQL Stream Enrichment (Bonus Requirement)
- Joined streaming order data with static product metadata using Spark SQL
- Added product details including:
    - Product Name
    - Category
    - Brand
- Demonstrated stream-to-static dataset integration

---

## 4. Hive Integration for Processed Data Storage
- Stored processed streaming data into Hive-compatible Parquet tables
- Enabled historical analytics and batch querying
- Created structured warehouse output for downstream analysis

---

## 5. Dynamic Real-Time Dashboard
- Built a live analytics dashboard using Flask
- Visualized:
    - Total Revenue
    - Total Orders
    - Live Streaming Transactions
- Added auto-refreshing UI for real-time monitoring

---

## 6. Real-Time Analytics
- Computed live KPIs including:
    - Revenue aggregation
    - Order count
    - Product/category enrichment
- Enabled continuous stream processing and monitoring

---

## 7. Modern UI Enhancements
- Added modern enterprise dashboard design
- Responsive analytics cards
- Real-time data table updates
- Dark-mode styled monitoring interface

---

# Project Architecture

E-Commerce Order Generator  
→ Kafka  
→ Spark Structured Streaming  
→ Spark SQL Enrichment  
→ Hive/Parquet Storage  
→ Flask Dashboard

---

# Technologies Used

- Apache Kafka
- Apache Spark Structured Streaming
- Spark SQL
- Hive-Compatible Parquet Storage
- Python
- Flask
- Docker
- Pandas
- PyArrow

---

# Dataset Information

The project uses:
- Simulated live e-commerce order streams
- Static product metadata dataset for enrichment

Example enriched fields:
- Product Name
- Category
- Brand
- Quantity
- Revenue

---

# Suggested Execution Flow

## 1. Start Docker Services

```bash
docker compose up -d
