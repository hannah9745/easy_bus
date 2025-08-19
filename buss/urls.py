from django.urls import path

from buss import views

urlpatterns = {
    path('', views.login, name='login'),
    path('login_btn', views.login_btn, name='login_btn'),
    path('viewfeedbacksearch', views.viewfeedbacksearch, name='viewfeedbacksearch'),

    path('add_notification', views.add_notification, name='add_notification'),
    path('admin_view_notification', views.admin_view_notification, name='admin_view_notification'),

    path('add_notification_post', views.add_notification_post, name='add_notification_post'),
    # path('viewprofile', views.viewprofile, name='viewprofile'),

    path('add_route', views.add_route, name='add_route'),
    path('add_route_post', views.add_route_post, name='add_route_post'),
    path('new_owner_reg', views.new_owner_reg, name='new_owner_reg'),
    path('new_owner_reg_post', views.new_owner_reg_post, name='new_owner_reg_post'),


    path('adminhome', views.adminhome, name='adminhome'),
    path('busownerreg', views.busownerreg, name='busownerreg'),
    path('busownerreg_post', views.busownerreg_post, name='busownerreg_post'),
    path('manage_bus_route', views.manage_bus_route, name='manage_bus_route'),

    path('sendreply/<id>', views.sendreply, name='sendreply'),
    path('sendreply_post', views.sendreply_post, name='sendreply_post'),
    path('stopadd', views.stopadd, name='stopadd'),
    path('stopadd_post', views.stopadd_post, name='stopadd_post'),

    path('stopmangmnt', views.stopmangmnt, name='stopmangmnt'),
    path('userinformtion', views.userinformtion, name='userinformation'),
    path('vrfyroute', views.vrfyroute, name='vrfyroute'),
    path('verifybusowner', views.verifybusowner, name='verifybusowner'),
    path('viewinformation',views.viewinformation,name='viewinformation'),
    path('viewtiming',views.viewtiming,name='viewtiming'),
    path('viewcomplaints',views.viewcomplaints,name='viewcomplaints'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('add_bus_to_route',views.add_bus_to_route,name='add_bus_to_root'),
    path('add_bus',views.add_bus,name='add_bus'),
    path('add_buss_post',views.add_buss_post,name='add_buss_post'),
    # path('view_trip',views.view_trip,name='view_trip'),


    path('addemploye',views.addemploye,name='addemploye'),
    path('search_bus_stops',views.search_bus_stops,name='search_bus_stops'),
    path('addtime',views.addtime,name='addtime'),
    path('assignemployee/<id>',views.assignemployee,name='assignemployee'),
    path('busowner_homepage',views.busowner_homepage,name='busowner_homepage'),
    path('managebus',views.managebus,name='managebus'),
    path('manageemploye',views.manageemploye,name='manageemploye'),
    path('trip',views.trip,name='trip'),
    path('viewcollection',views.view_collection,name='viewcollection'),
    path('view_notification',views.view_notification,name='view_notification'),
    path('notification_delete/<id>',views.notification_delete,name='notification_delete'),
    path('delete_stopmanagment/<id>',views.delete_stopmanagment,name='delete_st opmanagment'),
    path('delete_viewtime/<id>',views.delete_viewtime,name='delete_viewtime'),
    path('delete_assignedemp/<id>',views.delete_assignedemp,name='delete_assignedemp'),
    path('delete_new_owner/<id>',views.delete_new_owner,name='delete_new_owner'),
    path('add_assignemployee_post',views.add_assignemployee_post,name='add_assignemployee_post'),
    path('view_assignedemp',views.view_assignedemp,name='view_assignedemp'),


    path('edit_notification/<id>',views.edit_notification,name='edit_notification'),

    path('edit_notification_post',views.edit_notification_post,name='edit_notification_post'),
    path('edit_viewtime_post',views.edit_viewtime_post,name='edit_viewtime_post'),
    path('edit_stopadd/<id>',views.edit_stopadd,name='edit_stopadd'),
    path('edit_stopadd_post',views.edit_stopadd_post,name='edit_stopadd_post'),
    path('edit_busowner/<id>',views.edit_busowner,name='edit_busowner'),
    path('edit_busowner_post',views.edit_busowner_post,name='edit_busowner_post'),
    path('edit_bus_route/<id>',views.edit_bus_route,name='edit_bus_route'),
    path('edit_viewtime/<id>',views.edit_viewtime,name='edit_viewtime'),
    path('edit_busroute_post',views.edit_busroute_post,name='edit_busroute_post'),
    path('addemploye_post',views.addemploye_post,name='addemploye_post'),
    path('edit_manageemploye/<id>',views.edit_manageemploye,name='edit_manageemploye'),
    path('edit_manageemployee_post',views.edit_manageemployee_post,name='edit_manageemployee_post'),
    path('delete_employee/<id>',views.delete_employee,name='delete_employee'),
    path('delete_bus/<id>',views.delete_bus,name='delete_bus'),
    path('delete_trip/<id>',views.delete_trip,name='delete_trip'),
    path('add_viewtime',views.add_viewtime,name='add_viewtime'),
    path('reject_owner/<int:id>',views.reject_owner,name='reject_owner'),
    path('accept_owner/<int:id>',views.accept_owner,name='accept_owner'),


    path('edit_bus/<id>',views.edit_bus,name='edit_bus'),
    path('add_bus_to_route_post',views.add_bus_to_route_post,name='add_bus_to_route_post'),
    path('edit_bus_post',views.edit_bus_post,name='edit_bus_post'),
    # path('logincode',views.logincode,name='logincode'),

    # path('searchstopmangmnt',views.searchstopmangmnt,name='searchstopmangmnt'),


    path('viewtime/<int:id>',views.viewtime,name='viewtime'),
    path('view_bussowner',views.view_bussowner,name='view_bussowner'),

    path('view_bussowner_delete/<lid>',views.view_bussowner_delete,name='view_bussowner_delete'),
    path('manage_bus_route_delete/<id>',views.manage_bus_route_delete,name='manage_bus_route_delete'),


    path('logincode',views.logincode,name='logincode'),
    path('user_view_profile',views.user_view_profile,name='user_view_profile'),
    path('view_assinged_bus_flutter',views.view_assinged_bus_flutter,name='view_assinged_bus_flutter'),
    path('view_bus_route_flutter',views.view_bus_route_flutter,name='view_bus_route_flutter'),
    path('view_assinged_bus_flutter',views.view_assinged_bus_flutter,name='view_assinged_bus_flutter'),
    path('collection_details_flutter',views.collection_details_flutter,name='collection_details_flutter'),
    path('view_bus_shudule',views.view_bus_shudule,name='view_bus_shudule'),
    path('viewpayment',views.viewpayment,name='viewpayment'),
    path('viewpaymentuser',views.viewpaymentuser,name='viewpaymentuser'),
    path('viewtrip',views.viewtrip,name='viewtrip'),
    path('updateamount',views.updateamount,name='updateamount'),
    path('acc_bk',views.acc_bk,name='acc_bk'),
    path('rj_bk',views.rj_bk,name='rj_bk'),




}
