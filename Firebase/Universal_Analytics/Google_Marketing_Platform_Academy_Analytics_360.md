# Google Marketing Platform Academy: Analytics 360

> 2022/06/20 ~ ing

- source: [Google Skillshop](https://skillshop.exceedlms.com/student/path/248735-google-marketing-platform-academy-analytics-360?sid=f5331f40-1ccb-4efd-972c-094a6d278ebe&sid_i=0)



## GMP Academy: Google Analytics 360 BigQuery export under the hood

- [video](https://youtu.be/SYsExluE2C0)



##### GA360 BigQuery Export 101

- BigQuery as a central element
  - Visualize
  - Analyze
  - Activate



- What is the GA360 BigQuery Export
  - An advanced feature that enables analytics via **unsampled "raw" Analytics 360 data**
  - Unlike reporting, the GA360 BQ export provides **hit level (e.g. page or event) data of users** who visited and interacted on your website
  - The Export is **300+ columns** and each row contains data for 1 hit
    - The file is hierarchical, including **nested fields**



- Opt-in the BigQuery Export
  1. Set up a Google-APIs-Console project and prepare it for BigQuery Export
  2. Link BigQuery to Analytics360 in `Propertiey ➡ All Products ➡ Link BigQuery`



- BigQuery Export data structure 
  - Google Cloud Project
  - BigQuery Dataset
  - Table

![img](https://miro.medium.com/max/1316/1*vpw5oZWBjzxSh-J_KiccRQ.png)



- BigQuery Export Schema
  - GA360 BigQuery Export Schema is available in the Help Center
  - [Help Center](https://support.google.com/analytics/answer/3437719?hl=en)



- Export Modes
  - Data exported in batch multiple times a day
    - Daily tables
    - Intraday tables
  - Data exported continuously (streaming export)
    - Daily tables
    - Realtime tables (should query the view instead of a table)
  - Both intraday and realtime tables are deleted once the daily table is available



- Data freshness
  - `Daily table` < `Intraday table` < `Realtime table`
  - **Daily table**
    - Data shows up for the previous day's activity at ~8am GA timezone
  - **Intraday table**
    - This export happens at least 3 x day, every 8 hours
  - **Realtime table**
    - Realtime streaming of data straight into BigQuery (~15 minutes)
  - Streaming export requires enhances data freshness to be enabled
  - Certain fields such as userId and trafficSource are not available in realtime tables



- What skills are needed to use BigQuery?
  - Understanding of GA and Site Analytics
  - Basic SQL knowledge
  - Strong analytical skills
  - Understand importance of liking data analysis to business decisions



- What if some people in your team are not technical enough to use BigQuery?
  - You can use BigQuery for data analysis and modeling and then export it to Data Studio to create simpler reports



##### GA360 BigQuery Use Cases

- BigQuery Export overcomes these challenges:
  - Access to raw data
  - Individual level customer data
  - Opportunity to perform statistical analysis
  - Ability to tie in other data sources



- Top Use Cases
  - Go Beyond UI Limitations: `Reporting/Visualizaion/Aalysis`
  - Segmentation: `Reporting/Visualizaion/Aalysis` `Activation`
  - Custom Attribution: `Reporting/Visualizaion/Aalysis` `Activation`
  - Predictions with ML: `Reporting/Visualizaion/Aalysis` `Activation`
  - Enhanced Goal Tracking: `Activation`



- Which BQ field can server as a join key?

  - Typically GA's Client ID or Company's User ID (such as CRM or Membership ID)

  - What's available in GA BigQuery

    - `fullVisited` = Client ID (hashed)

    - **`clientId` = Client ID (unhashed)** ➡ MP

    - `userID` = User ID (CRM etc.) ➡ Data Import

    - **`customerDimensions.index` = Custom Dimension XX**

      - Client ID in a cd ➡ Data Import

      - User ID in a cd ➡ Data Import

    - `gclID` ➡ Google Ads/Conversions API



