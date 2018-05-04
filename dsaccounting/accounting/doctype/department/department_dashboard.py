from frappe import _

def get_data():
    return {
        'transactions': [
            {
                'label': _('Projects & Tasks'),
                'items': ['Project','DS Task']
            }
        ]
    }
