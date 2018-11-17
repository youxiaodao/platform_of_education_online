from django.middleware.security import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):

    def process_response(self,request,response):

        if request.method == "OPTIONS":
            response['Access-Control-Allow-Headers'] = 'Content-type,k1'  # k1是自定义请求头
            response['Access-Control-Allow-Method'] = 'PUT'
        response['Access-Control-Allow-Origin'] = "*"
        return response

    # def process_request(self,request,response):
    #     request['Access-Control-Allow-Origin'] = '*'
    #     return request
