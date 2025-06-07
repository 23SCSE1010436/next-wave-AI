import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('data/next_wave_tech.csv')

# ✅ 1. AI Investment Over Time (Line Chart)
ai_df = df[df['Technology'] == 'Artificial Intelligence']
fig1 = px.line(ai_df, x='Year', y='Investment_Billion_USD',
               title='AI Investment Growth (2010–2024)', markers=True)
fig1.update_layout(xaxis_title='Year', yaxis_title='Investment (Billion USD)')
fig1.show()

# ✅ 2. Investment in 2024 (Bar Chart)
latest = df[df['Year'] == 2024]
fig2 = px.bar(latest, x='Technology', y='Investment_Billion_USD',
              title='Technology Investment in 2024', text='Investment_Billion_USD')
fig2.update_traces(textposition='outside')
fig2.update_layout(yaxis_title='Investment (Billion USD)')
fig2.show()

# ✅ 3. Tech Market Share (Pie Chart)
fig3 = px.pie(latest, names='Technology', values='Market_Share',
              title='Technology Market Share in 2024')
fig3.show()
