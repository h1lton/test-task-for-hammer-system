def profile_serializer(user):
    data = {
        'tel': str(user.tel),
        'your_ref_code': user.ref_code,
        'used_ref_code': user.referrer.ref_code if user.referrer_id else None,
        'referrals': list(user.referrals.only('tel').values_list('tel', flat=True))
    }
    return data
