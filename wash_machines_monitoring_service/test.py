from datetime import datetime
import plotly.graph_objects as go

timestamps = []
ampere_values = []

# Read the text file and populate the lists dynamically
with open('wash2.txt', 'r') as file:
    for line in file:
        data = line.strip().split(', ')
        ampere_values.append(float(data[0][2:-1]))
        xd = str(data[3].replace("'", ""))
        xd2 = str(xd.replace(")", ""))
        timestamp = datetime.strptime(xd2, '%d/%m/%Y %H:%M:%S')
        timestamps.append(timestamp)


fig = go.Figure(data=go.Scatter(x=timestamps, y=ampere_values))
fig.update_layout(title='Ampere Values Over Time', xaxis_title='Timestamp', yaxis_title='Ampere')
fig.show()
