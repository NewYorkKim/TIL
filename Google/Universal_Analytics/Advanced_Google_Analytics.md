# Advanced Google Analytics

> 2023/01/28 ~ 2023/01/30

- source: [Analytics Academy](https://analytics.google.com/analytics/academy/)

## Data Collection and Processing

### Google Analytics data collection

- A tracking code: to track each user **interaction** that occurs on your website
- A hit: a URL string with parameters of useful information about your users
    - Pageview hit
    - Event hit
        - Action
        - Category
        - Label
        - Value
    - Transaction hit = Ecommerce hit
    - Social hit
    - Page timing hit


### Categorizing into users and sessions

- New vs. Returning Users
    - Cookie ➡ ID
- Sessions
    - Sessions time out after 30 minutes of inactivity by default
- Other data source
    - Measurement Protocol
    - Account Linking

### Applying configuration settings

- Data Filters
- Goals
    - Destination/Pageviews: When user lands on page of website
    - Event: When user performs particular action
    - Duration: Sessions over set amount of time
    - Page/Screens per Session: User views set amount of pages within session
- Data Grouping
- Custom Dimensions: Can be used as secondary dimension, primary dimension, segment
- Custom Metrics
- Imported Data
    - Hit Data
    - Extended data stored in a Custom Dimension or Metric
    - Summary data
- *Once data has been processed you can't apply configuration settings*

### Storing data and generating reports

- Dimensions and Metrics
    - Hit level
    - Session level
    - User level
- Aggregate tables: Are used to quickly display the standard reports in Analytics

### Creating a measurement plan

- Business Objective
- Strategy: Support the objective
- Tactics: Help you achieve your strategies
- Key Performance Indicators(KPIs): Help you measure your macro- or micro-conversions
    - Macro-conversions: Measure the tactics that support your various strategies
    - Micro-conversions: Metrics that help you better understand the user behavior that leads to macro-conversions


## Setting Up Data Collection and Configuration

### Organize your Analytics account

- Organizations
- Properties
    - ex) Website, Mobile
    - Cross-domain tracking = Site linking
        - Google Tag Manager
    - Rollup reporting: Can aggregate data automatically from multiple properties into a new combined property
        - ex) Website + Mobile
- Views
    - Raw Data
    - Test
    - Master
- *Limited number of properties and views*

### Set up advanced filters on views

- Filter
    - Predefined
    - Custom
    - Track activity in a specific website directory or track subdomains of your website in seperate views
    - Normalize the data in your reports to make them easier to use
    

### Create your own Custom Dimensions

- Javascript code
- Scope
    - Hit
    - Session
    - User
    - Product
- Secondary Dimensions

### Create your own Custom Metrics

- Javascript code
- Scope
    - Hit
    - Product
- Formatting Type
    - Integer
    - Currency (Decimal)
    - Time

### More useful configuration

- Demographics and Interests reports
- Internal Site Search
- Calculated Metrics
- Channel Groupings
- Content Grouping
- Enhanced Ecommerce
- User ID
- Data Import


## Advanced Analysis Tools and Techniques

### Segment data for insight

- User segments
    - Span multiple sessions
    - Max date range 90 days
    - ex) age, date, gender
- Session segments
    - Span single session
    - ex) Goal completed, Revenue generated
- User & Session segments
    - Dimensions
    - Metrics
    - Session Dates
    - Sequences of user actions
- Customized segments

### Analyze data by channel

- Last click attribution
- Multi-Channel Funnels (MCF) : Can tell you what role prior marketing activities played in the conversion process
 - Assisted conversion


## Advanced Marketing Tools

### Introduction to remarketing

- Google Search Remarketing
    - Must meet criteria
    - Must have 1000+ users
    - Demgographics dimensions not eligible

### Better targeting with Dynamic Remarketing

- Based on
    - Content or products users previously viewed on your website
    - Related and top-performing content and products
    - Purchase histories
    - Demographics
- Dynamic Remarketing
    - Find vertical attributes
    - Create Custom Dimenisons
    - Update site tags
    - Create Dynamic Remarketing audiences
    - Create Dynamic Remarketing attributes
    - Create Dynamic Remarketing campaign

### Course Summary

- Collect Data
- Create Reports
- Analyze Reports
- Test Solutions