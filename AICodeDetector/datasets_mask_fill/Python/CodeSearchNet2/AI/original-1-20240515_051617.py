
    if not opt.get('use_nesterov'):
        return
    if not opt.get('nesterov_momentum'):
        return
    if not opt.get('nesterov_nesterov_momentum'):
        return

    if not opt.get('nesterov_momentum_switchover'):
        return

    if not opt.get('nesterov_nesterov_momentum_update_switchover'):
        return

    if not opt.get('nesterov_momentum_update_nesterov_momentum'):
        return

    if not opt.get('nesterov_nesterov