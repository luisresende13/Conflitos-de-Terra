import plotly.graph_objects as go

def bar_chart(
    data,
    marker=dict(color='rgba(55, 83, 109, 0.7)', line=dict(color='rgba(55, 83, 109, 1.0)', width=2)),
    title="Conflitos de terra 2000-2021",
    xaxis_title="Município",
    yaxis_title="Registros",
    template='plotly_white',
    width=500,
    height=300,
    title_font=dict(family="Arial", size=20, color="black"),
    xaxis_font=dict(family="Arial", size=14, color="black"),
    yaxis_font=dict(family="Arial", size=14, color="black")
):
    # Create an interactive bar plot using plotly.graph_objects
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data.index,
        y=data.values,
        marker=marker,
    ))
    
    # Update layout with titles, axis labels, and font customization
    fig.update_layout(
        title=dict(text=title, font=title_font),
        xaxis=dict(title=xaxis_title, titlefont=xaxis_font),
        yaxis=dict(title=yaxis_title, titlefont=yaxis_font),
        template=template,
        width=width,
        height=height
    )
    
    # Show the plot
    fig.show()

def pie_chart(
    data,
    hoverinfo='label+percent',
    textinfo='value+percent',
    marker=dict(line=dict(color='rgba(55, 83, 109, 1.0)', width=2)),
    title="Conflitos de terra 2000-2021",
    template='plotly_white',
    width=600,
    height=400,
    title_font=dict(family="Arial", size=20, color="black"),
    label_font=dict(family="Arial", size=14, color="black"),
    color_map={}
):
    # Use the color map to set colors based on the state
    if color_map:
        colors = [color_map[label] for label in data.index]
        marker['colors'] = colors
        
    # Create an interactive pie chart using plotly.graph_objects
    fig = go.Figure()
    
    fig.add_trace(go.Pie(
        labels=data.index,
        values=data.values,
        hoverinfo=hoverinfo,
        textinfo=textinfo,
        marker=marker,
        textfont=label_font  # Custom font for the pie chart labels
    ))
    
    # Update layout with title and title font customization
    fig.update_layout(
        title=dict(text=title, font=title_font),
        template=template,
        width=width,
        height=height
    )
    
    # Show the plot
    fig.show()

color_maps = [{
    'SC': 'rgba(255, 99, 132, 0.7)',    # Santa Catarina
    'RS': 'rgba(54, 162, 235, 0.7)',     # Rio Grande do Sul
    'RR': 'rgba(255, 206, 86, 0.7)',     # Roraima
    'RO': 'rgba(75, 192, 192, 0.7)',     # Rondônia
    'PR': 'rgba(153, 102, 255, 0.7)',    # Paraná
    'PA': 'rgba(255, 159, 64, 0.7)',     # Pará
    'MT': 'rgba(255, 99, 71, 0.7)',      # Mato Grosso
    'MS': 'rgba(123, 239, 178, 0.7)',    # Mato Grosso do Sul
    'AP': 'rgba(255, 105, 180, 0.7)',    # Amapá
    'AM': 'rgba(0, 204, 204, 0.7)',       # Amazonas
    'AC': 'rgba(255, 165, 0, 0.7)'        # Acre
}, {
    'SC': 'rgba(34, 193, 195, 0.7)',     # Turquoise
    'RS': 'rgba(253, 187, 45, 0.7)',     # Orange Yellow
    'RR': 'rgba(0, 150, 136, 0.7)',       # Teal
    'RO': 'rgba(244, 67, 54, 0.7)',       # Red
    'PR': 'rgba(33, 150, 243, 0.7)',      # Blue
    'PA': 'rgba(156, 39, 176, 0.7)',      # Purple
    'MT': 'rgba(76, 175, 80, 0.7)',       # Green
    'MS': 'rgba(255, 235, 59, 0.7)',      # Yellow
    'AP': 'rgba(255, 82, 82, 0.7)',       # Pink
    'AM': 'rgba(62, 39, 35, 0.7)',        # Brown
    'AC': 'rgba(255, 193, 7, 0.7)'        # Amber
}, {
    'SC': 'rgba(255, 20, 147, 0.7)',      # Deep Pink
    'RS': 'rgba(70, 130, 180, 0.7)',      # Steel Blue
    'RR': 'rgba(255, 140, 0, 0.7)',       # Dark Orange
    'RO': 'rgba(0, 128, 128, 0.7)',       # Teal
    'PR': 'rgba(186, 85, 211, 0.7)',      # Medium Orchid
    'PA': 'rgba(127, 255, 212, 0.7)',     # Light Sea Green
    'MT': 'rgba(255, 69, 0, 0.7)',        # Red Orange
    'MS': 'rgba(60, 179, 113, 0.7)',      # Medium Sea Green
    'AP': 'rgba(255, 192, 203, 0.7)',     # Pink
    'AM': 'rgba(255, 255, 0, 0.7)',       # Yellow
    'AC': 'rgba(160, 82, 45, 0.7)'        # Sienna
}]
