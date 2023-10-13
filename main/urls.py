from django.urls import path
from main.views import show_main, create_product, register, login_user, logout_user, delete_product, increase_product, decrease_product, edit_product, show_xml, show_json, show_xml_by_id, show_json_by_id, get_product_json, add_product_ajax, delete_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('increase_product/<int:product_id>/', increase_product, name='increase_product'),
    path('decrease_product/<int:product_id>/', decrease_product, name='decrease_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-ajax/', delete_product_ajax, name='delete_product_ajax'),
]