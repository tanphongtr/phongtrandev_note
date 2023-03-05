def api_view(av_param):
    print('this is api_view {}'.format(av_param))

def swagger(param1, param2):
    print('this is swagger({}, {})'.format(param1, param2))
    def wrap_f(api_view):
        print('this is wrap_f({})'.format(api_view))
        def wrap_api_view(av_param):
            print('this is wrap_api_view({})'.format(av_param))
            api_view(av_param)
        return wrap_api_view
    return wrap_f

@swagger('ahaha', 'ahihi')
def api_view(av_param):
    print('this is api_view {}'.format(av_param))

# api_view('ahoho')
print('---')
swagger('ahaha', 'ahihi')(api_view)('ahoho')
