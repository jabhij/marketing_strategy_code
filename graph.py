import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample Data Preparation
data = {
    'Engagement Stage': ['Email Sent', 'Email Opened', 'Link Clicked', 'Webpage Visit', 'Transaction'],
    'Count': [1000, 750, 500, 300, 100]
}
df_funnel = pd.DataFrame(data)

# Time Spent Heatmap Data  
heatmap_data = pd.DataFrame({
    'Hour': ['8:00 AM', '12:00 PM', '4:00 PM', '8:00 PM'],
    'Clicks': [50, 120, 85, 200]
})

# Revenue vs Campaign Performance (Sample)
campaigns = ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D']
revenue = [20000, 15000, 30000, 18000]
engagement = [80, 60, 90, 70]

# Email Engagement by Region  
regions = ['North', 'South', 'East', 'West']
engagement_rates = [78, 85, 65, 90]

# Funnel Chart  
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
ax.barh(df_funnel['Engagement Stage'], df_funnel['Count'], color='maroon')
ax.set_title('Customer Journey Funnel', fontsize=14, color='maroon')
ax.set_xlabel('Count', fontsize=12, color='maroon')
ax.set_ylabel('Engagement Stage', fontsize=12, color='maroon')
ax.tick_params(axis='x', colors='maroon')
ax.tick_params(axis='y', colors='maroon')
plt.tight_layout()

# Save Chart
maroon_funnel_path = '/abhishekJ/data/maroon_customer_journey_funnel.png'
plt.savefig(maroon_funnel_path)
plt.close()

# Heatmap Chart 
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
bars = ax.bar(heatmap_data['Hour'], heatmap_data['Clicks'], color='maroon')
ax.set_title('Engagement Heatmap by Hour', fontsize=14, color='maroon')
ax.set_xlabel('Time of Day', fontsize=12, color='maroon')
ax.set_ylabel('Clicks', fontsize=12, color='maroon')
ax.tick_params(axis='x', colors='maroon')
ax.tick_params(axis='y', colors='maroon')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 10, str(bar.get_height()), 
            ha='center', color='white', fontsize=10)
plt.tight_layout()

# Save Chart
maroon_heatmap_path = '/abhishekJ/data/maroon_engagement_heatmap.png'
plt.savefig(maroon_heatmap_path)
plt.close()

# Revenue vs Engagement Chart  
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()
ax1.bar(campaigns, revenue, color='maroon', label='Revenue ($)')
ax2.plot(campaigns, engagement, color='darkred', marker='o', label='Engagement Rate (%)')

ax1.set_xlabel('Campaigns', fontsize=12, color='maroon')
ax1.set_ylabel('Revenue ($)', fontsize=12, color='maroon')
ax2.set_ylabel('Engagement Rate (%)', fontsize=12, color='darkred')
ax1.tick_params(axis='x', colors='maroon')
ax1.tick_params(axis='y', colors='maroon')
ax2.tick_params(axis='y', colors='darkred')
ax1.set_title('Campaign Performance: Revenue vs Engagement', fontsize=14, color='maroon')

plt.tight_layout()

# Save Chart
maroon_performance_path = '/abhishekJ/data/maroon_campaign_performance.png'
plt.savefig(maroon_performance_path)
plt.close()

# Email Engagement by Region  
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
bars = ax.bar(regions, engagement_rates, color='maroon')
ax.set_title('Email Engagement by Region', fontsize=14, color='maroon')
ax.set_xlabel('Regions', fontsize=12, color='maroon')
ax.set_ylabel('Engagement Rate (%)', fontsize=12, color='maroon')
ax.tick_params(axis='x', colors='maroon')
ax.tick_params(axis='y', colors='maroon')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, f"{bar.get_height()}%", 
            ha='center', color='white', fontsize=10)
plt.tight_layout()

# Save Chart
maroon_region_engagement_path = '/abhishekJ/data/maroon_email_engagement_region.png'
plt.savefig(maroon_region_engagement_path)
plt.close()
