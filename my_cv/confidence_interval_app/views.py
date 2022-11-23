from django.shortcuts import render
import pandas as pd


def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        data = pd.read_csv(uploaded_file, sep='\t', header=None)
        # data_tmp = data[[36, 41, 42]]
        # data_tmp[(data_tmp[41] == 'FollowingMode') & (data_tmp[42] == 'success')]
        # mean = data_tmp[(data_tmp[41] == 'FollowingMode') & (data_tmp[42] == 'success')][36].mean()
        # std = data_tmp[(data_tmp[41] == 'FollowingMode') & (data_tmp[42] == 'success')][36].std()
        data = data[[36, 41, 42]]
        data[(data[41] == 'FollowingMode') & (data[42] == 'success')]
        mean = data[(data[41] == 'FollowingMode') & (data[42] == 'success')][36].mean()
        std = data[(data[41] == 'FollowingMode') & (data[42] == 'success')][36].std()

        ans = mean + 2 * std
        content = {'data': ans}

    # print(data.head(3))
    return render(request, 'confidence_interval_app/index.html', content)
