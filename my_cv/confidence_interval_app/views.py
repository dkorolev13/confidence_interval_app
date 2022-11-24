from django.shortcuts import render
import pandas as pd


def index(request):
    content = {'data': '...'}
    if request.method == 'POST':

        if 'document' in request.FILES:

            uploaded_file = request.FILES['document']

            data = pd.read_csv(uploaded_file, sep='\t', header=None)
            data_tmp = data[[36, 41, 42]]
            mean = data_tmp[(data_tmp[41] == 'FollowingMode') & (data_tmp[42] == 'success')][36].mean()
            std = data_tmp[(data_tmp[41] == 'FollowingMode') & (data_tmp[42] == 'success')][36].std()

            ans = round(mean + 2 * std, 2)
            content = {'data': ans}
        else:
            content = {'data': '...'}

    return render(request, 'confidence_interval_app/index.html', content)
