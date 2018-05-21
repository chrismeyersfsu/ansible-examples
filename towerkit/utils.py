
def get_or_create(obj, name='Default', **kwargs):
    res = obj.get(name=name)
    if res and 'results' in res and len(res['results']) == 1:
        return res['results'][0]
    elif res and 'results' in res and len(res['results']) == 0:
        return obj.create(name=name, **kwargs)
    elif res and 'results' in res and len(res['results']) > 1:
        print("Error, more than 1 results found for unique search.")


def delete_all(resource):
    while True:
        req = resource.get(page_size=200)
        if req['count'] == 0:
            break
        map(lambda r: r.delete(), req['results'])

def cancel_all(resource, block=False):
    canceled = {}
    while True:
        req = resource.get(page_size=200, status='running')
        if req['count'] == 0:
            break

        count = 0
        for r in req['results']:
            if r.id in canceled:
                continue
            canceled[r.id] = True
            count += 1
        if count == 0:
            break


