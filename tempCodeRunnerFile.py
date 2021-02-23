x_axis_config = {'title':'结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title = '掷一个D6 1000次数结果', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout': my_layout}, filename='d6.html')