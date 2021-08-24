def review_owner_check_service(request, review_check):
    for rev in review_check:
        if rev.__dict__['critic_id'] == request.user.id:
            return True
