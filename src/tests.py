def clean_amount(x):
    try:
        return float(str(x).replace(',', ''))
    except:
        return None