def initial_session(user, request):  # 注册权限列表以及当前登录用户ID函数
    # 在session中注册用户ID
    request.session["user_id"] = user.pk
    print(user.pk)
    ###方案一####
    # #查询当前用户所有的权限，在session中注册权限列表，distinct是去除重复的权限
    # permissions = user.roles.all().values("permissions__url").distinct()
    # print("permissions",permissions)#permissions拿到的是<QuerySet [{'permissions__url': '/users/'}, {'permissions__url': '/users/add'}, {'permissions__url': '/users/delete/(\\d+)'}]>
    # permission_list = []
    # for item in permissions:
    #     permission_list.append(item["permissions__url"])
    # print("permission_list",permission_list)#拿到的是['/users/', '/users/add', '/users/delete/(\\d+)']
    # # 在session中注册用户权限列表
    # request.session["permission_list"] = permission_list
    ###方案二####
    permission = user.roles.all().values("permissions__url", "permissions__group_id", "permissions__action").distinct()
    permission_dict = {}
    for item in permission:
        gid = item.get("permissions__group_id")
        if not gid in permission_dict:
            permission_dict[gid] = {
                "urls": [item["permissions__url"], ],
                "actions": [item["permissions__action"], ]
            }
        else:
            permission_dict[gid]["urls"].append(item["permissions__url"])
            permission_dict[gid]["actions"].append(item["permissions__action"])
    request.session["permission_dict"] = permission_dict
    # 注册菜单权限
    permission=user.roles.all().values("permissions__url", "permissions__action","permissions__title",).distinct()
    memu_permission_list=[]
    for item in permission:
        if item["permissions__action"]=="list":
            memu_permission_list.append((item["permissions__url"],item["permissions__title"]))
    request.session["memu_permission_list"]=memu_permission_list