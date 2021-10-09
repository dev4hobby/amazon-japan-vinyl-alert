import requests
from .settings import IFTTT
def send_vinyl_to_webhook(vinyl: dict):
    '''
    Send vinyl info to IFTTT webhook
    -> SendSMS
    '''
    try:
        requests.post(
            IFTTT.get('new_arrival_url'),
            {
                "value1": f"{vinyl.get('artist', '?')} - {vinyl.get('title', '')[:16]}... 이 입고되었어요",
                "value2": {vinyl.get('price')},
                "value3": vinyl.get('url'),
            },
            IFTTT.get('headers')
        )
    except Exception as e:
        return {
            'status': False,
            'message': str(e),
        }
    return {
        'status': True,
        'message': 'Okay'
    }