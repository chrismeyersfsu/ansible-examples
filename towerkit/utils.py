
def get_or_create(obj, name='Default', **kwargs):
    res = obj.get(name=name)
    if res and 'results' in res and len(res['results']) == 1:
        return res['results'][0]
    elif res and 'results' in res and len(res['results']) == 0:
        return obj.create(name=name, **kwargs)
    elif res and 'results' in res and len(res['results']) > 1:
        print("Error, more than 1 results found for unique search.")


