synthesis_index_value = float(input())

if synthesis_index_value < 2:
    print('Analytic')
elif synthesis_index_value <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
