from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from .resulttohtml import compile_result_to_html_formate




class EditorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "compiler.html")
    


class ExecuteCode(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('user_enter_code')
        process = subprocess.Popen(['python', '-c', f"""{code}"""], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if err:
            data = {"output":compile_result_to_html_formate(err.decode('utf-8'))}
        else:
            data = {"output":compile_result_to_html_formate(out.decode('utf-8'))}
        return JsonResponse(data=data)