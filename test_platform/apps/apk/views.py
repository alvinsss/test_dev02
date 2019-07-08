from django.shortcuts import render
from project.models import Project
from apk.models import APK_UPLOADFILE
from apk.models import APK_RESULTS
from django.conf import settings
from django.http import JsonResponse ,HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import  csrf_exempt

import platform
import os
import time
# Create your views here.
# 管理页面
# @login_required

def apk_list(request):
    print("apk_list")
    apkfile_all = APK_UPLOADFILE.objects.filter(del_status=0)
    print(apkfile_all)
    return render(request, "apk_list.html",
                  {"apkfiles": apkfile_all
                      , "type": "list"})


def add_apk(request):
    print("add apk ")
    return render(request,"apk_add.html")

def result(request,apkid):
    print("result",apkid)
    results = APK_RESULTS.objects.filter(batch_id_id=apkid)
    print(results)
    return render(request,"apk_result.html",{"results":results,"type":"result"})

def detail_result(request,resultid):
    print("detail_apkresult",resultid)
    results = APK_RESULTS.objects.filter(id=resultid)
    print(results)
    return render(request,"apk_detail_result.html",{"results":results,"type":"apk_detail_result"})

@csrf_exempt
def save_uploadapkfile(request):

    if request.method == "GET":
        return render(request,"apk_list.html")

    if request.method == "POST":
        module_id  = request.POST.get( "module_id", "" )
        name_des   = request.POST.get("name_des","")
        uploadfile = request.FILES.get("file_obj",None)    # 获取上传的文件，如果没有文件，则默认为None
        tfid       = request.POST.get("tfid","")
        apk_testtype = request.POST.getlist("apk_testtype","")
        userid     = request.user.id
        username   = request.user
        print(name_des,uploadfile,tfid,username,userid)
        print("apk_testtype----->",apk_testtype,type(apk_testtype))
        if (platform.system() == "Windows"):
            tmp_dirs = 'D:\static\lapk'
            tmp_dir = os.path.join( tmp_dirs, str( username ),
                                    str( time.strftime( "%Y-%m-%d_%H%M%S", time.localtime() ) ) )
            print(tmp_dir)
        else:
            tmp_dir = os.path.join( settings.FILE_APK, str( username ),
                                    str( time.strftime( "%Y-%m-%d_%H:%M:%S", time.localtime() ) ) )
            print(tmp_dir)
        if not os.path.exists( tmp_dir ):
            print( tmp_dir + " not exists ,create dir is starting" )
            os.makedirs( tmp_dir )
        # tfid即新建
        if tfid == "":
            print("tfid is null ,create action")
            if not uploadfile:
                return JsonResponse( {"status": 10200, "message": "上传文件不存在！"} )
            if uploadfile.name.split( '.' )[-1] not in ['zip','apk']:
                return JsonResponse( {"status": 10200, "message": "上传文件类型错误！"} )
            FileName = os.path.join( tmp_dir, uploadfile.name )
            try:
                with open( FileName, 'wb+' ) as f:
                    # 分块写入文件
                    for chunk in uploadfile.chunks():
                        f.write( chunk )
                    if  userid == None  :
                        APK_UPLOADFILE.objects.create(module_id=module_id,userid="9999",username="AnonyUser",name_des=name_des,upapkfile=FileName,apk_testtype=apk_testtype )
                    else:
                        APK_UPLOADFILE.objects.create( userid=userid,module_id=module_id,username=username,name_des=name_des,upapkfile=FileName,apk_testtype=apk_testtype )

                    print("APK_UPLOADFILE.objects.create!")
            except Exception as e:
                print( e )
            return JsonResponse( {"status": 10200, "message": "创建成功！", "data": FileName} )
        else:
            if uploadfile == None:
                print("修改，未修改上传文件",uploadfile)
                apk_uploadinfo = APK_UPLOADFILE.objects.get( id=tfid )
                apk_uploadinfo.userid = userid
                apk_uploadinfo.name_des = name_des
                apk_uploadinfo.apk_testtype = apk_testtype
                apk_uploadinfo.save()
                return JsonResponse( {"status": 10200, "message": "修改成功！", "data": apk_uploadinfo.name_des} )
            else:
                print("修改上传文件",uploadfile)
                FileName = os.path.join( tmp_dir, uploadfile.name )
                try:
                    with open( FileName, 'wb+' ) as f:
                        # 分块写入文件
                        for chunk in uploadfile.chunks():
                            f.write( chunk )
                    apk_uploadinfo = APK_UPLOADFILE.objects.get( id=tfid )
                    apk_uploadinfo.userid = userid
                    apk_uploadinfo.name_des = name_des
                    apk_uploadinfo.apk_testtype = apk_testtype
                    apk_uploadinfo.upapkfile = FileName
                    apk_uploadinfo.save()
                except Exception as e:
                    print( e )
                return JsonResponse( {"status": 10200, "message": "修改成功！", "data": FileName} )
        return render(request,"apk_add.html")

@csrf_exempt
def run_apk_task(request,tid):
    print("run_apk_task",tid)
    pass
