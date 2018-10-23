import os
from aiohttp import web
import json

# constant
base_dir = './store/'


# upload file to server
async def upload(request):
    reader = await request.multipart()
    field = await reader.next()
    filename_hash = str(hash(field.filename))
    os.makedirs(base_dir + filename_hash[:2], exist_ok=True)
    filename = base_dir + filename_hash[:2] + '/' + filename_hash
    with open(filename, 'wb') as fd:
        while True:
            chunk = await field.read_chunk()
            if not chunk:
                break
            fd.write(chunk)

    response_obj = {'status': 'success',
                    'filename_hash': filename_hash, }
    return web.Response(text=json.dumps(response_obj))


# download file from server
async def download(request):
    filename_hash = request.rel_url.query['filename_hash']
    filename = base_dir + filename_hash[:2] + '/' + filename_hash

    try:
        response = web.FileResponse(filename)
        ContentDisposition = 'Attachment;filename=' + filename_hash
        response.headers['Content-Disposition'] = ContentDisposition
        return response

    except FileNotFoundError:
        response_obj = {'status': 'failed',
                        'error': 'file not found',
                        'filename_hash': filename_hash,
                        }

    except Exception as ex:
        response_obj = {'status': 'failed',
                        'error': 'internal error',
                        'filename_hash': filename_hash,
                        }
        print(ex)

    return web.Response(text=json.dumps(response_obj))


# delete file from server
async def delete(request):
    filename_hash = request.rel_url.query['filename_hash']
    filename = base_dir + filename_hash[:2] + '/' + filename_hash
    try:
        os.remove(filename)
        response_obj = {'status': 'success',
                        'filename_hash': filename_hash, }
    except OSError:
        response_obj = {'status': 'failed',
                        'error': 'file not found',
                        'filename_hash': filename_hash,
                        }
    except Exception as ex:
        response_obj = {'status': 'failed',
                        'error': 'internal error',
                        'filename_hash': filename_hash,
                        }
        print(ex)
    return web.Response(text=json.dumps(response_obj))


# url_routs
routes = [
    ('POST', '/upload', upload),
    ('GET', '/download', download),
    ('DELETE', '/delete', delete),
]
