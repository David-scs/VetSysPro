from django.utils.deprecation import MiddlewareMixin

class CurrentPageMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        current_page = "dashboard"  # Esto es solo un ejemplo, debes establecer esto de acuerdo a la página actual o URL
        response.context_data['current_page'] = current_page
        return response
    
class CurrentPageMiddleware2(MiddlewareMixin):
    def process_template_response(self, request, response):
        current_page2 = "vista__mascota"  # Esto es solo un ejemplo, debes establecer esto de acuerdo a la página actual o URL
        response.context_data['current_page'] = current_page2
        return response