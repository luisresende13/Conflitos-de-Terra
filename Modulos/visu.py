import plotly.graph_objects as go

def bar_chart(
    data,
    marker=dict(color='rgba(55, 83, 109, 0.7)', line=dict(color='rgba(55, 83, 109, 1.0)', width=2)),
    title="Conflitos de terra 2000-2021",
    xaxis_title="Município",
    yaxis_title="Registros",
    template='plotly_white',
    width=500,
    height=300        
):

    # Create an interactive bar plot using plotly.graph_objects
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data.index,
        y=data.values,
        marker=marker,
    ))
    
    # Update layout with titles and axis labels
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
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
    height=400
):
    
    # Create an interactive pie chart using plotly.graph_objects
    fig = go.Figure()
    
    fig.add_trace(go.Pie(
        labels=data.index,
        values=data.values,
        hoverinfo=hoverinfo,
        textinfo=textinfo,
        marker=marker
    ))
    
    # Update layout with title
    fig.update_layout(
        title=title,
        template=template,
        width=width,
        height=height
    )
    
    # Show the plot
    fig.show()
